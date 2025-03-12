###################################################
# Rating Products
###################################################
import pandas as pd
import math
import scipy.stats as st
from sklearn.preprocessing import MinMaxScaler

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 500)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.float_format', lambda x: '%.5f' % x)

####################
# Time-Based Weighted Average
####################

def weighted_average_time_based(dataframe, value_col, day_col, w1=28, w2=26, w3=24, w4=22):
    return dataframe.loc[dataframe[day_col] <= 30, value_col].mean() * w1 / 100 + \
           dataframe.loc[(dataframe[day_col] > 30) & (dataframe[day_col] <= 90), value_col].mean() * w2 / 100 + \
           dataframe.loc[(dataframe[day_col] > 90) & (dataframe[day_col] <= 180), value_col].mean() * w3 / 100 + \
           dataframe.loc[(dataframe[day_col] > 180), value_col].mean() * w4 / 100

####################
# User-Based Weighted Average
####################
def weighted_average_user_based(dataframe,value_col,evaluation_col, w1=22, w2=24, w3=26, w4=28):
    return dataframe.loc[dataframe[value_col,] <= 10, evaluation_col].mean() * w1 / 100 + \
           dataframe.loc[(dataframe[value_col,] > 10) & (dataframe[value_col,] <= 45), evaluation_col].mean() * w2 / 100 + \
           dataframe.loc[(dataframe[value_col,] > 45) & (dataframe[value_col,] <= 75), evaluation_col].mean() * w3 / 100 + \
           dataframe.loc[(dataframe[value_col,] > 75), evaluation_col].mean() * w4 / 100


####################
# Weighted Rating      Gebalanceerde meting, zowel op tijds- als gebruikersbasis beoordeeld
####################

def weighted_course_rating(dataframe, time_w=50, user_w=50):
    return weighted_average_time_based(dataframe) * time_w/100 + weighted_average_user_based(dataframe)*user_w/100

#********************************************************************************************************************************************


############################################
# SORTING REVIEWS  --->>> Goed reviews / Slecht reviews
############################################
import pandas as pd
import math
import scipy.stats as st

pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.float_format', lambda x: '%.5f' % x)

###################################################
# Up-Down Diff Score = (up ratings) − (down ratings)   -->> Welke comment is beter
###################################################
def up_down_score_diff(up, down):
    return up - down


###################################################
# Score = Average rating = (up ratings) / (all ratings) --  Nuttigheidsratio. Hoeveel voordeel wordt behaald?
###################################################

def average_rating_score(up, down):
    if up + down == 0:
        return 0
    return up / (up + down)

###################################################
# Wilson Lower Bound Score  -->> Berekenen van de kansverhoudingen van binaire gebeurtenissen
###################################################

def wilsonlowerbound(up, down, confidence=0.95):
    """
    Berekenen van de Wilson Lower Bound Score

De onderste grens van het betrouwbaarheidsinterval, berekend voor de Bernoulli-parameter p, wordt geaccepteerd als de WLB-score.
De te berekenen score wordt gebruikt voor de productranglijst.
Opmerking:
Als de scores tussen 1-5 liggen, worden 1-3 als negatief en 4-5 als positief gemarkeerd, en kunnen ze geschikt worden gemaakt voor Bernoulli (er zijn twee toestanden: negatief-positief — heeft ongeluk gehad/heeft geen ongeluk gehad...). Dit wordt gedaan om een binaire toestand te creëren. Dit brengt enkele problemen met zich mee. Daarom moet de Bayesiaanse gemiddelde score worden berekend.

Parameters
up: int
Aantal positieve stemmen

down: int
Aantal negatieve stemmen

confidence: float
Betrouwbaarheid

Return
Wilson score: float
"""
    n = up + down
    # n bir tam sayı olduğu için direkt karşılaştırma yapıyoruz
    if n == 0:
        return 0
    z = st.norm.ppf(1 - (1 - confidence) / 2)
    phat = 1.0 * up / n
    return (phat + z * z / (2 * n) - z * math.sqrt((phat * (1 - phat) + z * z / (4 * n)) / n)) / (1 + z * z / n)



























