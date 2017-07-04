
# coding: utf-8

# Describe data
# Author :  Juan Pablo Ramirez G
# Date : July 4, 2017

import matplotlib.pyplot as plt
import datetime as dt
import pandas as pd
import numpy as np


print "Summaring data please wait.."

# Read and sort data
data = pd.read_csv('Temperature_2013_01_01__2017_05_31.csv')
data['fecha_hora'] = pd.to_datetime(data['fecha_hora'])
data = data.sort_values(by='fecha_hora')

'''#Get data in period
start = dt.datetime(2013, 1, 1)
end = dt.datetime(2015, 3, 1)
periodo = data[(data['fecha_hora'] > start) & (data['fecha_hora'] < end)]
period = periodo.copy()
'''
periodo = data.copy()
period = periodo.copy()

# Grouop data
period['year'] = periodo['fecha_hora'].dt.year
period['month'] = periodo['fecha_hora'].dt.month
period['day'] = periodo['fecha_hora'].dt.day
period = period.drop(['fecha_hora','Calidad', 'wrong_values', 'index_r'],1)

# Get global info about data
# by day
temp_mean_d = period.groupby(['year', 'month', 'day']).mean()
temp_meand = temp_mean_d.Temperatura.as_matrix()
temp_meand = temp_meand[np.newaxis].T

temp_std_d = period.groupby(['year', 'month', 'day']).std()
temp_stdd = temp_std_d.Temperatura.as_matrix()
temp_stdd = temp_stdd[np.newaxis].T

temp_min_d = period.groupby(['year', 'month', 'day']).min()
temp_mind = temp_min_d.Temperatura.as_matrix()
temp_mind = temp_mind[np.newaxis].T

temp_25_d = period.groupby(['year', 'month', 'day']).quantile(.25)
temp_25d = temp_25_d.Temperatura.as_matrix()
temp_25d = temp_25d[np.newaxis].T

temp_50_d = period.groupby(['year', 'month', 'day']).quantile(.50)
temp_50d = temp_50_d.Temperatura.as_matrix()
temp_50d = temp_50d[np.newaxis].T

temp_75_d = period.groupby(['year', 'month', 'day']).quantile(.75)
temp_75d = temp_75_d.Temperatura.as_matrix()
temp_75d = temp_75d[np.newaxis].T

temp_max_d = period.groupby(['year', 'month', 'day']).max()
temp_maxd = temp_max_d.Temperatura.as_matrix()
temp_maxd = temp_maxd[np.newaxis].T

temp_skew_d = period.groupby(['year', 'month', 'day']).skew()
temp_skewd = temp_skew_d.Temperatura.as_matrix()
temp_skewd = temp_skewd[np.newaxis].T

temp_var_d = period.groupby(['year', 'month', 'day']).var()
temp_vard = temp_var_d.Temperatura.as_matrix()
temp_vard = temp_vard[np.newaxis].T


# by month
temp_mean_m = period.groupby(['year', 'month']).mean()
temp_meanm = temp_mean_m.Temperatura.as_matrix()
temp_meanm = temp_meanm[np.newaxis].T

temp_std_m = period.groupby(['year', 'month']).std()
temp_stdm = temp_std_m.Temperatura.as_matrix()
temp_stdm = temp_stdm[np.newaxis].T

temp_min_m = period.groupby(['year', 'month']).min()
temp_minm = temp_min_m.Temperatura.as_matrix()
temp_minm = temp_minm[np.newaxis].T

temp_25_m = period.groupby(['year', 'month']).quantile(.25)
temp_25m = temp_25_m.Temperatura.as_matrix()
temp_25m = temp_25m[np.newaxis].T

temp_50_m = period.groupby(['year', 'month']).quantile(.50)
temp_50m = temp_50_m.Temperatura.as_matrix()
temp_50m = temp_50m[np.newaxis].T

temp_75_m = period.groupby(['year', 'month']).quantile(.75)
temp_75m = temp_75_m.Temperatura.as_matrix()
temp_75m = temp_75m[np.newaxis].T

temp_max_m = period.groupby(['year', 'month']).max()
temp_maxm = temp_max_m.Temperatura.as_matrix()
temp_maxm = temp_maxm[np.newaxis].T

temp_skew_m = period.groupby(['year', 'month']).skew()
temp_skewm = temp_skew_m.Temperatura.as_matrix()
temp_skewm = temp_skewm[np.newaxis].T

temp_var_m = period.groupby(['year', 'month']).var()
temp_varm = temp_var_m.Temperatura.as_matrix()
temp_varm = temp_varm[np.newaxis].T


# by year
temp_mean_y = period.groupby(['year']).mean()
temp_meany = temp_mean_y.Temperatura.as_matrix()
temp_meany = temp_meany[np.newaxis].T

temp_std_y = period.groupby(['year']).std()
temp_stdy = temp_std_y.Temperatura.as_matrix()
temp_stdy = temp_stdy[np.newaxis].T

temp_min_y = period.groupby(['year']).min()
temp_miny = temp_min_y.Temperatura.as_matrix()
temp_miny = temp_miny[np.newaxis].T

temp_25_y = period.groupby(['year']).quantile(.25)
temp_25y = temp_25_y.Temperatura.as_matrix()
temp_25y = temp_25y[np.newaxis].T

temp_50_y = period.groupby(['year']).quantile(.50)
temp_50y = temp_50_y.Temperatura.as_matrix()
temp_50y = temp_50y[np.newaxis].T

temp_75_y = period.groupby(['year']).quantile(.75)
temp_75y = temp_75_y.Temperatura.as_matrix()
temp_75y = temp_75y[np.newaxis].T

temp_max_y = period.groupby(['year']).max()
temp_maxy = temp_max_y.Temperatura.as_matrix()
temp_maxy = temp_maxy[np.newaxis].T

temp_skew_y = period.groupby(['year']).skew()
temp_skewy = temp_skew_y.Temperatura.as_matrix()
temp_skewy = temp_skewy[np.newaxis].T

temp_var_y = period.groupby(['year']).var()
temp_vary = temp_var_y.Temperatura.as_matrix()
temp_vary = temp_vary[np.newaxis].T


# Show information

# Temperature summary by year
temp_mean_y = temp_mean_y.drop(['day','month'],1)
temp_year = temp_mean_y.assign(temp_mean = temp_meany,
                               temp_std=temp_stdy,
                               temp_min = temp_miny,
                               temp_max = temp_maxy,
                               temp_25 = temp_25y,
                               temp_50 = temp_50y,
                               temp_75 = temp_25y,
                               temp_var = temp_vary,
                               temp_skew = temp_skewy
                              ).copy()


# Temperature summary by Month
temp_mean_m = temp_mean_m.drop(['day'],1)
temp_month = temp_mean_m.assign(temp_mean = temp_meanm,
                               temp_std=temp_stdm,
                               temp_min = temp_minm,
                               temp_max = temp_maxm,
                               temp_25 = temp_25m,
                               temp_50 = temp_50m,
                               temp_75 = temp_25m,
                               temp_var = temp_varm,
                               temp_skew = temp_skewm
                              ).copy()

# Temperature summary by day
temp_day = temp_mean_d.assign(temp_mean = temp_meand,
                               temp_std=temp_stdd,
                               temp_min = temp_mind,
                               temp_max = temp_maxd,
                               temp_25 = temp_25d,
                               temp_50 = temp_50d,
                               temp_75 = temp_25d,
                               temp_var = temp_vard,
                               temp_skew = temp_skewd
                              ).copy()


temp_day.to_csv('Temperature_summary_day.csv', sep=',')

temp_month.to_csv('Temperature_summary_month.csv', sep=',')

temp_year.to_csv('Temperature_summary_year.csv', sep=',')


# Plotting data
# Temperature average by year
labels = ['2013', '2014', '2015' ,'2016' ,'2017']
x = list(range(temp_meany.shape[0]))

plt.figure()
plt.scatter(x, temp_meany)
plt.plot(x, temp_meany, label="Temp Mean")

plt.scatter(x, temp_miny)
plt.plot(x, temp_miny, label="Temp Min")

plt.scatter(x, temp_maxy)
plt.plot(x, temp_maxy,label="Temp Max")
plt.xticks(x, labels)
plt.xlabel('YEAR')
plt.ylabel('Temperature average')
plt.ylim((5,35))

plt.legend(loc='lower right')
plt.show()

print "Summary finished, review the files Summary."

print "Temperature_summary_year.csv"
print "Temperature_summary_month.csv"
print "Temperature_summary_day.csv'"
