#!/usr/bin/env python
# coding: utf-8

# In[117]:


import pandas as pd
import mlxtend
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
data = pd.read_excel('greenhouse-gas-emissions-by-region-industry-and-household-year-ended-2018.xlsx')
data.head()


# In[118]:


data['Industry'] = data['Industry'].str.strip()
data = data[~data['Industry'].str.contains('Total')]
data


# In[119]:


basket = (data[data['gas'] == "Carbon dioxide equivalents"]
         .groupby(['Industry', 'region'])['data_val']
         .sum().unstack().reset_index().fillna(0)
         .set_index('Industry'))
basket


# In[120]:


def encode_units(x):
    if x <= 10000:
        return 0
    if x >= 10000:
        return 1
basket_sets = basket.applymap(encode_units)
basket_sets


# In[121]:


frequent_itemsets = apriori(basket_sets, min_support = 0.054, use_colnames=True)
rules = association_rules(frequent_itemsets, metric = "lift", min_threshold = 1)
rules.head()


# In[ ]:




