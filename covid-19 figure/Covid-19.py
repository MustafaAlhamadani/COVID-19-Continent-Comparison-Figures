#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


data = pd.read_csv('country_wise_latest.csv')


# In[3]:


data


# In[5]:


plt.style.use('seaborn')
fig, (ax1, ax2, ax3) = plt.subplots(nrows=3, ncols=1, figsize=(20, 20))




plot = ax1.bar(data['WHO Region'], data['Confirmed'])
ax1.set(xlabel='Regions', ylabel='Confirmed Cases (in millions)', title='Total Confirmed cases in the Regions')
font = {'weight' : 'bold',
        'size'   : 20}
plt.rc('font', **font)


plot2 = ax2.bar(data['WHO Region'], data['Deaths'])
ax2.set(xlabel='Regions', ylabel='Death Cases',title='Total Confirmed Deaths in the Regions' )


plot3 = ax3.bar(data['WHO Region'], data['Recovered']);
ax3.set(xlabel= 'Regions', ylabel='Recovered cases (in millions)', title='Total recovered cases in the regions')
fig.suptitle('COVID-19 Regions comparison (2020/08)');


# In[6]:


fig.savefig('covid-19.png')


# In[9]:


fig, ax = plt.subplots(figsize=(10,10))
plot = ax.bar(data['WHO Region'], data['Confirmed'])
ax.set(xlabel='Regions', ylabel='Confirmed Cases (in millions)', title='COVID-19 Confirmed Cases in the Regions')
font = {'weight' : 'bold',
        'size'   : 20}
plt.rc('font', **font)


# In[10]:


fig.savefig('covid confirmed.png')


# In[12]:


fig, ax = plt.subplots(figsize=(10,10))
plot = ax.bar(data['WHO Region'], data['Deaths'])
ax.set(xlabel='Regions', ylabel='Death Cases',title='Covid-19 Confirmed Death Cases in the regions' );


# In[13]:


fig.savefig('covid deaths.png')


# In[15]:


fig, ax = plt.subplots(figsize=(10,10))
plot = ax.bar(data['WHO Region'], data['Recovered']);
ax.set(xlabel= 'Regions', ylabel='Recovered cases (in millions)', title='COVID-19 Confirmed Recovered cases in the Regions');


# In[16]:


fig.savefig('Covid Recovered.png')


# In[17]:


fig, ax = plt.subplots(figsize=(10,10))
plt.barh(data['WHO Region'],data['Deaths / 100 Cases'])
ax.set(xlabel='Deaths per 100 cases', ylabel='Regions',title='Covid-19 Deaths per 100 cases in the Regions' );


# In[18]:


fig.savefig('deaths per 100 cases.png')


# In[19]:


fig, ax = plt.subplots(figsize=(15,10))
plt.barh(data['WHO Region'],data['Recovered / 100 Cases'])
ax.set(xlabel='Recovered per 100 cases', ylabel='Regions',title='Covid-19 Recoveries per 100 cases in the Regions' );


# In[20]:


fig.savefig('Recovered per 100 cases.png')


# In[ ]:




