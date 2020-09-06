#!/usr/bin/env python
# coding: utf-8

# In[1]:
#made this in jupyter notebook and I shared it here for acknowledgement

import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


data = pd.read_csv('country_wise_latest.csv')


# In[3]:


data


# In[14]:


plt.style.use('seaborn')
fig, (ax1, ax2, ax3) = plt.subplots(nrows=3, ncols=1, figsize=(20, 20))




plot = ax1.bar(data['WHO Region'], data['Confirmed'])
ax1.set(xlabel='Continents', ylabel='Confirmed Cases (in millions)')
font = {'weight' : 'bold',
        'size'   : 20}
plt.rc('font', **font)


plot2 = ax2.bar(data['WHO Region'], data['Deaths'])
ax2.set(xlabel='Continents', ylabel='Death Cases', )


plot3 = ax3.bar(data['WHO Region'], data['Recovered']);
ax3.set(xlabel= 'Continents', ylabel='Recovered cases (in millions)')
fig.suptitle('COVID-19 Continents comparison (2020/08)');


# In[240]:


fig.savefig('covid-19.png')


# In[212]:


confirmed = data['Deaths'].groupby(data['WHO Region']).sum()


# In[213]:


confirmed


# In[18]:


fig, ax = plt.subplots(figsize=(10,10))
plot = ax.bar(data['WHO Region'], data['Confirmed'])
ax.set(xlabel='Continents', ylabel='Confirmed Cases (in millions)', title='COVID-19 Confirmed Cases')
font = {'weight' : 'bold',
        'size'   : 20}
plt.rc('font', **font)


# In[19]:


fig.savefig('covid confirmed.png')


# In[24]:


fig, ax = plt.subplots(figsize=(10,10))
plot = ax.bar(data['WHO Region'], data['Deaths'])
ax.set(xlabel='Continents', ylabel='Death Cases',title='Covid-19 Death Cases' )


# In[25]:


fig.savefig('covid deaths.png')


# In[26]:


fig, ax = plt.subplots(figsize=(10,10))
plot = ax.bar(data['WHO Region'], data['Recovered']);
ax.set(xlabel= 'Continents', ylabel='Recovered cases (in millions)', title='COVID-19 Recovered cases')


# In[23]:


fig.savefig('Covid Recovered')


# In[50]:


fig, ax = plt.subplots(figsize=(10,10))
plt.barh(data['WHO Region'],data['Deaths / 100 Cases'])
ax.set(xlabel='Deaths per 100 cases', ylabel='Continents',title='Covid-19 Deaths per 100 cases' );


# In[51]:


fig.savefig('deaths per 100 cases.png')


# In[53]:


fig, ax = plt.subplots(figsize=(15,10))
plt.barh(data['WHO Region'],data['Recovered / 100 Cases'])
ax.set(xlabel='Recovered per 100 cases', ylabel='Continents',title='Covid-19 Recoveries per 100 cases' );


# In[54]:


fig.savefig('Recovered per 100 cases.png')


# In[ ]:




