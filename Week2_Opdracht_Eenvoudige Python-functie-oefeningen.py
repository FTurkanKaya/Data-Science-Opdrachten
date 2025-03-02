####################################################################
#####################################################################
##                           OPDRACHT - 2                         ##
#####################################################################
#####################################################################

# VRAAG 1 (Wat zijn de gegeven waarden voor datatypes?)
#############
x= 8

# --->>  int

y = 3.2
# --->>  float

z = 8j + 18
# --->>  complex

a = "Hello World"
# --->>  str

c = 23 < 22
# --->>  bool

l= [1,2,3,4]
# --->>  List

d = {"Name": "Jake",
     "Age": 27,
     "Address": "Downtown"}
# --->>  dict

t = ("MachineLearning", "Data Science")
# --->>  tuple

s = {"Python","Machine Learning", "Data Science"}
# --->>  set

type(s)

#VRAAG 2 (Maak alle letters in de gegeven string hoofdletters.
# Vervang komma's en punten door spaties en splits de string in afzonderlijke woorden.)
#############
text = "The goal is to turn data into information, and information into insight."

# Vervang komma's en punten door een spatie
text = text.replace(",", "").replace(".", "")

# Splits de woorden en zet ze in een lijst
word_list = text.split()

print(word_list)
# ['The', 'goal', 'is', 'to', 'turn', 'data', 'into', 'information', 'and', 'information', 'into', 'insight']


# VRAAG 3 (Voer de onderstaande stappen uit op de gegeven lijst.)
#############
lst = ["D", "A","T","A","S","C","I","E","N","C","E"]

# Stap1_ Hoeveel elementen heeft de lijst?
len(lst)  #  --> 11

# Stap2_ Het element op index 0 en index 10?
lst[0]  # --> "D"
lst[10]  # --> "E"

# Stap3_ Maak een lijst met de elementen ["D","A","T","A"]
lest_k = lst[0:4]

#**************************
new_list = []
for i in lst:
    if i == "D" or i == "T" or i == "A":
        new_list.append(i)
print(new_list)    # Uitvoer: ['D', 'A', 'T', 'A']

#**********************
new_list = [i for i in lst if i == "D" or i == "T" or i == "A"]  # Voeg de elementen "D", "T" of "A" toe aan de nieuwe lijst.
print(new_list)  # Uitvoer: ['D', 'A', 'T', 'A']

# Stap4_ Verwijder het element op index 8.
dir(lst)
lst.pop(8)
print(lst)

# Stap5_ Voeg een nieuw element toe.
lst.append("F")

# Stap6_ Voeg het element "N" opnieuw toe op index 8.
lst.insert(8, "N")


# VRAAG 4 (Voer de aangegeven stappen uit op de gegeven woordenboekstructuur.)
#############
dict = { "Cristian": ["America", 18],
         "Daisy": ["England", 12],
         "Antonio": [ "Spain", 22],
         "Dante": ["Italy", 25]}

# Stap1_ Verkrijg de sleutels (keys)
dict.keys()

# Stap2_ Verkrijg de waarden (values)
dict.values()

# Stap3_ Werk de waarde van de sleutel "Daisy" bij naar 13 in plaats van 12
dict["Daisy"] = ["England", 13]

dict["Daisy"][1] = 13

# Stap4_ Voeg een nieuw element toe: sleutel "Ahmet", waarde ["Turkey", 24]
dict.update({"Ahmet" : ["Turkey", 24]})

# Stap5_ Verwijder "Antonio"
dict.pop("Antonio")



# VRAAG 5 (Schrijf een functie die een lijst als parameter neemt en de even
# en oneven getallen in aparte lijsten plaatst en deze lijsten retourneert.)
#############
l = [2,13,18,93,22]

l = [2,13,18,93,22]

def delen(lis):
     even_list = []
     odd_list = []
     for i in l:
          if i % 2 == 0:
               even_list.append(i)
          else:
               odd_list.append(i)
     return even_list, odd_list

even_list, odd_list = delen(list)  ## De twee lijsten die worden geretourneerd door de functie, worden toegewezen aan twee afzonderlijke variabelen buiten de functie.

delen(l)

# VRAAG 6 (De eerste drie studenten zijn van de Faculteit Ingenieurswetenschappen;
# de laatste drie studenten zijn van de Faculteit Geneeskunde.
# Print de studenten op basis van hun faculteit. Gebruik enumerate.)
#############
students = ["Ali", "Veli","Ayse","Talat", "Zeynep", "Ahmet"]

for i, student in enumerate(students, 1):
    if i < 4 :
        print(f"Faculteit Ingenieurswetenschappen {i}. student: {student}")

    else:
        print(f"Faculteit Geneeskunde {i - 3}. student: {student}")

#****************************************************************
messages = [
    f"Muhendislik Fakultesi {i}. ogrenci : {student}" if i < 4
    else f"Tip Fakultesi {i}. ogrenci : {student}"
    for i, student in enumerate(students, 1)
]

for message in messages:
    print(message)

# VRAAG 7 (Gebruik de ZIP-functie om de onderstaande 3 lijsten samen te voegen
# en de cursusinformatie af te drukken.)
#############
Les_code = ["CMP1005", "PS1001", "HUK1005", "SEN2204"]
Studie_punten = [3,4,2,4]
quatum = [30,75,150,25]

algemeen = zip(Les_code, Studie_punten, quatum)

for code, punten, persoon  in algemeen:
    print(f"De cursus met code {code}, heeft {punten} studiepunten en de capaciteit is {persoon} personen.")



# VRAAG 8 (Als de eerste set de tweede set bevat,
# print dan de gemeenschappelijke elementen;
# als dat niet het geval is, print dan het verschil van de tweede set ten opzichte van de eerste set.)
#############

kume1 = set(["data", "python"])
kume2 = set(["data", "function", "qcut", "lambda", "python", "miuul"])

if kume1.issuperset(kume2):
    print(kume1.intersection(kume2))
else:
    print(kume2.difference(kume1))


