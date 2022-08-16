import pandas as pd
import time
import datetime
pd.set_option('display.max_columns', None)

# Section cleans up datasets, dropping NaNs and converting dates to epoch time
# openweather = pd.read_csv('Sources/openweather.csv', sep = ';', header = 0)
# dict = list(openweather.columns)
# dict[0] = "timestamp"
# for index, row in openweather.iterrows():
#   val = openweather.at[index,"dt_iso.1"]
#   openweather.at[index,"dt_iso.1"] = time.mktime(datetime.datetime.strptime(val, "%Y-%m-%d %H:%M").timetuple())
# print (openweather.at[6654,"dt_iso.1"]) #sample to check if conversion worked
# openweather.to_csv('Products/openweather2.csv', sep = ';', header = dict, index=False)

# laertis = pd.read_csv('Sources/Laertis2.csv', sep = ';', header = 0)
# dict = ["Laertis_timestamp","Laertis_humidity","Laertis_temperature","Laertis_pressure","Laertis_eCO2","Laertis_TVOC","Laertis_light","Laertis_PM1","Laertis_dBA","Laertis_PM10","Laertis_PM2.5"]

# laertis = laertis.dropna()
# for index, row in laertis.iterrows():
#   val = laertis.at[index,"timestamp.1"]
#   laertis.at[index,"timestamp.1"] = time.mktime(datetime.datetime.strptime(val, "%Y-%m-%d %H:%M").timetuple())
# print (laertis.at[6654,"timestamp.1"])
# laertis.to_csv('Products/laertisNew.csv', sep = ';', header = dict, index=False)

openweather = pd.read_csv('Products/openweather2.csv', sep = ';', header = 0)
laertis = pd.read_csv('Products/laertisNew.csv', sep = ';', header = 0)

dict = list(laertis.columns) + list(openweather.columns)
dict.pop(11)
print(dict)
# Section merges datasets
dataset = pd.merge(laertis,openweather,how='outer',on="timestamp")
dataset = dataset.interpolate(method='cubic', axis=0)

print(dataset.head(1))

dataset = dataset[dataset['weather_id'].notna()]
dataset = dataset[dataset['Laertis_humidity'].notna()]
dataset.to_csv('Products/dataset.csv', sep = ';', header = dict, index = False)
# weather_id,'''