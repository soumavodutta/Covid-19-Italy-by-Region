#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[7]:


data = pd.read_csv("F:\covid19_italy_region.csv")


# In[9]:


data.head() #data() will give the whole set, .head() will give first 5.


# In[11]:


data.columns


# In[14]:


data.tail() #.tail() will give last 5.


# In[15]:


data.describe() #by this we can fill the nul values only if we want.


# In[17]:


data.isnull().sum()


# # relating the variables with sactterplots

# In[18]:


data.columns


# In[26]:


sns.relplot(y="TotalHospitalizedPatients", x="IntensiveCarePatients", data=data) # we can't write axis name in uppercase, otherwise it will give error


# In[29]:


sns.relplot(y="TotalHospitalizedPatients", x="IntensiveCarePatients", hue= "Recovered", data=data)


# In[30]:


sns.pairplot(data)


# In[34]:


data.columns


# In[39]:


sns.relplot(x='NewPositiveCases', y='HomeConfinement', kind = 'line', data = data)


# In[41]:


sns.relplot(y='RegionName', x='HomeConfinement', kind = 'line', data = data)


# In[42]:


sns.relplot(y='RegionName', x='Recovered', kind = 'line', data = data)


# In[44]:


data.columns


# In[47]:


sns.catplot(y='Recovered', x='HomeConfinement', data = data) 


# # conclusion

# In[48]:


## 1. People are incresing the Recovery section in terms od total number of cases.
## 2. We need to flatten the curve of total number of cases on a daily basis. (line - 42)
## 3. number of deaths are increasing, we need to shorten the curve to decrease the the number of deaths


# In[ ]:




