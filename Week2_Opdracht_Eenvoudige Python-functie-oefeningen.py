####################################################################
#####################################################################
##                           HUISWERK - 2                         ##
#####################################################################
#####################################################################

# VRAAG 1 (Verilen degerlerin veri yapilari nedir?)
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

# VRAAG 2 (Verilen string ifadenin tum harfleri buyuk harf olsun.
# Virgul ve nokta yerine space koyunuz,
# Kelime kelime ayiriniz)
#############
text = "The goal is to turn data into information, and information into insight."

# Virgül ve noktayı boşluk ile değiştir
text = text.replace(",", "").replace(".", "")

# Kelimeleri bölerek listeye at
word_list = text.split()

print(word_list)
# ['The', 'goal', 'is', 'to', 'turn', 'data', 'into', 'information', 'and', 'information', 'into', 'insight']

# VRAAG 3 (Verilen listeye belirtilen adimlari uygulayiniz)
#############
lst = ["D", "A","T","A","S","C","I","E","N","C","E"]

#Adim1_ Listenin eleman sayisi?
len(lst)  #  --> 11

#Adim2_ Sifirinci ve onuncu indexdeki elemanlar?
lst[0]  # --> "D"
lst[10]  # --> "E"

#Adim3_ Verilen liste uzerinden ["D","A","T","A"] listesi olusturunuz
lest_k = lst[0:4]

#**************************
new_list = []
for i in lst:
    if i == "D" or i == "T" or i == "A":
        new_list.append(i)
print(new_list)    # Çıktı: ['D', 'A', 'T', 'A']

#**********************
new_list = [i for i in lst if i == "D" or i == "T" or i == "A"] # i elemanlari alip new liste atiyor.
print(new_list)  # Çıktı: ['D', 'A', 'T', 'A']

#Adim4_ Sekizinci indexteki elemani siliniz.
dir(lst)
lst.pop(8)
print(lst)

#Adim5_ Yeni bir eleman ekleyiniz
lst.append("F")

#Adim6_ Sekizinci indexe "N" elemanini tekrar eklayiniz
lst.insert(8, "N")

# VRAAG 4 (Verilen sozluk yapisina belirtilen adimlari uygulayiniz)
#############
dict = { "Cristian": ["America", 18],
         "Daisy": ["England", 12],
         "Antonio": [ "Spain", 22],
         "Dante": ["Italy", 25]}

#Adim1_ KEY degerlerine erisiniz
dict.keys()

#Adim2_ VALUE degerlerine erisiniz
dict.values()

#Adim3_ Daisy key ine ait 12 degerini 13 olarak guncelleyiniz
dict["Daisy"] = ["England", 13]

dict["Daisy"][1] = 13

#Adim4_ Key degeri "Ahmet" value degeri [Turkey,24] olan yeni deger ekle
dict.update({"Ahmet" : ["Turkey", 24]})

#Adim5_ Antonio' yu siliniz
dict.pop("Antonio")


# VRAAG 5 (Parametre olarak bir liste alan, listenin icerisindeki tek ve cift sayilari ayri ayri listelere atayabilen
#                   ve bu listeleri return eden fonksiyon yaziniz)
#############
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

even_list, odd_list = delen(list)  ## fonksiyon icinde return tarafindan dondurulen iki liste disarida farkli iki liste degiskenine ataniyor.

delen(l)

# VRAAG 6 (Ilk uc ogrenci Muhendislik; son uc ogrenci Tip fakultesi ogrencisidir.
# listede ki ogrencileri fakultelere gore yazdir. Enumerate kullaniniz)
#############
students = ["Ali", "Veli","Ayse","Talat", "Zeynep", "Ahmet"]

for i, student in enumerate(students, 1):
    if i < 4 :
        print(f"Muhendislik Fakultesi {i}. ogrenci : {student}")

    else:
        print(f"Tıp Fakültesi {i - 3}. öğrenci: {student}")


#Muhendislik Fakultesi 1. ogrenci : Ali
#Muhendislik Fakultesi 2. ogrenci : Veli
#Muhendislik Fakultesi 3. ogrenci : Ayse
#Tıp Fakültesi 1. öğrenci: Talat
#Tıp Fakültesi 2. öğrenci: Zeynep
#Tıp Fakültesi 3. öğrenci: Ahmet
#****************************************************************
messages = [
    f"Muhendislik Fakultesi {i}. ogrenci : {student}" if i < 4
    else f"Tip Fakultesi {i}. ogrenci : {student}"
    for i, student in enumerate(students, 1)
]

for message in messages:
    print(message)

# VRAAG 7 (Asagidaki 3 adet listeyi ZIP kodu kullanarak ders bilgilerini yazdiriniz)
#############
Les_code = ["CMP1005", "PS1001", "HUK1005", "SEN2204"]
Studie_punten = [3,4,2,4]
quatum = [30,75,150,25]

algemeen = zip(Les_code, Studie_punten, quatum)

for code, punten, persoon  in algemeen:
    print(f"Kredisi {punten} olan {code} kodlu dersin kontenjani {persoon} kisidir.")

#Kredisi 3 olan CMP1005 kodlu dersin kontenjani 30 kisidir.
#Kredisi 4 olan PS1001 kodlu dersin kontenjani 75 kisidir.
#Kredisi 2 olan HUK1005 kodlu dersin kontenjani 150 kisidir.
#Kredisi 4 olan SEN2204 kodlu dersin kontenjani 25 kisidir.


# VRAAG 8 (Asagida verilen setlerden 1. set 2. seti kapsiyor ise ortak elemanlarini;
# eger kapsamiyor ise 2. setin 1. setten farkini yazdiracak fonksiyonu kodlayiniz)
#############

kume1 = set(["data", "python"])
kume2 = set(["data", "function", "qcut", "lambda", "python", "miuul"])

if kume1.issuperset(kume2):
    print(kume1.intersection(kume2))
else:
    print(kume2.difference(kume1))

