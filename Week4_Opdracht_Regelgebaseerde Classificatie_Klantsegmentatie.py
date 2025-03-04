####################################################################
#####################################################################
##                           OPDRACHT - 4                         ##
#####################################################################
#####################################################################
"""
Werkprobleem
Een mobiel applicatiebedrijf wil gebruik maken van bepaalde demografische
en gebruiksinformatie van gebruikers om nieuwe klantprofielen te creëren
en het gemiddelde inkomen te voorspellen dat nieuwe klanten aan het bedrijf kunnen bijdragen op basis van deze segmenten.
"""
###############################################################
#TAAK-1 Aantwoord onderstaande vragen:
###############################################################
# VRAAG 1 (Lees het bestand customers.csv in
#           en toon algemene informatie over de dataset.)

import pandas as pd
#csv okuma
df = pd.read_csv("customers.csv", sep = ",")

#*******************************************************************************
##  VRAAG 2 (Hoeveel unieke PLATFORM waarden zijn er? Wat zijn de frequenties?)

df["PLATFORM"].nunique()
df["PLATFORM"].value_counts().count()

#Frequenties:
df["PLATFORM"].value_counts()

#*******************************************************************************
##  VRAAG 3 (Hoeveel unieke PRICE waarden zijn er?)
df["PRICE"].nunique()
df["PRICE"].value_counts().count()

#*******************************************************************************
##  VRAAG 4 (Hoeveel verkopen zijn er voor elke PRICE waarde?)

df.groupby("PRICE")["PLATFORM"].count()
df.groupby("PRICE").size()

#*******************************************************************************
##  VRAAG 5 (Uit welk land zijn er hoeveel verkopen?)

df.groupby("REGION")["PLATFORM"].count()
df.groupby("REGION").size()

#*******************************************************************************
##  VRAAG 6 (Hoeveel winst is er gemaakt per land?)

df.groupby("REGION")["PRICE"].sum()

#*******************************************************************************
##  VRAAG 7 (Wat zijn de verkoopcijfers per PLATFORM type?)

df.groupby("PLATFORM")["PRICE"].count()
df.groupby("PLATFORM").size()

#*******************************************************************************
##  VRAAG 8 (Wat zijn de gemiddelde PRICE waarden per land?)

df.groupby("REGION")["PRICE"].median()


#*******************************************************************************
##  VRAAG 9 (Wat zijn de gemiddelde PRICE waarden per PLATFORM?)

df.groupby("PLATFORM")["PRICE"].median()

#*******************************************************************************
##  VRAAG 10 (Wat zijn de gemiddelde PRICE waarden per REGION-PLATFORM combinatie?)

df.groupby(["REGION", "PLATFORM"])["PRICE"].median()


###############################################################
#TAAK-2 Wat zijn de gemiddelde inkomsten per region, platform, gender, leeftijdsgroep?
###############################################################
df.groupby(["REGION", "PLATFORM", "GENDER", "AGE"])["PRICE"].median()


###############################################################
#TAAK-3 Sorteer de output op aflopende volgorde van PRICE en sla de resultaten op als agg_df.
###############################################################
agg_df = (df.groupby(["REGION", "PLATFORM", "GENDER", "AGE"])["PRICE"]
          .median()
          .sort_values(ascending = False))

###############################################################
#TAAK-4 Definieer de namen in de index als variabelen.
###############################################################

agg_df = agg_df.reset_index()

# agg_df was een series, maar nu is het een dataframe geworden.!!!!

###############################################################
#TAAK-5 Maak de AGE variabele categorisch en voeg deze toe aan agg_df.
#       De leeftijdscategorieën moeten als volgt zijn.
#       0_18
#       19_23
#       24_30
#       31_40
#       41_70
###############################################################

agg_df["AGE"] = pd.Categorical(agg_df["AGE"])
agg_df["AGE"].dtype

labels = ["0-18", "19-23", "24-30", "31-40", "41-70"]

agg_df["AGE"] = pd.cut(agg_df["AGE"], [0, 18, 23, 30, 40, 70], labels = labels)

###############################################################
#TAAK-6 Maak nieuwe niveau-gebaseerde klantgroepen. Voeg een nieuwe variabele toe: customer_profile.
###############################################################






###############################################################
#TAAK-7
"""
Verdeel de nieuwe klanten (bijvoorbeeld: USA_ANDROID_MALE_0_18) in 4 segmenten op basis van PRICE.

Voeg de segmenten toe als een nieuwe variabele met de naam SEGMENT aan agg_df.
Beschrijf de segmenten (groepeer op segmenten en haal de gemiddelde, 
maximale en som van de prijs op). Hint: gebruik pd.qcut(agg_df[“PRICE”], 4, labels=[“D”, “C”, “B”, “A”])
"""
###############################################################










###############################################################
#TAAK-8
"""
Classificeer de nieuwe klanten en voorspel hoeveel inkomen ze kunnen genereren.

In welk segment valt een 33-jarige Turkse vrouw die Android gebruikt en hoeveel inkomen wordt gemiddeld verwacht?
In welk segment valt een 35-jarige Franse vrouw die iOS gebruikt en hoeveel inkomen wordt gemiddeld verwacht?
"""
###############################################################









