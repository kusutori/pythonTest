#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
data = pd.read_csv(r'C:\\Users\\23382\\Desktop\\2022_APMCM_C_Data.csv')	#读取csv文件
data


# In[2]:


print(data.isnull().sum())  #统计每列有几个缺失值
missing_col = data.columns[data.isnull().any()].tolist() #找出存在缺失值的列

import numpy as np
#统计每个变量的缺失值占比
def CountNA(data):
    cols = data.columns.tolist()    #cols为data的所有列名
    n_df = data.shape[0]    #n_df为数据的行数
    for col in cols:
        missing = np.count_nonzero(data[col].isnull().values)  #col列中存在的缺失值个数
        mis_perc = float(missing) / n_df * 100
        print("{col}的缺失比例是{miss}%".format(col=col,miss=mis_perc))


# In[ ]:





# In[3]:


data.isnull().sum()


# In[4]:


data.fillna(data.median(),inplace=True) # 对每一列的缺失值，填充当列的均值


# In[5]:


data


# In[6]:


data.isnull().sum()


# In[7]:


cos_list = ['AverageTemperature','AverageTemperatureUncertainty']


# In[8]:


#当数值超出这个距离，可以认为它是异常值
cols = data.columns.tolist()
for item in cos_list:
    data[item + '_zscore'] = (data[item] - data[item].mean()) / data[item].std()
    z_abnormal = abs(data[item + '_zscore']) > 3
    print(item + '中有' + str(z_abnormal.sum())+'个异常值')


# In[9]:


for i in range(239177):
    if z_abnormal[i]:
        data['AverageTemperature'][i]=data.median()[0]
        data['AverageTemperatureUncertainty'][i]=data.median()[1] 


# In[10]:


data


# In[11]:


data['AverageTemperature'][0]=data.median()[0]


# In[12]:


data['AverageTemperature'][0]


# In[13]:


data.median()


# In[15]:


for item in cos_list:
    data[item + '_zscore'] = (data[item] - data[item].mean()) / data[item].std()
    z_abnormal = abs(data[item + '_zscore']) > 3
    print(item + '中有' + str(z_abnormal.sum())+'个异常值')


# In[ ]:




