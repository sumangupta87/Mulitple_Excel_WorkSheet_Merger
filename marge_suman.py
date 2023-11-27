#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Input
inPath = "D:\\Nov2023\\Suman\\"
outPath = "D:\\Nov2023\\Suman\\"

sheets = ['ABC1', 'ABC2']
files = ['Suman1.xlsx','Suman2.xlsx','Suman3.xlsx']


# In[2]:


import pandas as pd


# In[3]:


margeSheet = {}
for sheet in sheets:
    margeFile = []
    for file in files:
        margeFile.append(pd.read_excel(inPath+file,sheet_name = sheet))
        
    margeSheet[sheet]=margeFile


# In[4]:


out = {}

for sheet in margeSheet.keys():
    out[sheet] = pd.concat(margeSheet[sheet], axis = 0)


# In[5]:


for wrkst in out.keys():
    out[wrkst].to_csv(outPath+wrkst+'.csv')


# In[ ]:




