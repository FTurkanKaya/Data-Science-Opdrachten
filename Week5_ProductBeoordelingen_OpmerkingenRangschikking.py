"""
Verhaal van de Dataset

In dit project zullen we gebruik maken van beoordelingsgegevens afkomstig van een e-commerceplatform. De dataset bevat gebruikersbeoordelingen en opmerkingen over een product in de categorie elektronica. De dataset bevat de volgende variabelen:

reviewerID:     Gebruikers-ID
productID:      Product-ID
reviewerName:   Gebruikersnaam
helpful:        Mate van nuttigheid van de beoordeling
reviewText:     Beoordelingstekst
overall:        Productscore (tussen 1 en 5)
summary:        Samenvatting van de beoordeling
unixReviewTime: Beoordelingstijdstip (Unix-tijdstempel)
reviewTime:     Beoordelingstijdstip (ruw formaat)
day_diff:       Aantal dagen sinds de beoordeling
helpful_yes:    Aantal keer dat de beoordeling als nuttig is beschouwd
total_vote:     Totaal aantal stemmen op de beoordeling

"""
import pandas as pd
import math
import scipy.stats as st                         ## voor de Statistische bewerking


pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 500)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.float_format', lambda x: '%.5f' % x)


#Het pad naar het bestand waar de module zich bevindt, wordt opgegeven.
import sys
print(sys.path)

import os
print(os.getcwd())
print(os.path.join(os.getcwd(), 'Python_Eurotech'))

sys.path.append(os.path.join(os.getcwd(), 'Data-Science-Opdrachten'))
print(sys.path)

df = pd.read_csv(r"C:\Users\onayk\PycharmProjects\Data-Science-Opdrachten\dataset\amazon_review.csv")

df.head()
df.shape



#######################################
# TAAK1
#######################################
# STAP 1
# Bereken Gemiddelde score van het Product
#**************************************

df['overall'].mean()
df.info()



# STAP 2
# Bereken de gewogen gemiddelde score op basis van de datum.
# Geef recentere beoordelingen een hoger gewicht.
#**************************************
# De function voor tijd gebaseerde gewogen gemiddelde importeren

import importlib
import Week5_rating_sorting_Reviews_Formules as rs
importlib.reload(rs)  # Modülü yeniden yükler

# De relevante kolommen worden uit de dataframe gehaald en vereenvoudigd.
df = df[['reviewerName','helpful', 'reviewText', 'overall', 'reviewTime', 'day_diff', 'helpful_yes', 'total_vote']]

# 'reviewTime' is een 'object' datatype en moet naar 'Date' datatype veranderen
df['reviewTime'] = pd.to_datetime(df['reviewTime'])
df.info()

#  We roepen de functie aan vanuit het bestand waarin we deze als een module hebben gemaakt.
rs.weighted_average_time_based(df, "overall", "day_diff")
# Out[36]: 4.6987161061560725

df['overall'].mean()
# Out[37]: 4.587589013224822



# STAP 3
# Vergelijk de gewogen gemiddelde score met de huidige gemiddelde score
# en interpreteer de resultaten.
#**************************************
"""
"Het gewogen gemiddelde score is 4.6987, terwijl de standaard gemiddelde score 4.5876 is berekend.
Het hogere gewogen cijfer geeft aan dat de recente beoordelingen hogere scores bevatten.

Deze situatie kan op verschillende manieren worden geïnterpreteerd:

De ontwikkeling van het product in de loop van de tijd: Mogelijke problemen met het product kunnen zijn opgelost 
en nieuwe gebruikers hebben mogelijk hogere scores gegeven.
Toegenomen klanttevredenheid: De verkoper heeft mogelijk de servicekwaliteit verbeterd of de klantenondersteuningsprocessen geoptimaliseerd.
Verschillende neigingen van oude en nieuwe beoordelingen: Gebruikers die het product eerst hebben aangeschaft, kunnen kritischer zijn geweest, 
terwijl gebruikers die later kwamen, meer tevreden over het product waren.
Het traditionele gemiddelde beschouwt alle oude en nieuwe beoordelingen als gelijk, 
terwijl het tijdgewogen gemiddelde meer actuele en waarschijnlijk accuratere klantpercepties weerspiegelt. 
Daarom zorgt het gebruik van gewogen beoordelingen door gebruikers voor een meer nauwkeurige en actuele productbeoordeling, 
wat hen helpt bij het nemen van beter geïnformeerde beslissingen."
"""

#######################################
# TAAK2 --  Bepaal 20 beoordelingen die op de productdetailpagina weergegeven moeten worden.
#######################################
# STAP 1
# Maak variabel van helpful_no
#**************************************
import Week5_rating_sorting_Reviews_Formules as rs

# We roepen de functie aan vanuit het bestand waarin we deze als een module hebben gemaakt.
df['helpful_no'] = (rs.up_down_score_diff(df['total_vote'], df['helpful_yes']))

df.head()

# STAP 2
# Bereken de scores van score_pos_neg_diff, score_average_rating ve wilson_lower_bound
# en Voeg de dataset toe.
#**************************************

# score_pos_neg_diff
df["score_pos_neg_diff"] = df.apply(lambda x: rs.up_down_score_diff(x['helpful_yes'], x['helpful_no']), axis=1)  # pozitiften negatif sayiyi cikar

# score_average_rating
df["average_rating_score"] = df.apply(lambda x: rs.average_rating_score(x['helpful_yes'], x['helpful_no']), axis=1)

# wilson_lower_bound
df["wilsonlowerbound"] = df.apply(lambda x: rs.wilsonlowerbound(x['helpful_yes'], x['helpful_no']), axis=1)

df.head()

# STAP 3
# Bepaal de top 20 beoordelingen met de hoogste score op basis van de Wilson-lagere limiet
# en interpreteer de resultaten.
#**************************************
df = df[['reviewerName','helpful', 'overall','day_diff', 'helpful_yes','helpful_no', 'total_vote', 'score_pos_neg_diff', 'average_rating_score', 'wilsonlowerbound']]
df.sort_values('wilsonlowerbound', ascending=False).head(20).reset_index(drop=True)


"""

 
Analyse van de Beoordelingen:

Een hoge score_pos_neg_diff waarde geeft aan dat er meestal meer positieve beoordelingen zijn en dat gebruikers tevreden zijn met hun beoordeling. 
Aan de andere kant betekent een lage waarde dat er meer negatieve beoordelingen zijn.
Hoewel de score_pos_neg_diff hoog is, kan het laag in de ranglijst staan, wat kan wijzen op een klein aantal beoordelingen of een lage hoeveelheid stemmen. 
Een product met weinig beoordelingen kan, ondanks meer positieve feedback, lager in de ranglijst staan vanwege de betrouwbaarheid. Dit betekent dat, 
hoewel het verschil tussen "helpful_yes" en "helpful_no" groot is, de algemene beoordeling van het product en statistieken zoals wilsonlowerbound van invloed kunnen zijn.

Hoewel de score_pos_neg_diff het verschil tussen positieve en negatieve beoordelingen aangeeft, 
moeten factoren zoals betrouwbaarheid in overweging worden genomen bij rangschikkingen. 
Het aantal beoordelingen en de betrouwbaarheid (bijvoorbeeld wilsonlowerbound) kunnen de rangschikking beïnvloeden. 
Zelfs als de score_pos_neg_diff hoog is, kan de rangschikking lager zijn als het aantal beoordelingen klein is of de betrouwbaarheid laag is.

De hoogste behulpzaamheidsratio (average_rating_score):
De meeste van de eerste 20 beoordelingen hebben hoge average_rating_score-waarden, vooral die met een waarde van 1.00000. 
Dit toont aan dat de meeste beoordelaars de beoordelingen als zeer behulpzaam beschouwen. We kunnen echter ook opmerken 
dat de hoge average_rating_score niet alleen te wijten is aan positieve beoordelingen en likes:

Het hoge aantal positieve beoordelingen en het gebrek aan negatieve beoordelingen: 
Een hoge Average Rating Score betekent meestal een hoog aantal "helpful_yes" stemmen. 
Als er geen "helpful_no"-stemmen zijn en alleen "helpful_yes" hoog is, zal de average_rating_score 1.00000 zijn. 
Dit wordt bijvoorbeeld waargenomen bij de beoordelingen op index 12 (Eskimo) en index 13 (Stayeraug), 
waar er geen negatieve feedback is, wat resulteert in een average_rating_score van 1.00000.

Een laag aantal beoordelingen: 
Een klein aantal beoordelingen kan de lage "helpful_no"-waarde en daarmee de hoge "average_rating_score" beïnvloeden. 
Hoe minder beoordelingen, hoe lager doorgaans het aantal negatieve beoordelingen. 
In dit geval kan het aantal positieve reacties hoog zijn, zelfs met weinig beoordelingen. 
Dit kan ertoe leiden dat de beoordelingen minder variatie tonen en slechts één positieve ervaring weerspiegelen. 
Dit is bijvoorbeeld zichtbaar bij gebruikers met weinig beoordelingen, zoals "Twister" en "goconfigure".

De invloed van negatieve beoordelingen: 
Als een beoordeling veel "helpful_yes"-stemmen heeft, duidt dit meestal op een positieve ervaring en waarschijnlijk verhoogde tevredenheid. 
Als er echter weinig of geen negatieve feedback is, kan de vraag rijzen of de beoordeling realistisch is. 
Dus, als een beoordeling alleen positieve feedback heeft en de average_rating_score hoog is, kan deze beoordeling slechts een gedeeltelijke weergave zijn van de ervaring. 
Het ontbreken van negatieve feedback kan betekenen dat de beoordeling onvolledig of misleidend is. 
Een realistische en gedetailleerde beoordeling bevat meestal zowel positieve als negatieve aspecten.

Conclusie en Evaluatie: 
De reden voor de hoge average_rating_score is niet alleen de hoge positieve feedback, 
maar ook het lage aantal "helpful_no"-stemmen en het lage aantal beoordelingen. 
Hoewel dit in lijn is met beoordelingen die meer likes en als behulpzaam worden beschouwd, 
moeten we bedenken dat het ontbreken van negatieve feedback en het baseren van beoordelingen op alleen positieve ervaringen een onrealistische beoordeling kan veroorzaken. 
In dit geval kan het lage aantal beoordelingen en het gebrek aan negatieve feedback vragen oproepen over de volledigheid en realiteit van de beoordelingen. 
De hoge average_rating_score komt waarschijnlijk voort uit het feit dat er geen negatieve beoordelingen zijn, wat betekent dat de beoordelingen minder gevarieerd en evenwichtig zijn.

Wilson Lower Bound Scores (wilsonlowerbound):
De wilsonlowerbound-waarde is ook hoog. 
Deze waarde biedt meer betrouwbare beoordelingen voor beoordelingen met een laag aantal stemmen, 
en dergelijke scores kunnen betrouwbare resultaten opleveren, zelfs voor beoordelingen met slechts een paar stemmen. 
In de eerste 10 beoordelingen is deze score meestal boven de 0,7, en er zijn veel meer betrouwbare scores. 
Dit betekent dat de meeste beoordelingen betrouwbaar zijn en in overweging kunnen worden genomen.

Lage Scores:
Sommige beoordelingen, zoals die van R. Sutton, Jr. "RWSynergy", R. Heisler en SkincareCEO, hebben lagere wilsonlowerbound- en average_rating_score-waarden. 
Deze beoordelingen hebben vaak lagere stemmingen ontvangen en zijn dus minder betrouwbare beoordelingen. 
Vooral beoordelingen van Amazon-klanten zoals "Kelly" hebben lage scores. 
Dit geeft aan dat hoewel het aantal beoordelingen is gestegen, de beoordelingen minder betrouwbaar kunnen zijn.

Lage Stemmen en Hulp Situaties:
In sommige beoordelingen, zoals bij Twister, Stayeraug en sb21 "sb21", is het aantal stemmen laag, maar de average_rating_score is nog steeds vrij hoog 
en de wilsonlowerbound toont een redelijk waarde. Het lage aantal beoordelingen kan echter de betrouwbaarheid van deze scores beperken.

Conclusies:
Hoge Scores en Betrouwbaarheid: 
Beoordelingen met hoge scores zijn meestal betrouwbare beoordelingen, vooral wanneer zowel average_rating_score als wilsonlowerbound hoog zijn. 
Deze beoordelingen worden over het algemeen als juist en nuttig beschouwd.
Lage Stemmen: Beoordelingen met een laag aantal stemmen kunnen beperkt zijn in betrouwbaarheid, 
maar wanneer ze worden toegevoegd aan een breder beoordelingskader, kunnen er bepaalde patronen worden geïdentificeerd.
Betrouwbaarheidstest: Wilsonlowerbound kan worden gebruikt om beoordelingen met een laag aantal stemmen te testen op betrouwbaarheid. 
Dit is vooral nuttig voor nieuwe of minder bekende producten.
"""
















