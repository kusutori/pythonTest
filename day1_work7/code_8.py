#!/usr/bin/env python
# coding: utf-8

# In[41]:


import tensorflow as tf
from tensorflow import keras
from keras.datasets import imdb


# In[42]:


import pandas as pd
import numpy as np
import re
import nltk
import matplotlib.pyplot as plt
import seaborn as sns


# In[43]:


data="D:/imdb.csv"


# In[44]:


data=pd.read_csv(data)


# In[45]:


data.head()


# In[46]:


data.shape


# In[47]:


data.sentiment.value_counts().plot(kind="pie")


# In[48]:


x=data["sentimenttext"]


# In[49]:


y=data["sentiment"]


# In[50]:


from sklearn.feature_extraction.text import TfidfVectorizer


# In[51]:


#将文本转换为数字
#max_features 属性指定最多应使用 2,000 个出现次数最多的词来创建特征词典
# min_df 属性指定只包含在所有文档中出现至少五次的单词。Max_df 定义不包括出现在超过 70% 的文档中的词。
vectorizer=TfidfVectorizer(max_features=2000,min_df=5,max_df=0.7,stop_words=stopwords.words("english"))
x=vectorizer.fit_transform(x).toarray()


# In[52]:


from sklearn.model_selection import train_test_split


# In[53]:


#将数据划分为训练集和测试集
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=43)


# In[54]:


from sklearn.ensemble import RandomForestClassifier


# In[55]:


#确定随机森林中树的数量和随机状态
clf=RandomForestClassifier(n_estimators=250,random_state=0)


# In[56]:


#训练模型
clf.fit(x_train,y_train)


# In[57]:


#对测试数据进行预测
y_pred=clf.predict(x_test)


# In[58]:


from sklearn.metrics import classification_report,confusion_matrix,accuracy_score


# In[59]:


#混淆矩阵查看分类情况
print(confusion_matrix(y_test,y_pred))


# In[60]:


#准确率、召回率和 F1 度量分类情况
print(classification_report(y_test,y_pred))


# In[61]:


#准确率
print(accuracy_score(y_test,y_pred))


# In[63]:


#对单个事例的预测
print(clf.predict(vectorizer.transform(["The movie was really good,I liked it"])))


# In[ ]:




