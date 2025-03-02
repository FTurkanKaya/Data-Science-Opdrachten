
import seaborn as sns
from pandas import isnull
import pandas as pd
import numpy as np

# Taak 1:
## Laad de Titanic dataset uit de Seaborn-bibliotheek
df = sns.load_dataset("titanic")

# Taak 2:
## Zoek het aantal vrouwen en mannen passagiers in de Titanic dataset.
df.head()
df["sex"].value_counts()

# Taak 3:
## Zoek het aantal unieke waarden voor elke kolom.
df.nunique()

# Taak 4:
## Zoek het aantal unieke waarden voor de 'pclass' kolom.
df['pclass'].nunique()

# Taak 5:
## Zoek het aantal unieke waarden voor de 'pclass' en 'parch' kolommen.
column = ["pclass", "parch"]
df[column].nunique()

# Taak 6:
## Controleer het datatype van de 'embarked' kolom.
## Verander het naar 'category' en controleer opnieuw.
df['embarked'].dtype
## -->dtype('O')
df['embarked'] = df['embarked'].astype('category')
df['embarked'].dtype
## -->CategoricalDtype(categories=['C', 'Q', 'S'], ordered=False, categories_dtype=object)

# Taak 7:
## Haal alle gegevens op van passagiers die 'C' zijn in de 'embarked' kolom.
df[df["embarked"] == 'C']

# Taak 8:
## Haal alle gegevens op van passagiers die niet 'S' zijn in de 'embarked' kolom.
df[df["embarked"] != 'S']

# Taak 9:
## Haal alle gegevens op van vrouwelijke passagiers die jonger zijn dan 30 jaar.
df[(df["age"] < 30) & (df["sex"] == 'female')]

# Taak 10:
## Haal gegevens op van passagiers waarvan de 'Fare' groter is dan 500 en de leeftijd ouder is dan 70.
df.columns
df[(df["fare"]  > 500) & (df["age"] > 70)]

# Taak 11:
## Zoek het totaal aantal ontbrekende waarden in elke kolom.
df.isnull().sum()

# Taak 12:
## Verwijder de 'who' kolom uit de DataFrame.
df.drop("who", axis= 1).head()

# Taak 13:
## Vul de ontbrekende waarden in de 'deck' kolom met de meest voorkomende waarde (mode).
# Zoek de meest voorkomende waarde in de 'deck' kolom
df['deck'].value_counts()  ##--> Aantal waarden
mode_value = df['deck'].mode()[0]  ##--> 'C', de meest voorkomende waarde.
## Omdat mode() een serie retourneert, gebruiken we [0] om de eerste waarde te verkrijgen.
df['deck'] = df['deck'].fillna(mode_value)
df["deck"]  ## Toont de gehele kolom

# Taak 14:
## Vul de ontbrekende waarden in de 'age' kolom met de mediaan van de 'age' kolom.
df_median = df["age"].median()
df['age'] = df['age'].fillna(df_median)
df["age"]

# Taak 15:
## Zoek de sum, count en mean van de 'survived' kolom voor de verschillende combinaties van 'pclass' en 'sex' kolommen.
df.groupby(["pclass","sex"]).agg({"survived": ["sum", "count", "mean"]})

# Taak 16:
## Maak een functie die 1 geeft voor passagiers jonger dan 30 jaar en 0 voor de rest. Voeg een nieuwe kolom 'age_flag' toe aan de Titanic dataset.
## Gebruik apply en lambda voor de oplossing.
df['age_flag'] = df['age'].apply(lambda x: 1 if x < 30 else 0)
print(df)

# Taak 17:
## Laad de 'Tips' dataset uit de Seaborn-bibliotheek.
df2 = sns.load_dataset("tips")

# Taak 18:
## Zoek de som, min, max en gemiddelde waarde van de 'total_bill' kolom, gegroepeerd op de 'time' kolom (Dinner, Lunch).
df2.head()
df2.groupby("time")[["total_bill"]].agg(["min", "max", "mean"]).unstack()
df2.groupby("time").agg({"total_bill":["min", "max", "mean"]})

# Taak 19:
## Zoek de som, min, max en gemiddelde waarde van de 'total_bill' kolom, gegroepeerd op de dagen ('day') en 'time'.
df2.groupby(["day", "time"]).agg({"total_bill":["sum","min", "max", "mean"]})

# Taak 20:
## Zoek de som, min, max en gemiddelde waarde van 'total_bill' en 'tip' voor vrouwelijke klanten tijdens 'Lunch', gegroepeerd op 'day'.
female_lunch = df2[(df2["sex"] == "Female") & (df2["time"] == "Lunch")]
female_lunch.groupby("day").agg({"total_bill":["sum", "min", "max", "mean"],
                                 "tip":["sum", "min", "max", "mean"]})

# Taak 21:
## Wat is het gemiddelde van 'total_bill' voor bestellingen waarvan 'size' minder is dan 3 en 'total_bill' groter dan 10? Gebruik loc.
size_total = df2.loc[(df2.loc[:, "size"] < 3) & (df2.loc[:, "total_bill"] > 10),"total_bill"].mean()
print(size_total)

# Taak 22:
## Maak een nieuwe kolom 'total_bill_tip_sum' waarin de som van 'total_bill' en 'tip' voor elke klant wordt weergegeven.
df2['total_bill_tip_sum'] = df2['tip'] + df2['total_bill']

# Taak 23:
## Sorteer de DataFrame op 'total_bill_tip_sum' van groot naar klein en sla de top 30 op in een nieuwe DataFrame.
sorted_df = df2.sort_values(by='total_bill_tip_sum', ascending=False)
top_30 = sorted_df.head(30)

