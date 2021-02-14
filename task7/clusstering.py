#!/usr/bin/env python
# coding: utf-8

# In[63]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# Set the styles to Seaborn
sns.set()
# Import the KMeans module so we can perform k-means clustering with sklearn
from sklearn.cluster import KMeans


# In[64]:


data = pd.read_csv('global_tempurature_2013_January.csv',error_bad_lines=False, index_col=False)


# In[65]:


data


# In[66]:


plt.scatter(data['Country'],data['AverageTemperature'])
# Set limits of the axes, again to resemble the world map
plt.title("Annual Average Global Temperature: Continential", size=20)
plt.xlabel("Country", size=17)
plt.ylabel("AverageTemperature", size=17)

plt.show()


# In[74]:


x = data.iloc[:,2:5]


# In[75]:


x


# In[69]:


kmeans = KMeans(7)
#specify the number of clusters required


# In[70]:


kmeans.fit(x)
# model is made ready for the clustering and labelling the clusters


# In[71]:


identified_clusters = kmeans.fit_predict(x)
identified_clusters


# In[72]:


data_with_clusters = data.copy()
data_with_clusters['Cluster'] = identified_clusters
data_with_clusters


# In[73]:


plt.scatter(data_with_clusters['Country'],data_with_clusters['AverageTemperature'],c=data_with_clusters['Cluster'],cmap='rainbow')
plt.title("Annual Average Global Temperature: Continential", size=20)
plt.xlabel("Country", size=17)
plt.ylabel("AverageTemperature", size=17)

plt.show()


# In[ ]:




