# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.7.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib
import seaborn as sns
# %matplotlib inline

pop = pd.read_csv('./data/suginami_population.csv')
pop = pop.drop(['総世帯数','総人口','総男','総女'],axis=1)
pop = pop.rename(columns={'男': '男.0'})
pop = pop.rename(columns={'女': '女.0'})
pop.head()

m_cols = [c for c in pop.columns if '男' in c]
f_cols = [c for c in pop.columns if '女' in c]
m_pop = pop[m_cols]
f_pop = pop[f_cols]
m_pop.columns = [c.replace('男.','') for c in m_pop.columns]
f_pop.columns = [c.replace('女.','') for c in f_pop.columns]


def generate_population_plamid(df,s_name):
    age_colors = ["#4169e1", "#ff1493"]
    age_names = ho1.columns

    sns.set(style = 'whitegrid')
    fig, ax = plt.subplots(figsize = (5, 10))
    plt.subplots_adjust(left = 0.2, right = 0.85, bottom = 0.05, top = 1.0)

    df['Male'] *= -1

    for name, color in zip(age_names,age_colors):
            sns.barplot(x = name, y = df.index, 
                data = df, color = color, label = name,
                orient = 'h', order = df.index, 
                ax = ax)

    ax.set_xlabel("")
    ax.set_ylabel("age", fontsize = 12)
    ax.set_xlim(-120, 120)
    ax.set_xticklabels(['120','100', '50', '0', '50', '100', '120'])
    ax.legend(loc = 'lower left')
    plt.savefig('graph_%s.png'%s_name)
    plt.close()


limit = 100
for i in range(pop.shape[0]):
    s_name = pop.iloc[i,0]
    row = pd.concat([m_pop.iloc[i,:],f_pop.iloc[i,:]],axis=1)
    row.columns = ['Male','Female']
    row = row.reset_index()
    row = row.drop('index',axis=1)
    row = row.sort_index(ascending=False)
    row = row.iloc[(limit*-1):]
    generate_population_plamid(row,s_name)
