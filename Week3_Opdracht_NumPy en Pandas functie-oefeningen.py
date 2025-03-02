

##  GOREV 1:
##  Seaborn kutuphanesi icinden Titanic veri setini tanimlayiniz
import seaborn as sns
from pandas import isnull

df = sns.load_dataset("titanic")

#****************************************************************************
##  GOREV 2:
##  Titanic veri setindeki kadin ve erkek yolcularin sayisini bulunuz.
df.head()
df["sex"].value_counts()

#****************************************************************************
##  GOREV 3:
##  Her bir sutuna ait unique degerlerin sayisini bulunuz.
df.nunique()

#****************************************************************************
##  GOREV 4:
##  'pclass' degiskeninin unique degerlerinin sayisini bulunuz.
df['pclass'].nunique()

#****************************************************************************
##  GOREV 5:
##  'pclass'  ve ' parch' degiskeninin unique degerlerinin sayisini bulunuz.
column = ["pclass", "parch"]
df[column].nunique()

#****************************************************************************
##  GOREV 6:
##  'embarked' degiskeninin tipini kontrol ediniz.
## Tipini category olarak degistiriniz ve tekrar kontrol ediniz.

df['embarked'].dtype
        # -->dtype('O')

df['embarked'] = df['embarked'].astype('category')
df['embarked'].dtype
        # -->CategoricalDtype(categories=['C', 'Q', 'S'], ordered=False, categories_dtype=object)

#****************************************************************************
##  GOREV 7:
##  'embarked' degeri 'C' olanlarin tum bilgilerini isteyiniz

df[df["embarked"] == 'C']

#****************************************************************************
##  GOREV 8:
##  'embarked' degeri 'S' olmayanlarin tum bilgilerini isteyiniz
df[df["embarked"] != 'S']

#****************************************************************************
##  GOREV 9:
##  Yasi 30 dan kucuk olan kadin yolcularin tum bilgilerini gosteriniz
df[(df["age"] < 30) & (df["sex"] == 'female')]

#****************************************************************************
##  GOREV 10:
##  'Fare'i 500 den buyuk ve yasi 70 den buyuk yolcularin bilgilerini gosteriniz
df.columns
df[(df["fare"]  > 500) & (df["age"] > 70)]

#****************************************************************************
##  GOREV 11:
##  Her bir degiskendeki bos degerlerin toplamini bulunuz.
df.isnull().sum()

#****************************************************************************
##  GOREV 12:
##  'who' degiskenini dataframe den cikariniz.
df.drop("who", axis= 1).head()

#****************************************************************************
##  GOREV 13:
##  'deck'degiskenindeki bos degerleri deck degiskeninin en cok tekrar eden degeri (mode) ile doldurunuz.

# 'deck' sütunundaki en çok tekrar eden değeri (mode) bulalım
df['deck'].value_counts() ##---> degerlerin sayisal ifadesi

mode_value = df['deck'].mode()[0]  ##--> 'C'   en çok tekrar eden değeri alır.
                                   # mode() fonksiyonu bir seri döndürdüğü için,
                                   #   [0] ile ilk değeri alıyoruz.

df['deck'] = df['deck'].fillna(mode_value)
df["deck"]  ##--Tum Column u gosterir

#****************************************************************************
##  GOREV 14:
##  'age' degiskenindeki bos degerleri ege degiskeninin medyani ile doldurunuz.

df_median = df["age"].median()
df['age'] = df['age'].fillna(df_median)
df["age"]

#****************************************************************************
##  GOREV 15:
##  'survived' degiskeninin 'pclass' ve 'cinsiyet' degiskenleri kiriliminda
    ## sum, count, mean degerlerini bulunuz

df.groupby(["pclass","sex"]).agg({"survived": ["sum", "count", "mean"]})

#****************************************************************************
##  GOREV 16:
##  30 yasin altinda olanlar 1; 30 yasin ustunde olanlara 0 verecek bir fonksiyon yazin.
##  yazdiginiz fonksiyonu kullanarak titanik veri setinde 'age_flag' adinda bir degisken olusturun.
##  (apply ve lambda yapilarini kullaniniz)

# 'age_flag' sütununu oluşturup, 30'dan küçükse 1, aksi takdirde 0 atayalım
df['age_flag'] = df['age'].apply(lambda x: 1 if x < 30 else 0)

print(df)

#****************************************************************************
##  GOREV 17:
##  Seaborn kutuphanesi icerisinden 'Tips' veri setini tanimlayiniz.
df2 = sns.load_dataset("tips")

##  GOREV 18:
## 'Time' degiskeninin kategorilerine (Dinner, Lunch) gore
##  total_bill degerlerinin toplamini, min,max ve ortalamasini bulunuz.

df2.head()
df2.groupby("time")[["total_bill"]].agg(["min", "max", "mean"]).unstack()

df2.groupby("time").agg({"total_bill":["min", "max", "mean"]})

#****************************************************************************
##  GOREV 19:
##  Gunlere ve time gore total_bill degerlerinin toplamini, min, max ve ortalamasini bulunuz.

df2.groupby(["day", "time"]).agg({"total_bill":["sum","min", "max", "mean"]})

#****************************************************************************
##  GOREV 20:
##  Lunch zamanina ve kadin musterilere ait 'total_bill ve tip' degerlerinin 'day''e gore
##  toplamini, min, max ve ortalamasini bulunuz.
import pandas as pd

import pandas as pd

# "Lunch" zamanındaki ve "Female" müşterilere ait verileri filtrele
female_lunch = df2[(df2["sex"] == "Female") & (df2["time"] == "Lunch")]  ## daha guvenli. kolon adi farkli karakter icerebilir
# veya
female_lunch1 = df2[(df2.sex == "Female") & (df2.time == "Lunch")]  ## Pandas column adini bir fonksiyon veya property sanabilir.
# Günlere (day) göre total_bill ve tip değerlerinin toplamı, min, max ve ortalamasını hesapla
female_lunch.groupby("day").agg({"total_bill":["sum", "min", "max", "mean"],
                                 "tip":["sum", "min", "max", "mean"]})




#****************************************************************************
##  GOREV 21:
##  'size' i 3 den kucuk, 'total_bill' 10 dan buyuk olan siparislerin ortalamasi nedir? [loc kullaniniz)
import numpy as np
df2.head()

size_total = df2.loc[(df2.loc[:, "size"] < 3) & (df2.loc[:, "total_bill"] > 10),"total_bill"].mean()  ## Loc kullanimda adres belirtmek gerekir. 'total_bill'

size_total.mean()  ## Bazi sutunlarda categorik veri oldugu icin hata veriyor.
print(size_total)

size_total.apply(np.mean)  ## Bazi sutunlarda categorik veri oldugu icin hata veriyor.

size_total.transform(lambda x: (x.mean()))  ## Bazi sutunlarda categorik veri oldugu icin hata veriyor.

#****************************************************************************
##  GOREV 22:
## 'total_bill_tip_sum adinda yeni bir degisken olusturunuz.
##  Her bir musterinin odedigi 'totalbill' ve 'tip' in toplamini versin

# 'tip' ve 'total_bill' sütunlarının toplamını 'total_bill_tip_sum' adında yeni bir sütun olarak ekleyelim
df2['total_bill_tip_sum'] = df2['tip'] + df2['total_bill']

#****************************************************************************
##  GOREV 23:
##  'total_bill_tip_sum' degiskenine gore buyukten kucuge gore siralayiniz ve
##  ilk 30 kisiyi yeni bir dataframe'e atayiniz.

sorted_df = df2.sort_values(by='total_bill_tip_sum', ascending=False)

# İlk 30
top_30 = sorted_df.head(30)

