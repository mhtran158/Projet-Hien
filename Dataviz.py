# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 05:59:15 2024

@author: chau
"""

import pandas as pd
import pandas as pd
import numpy as np
import seaborn as sns
import statsmodels.api as sm
import scipy.stats as stats
import matplotlib_inline
import matplotlib.pyplot as plt
df=pd.read_csv('CO2.csv', sep=';', encoding='latin-1')
df.head()
data=pd.read_csv('data.csv',sep=',', header=0, index_col=0)
data.head()
print('\n')

#Distribution CO2 dans le fichier "CO2" et fichier "data":

fig, ax = plt.subplots(1,2,figsize=(16,5))
sns.histplot(df['CO2 (g/km)'],bins =100,ax=ax[0]);
sns.histplot(data['Ewltp (g/km)'], bins=100, color='orange',ax=ax[1])
plt.show()

fig, ax = plt.subplots(1,2,figsize=(16,5))
sns.boxplot(y='CO2 (g/km)',data=df, ax=ax[0]);
sns.boxplot(y='Ewltp (g/km)',data=data,color='orange', ax=ax[1]);
plt.show()
print('\n')
#Nous constatons qu'il y a une amélioration d'émission CO2 en 2019 car la distribution CO2 est au tour de 200 g/km en 2013 
#alors qu'en 2019 la moyenne est au tour de 100 g/km

#Réaliser un heatmap pour étudier la corrélation des variables
sns.set()
var_num=df.select_dtypes(include=['int64','float64'])
cor=var_num.corr()
fig,ax=plt.subplots(figsize=(13,13))
sns.heatmap(cor,annot=True,ax=ax,cmap='coolwarm')
plt.show()
#Nous constatons deux points :
#HC, NOX, HC+NOX sont des polluants qui seront exclus de nos études car malgré 1/4 de NAN, la corrélation
#entre l'émission CO2 et la HC+NOX est forte. C'est pour cette raison que nous allons concentrer sur CO2 qui est un
#un bon marqueur pour suivre l'ensnsemble de la polllution 
#Absence de corrrélation entre la variable 'Particules'et les autres variables 
#Les variables Consommation urbaine, consommation mixte, consommation extra urbaine sont complètement 
#corrélées avec la variable l'émission CO2. L'émission vient de combustion de l'energie fossil. Il est
#important de faire varier la relation entre la consommation de carburant et l'émission CO2
#Ces variables ne font pas donc partie des variables explicatives et seront exclus
#de nos études    
print('\n')  

#Graphique sur la distribution de carburant
plt.figure(figsize=(10,10))
plt.subplots(1,3,1)
sns.countplot(x='Carburant',data=df)
plt.subplots(1,3,2)
sns.relplot(x = "Puissance maximale (kW)", y = "CO2 (g/km)", hue = "Carburant", data = df);
plt.subplots(1,3,3)
sns.catplot(x= 'Carburant', y='CO2 (g/km)', kind='bar', data=df)
plt.xticks(rotation=90)

#Graphique sur la masse et CO2 et hybride:
fig, ax = plt.subplots(1,2,figsize=(16,5))  
sns.relplot(x='masse vide euro min (kg)',y = "CO2 (g/km)",size="Puissance maximale (kW)", hue="Puissance maximale (kW)",data=df,ax=ax[0]);  
sns.relplot(x = "Puissance maximale (kW)", y = "CO2 (g/km)", hue = "Hybride", data = df,ax=ax[1]);

#Graphique sur carrosserie et gamme:
fig, ax = plt.subplots(1,2,figsize=(16,5))   
sns.catplot(x= 'Carrosserie', y='CO2 (g/km)', kind='bar', data=df,ax = ax[0])
plt.xticks(rotation=90)
sns.catplot(x= 'gamme', y='CO2 (g/km)', kind='bar', data=df,ax = ax[1])
plt.xticks(rotation=90)

