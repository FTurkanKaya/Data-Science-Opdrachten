
#####################################################################
#####################################################################
##                           OPDRACHT 6 - AB TEST                  ##
#####################################################################
#####################################################################
"""
Zakelijke Probleem

Digitale advertentieplatforms bieden adverteerders verschillende biedstrategieën aan
om conversiepercentages te optimaliseren. Onlangs is een nieuwe methode, genaamd "gemiddeld bieden" (average bidding),
geïntroduceerd als alternatief voor het bestaande model "maximaal bieden" (maximum bidding).

Een van onze klanten, veridunya.com, wil testen of deze nieuwe biedstrategie efficiënter is.
Om te bepalen of average bidding een hoger conversiepercentage oplevert dan maximum bidding,
heeft het bedrijf een A/B-test uitgevoerd.

Deze A/B-test loopt nu al een maand en veridunya.com verwacht van u een analyse van de testresultaten.
De belangrijkste prestatie-indicator voor het bedrijf is de aankoop (purchase) metriek.
Daarom moeten de statistische analyses zich hierop concentreren.

#***********************************************************************
Datasetbeschrijving

Deze dataset bevat gegevens over advertentieweergaven en gebruikersinteracties op een e-commercesite. 
Het omvat het aantal keren dat bezoekers op de weergegeven advertenties hebben geklikt en de gegenereerde inkomsten.

In de studie zijn er twee verschillende groepen:

Controlegroep: De methode Maximum Bidding is toegepast.
Testgroep: De methode Average Bidding is toegepast.
De gegevens zijn opgeslagen in een Excel-bestand genaamd ab_test_data.xlsx, 
waarbij elke groep zich op een aparte werkblad bevindt.

#**************************************************************************
Metric Definities

Impressie (Impression): Het aantal keren dat een advertentie is weergegeven.
Klik (Click)          : Het aantal keren dat er op een weergegeven advertentie is geklikt.
Aankoop (Purchase)    : Het aantal aankopen dat is gedaan na het klikken op een advertentie.
Inkomsten (Earning)   : De inkomsten die zijn gegenereerd na een aankoop.
"""
##########################################
# TAAK 1 (Gegevensvoorbereiding en Analyse)
##########################################
# Stap 1:
# Lees de gegevens van de controle- en testgroep uit het bestand 'ab_test_data.xlsx'.
# Wijs de gegevens van de controle- en testgroep toe aan afzonderlijke variabelen.
#*******************************************************
import itertools
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
# !pip install statsmodels
import statsmodels.stats.api as sms
from scipy.stats import ttest_1samp, shapiro, levene, ttest_ind, mannwhitneyu, \
    pearsonr, spearmanr, kendalltau, f_oneway, kruskal
from statsmodels.stats.proportion import proportions_ztest

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 10)
pd.set_option('display.float_format', lambda x: '%.4f' % x)

print(os.getcwd())

filePath = "Data-Science-Opdrachten/dataset/ab_test_data.xlsx"
df_controlGroup = pd.read_excel(filePath, sheet_name="Control Group")
df_testGroup = pd.read_excel(filePath, sheet_name="Test Group")

df_controlGroup.head()  # Maximum Bidding
df_testGroup.head()  # Average Bidding


# Stap 2:
# Analyseer de basisstatistieken van beide groepen.
# Bereken kernstatistieken zoals het gemiddelde, de mediaan en de standaarddeviatie.
# Evalueer of er zichtbare verschillen zijn tussen de groepen.
#*******************************************************

############################
# Beschrijvende Statistieken
############################

# Basisstatistieken voor de controlegroep
control_stats = df_controlGroup.describe().T

# Basisstatistieken voor de testgroep
test_stats = df_testGroup.describe().T

# Statistieken combineren
summary_df = pd.concat([control_stats['mean'], test_stats['mean']], axis=1)
summary_df.columns = ['Control Group - Mean', 'Test Group - Mean']

############################
# Confidence Intervals (Betrouwbaarheidsintervallen)
############################
sms.DescrStatsW(df_testGroup['Purchase']).tconfint_mean()
sms.DescrStatsW(df_controlGroup['Purchase']).tconfint_mean()

######################################################
# Correlatie
######################################################
"""
Korelatiecoëfficiënt-Pearson (varieert tussen -1 en 1):
• Positieve correlatie
• Negatieve correlatie
• Geen correlatie

-1.00 - 0.00 → Negatieve correlatie
0.00 - 0.00 → Geen correlatie
0.00 - 1.00 → Positieve correlatie
"""
# Berekening van correlaties tussen variabelen

def correlation_matrix(dataframe, target='Purchase'):
    otherColumns = dataframe.drop(target, axis=1).columns
    correlations = [dataframe[target].corr(dataframe[col]) for col in otherColumns]
    for col, corr in zip(otherColumns, correlations):
        print(f"{col} correlatie met {target}: {corr}")

correlation_matrix(df_controlGroup)
correlation_matrix(df_testGroup)


# Visuele analyse van de correlatie:
#********************************************************************

def correlation_matrix_heatmap(dataframe, target = 'Purchase'):
    otherColumns = dataframe.drop(target, axis = 1).columns
    for col in otherColumns:
        plt.figure(figsize=(6, 4))
        sns.scatterplot(data=dataframe, x='Purchase', y=col)
        plt.title(f'Purchase vs {col}')
        plt.show()

correlation_matrix_heatmap(df_controlGroup)
correlation_matrix_heatmap(df_testGroup)

#*************************************************************************************************
# Verkoopconversieratio en winst per verkoopberekeningen
#**********************************************************************************************
# Earnings_Per_Sale waarde geeft aan hoeveel inkomsten worden gegenereerd per aankoop.
# Click_To_Sale_Rate percentage laat zien hoeveel van de klikken resulteren in een aankoop.

def calculate_conversion_and_earning(df):
    df['Click_To_Sale_Rate'] = (df['Purchase'] / df['Click']) * 100
    df['Earnings_Per_Sale'] = (df['Earning'] / df['Purchase']) * 100

    return df

calculate_conversion_and_earning(df_controlGroup)
calculate_conversion_and_earning(df_testGroup)


#**********************************************************************************

# Stap 3:
#Na de analyse worden de gegevens van de controle- en testgroep samengevoegd met behulp van de concat-methode.
#*******************************************************
df_controlGroup["Group"] = "Control"
df_testGroup["Group"] = "Test"

df = pd.concat([df_controlGroup, df_testGroup], ignore_index=True)
df.head()
df.tail()

#############################################
# TAAK 2 (Hypothesevorming voor A/B-test )
#############################################
#Stap 1:
#Formuleer de hypothesen als volgt:

#H₀ (Nulhypothese): Er is geen significant verschil tussen de twee groepen. (M₁ = M₂)
#H₁ (Alternatieve hypothese): Er is een significant verschil tussen de twee groepen. (M₁ ≠ M₂)
#*******************************************************
# H0: M1 = M2 (Hoofdgroep en testgroep vertonen geen significant verschil in 'PURCHASE' (aankoop) gemiddelden.)
# H1: M1 != M2 (...) er is een significant verschil.



#Stap 2:
#Bereken en vergelijk de gemiddelde aankoopcijfers (purchase) van de controle-
# en testgroep om een eerste indruk te krijgen van mogelijke verschillen.
#*******************************************************
df.groupby("Group").agg({"Purchase": "mean",
                         "Click_To_Sale_Rate": "mean",
                         "Earnings_Per_Sale": "mean"})


"""
BEOORDELING:
---------------------------------------------------------------------------------------------------------
• De gemiddelde aankoopwaarde van de testgroep (582,10) is hoger dan die van de controlegroep (550,89).
• Het verschil is ongeveer 31,21 (582,10 - 550,89).
• Maar is dit verschil statistisch significant? Hiervoor moeten we de p-waarde berekenen.

Als p-waarde < 0,05, dan is dit verschil significant en kunnen we de H₀-hypothese verwerpen.
Als p-waarde ≥ 0,05, dan kan dit verschil toevallig zijn en kunnen we de H₀-hypothese niet verwerpen.
"""

#############################################
# TAAK 3 (Hypothesetest en Veronderstellingscontroles )
#############################################
#Stap 1:
# Voordat we de hypothesetest starten, moeten we de volgende aannames controleren:
# 1 --->> Normaliteitstest
#           Beoordeel aan de hand van de testresultaten of de controle-
#           en testgroepen voldoen aan de normaliteitsaanname.
#************************************************************
# Varsayım Kontrolü:
# H0: De testgroep en de controlegroep voldoen aan de aanname van een normale verdeling in de 'PURCHASE'-gegevens.
# H1:..voldoet niet aan deze aanname.

missing_data = df.isnull().sum()

# Normale verdeling hypothesetest voor de controlegroep (Shapiro)
test_stat, pvalue = shapiro(df.loc[df["Group"] == "Control", "Purchase"]) #.dropna())
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))


# Normale verdeling hypothesetest voor de testgroep
test_stat, pvalue = shapiro(df.loc[df["Group"] == "Test", "Purchase"]) #.dropna())
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))


"""
Resultaat en Beoordeling:
• Voor beide groepen zijn de p-waarden groter dan 0,05, wat betekent dat beide groepen een normale verdeling vertonen.
• In dit geval kunnen parametrische tests (bijvoorbeeld de t-test) worden gebruikt, omdat de gegevens normaal verdeeld zijn.
"""


#2 --->> Homogeniteit van variantie (Levene’s Test)
#           Evalueer de testresultaten om te bepalen of
#           er een significant verschil is in variantie tussen de groepen.
#************************************************************
#Aanname van Variantiehomogeniteit
#H₀: De varianties zijn homogeen.
#H₁: De varianties zijn niet homogeen.

#Hypothesetest voor variantiehomogeniteit tussen de test- en controlegroep

test_stat, pvalue = levene(df.loc[df["Group"] == "Control", "Purchase"],
                                    df.loc[df["Group"] == "Test", "Purchase"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

#Als p-waarde < 0.05, dan wordt H₀ verworpen.
# Als p-waarde ≥ 0.05, dan kan H₀ niet worden verworpen.

"""
Interpretatie:
1- Hypothesen:

    H₀ (Nulhypothese): De varianties zijn homogeen (gelijk).
    
    H₁ (Alternatieve hypothese): De varianties zijn niet homogeen (niet gelijk).

2- p-waarde: 0.1083

    p-waarde > 0.05, wat betekent dat de nulhypothese niet wordt verworpen.
    
    Een p-waarde groter dan 0.05 geeft aan dat de varianties gelijk zijn en 
    dat er dus geen significant verschil in variantie tussen de groepen is.

3- Conclusie:

    We kunnen de nulhypothese niet verwerpen.
    
    Dit betekent dat er geen verschil in varianties tussen de groepen is, en we mogen aannemen dat de varianties homogeen zijn.
"""

# Stap 2:
# Kies de juiste statistische test op basis van de resultaten van de normaliteits- en variantietests.
#***************************************************************
#
"""
* De veronderstellingen zijn als volgt:

Als de veronderstellingen zijn voldaan, wordt de onafhankelijke twee-sample t-toets (parametrische test) gebruikt.

Als de veronderstellingen niet zijn voldaan, wordt de Mann-Whitney U-test (non-parametrische test) gebruikt.

Volgens de resultaten van de normaliteitstest en de test voor homogene variantie kan worden gesteld dat 
de varianties van de controlegroep en de testgroep als gelijk worden beschouwd. 
Dit betekent dat er geen probleem is met het gebruik van parametrische tests (zoals de t-toets) en dat deze test geldig is.

"""

# Stap 3:
# Analyseer de verkregen p-waarde en beoordeel of
# er een significant verschil is in het gemiddelde aantal aankopen tussen de controle- en testgroepen.
#***************************************************************

test_stat, pvalue = ttest_ind(df.loc[df["Group"] == "Control", "Purchase"],
                              df.loc[df["Group"] == "Test", "Purchase"],
                              equal_var=True)

print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

"""
H0 (nulhypothese): Er is geen statistisch significant verschil tussen de 'PURCHASE' (aankoop) gemiddelden 
                    van de controlegroep en de testgroep (M1 = M2).
H1 (alternatieve hypothese): Er is een statistisch significant verschil tussen de 'PURCHASE' (aankoop) gemiddelden 
                    van de controlegroep en de testgroep (M1 ≠ M2).

p-waarde: 0.3493
Als de p-waarde kleiner is dan 0.05, wordt de nulhypothese verworpen (H0 wordt verworpen).
Als de p-waarde groter is dan 0.05, kan de nulhypothese niet worden verworpen.

In dit geval is de p-waarde 0.3493, wat groter is dan 0.05. Dit betekent dat we de nulhypothese niet kunnen verwerpen. 
Dit geeft aan dat er geen statistisch significant verschil is tussen de 'PURCHASE' (aankoop) gemiddelden van de controlegroep 
en de testgroep. Kortom, er is geen verschil tussen de groepen.
"""
###################################################################################################################################
# EXTRA ***
# Als de veronderstellingen niet zouden worden voldaan, dan zouden non-parametrische tests,
# zoals de Mann-Whitney U-test, nodig zijn.
# #************************************************************

test_stat, pvalue = mannwhitneyu(df.loc[df["Group"] == "Control", "Purchase"],
                                 df.loc[df["Group"] == "Test", "Purchase"])

print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))


################################################################################################################################

#############################################
# Taak 4: Conclusie en Aanbeveling
#############################################
#Stap 1:
# Leg uit welke statistische test je hebt gebruikt en waarom je deze test hebt gekozen.
#*********************************************
"""
Gebruikte test: Onafhankelijke Twee-Groep t-test (parametrisch) (Independent Two-Sample t-test)

Reden voor het kiezen van de test:
Geschiktheid van de test:
• Normaliteitshypothese: De aankoopgegevens van beide groepen volgen een normale verdeling 
                        (resultaten van de normaliteitstest p > 0.05).
• Homogeniteit van variantiehypothese: De varianties van de groepen zijn gelijk 
                        (resultaten van de homogeniteit van variantietest p > 0.05).
Gezien deze voorwaarden is het correct om de t-test te gebruiken.

De t-test wordt gebruikt om te bepalen of er een significant verschil is tussen 
de aankoopgemiddelden van de twee onafhankelijke groepen: de Controle Groep (Maximum Bidding) en de Test Groep (Average Bidding).

H0 Hypothese: M₁ = M₂, oftewel er is geen significant verschil tussen de aankoopgemiddelden van de twee groepen.
H1 Hypothese: M₁ ≠ M₂, oftewel er is een significant verschil tussen de aankoopgemiddelden van de twee groepen.
"""


#Stap 2:
#  --->> Op basis van de testresultaten, welke biedstrategie zou je de klant aanbevelen?
#***********************************************
"""
Testresultaten:
Teststatistiek (Test Stat): -0.9416
p-waarde: 0.3493

Interpretatie:
De p-waarde is 0.3493, wat aangeeft dat deze groter is dan 0.05.
We kunnen de nulhypothese (H0) niet verwerpen. Dit betekent dat er geen statistisch significant verschil is 
tussen de aankoopgemiddelden van de Controle Groep en de Test Groep.


Resultaten en Aanbeveling:
Aangezien de p-waarde > 0.05 is, is het verschil tussen de aankoopgemiddelden van de groepen statistisch gezien niet significant.
Daarom is het moeilijk om een effectievere biedstrategie te bepalen tussen 
Average Bidding (testgroep) en Maximum Bidding (controlegroep). Beide biedstrategieën lijken vergelijkbare resultaten op te leveren.
"""

#  --->> Is Maximum Bidding of Average Bidding effectiever? en Onderbouw je aanbeveling met een duidelijke uitleg en de testresultaten.
#***********************************************************************************************
"""
Aanbevelingen voor de Klant:

Toekomstige Stappen en Strategieontwikkeling:
--->> Onvoldoende Dataset:
Hoewel er aanvankelijk geen verschil tussen de groepen werd waargenomen, kan deze test met de huidige dataset onvoldoende zijn. 
Er kan mogelijk een verschil zijn tussen de groepen, maar meer data of een langere testperiode kan nodig zijn.
De Wet van Grote Aantallen kan hier een belangrijke rol spelen. Deze wet stelt dat wanneer een experiment veelvuldig wordt herhaald,
 de gemiddelde resultaten dichter bij de werkelijke waarde komen te liggen.
Als de dataset niet groot genoeg is, kunnen kleine verschillen tussen de groepen mogelijk niet statistisch significant zijn.
 Dit komt omdat analyses met een kleine dataset meer gevoelig kunnen zijn voor willekeurige variaties (of toevallige verschillen).
Met een grotere dataset zullen de echte verschillen tussen de groepen duidelijker worden en 
kunnen statistische tests betrouwbaardere resultaten opleveren. Dit kan binnen de context van de Wet van Grote Aantallen worden beoordeeld.

---->> A/B Test met Grotere Dataset:
Bijvoorbeeld, de testperiode kan worden verlengd of er kan een analyse worden uitgevoerd voor verschillende gebruikerssegmenten.

---->> Segmentatie:
Als wordt aangenomen dat de Average Bidding-strategie effectiever is voor verschillende gebruikerssegmenten, 
kan segmentatie worden toegepast om meer specifieke tests uit te voeren.
Bijvoorbeeld, gebruikers kunnen worden verdeeld op basis van leeftijd, inkomen, apparaattype, geografische locatie, enz.
 A/B-tests kunnen dan per segment worden uitgevoerd, wat diepere inzichten kan opleveren.

---->> Optimalisatie:
Hoewel beide strategieën op dit moment vergelijkbare resultaten opleveren, 
kunnen andere metrische analyses worden uitgevoerd op basis van kostenefficiëntie en bedrijfsdoelen.
De Average Bidding-strategie kan mogelijk kostenefficiënter en duurzamer zijn, 
omdat middelgrote biedstrategieën vaak meer stabiele resultaten bieden.

---->> Andere Metrieken:
In plaats van de test te beperken tot alleen de aankoop (purchase) metric, 
kan de test ook worden uitgebreid met andere metrische gegevens, 
zoals click-through rate (CTR), inkomsten (revenue), en andere relevante business metrics.
Dit zou helpen bij het evalueren van de effectiviteit van de strategieën op basis van conversieratio’s, marktaandeel en
 andere belangrijke prestatie-indicatoren.

Verbetering van de A/B Test:
---->> Testduur:
De duur van de A/B-test kan mogelijk niet lang genoeg zijn. 
Gegevens verzameld in een kortere periode kunnen misleidend zijn door willekeurige variaties of seizoensgebonden invloeden. 
De testperiode kan worden verlengd en opnieuw worden uitgevoerd in verschillende tijdsintervallen.

---->> Herhaling van de Test en Verdere Analyse:
Het zou nuttig kunnen zijn om de test meerdere keren uit te voeren om te zien welke resultaten er onder verschillende omstandigheden, 
op verschillende dagen of met verschillende advertentiecampagnes worden behaald.

Conclusie:
Uit deze test blijkt dat beide biedstrategieën vergelijkbare effecten hebben. 
Dit maakt het moeilijk om momenteel een strategie te kiezen op basis van de aankoop (purchase) metric.
Echter, afhankelijk van de bedrijfsomstandigheden en klantdoelen, kan een strategische wijziging nodig zijn. 
Beide strategieën kunnen vergelijkbare resultaten opleveren,
maar op basis van marktomstandigheden, advertentie-uitgaven en een bredere dataset kunnen er duidelijkere beslissingen worden genomen.

"""