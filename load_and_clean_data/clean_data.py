# coding: utf-8

# load_and_clean_data_temperature
# Author :  Juan Pablo Ramirez G
# Date : July 4, 2017

import glob
import datetime as dt
import pandas as pd
import numpy as np

print "Loading and cleaning Data, please wait..."

# Load all csv files
path ='datos' # path files
allFiles = glob.glob(path + "/*.csv")
data = pd.DataFrame()
list_ = []
for file_ in allFiles:
    df = pd.read_csv(file_)
    list_.append(df)
data = pd.concat(list_)

# Ordering data by datetime
data['fecha_hora'] = pd.to_datetime(data['fecha_hora'])
data = data.sort_values(by='fecha_hora')

# Reindexing data
re_index = list(range(data.shape[0]))
data['index_r'] = re_index
data = data.set_index('index_r')

# Fixing wrong values
data['wrong_values'] = data['Temperatura']
# Calidad 151, 1513; Temperatura = 0
data.loc[data['Calidad'] == 151, 'Temperatura'] = None
data.loc[data['Calidad'] == 1513, 'Temperatura'] = None
data.loc[data['Temperatura'] == 0, 'Temperatura'] = None
t = data['Temperatura']
t2 = t.interpolate('values')
data['Temperatura'] = t2
data['Temperatura'] = data['Temperatura'].replace({None: 24.6})

# Store clean and sorted data
data.to_csv('Temperature_2013_01_01__2017_05_31.csv', sep=',')

print "Cleaning finished."
print "Look at Temperature_2013_01_01__2017_05_31.csv file."
