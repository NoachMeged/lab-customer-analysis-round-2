#!/usr/bin/env python
# coding: utf-8

# In[83]:


import pandas as pd
import numpy as np

df = pd.read_csv ("/Users/noachmeged/Documents/Ironhack/Labs/lab-customer-analysis-round-2/files_for_lab/csv_files/marketing_customer_analysis.csv", sep=",")


# In[6]:


# Show the DataFrame's shape.
df.shape


# In[7]:


# Standardize header names.

df.columns = df.columns.str.lower().str.replace(" ", "_")


# In[8]:


# Which columns are numerical?
numerical = df.select_dtypes("number")
print(numerical.columns)


# In[9]:


# Which columns are numerical?
categorial = df.select_dtypes("object")
print(categorial.columns)


# In[10]:


# Check and deal with NaN values.

df.isna().sum()


# In[11]:


# Check and deal with NaN values of state.
df['state'].value_counts()


# In[12]:


# Check and deal with NaN values of state - call them others
df['state'] = df['state'].fillna('others')
df.isna().sum()
df['state'].value_counts()


# In[13]:


# Check and deal with NaN values responses - count it as no
df['response'] = df['response'].fillna('no')
df.isna().sum()


# In[291]:


# Check and deal with NaN values months_since_last_claim - use the median
df["months_since_last_claim"] = df["months_since_last_claim"].astype(str)
df["months_since_last_claim"] = df["months_since_last_claim"].astype(float)
col_median = df["months_since_last_claim"].dropna().median()
df["months_since_last_claim"] = df["months_since_last_claim"].fillna(col_median)
print(df["months_since_last_claim"])
df.isna().sum()


# In[14]:


# Check and deal with NaN values number of open complaints - drop the open nans for complaints
df = df.dropna(subset=["number_of_open_complaints"], axis = 0)
df['number_of_open_complaints'].value_counts()
df.isna().sum()


# In[15]:


# Check and deal with NaN values vehicle_class - drop the NaNs
df = df.dropna(subset=["vehicle_size"], axis = 0)
df.isna().sum()


# In[16]:


# Check and deal with NaN values vehicle_type - drop the open nans for complain
df['vehicle_type'].value_counts()


# In[17]:


# Check and deal with NaN values vehicle_type - categorize the NaNs as "B"

df['vehicle_type'] = df['vehicle_type'].fillna('B')

df['vehicle_type'].value_counts()


# In[18]:


# Clean withdrop of unnamed:_0 and rename of employmentstatus to employment_status
df = df.rename(columns={"employmentstatus": "employment_status"})


df.isna().sum()


# In[26]:


# Datetime format - Extract the months from the dataset and store in a separate column. 
# Then filter the data to show only the information for the first quarter , ie. January, February and March. 
# Hint: If data from March does not exist, consider only January and February.
import pandas as pd

import datetime
from datetime import date


# In[27]:


df["effective_to_date"]


# In[82]:


# Datetime format - use pd.to_datetime to get the datas in the write format
df['effective_to_date'] = pd.to_datetime(df['effective_to_date'], format='%Y-%m-%d')
df['effective_to_date']


# In[67]:


#  Extract the months from the dataset and store in a separate column. 
df['effective_to_date_month'] = df['effective_to_date'].dt.month
df['effective_to_date'].dt.month


# In[68]:


# Then filter the data to show only the information for the first quarter , ie. January, February and March
first_quarter_data = df[(df['effective_to_date_month'] >= 1) & (df['effective_to_date_month'] <= 3)]


# In[70]:


# Hint: If data from March does not exist, consider only January and February.- march doesn't excist 
first_quarter_data['effective_to_date_month'].value_counts()


# In[81]:


# BONUS: Put all the previously mentioned data transformations into a function.
# Standardize header names.
df.columns = df.columns.to_series().apply(lambda x: x.lower().replace(" ", "_"))

def standerize_header_names(df):
    df.columns = df.columns.str.lower().str.replace(" ", "_")
    return df




# In[ ]:




