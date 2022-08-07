from csv import reader
import string
import pandas as pd
from regex import F
import time
import datetime

pd.set_option('display.max_columns', None)

# openweather = pd.read_csv('openweather.csv', sep = ';', header = None)
# print(openweather.head())


laertis = pd.read_csv('Laertis2.csv', sep = ';', header = None)
laertis = laertis.dropna()

for index, row in laertis.iterrows():
    unixtest = time.mktime(datetime.datetime.strptime(laertis[0][index], "%Y-%m-%d %H:%M").timetuple())
    laertis[0][index] = unixtest

laertis.to_csv('Laertis2.csv', sep = ';', header = None, index = False)