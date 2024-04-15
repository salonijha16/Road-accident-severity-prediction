#!/usr/bin/env python
# coding: utf-8

# In[14]:


import pandas as pd
import numpy as np


# In[3]:


acc=pd.read_csv('Accident_Information.csv')


# In[4]:


acc=pd.read_csv('Accident_Information.csv', encoding='latin')


# In[5]:


df=pd.read_csv('Accident_Information.csv')


# In[6]:


import pandas as pd
import os
print(os.listdir("../input"))


# In[7]:


df=pd.read_csv('Accident_Information.csv',low_memory=False)


# In[8]:


df.head()


# In[9]:


acc=pd.read_csv('Accident_Information.csv',low_memory=False,encoding='latin')
acc.head()


# In[10]:


veh=pd.read_csv('Vehicle_Information.csv',low_memory=False,encoding='latin')
veh.head()


# In[11]:


df=pd.merge(veh,acc,how='inner',on='Accident_Index')
print(df.shape)
df.head()


# In[12]:


null_count=df.isnull().sum()
null_count[null_count]


# In[10]:


veh=pd.read_csv('Vehicle_Information.csv',low_memory=False,encoding='latin')
veh.head()


# In[15]:


import pandas as pd
import numpy as np
from datetime import datetime as dt
import time


# In[ ]:




