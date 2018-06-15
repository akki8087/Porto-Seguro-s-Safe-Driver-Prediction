# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 20:58:08 2018

@author: NP
"""



import numpy as np
import pandas as pd
import math

data = pd.read_csv('train.csv')
X = data.iloc[:,2:]
test = pd.read_csv('test.csv')

#X = data.iloc[:,1:-3]
#y = data.iloc[:,-1]

total = data.append(test)

X_t = total.iloc[:,1:-1]
col = X_t.columns
cat_col = []
bin_col = []
num_col = []
for i in col:
    if 'cat' in i:
        cat_col.append(i)
    elif 'bin' in i:
        bin_col.append(i)
    else:
        num_col.append(i)

       