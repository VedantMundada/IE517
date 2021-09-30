# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 09:59:55 2021

@author: chint
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
df=pd.read_csv('D:/UIUC_courses/IE517/project/MLF_GP1_CreditScore.csv')

rank=pd.read_csv('D:/UIUC_courses/IE517/project/lookup_table.csv')

temp=[]
for i in range(len(df['Rating'])):
    for j in range(len(rank['Rating'])):
        if (np.char.lower(str(df['Rating'].values[i]))==rank['Rating'].values[j]):
             temp.append(float(rank['rank'].values[j]))

df['Rating']=temp
pd_corr=df.corr()
sns.heatmap(pd_corr)
plt.show()

corr_labels=['Rating','CFO','CFO/Debt','ROE','Free Cash Flow', 'Current Liabilities','Cash','Current Liquidity']
sns.heatmap(df[corr_labels].corr())

print("As we see from the above correleation plots, there is no strong correlation between any of the features")

