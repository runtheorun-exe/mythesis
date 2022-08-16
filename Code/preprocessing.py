import pandas as pd
import time
import datetime
pd.set_option('display.max_columns', None)

# Section cleans up datasets, dropping NaNs and converting dates to epoch time
openweather = pd.read_csv('Sources/openweather.csv', sep = ';', header = 0)
for index, row in openweather.iterrows():
  if index != 0 :    
    openweather[0][index] = time.mktime(datetime.datetime.strptime(openweather[0][index], "%Y-%m-%d %H:%M").timetuple())
print (openweather[0][0])
openweather.to_csv('Products/openweather2.csv', sep = ';', header = None, index = False)

laertis = pd.read_csv('Sources/Laertis2.csv', sep = ';', header = 0)
laertis = laertis.dropna()
for index, row in laertis.iterrows():
  if index != 0 :
    laertis[0][index] = time.mktime(datetime.datetime.strptime(laertis[0][index], "%Y-%m-%d %H:%M").timetuple())

laertis.to_csv('Products/laertisNew.csv', sep = ';', header = None, index = False)

openweather = pd.read_csv('Products/openweather2.csv', sep = ';', header = 0)
laertis = pd.read_csv('Products/laertisNew.csv', sep = ';', header = 0)

dataset = pd.merge(laertis,openweather,how='outer',on="timestamp")
dataset = dataset.interpolate(method='cubic', axis=0)
print(dataset.head(1))

dataset.to_csv('Products/dataset.csv', sep = ';', header = None, index = False)