# ML Project Program 01 

# import libraries
import numpy as np
import pandas as pd

# import dataset
data = pd.read_csv("./uber.csv")
# print first few data of uber dataset
data.head
# print information of Uber dataset
data.info()
# dtypes is nothing but the data types
# object is string data
# converting object to date & time
data["pickup_datetime"] = pd.to_datetime(data["pickup_datetime"])
data.info()
# successfully converted object to date & time by using to_datetime() method
# find missing values
data.isnull()
# find total number of missing values 
data.isnull().sum()
# 0 means false & 1 means True
# if Ture means null or missing values in dataset or in row
# drop the row if it has missing values

data.dropna(inplace = True)
# After drop missing value row

data.isnull().sum()
# Now create a Machine Learning Model

# import lib

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
# x is predictor variable
x = data.drop("fare_amount", axis = 1)

# y is target variable
y = data["fare_amount"]
# to apply model

x['pickup_datetime'] = pd.to_numeric(pd.to_datetime(x['pickup_datetime']))
x = x.loc[:, x.columns.str.contains('^Unnamed')]
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

# testing data is 20%
# training data is 80%, allocated to model
# creating Linear Regression model

lrmodel = LinearRegression()
lrmodel.fit(x_train, y_train)
# model is created
# prediction

pred = lrmodel.predict(x_test)
# Calculating RMSE
lrmodelrmse = np.sqrt(mean_squared_error(pred, y_test))
print("RMSE error is: ",lrmodelrmse)
# Random Forest Regression

from sklearn.ensemble import RandomForestRegressor

# create RFR Model
rfrmodel = RandomForestRegressor(n_estimators = 100, random_state = 101)
# fit the forest

rfrmodel.fit(x_train, y_train)
rfrmodel_pred = rfrmodel.predict(x_test)
# Calculate RMSE for RFR

rfrmodel_rmse = np.sqrt(mean_squared_error(rfrmodel_pred, y_test))
print("RFR RMSE error is: ", rfrmodel_rmse)

# prediction

pred = lrmodel.predict(x_test)
print("hh",pred)
lrmodel.predict(x_test)
from sklearn import metrics

# R2 score

# R2 score Linear Regression
metrics.r2_score(y_test, pred)
# R2 score RF Model
metrics.r2_score(y_test, rfrmodel_pred)
# R2 score Linear Regression is 894% that means model not fit.
# R2 score RF Model is: 52%

# Random Forest Model best fit for this dataset, is perfect