# coding: utf-8

# linear model
# Author :  Juan Pablo Ramirez G
# Date : July 4, 2017

import pandas as pd
import numpy as np
import datetime as dt
from sklearn import linear_model
import matplotlib.pyplot as plt


print "predicting, please wait..."

# Read and sort data
data = pd.read_csv('Temperature_2013_01_01__2017_05_31.csv')
data['fecha_hora'] = pd.to_datetime(data['fecha_hora'])
data = data.sort_values(by='fecha_hora')

# Set date from you want predict temperature, for the seven next days
# example date_prediction_to = dt.datetime(2015, 1, 1) from Enero 1, 2013
date_prediction_to = dt.datetime(2014, 2, 1)

# Getting period for fit(train) the model
star_day = date_prediction_to - dt.timedelta(days=7)
end_day = date_prediction_to - dt.timedelta(days=1)

# Group data and delete unnecesary columns for period
period_ = data[(data['fecha_hora'] > star_day) & (data['fecha_hora'] < end_day)]
period = period_.copy()
period['year'] = period_['fecha_hora'].dt.year
period['month'] = period_['fecha_hora'].dt.month
period['day'] = period_['fecha_hora'].dt.day
period = period.drop(['fecha_hora','Calidad', 'wrong_values', 'index_r'],1)

#Temperature by day
temp_mean_ = period.groupby(['year', 'month', 'day']).mean()

########### Fit(train) the model ##################
# get data for trainning
data_temp_train = temp_mean_.Temperatura.as_matrix()
data_temp_train.resize((data_temp_train.shape[0], 1))
data_time_train = np.arange(data_temp_train.shape[0])
data_time_train.resize((data_time_train.shape[0], 1))

# Create linear regression object
regr = linear_model.LinearRegression()

# Train the model using the training sets
regr.fit(data_time_train, data_temp_train)
###################################################

################## testing model ########################
#--------- data for test model if that data exist ----------#
date_prediction_to_7 = date_prediction_to + dt.timedelta(days=7)
period_prediction_ = data[(data['fecha_hora'] > date_prediction_to) &
                          (data['fecha_hora'] < date_prediction_to_7)]
period_prediction = period_prediction_.copy()
period_prediction['year'] = period_prediction_['fecha_hora'].dt.year
period_prediction['month'] = period_prediction_['fecha_hora'].dt.month
period_prediction['day'] = period_prediction_['fecha_hora'].dt.day
period_prediction = period_prediction.drop(['fecha_hora','Calidad', 'wrong_values', 'index_r'],1)

#Temperature by day
temp_mean_test = period_prediction.groupby(['year', 'month', 'day']).mean()

# test data
data_temp_test = temp_mean_test.Temperatura.as_matrix()
data_temp_test.resize((data_temp_test.shape[0], 1))
data_time_test = np.arange(data_temp_test.shape[0])
data_time_test.resize((data_time_test.shape[0], 1))
#------------------------------------------------------------#

# Out model and real values
out = regr.predict(data_time_test)
summary = temp_mean_test.assign(out_model = out, real_temp=data_temp_test).copy
print summary


# The coefficients
print('Coefficients: \n', regr.coef_)

# The mean squared error
print("Mean squared error: %.2f"
      % np.mean((regr.predict(data_time_test) - data_temp_test) ** 2))

# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % regr.score(data_time_test, data_temp_test))

# Plot outputs
plt.scatter(data_time_test, data_temp_test,  color='black')
plt.plot(data_time_test, regr.predict(data_time_test), color='blue',
         linewidth=1)
plt.show()
############################################################################
