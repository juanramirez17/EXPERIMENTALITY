# coding: utf-8

# Polynomial model and kalman filter
# Author :  Juan Pablo Ramirez G
# Date : July 4, 2017

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import Ridge
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
import datetime as dt

print "predicting, please wait..."

# Read and sort data
data = pd.read_csv('Temperature_2013_01_01__2017_05_31.csv')
data['fecha_hora'] = pd.to_datetime(data['fecha_hora'])
data = data.sort_values(by='fecha_hora')

# Set date from you want predict temperature, for the seven next days
# example: date_prediction_to = dt.datetime(2015, 1, 1) from Enero 1, 2013
date_prediction_to = dt.datetime(2015, 2, 28)

# Getting period for fit(train) the model
start_day = date_prediction_to - dt.timedelta(days=8)
end_day = date_prediction_to - dt.timedelta(days=1)

# Group data and delete unnecesary columns for period
period_ = data[(data['fecha_hora'] > start_day) & (data['fecha_hora'] < end_day)]
period = period_.copy()
period['year'] = period_['fecha_hora'].dt.year
period['month'] = period_['fecha_hora'].dt.month
period['day'] = period_['fecha_hora'].dt.day
period = period.drop(['fecha_hora','Calidad', 'wrong_values', 'index_r'],1)

#Temperature by day data trainning
temp_mean_ = period.groupby(['year', 'month', 'day']).mean()

temp_mean_train = temp_mean_.Temperatura
time_plot_train = np.arange(temp_mean_.shape[0])

temp_mean_train = temp_mean_train[:, np.newaxis]

################### Fit(train) polynomial model #########################
# create matrix versions of these arrays (transpose)
time_train = time_plot_train[:, np.newaxis]
model = make_pipeline(PolynomialFeatures(4), Ridge())
model.fit(time_train, temp_mean_train)
##########################################################################

############ Forecast for 7 next days with polynomial model #########################
date_prediction_to_7 = date_prediction_to + dt.timedelta(days=7)
period_prediction_ = data[(data['fecha_hora'] > date_prediction_to) &
                          (data['fecha_hora'] < date_prediction_to_7)]
period_prediction = period_prediction_.copy()
period_prediction['year'] = period_prediction_['fecha_hora'].dt.year
period_prediction['month'] = period_prediction_['fecha_hora'].dt.month
period_prediction['day'] = period_prediction_['fecha_hora'].dt.day
period_prediction = period_prediction.drop(['fecha_hora','Calidad', 'wrong_values', 'index_r'],1)

temp_mean_test_ = period_prediction.groupby(['year', 'month', 'day']).mean()

#Temperature by day for test model
temp_mean_test = temp_mean_test_.Temperatura
time_plot_test = np.arange(temp_mean_test_.shape[0])

# create matrix versions of these arrays (transpose)
time_test = time_plot_test[:, np.newaxis]
out_model = model.predict(time_test)
####################################################################################

##################### Kalman Filter ########################################
# intial parameters
n_iter = 7
sz = (n_iter,) # size of array with forecast values
temp_mean_test = temp_mean_test[:, np.newaxis] #Real temperature
z = out_model # measure data will be de model output

Q = 1e-5 # process variance

# wt
temp_var_train_ = period.groupby(['year', 'month', 'day']).var()
wt = (temp_var_train_.Temperatura.sum())/(temp_var_train_.shape[0])
wt = 0

# allocate space for arrays
xhat=np.zeros(sz)      # a posteri estimate of x
P=np.zeros(sz)         # a posteri error estimate
xhatminus=np.zeros(sz) # a priori estimate of x
Pminus=np.zeros(sz)    # a priori error estimate
K=np.zeros(sz)         # gain or blending factor

R = 0.01**2 # estimate of measurement variance, change to see effect

# intial guesses
xhat[0] = temp_mean_train[0]
P[0] = 1.0

for k in range(1,n_iter):
    # time update
    xhatminus[k] = xhat[k-1]+wt
    Pminus[k] = P[k-1]+Q

    # measurement update
    K[k] = Pminus[k]/( Pminus[k]+R )
    xhat[k] = xhatminus[k]+K[k]*(z[k]-xhatminus[k])
    P[k] = (1-K[k])*Pminus[k]
#####################################################################

# ordering data for show
kalman_out = xhat[np.newaxis]
kalman_out = kalman_out.T

# Out of models
summary = temp_mean_test_.assign(kalman_out = kalman_out, out_model=out_model).copy()
print summary

plt.figure()
plt.plot(z,'r-',label='noisy measurements (regression model)')
plt.plot(xhat,'b-',label='a posteri estimate')
plt.plot(temp_mean_test,'g',label='truth value')
plt.legend(loc='lower left')
plt.title('Estimate vs Real Temp vs Reg Mod', fontweight='bold')
plt.xlabel('index day')
plt.ylabel('Temperature')
plt.axis([1, 8, 10, 35 ])

plt.show()
