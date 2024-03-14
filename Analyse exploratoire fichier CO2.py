# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 09:55:28 2024

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
#Information générale
df.info()
#Modalité des variables:

print(df['Marque'].value_counts())
print(df['Carburant'].value_counts())
print(df['Carburant'].value_counts())
print(df['Hybride'].value_counts())
print(df['Boîte de vitesse'].value_counts())
print(df['Champ V9'].value_counts())
print(df['gamme'].value_counts())
# Les types de variables
df.dtypes.value_counts()
#Nombre de valeurs manquantes par colonne
print(df.isnull().sum(axis=0))
#Nombre de valeurs manquantes par ligne
print(df.isnull().sum(axis=1))
print('\n')
#Nombre total de valeurs manquantes
print('Nombre total valeur manquante:',df.isnull().values.sum())
#% global de valeurs manquantes
NBNAN=df.isnull().values.sum()
NBVALM=df.count().sum()
PourcentageNAN=(NBNAN/(NBNAN+NBVALM))*100
print('Nombre de NAN:',NBNAN, 'Nombre de valeur non manquantes:', NBVALM, '% de NAN:', PourcentageNAN,'%')
#Colonnes contenant valeur manquantes
print(df.isna().any(axis=0).sum(),'colonnes contenant valeurs manquantes \n')
print(df.isna().any(axis=0).sum(),'colonnes contenant valeurs manquantes \n')
print(df.isna().any(axis=1).sum(), 'lignes contenant valeur manquantes \n')
print(df.isna().sum(axis=0).idxmax(),'colonne contenant le plus de valeurs manquantes \n')
# Description
df.describe()
#Réaliser un heatmap pour étudier la corrélation des variables

sns.set()
var_num=df.select_dtypes(include=['int64','float64'])
cor=var_num.corr()
fig,ax=plt.subplots(figsize=(13,13))
sns.heatmap(cor,annot=True,ax=ax,cmap='coolwarm')
plt.show()
#Etude des doublons
df.duplicated()
#Nombre de doulons
print('Nombre total des doublons:',df.duplicated().sum())
#Distribution CO2 dans le fichier "CO2":

sns.histplot(df['CO2 (g/km)'],bins =100);
#Graphique sur la distribution de CO2 dans le fichier "data":
data=pd.read_csv('data.csv',sep=',', header=0, index_col=0)
data.head()

plt.hist(data['Ewltp (g/km)'], bins=100, color='orange')
plt.xlabel('Co2')
plt.ylabel('Count')
plt.title('Histogramme Distribution Emission Co2');
plt.show()
#Graphique sur la distribution de carburant
sns.countplot(x='Carburant',data=df)
sns.relplot(x = "Puissance maximale (kW)", y = "CO2 (g/km)", hue = "Carburant", data = df);
#Graphique sur la masse et CO2:
sns.relplot(x='masse vide euro min (kg)',y = "CO2 (g/km)",size="Puissance maximale (kW)", hue="Puissance maximale (kW)",data=df);
#Graphique sur la distribution de catégorie hybride/non
sns.relplot(x = "Puissance maximale (kW)", y = "CO2 (g/km)", hue = "Hybride", data = df);
#Corrélation C02 et autres polluants
df1=df.iloc[:,14:20]
cor=df1.corr()
fig,ax=plt.subplots(figsize=(8,8))
sns.heatmap(cor, annot=True,ax=ax,cmap='coolwarm')
plt.show()

