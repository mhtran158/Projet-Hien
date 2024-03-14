# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 08:35:03 2024

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
#Lire le fichier
df=pd.read_csv('CO2.csv', sep=';', encoding='latin-1')
df.head()

#Suppression des colonnes inutiles:
col_supprim=['Marque','Modèle dossier','Modèle UTAC','Désignation commerciale','CNIT','Type Variante Version (TVV)','Puissance administrative','Consommation urbaine (l/100km)','Consommation extra-urbaine (l/100km)','Consommation mixte (l/100km)','CO type I (g/km)','HC (g/km)','NOX (g/km)','HC+NOX (g/km)','Particules (g/km)',
'masse vide euro max (kg)','Champ V9','Date de mise à jour']
df1=df.drop(col_supprim, axis=1)
df1.info()
df1.head()

#Vérification de doublons:
df1.duplicated().sum()

#Supprimer des doublonset conserver la première ligne:
df1=df1.drop_duplicates(keep='first')
 
#Vérification s'il existe encore des doublons:0
df1.duplicated().sum()

#Afficher info et description de nouveau dataframe:
df1.info()
df1.describe()

#Vérification s'il y a des valeurs manquantes:
df1.isnull().sum()

#Créer label CO2:
def cat_CO2(x):
    if x<=100:
        return 'A'
    if x>100 and x<=120:
        return 'B'
    if x>120 and x<=140:
        return 'C'
    if x>140 and x<=160:
        return 'D'
    if x>160 and x<=200:
        return 'E'
    if x>200 and x<=250:
        return 'F'
    if x>250:
        return 'G'
df1['CO2_label']=df1['CO2 (g/km)'].apply(cat_CO2)
df1.isnull().sum()
#Après nettoyage de doublons, nous avons 17 valeurs manquantes dans la colonne CO2 et CO2_label, qui correspond
#effectivement à la valeur manquante de la valeur cible CO2

#Renommer les colonnes:
new_name={'Carburant':'Carburant','Puissance maximale (kW)':'Puissance maximale','Boîte de vitesse':'Boite de vitesse',
          'CO2 (g/km)':'CO2','masse vide euro min (kg)':'masse vide','Carrosserie':'Carrosserie','gamme':'Gamme',
          'CO2_label':'CO2_label'}
df1=df1.rename(new_name,axis=1)
df1.info() 

#Afficher les modalités de colonnes pour ensuite simplifier les valeurs:
print(df1['Carburant'].value_counts())
print(df1['Hybride'].value_counts())
print(df1['Boite de vitesse'].value_counts())
print(df1['Gamme'].value_counts())
print(df1['Carrosserie'].value_counts())    
df1['Gamme']=df1['Gamme'].replace('MOY_INFER','MOY-INFER')
df1['Gamme'].value_counts() 
def categorie_gamme(x):
    if x=='MOY-INFER':
        return 'MOYENNE'
    if x=='MOY-SUPER':
        return 'MOYENNE'
    if x=='ECONOMIQUE':
        return 'INFERIEURE'
    if x=='LUXE':
        return 'LUXE'
    if x=='INFERIEURE':
        return 'INFERIEURE'
    if x=='SUPERIEURE':
        return 'SUPERIEURE'
df1['Gamme']=df1['Gamme'].apply(categorie_gamme)
print(df1['Gamme'].value_counts())    
        