#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
data=pd.read_csv("C:\\Users\\user\\Desktop\\pyth ass\\Pokemon.csv")
data.head()


### Speed_High_Low --> Speed_High,Speed_Low
speed_mean = data["Speed"].mean()

def set_speed(val):
    if val < speed_mean:
        return "High speed"
    elif val == speed_mean:
        return "Neutral speed"
    else:
        return "Low speed"
data["Speed_High_Low"]=data["Speed"].apply(set_speed)
data



# In[2]:


### HP_High_Low --> HP_High,HP_Low
hp_mean = data["HP"].mean()

def set_hp(val):
    if val < hp_mean:
        return "High HP"
    elif val == speed_mean:
        return "Neutral  HP"
    else:
        return "Low HP"
data["HP_High_Low"]=data["HP"].apply(set_hp)
data


# In[ ]:




