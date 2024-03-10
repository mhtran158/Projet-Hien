import pandas as pd
import  pandas as pd
import numpy as np
import seaborn as sns
import statsmodels.api as sm
import scipy.stats as stats
import matplotlib_inline
import matplotlib.pyplot as plt
CO2='CO2.csv'
data='data.csv'
df=pd.read_csv(filepath_or_buffer=CO2, sep=';', encoding = 'latin-1')
df.head()
sns.histplot(df['CO2 (g/km)'],bins =100);
data=pd.read_csv('data.csv',sep=',', header=0, index_col=0)
data.head()
#Modalité de chaque variable
print(df['Marque'].value_counts())
print(df['Carburant'].value_counts())
print(df['Carburant'].value_counts())
print(df['Hybride'].value_counts())
print(df['Boîte de vitesse'].value_counts())
print(df['Champ V9'].value_counts())
print(df['gamme'].value_counts())
# Les types de variables
df.dtypes.value_counts()
#Le nom des colonnes et leur type
df.info()
#Nombre de valeurs manquantes par colonne
df.isnull().sum(axis=0)
#Nombre de valeurs manquantes par ligne
df.isnull().sum(axis=1)
#Nombre total de valeurs manquantes
df.isnull().values.sum()
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
df.describe()
#Réaliser un heatmap pour étudier la corrélation des variables
df=pd.read_csv(filepath_or_buffer=CO2,sep=';',encoding='latin-1')
sns.set()
var_num=df.select_dtypes(include=['int64','float64'])
cor=var_num.corr()
fig,ax=plt.subplots(figsize=(13,13))
sns.heatmap(cor, annot=True, ax=ax,cmap='coolwarm')
plt.show()
#Etude des doublons
df.duplicated()
#Nombre de doulons
df.duplicated().sum()
#Distribution de variable CO2
sns.histplot(df['CO2 (g/km)'],bins =100);
data=pd.read_csv(filepath_or_buffer=data,sep=';')
data.head()
#Distribution du C02 du fichier "data"
plt.hist(data['Ewltp (g/km)'], bins=100, color='orange')
plt.xlabel('Co2')
plt.ylabel('Count')
plt.title('Histogramme Distribution Emission Co2');
