
# coding: utf-8

# In[1]:


import pandas as pd
from pandas import Series
import matplotlib.pyplot as plt
import numpy as np


# In[2]:


arr = np.array([1, 2, 3])


# In[4]:


print(arr)


# In[9]:


arr1 = np.random.randint(0, 1000, size=(5, 4))


# In[10]:


arr1


# In[11]:


arr1.ndim


# In[12]:


arr1.size


# In[13]:


arr1.shape


# In[14]:


# In[15]:


img = plt.imread("D:/xwz.png")


# In[16]:


img


# In[17]:


plt.imshow(img)


# In[18]:


img = img-0.5


# In[20]:


plt.imshow(img)


# In[21]:


a = np.array(range(15)).reshape(3, 5)


# In[22]:


a


# In[23]:


a.T


# In[26]:


b = np.ones(shape=(2, 3))


# In[27]:


b


# In[30]:


np.eye(3, k=-1)


# In[33]:


np.identity(6)


# In[36]:


np.arange(0, 10, 3)


# In[37]:


x = np.arange(16)


# In[38]:


x


# In[40]:


y = x*5


# In[41]:


y


# In[42]:


y[11]


# In[43]:


y[4:9]


# In[45]:


y[:10:3]


# In[46]:


y[::-1]


# In[47]:


y[0] = 2


# In[48]:


y


# In[49]:


x = np.arange(0, 100, 5).reshape(4, 5)


# In[50]:


x


# In[51]:


x[1, 2]


# In[52]:


x[1:4, 3]


# In[53]:


img = plt.imread("D:/xwz.png")


# In[55]:


plt.imshow(img[::-1, ::-1, :])


# In[56]:


img.shape


# In[59]:


y = np.concatenate((img, img), axis=0)


# In[60]:


plt.imshow(y)


# In[61]:


# In[62]:


# In[63]:


users = pd.Series(data=[2, 45, 33, 62])


# In[64]:


users


# In[65]:


user = pd.Index(["Mary", "Jane", "Sue", "Kitty"])


# In[66]:


user


# In[67]:


users = pd.Series(data=[24, 45, 33, 62], index=user)


# In[68]:


users


# In[72]:


users[0]


# In[73]:


users[:3]


# In[75]:


users[users > 30]


# In[77]:


user.unique()


# In[78]:


users+1


# In[96]:


tinydict = {"a": 1, "b": 2, "c": 3}


# In[85]:


tinydict["b"]


# In[86]:


tinydict["b"] = 4


# In[87]:


tinydict


# In[88]:


tinydict["d"] = 5


# In[89]:


tinydict


# In[90]:


del tinydict["a"]


# In[91]:


tinydict


# In[93]:


tinydict.clear()


# In[94]:


tinydict


# In[99]:


tinydict.items()


# In[ ]:
