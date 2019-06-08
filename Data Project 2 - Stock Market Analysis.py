#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
from pandas import Series,DataFrame
import numpy as np


import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')
get_ipython().magic(u'matplotlib inline')

# Reading stock data from yahoo
from pandas.io.data import DataReader

from datetime import datetime

# For division
from __future__ import division


# In[ ]:


tech_list = ['AAPL','GOOG','MSFT','AMZN']

end = datetime.now()
start = datetime(end.year - 1,end.month,end.day)

#For loop for grabing yahoo finance data and setting as a dataframe

for stock in tech_list:   
    # Set DataFrame as the Stock Ticker
    globals()[stock] = DataReader(stock,'yahoo',start,end)


# In[5]:


MSFT.describe()


# In[6]:


MSFT.info()


# In[ ]:


MSFT['Adj Close'].plot(legend=True,figsize=(10,4))


# In[ ]:


MSFT['Volume'].plot(legend=True,figsize=(10,4))


# In[18]:


MSFT.head()


# In[ ]:


# For calculating Moving Averages
ma_day = [10,20,50]

for ma in ma_day:
     column_name = "MA for %s days" %(str(ma))
     MSFT[column_name] = MSFT['Adj Close'].rolling(ma).mean()


# In[ ]:


MSFT[['Adj Close','MA for 10 days','MA for 20 days','MA for 50 days']].plot(subplots=False,figsize=(10,4))


# In[2]:


# We'll use pct_change to find the percent change for each day
MSFT['Daily Return'] = MSFT['Adj Close'].pct_change()
# Then we'll plot the daily return percentage
MSFT['Daily Return'].plot(figsize=(12,4),legend=True,linestyle='--',marker='o')


# In[3]:


sns.distplot(MSFT['Daily Return'].dropna(),bins=100,color='purple')


# In[55]:


# Closing prices
closing_df = DataReader(['AAPL','GOOG','MSFT','AMZN'],'yahoo',start,end)['Adj Close']


# In[57]:


closing_df.head()


# In[8]:


# Make a new tech returns DataFrame
tech_rets = closing_df.pct_change()
# Using joinplot to compare the daily returns of Google and Microsoft
sns.jointplot('GOOG','MSFT',tech_rets,kind='scatter')


# In[7]:


sns.pairplot(tech_rets.dropna())


# In[ ]:




