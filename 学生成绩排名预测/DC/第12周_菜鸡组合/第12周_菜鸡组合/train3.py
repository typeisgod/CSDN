# -*- coding: utf-8 -*-
"""
Created on Mon May 21 15:07:52 2018

@author: 71405
"""

import pickle
x=pickle.load(open('train_x2.pkl','rb'))
y=pickle.load(open('train_y2.pkl','rb'))
#Label=pickle.load(open('train_label.pkl','rb'))
from sklearn.ensemble import RandomForestRegressor
from sklearn.neighbors import KNeighborsClassifier  
from sklearn import svm 
import numpy as np

x_train=np.array(x)
y_train=np.array(y)
x_test=np.array(x[450:])
y_test=np.array(y[450:])
from sklearn.linear_model import LinearRegression
#model = KNeighborsClassifier(10)
#model=svm.SVC(C=2, kernel='rbf',decision_function_shape='ovr')
#model=LinearRegression()
#model = RandomForestRegressor(1000)
model.fit(x_train,y_train)
scores=model.score(x_test,y_test)
s=model.predict(x_test)
scores=model.score(x_test,y_test)


i=0
t=0




while i<len(s):
    if(abs(round(s[i])-y_test[i]) <= 1):
        t=t+1
    i=i+1
t=t/len(s)

n = len(s)
rou = 1 - 6 * sum((s - y_test) ** 2) / (n * (n ** 2 - 1))

