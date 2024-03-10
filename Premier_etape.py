#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
import seaborn as sns


# In[7]:


df=pd.read_csv('cl_JUIN_2013-complet3.csv',sep=';',header=0, index_col=0, encoding='latin-1')
df.head()


# In[5]:


data=pd.read_csv('data.csv',sep=',', header=0, index_col=0, encoding='latin-1')
data.head()


# In[8]:


df.info()


# In[9]:


df.isnull().sum().sort_values(ascending=True)


# In[10]:


df.describe()


# In[11]:





# In[9]:





# In[10]:


l1=df.isna().any(axis=0)
print(l1.sum())
l2=df.isna().any(axis=1)
print(l2.sum())


# In[11]:


def first_infos(df):

    n_cols = len(df.columns)
    n_rows = len(df)
    n_duplicates = df.duplicated().sum()
    n_na = df.isna().sum().sum()

    return(n_cols, n_rows, n_duplicates, n_na)

first_infos(df)


# In[12]:


def first_infos(data):

    n_cols = len(data.columns)
    n_rows = len(data)
    n_duplicates = data.duplicated().sum()
    n_na = data.isna().sum().sum()

    return(n_cols, n_rows, n_duplicates, n_na)

first_infos(data)


# In[15]:


df.isnull().sum()


# In[ ]:




