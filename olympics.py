#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[4]:


df = pd.read_csv("summer(1).csv") 
df


# In[5]:


del df['Discipline']
df


# In[6]:


df.dropna(inplace=True)
df


# 
# 1. In how many cities Summer Olympics is held so far?

# In[7]:


len(df['City'].unique())


# 2. Which sport is having most number of Gold Medals so far? (Top 5)

# In[8]:


df_gold_medal = df[df['Medal'] == 'Gold']
 
lst = []
for i in df_gold_medal['Sport'].unique():
     lst.append([i, len(df_gold_medal[df_gold_medal['Sport'] == i])])
 
pd.DataFrame(lst, columns = ['Sport','Gold_Medals']).sort_values(by = 'Gold_Medals', ascending = False).head().plot.bar(x = 'Sport', y = 'Gold_Medals')


# 
# 3. Which sport is having most number of medals so far? (Top 5)

# In[9]:


lst = []
for i in df['Sport'].unique():
     lst.append([i, len(df[df['Sport'] == i])])
 
pd.DataFrame(lst, columns = ['Sport','Medals']).sort_values(by = 'Medals', ascending = False).head().plot.bar(x = 'Sport', y = 'Medals')


# 4. Which player has won most number of medals? 

# In[10]:


lst = []
for i in df['Athlete'].unique():
     lst.append([i, len(df[df['Athlete'] == i])])
 
pd.DataFrame(lst, columns = ['Player', 'Medals']).sort_values(by = 'Medals', ascending = False).head().plot.bar(x = 'Player' , y = 'Medals')


# 
# 5. Which player has won most number of Gold Medals? (Top 5)

# In[12]:


dfgold_medals = df[df['Medal'] == 'Gold']
 
lst = []
for i in dfgold_medals['Athlete'].unique():
     lst.append([i, len(dfgold_medals[dfgold_medals['Athlete'] == i])])
 
pd.DataFrame(lst, columns = ['Player','Gold_Medals']).sort_values(by = 'Gold_Medals', ascending = False).head().plot.bar(x = 'Player' , y = 'Gold_Medals')


# 
# 6. In which year India won first Gold Medal in Summer Olympics?

# In[14]:


dfGold_Medal = df[df['Medal'] == 'Gold']
dfGold_India = dfGold_Medal[dfGold_Medal['Country'] == 'IND']
 
lst = []
for i in dfGold_India['Year'].unique():
     lst.append(i)
min(lst)


# 
# 7. Which event is most popular in terms on number of players? (Top 5)

# In[15]:


lst = []
for i in df['Event'].unique():
     lst.append([i, len(df[df['Event'] == i])])
 
pd.DataFrame(lst,columns = ['Event','Total_Players']).sort_values(by = 'Total_Players', ascending = False).head().plot.bar(x = 'Event', y = 'Total_Players')


# 
# 8. Which sport is having most female Gold Medalists? (Top 5)

# In[17]:


dfgold_medalss = df[df['Medal'] == 'Gold']
dfgold_women = dfgold_medalss[dfgold_medalss['Gender'] == 'Women']
lst = []
for i in dfgold_women['Sport'].unique():
     lst.append([i,len(dfgold_women[dfgold_women['Sport'] == i])])
 
pd.DataFrame(lst, columns = ['Sport', 'Gold_Medals_For_Female']).sort_values(by = 'Gold_Medals_For_Female', ascending = False).head().plot.bar(x = 'Sport', y = 'Gold_Medals_For_Female')


# In[ ]:




