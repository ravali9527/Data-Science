#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 15:58:13 2018

@author: ravali
"""
DIR='/Users/ravali/Documents/Data-Science/data'
import pandas as pd
import numpy as np
df1 = pd.read_csv(DIR+'/dataset1new.csv', delimiter=',')
df2 = pd.read_csv(DIR+'/dataset2new.csv', delimiter=',')
df3=pd.merge(df1, df2, on='S.NO')       #merge two data sets into single data set
df_num = df3.select_dtypes(include=[np.number])     #select only columns with numerical values for normalization
df_norm = 1000*(df_num - df_num.mean()) / (df_num.max() - df_num.min())    #normalize the data in te data frame
df3[df_norm.columns] = df_norm      # replace the data frame columns with normalizedcolumns
df3.drop('S.NO', axis=1, inplace=True)    # drop S.No in data frame as it is least used in prediction
print(df3)
df3.to_csv('/Users/ravali/Documents/Data-Science/data/output.csv', sep=',') 