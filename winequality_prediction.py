# -*- coding: utf-8 -*-
"""WineQuality_Prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yYzmthI6TyChSkpG10KVDtUYkKVG_6ea
"""

# Machine Learning model to predict the wine quality using Regression
# Importing important packages


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn as sk
import statsmodels.api as sm
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression

# Reading the dataset
wine=pd.read_csv('winequality.csv')
wine.info()

# Performing stastical analysis on the data for better understanding

wine.describe()

# Visualizing to understand the relationship between each pair of variables

plt.figure(figsize=(30,15))
sns.pairplot(data=wine,hue="quality")
plt.show()

# Visulaizing using a Heatmap

plt.figure(figsize=(20,10))
sns.heatmap(wine.corr(),cmap="coolwarm",annot=True,vmin=-1,vmax=1)
plt.show()

# Assigning Quality as Dependent attribute and remaining all as Independent Attributes

x=wine.iloc[:, :-1].values
y=wine.iloc[:, -1].values

# Splitting the dataset into Training & Testing data
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)

# Fitting Multiple Training Regression to the Training dataset
reg=LinearRegression()
reg.fit(x_train,y_train)

# Test Prediction

print("Quality prediction for user input:",reg.predict([[15,0.01,0,5,0.001,30,50,0.95,3,0.9,15]]))
print()
print()

# Evaluating the model using Mean Squared Error Metric after fitting it with test  dataset

y_pred=reg.predict(x_test)
print("Mean Squared Error(MSE): ",mean_squared_error(y_test,y_pred))