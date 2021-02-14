#!/usr/bin/env python
# coding: utf-8
# In[40]:
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# Set the styles to Seaborn
sns.set()
# Import the KMeans module so we can perform k-means clustering with sklearn
from sklearn.cluster import KMeans

# In[41]:

data = pd.read_csv('global_tempurature_2013_January.csv',error_bad_lines=False, index_col=False)

# In[42]:

data

# In[59]:

plt.scatter(data['Logitude'],data['Latitude'])
# Set limits of the axes, again to resemble the world map
plt.title("Annual Average Global Temperature: 2013 January", size=20)
plt.xlabel("Logitude", size=17)
plt.ylabel("Latitude", size=17)
plt.xlim(-10,160)
plt.ylim(-10,60)
plt.show()

# In[47]:

x = data.iloc[:,5:7]

# In[48]:

x

# In[49]:

kmeans = KMeans(7)
#specify the number of clusters required
# In[50]:

kmeans.fit(x)
# model is made ready for the clustering and labelling the clusters
# In[51]:

identified_clusters = kmeans.fit_predict(x)
identified_clusters

# In[52]:

data_with_clusters = data.copy()
data_with_clusters['Cluster'] = identified_clusters
data_with_clusters

# In[60]:

plt.scatter(data_with_clusters['Logitude'],data_with_clusters['Latitude'],c=data_with_clusters['Cluster'],cmap='rainbow')
plt.title("Annual Average Global Temperature: 2013 January", size=20)
plt.xlabel("Logitude", size=17)
plt.ylabel("Latitude", size=17)
plt.xlim(-10,160)
plt.ylim(-10,60)
plt.show()

# In[ ]:
