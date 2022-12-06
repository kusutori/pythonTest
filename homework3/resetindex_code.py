#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


obj=pd.read_csv("D:/score.csv")


# In[3]:


obj


# In[7]:


b=obj.sort_values(by="语文",axis=0,ascending=True)


# In[8]:


b


# In[9]:


b=obj.sort_index(axis=0,ascending=True)


# In[10]:


b


# In[11]:


c=obj.drop([1])


# In[12]:


c


# In[14]:


c.reset_index()


# In[16]:


data=c.set_index(["语文"],inplace=False,drop=False)


# In[17]:


data


# In[18]:


data.loc[53]


# In[20]:


obj.describe()


# In[26]:


d=obj[(obj["数学"]>60)|(obj["英语"]>70)]


# In[27]:


d


# In[28]:


obj=pd.read_excel("D:/data1.xlsx")


# In[29]:


obj


# In[30]:


x=obj["ID"].isna()


# In[31]:


x


# In[34]:


y=obj[~obj["ID"].isnull()]


# In[35]:


y


# In[37]:


obj=pd.read_csv("D:/score.csv")


# In[38]:


obj


# In[41]:


df=obj.query("语文>60|数学>70")


# In[42]:


df


# In[46]:


obj[obj["语文"].isin([37,97])]


# In[48]:


obj[obj["数学"].between(50,70)]


# In[49]:


obj2=pd.read_csv("D:/identity.csv")


# In[50]:


obj2


# In[53]:


s=obj[obj["name"].isin(obj2["name"])]


# In[54]:


s


# In[58]:


obj["语文"].sub(10)


# In[ ]:




