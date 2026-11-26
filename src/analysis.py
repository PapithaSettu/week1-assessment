#!/usr/bin/env python
# coding: utf-8

# # Employee Analysis
# 
# 

# ## Data

# In[4]:


df.groupby("department").agg(headcount=("id","count"),avg_salary=("salary","mean"))


# In[2]:


import pandas as pd 
df=pd.read_csv("../data/employees.csv")
df.head()


# # Headcount by Department

# In[5]:


get_ipython().run_line_magic('timeit', 'df.groupby("department")["salary"].mean()')


# In[6]:


df[df["city"]=="Chennai"]


# In[ ]:





# ## Finding
# 

# 
