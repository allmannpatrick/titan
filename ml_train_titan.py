#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 17:42:32 2021

@author: ap
"""
import pandas as pd
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split


df= pd.read_csv('train.csv')







def get_title(name):
    if '.' in name:
        return name.split(',')[1].split('.')[0].strip()
    else: return 'No title exists.'
    
#df['Title'] = df['Name'].map(lambda x: get_title(x))


df['Age'].fillna(df['Age'].median(),inplace=True)

df['Embarked'].fillna('S',inplace=True)

del df['Cabin']

df.drop("Ticket", axis=1, inplace=True)
df.drop("Name", axis=1, inplace=True)



df.Sex.replace(('male','female'),(0,1),inplace=True)
#df.Title.replace(('Capt', 'Col', 'Don', 'Dr', 'Jonkheer','Lady', 'Major', 'Master', 'Miss', 'Mlle', 'Mme', 'Mr', 'Mrs','Ms','Rev', 'Sir', 'the Countess'),(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16),inplace=True)
df.Embarked.replace(('S','C','Q'),(0,1,2),inplace=True)

predictors = df.drop(['Survived', 'PassengerId'], axis=1)
target = df["Survived"]


x_train, x_val, y_train, y_val = train_test_split(predictors, target, test_size = 0.22, random_state = 0)



randomforest = RandomForestClassifier()
randomforest.fit(x_train, y_train)
y_pred = randomforest.predict(x_val)

filename = 'titanic_model.sav'
pickle.dump(randomforest, open(filename, 'wb'))
