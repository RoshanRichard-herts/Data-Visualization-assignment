#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  4 15:50:31 2023

@author: roshanrichard
"""

import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import numpy as np
import pandas as pd

fig = plt.figure(figsize = (10,7),layout="constrained")

gs = GridSpec(3, 3, figure=fig)
ax1 = fig.add_subplot(gs[0, :])
ax2 = fig.add_subplot(gs[1, :-1])
ax3 = fig.add_subplot(gs[1:, -1])
ax4 = fig.add_subplot(gs[-1, 0])
ax5 = fig.add_subplot(gs[-1, -2])

''' axes one '''

df = pd.read_csv('GDP.csv')

years,i = [],1
# To populate the years list
for i in range(42):
    years.append(str(1975+i))
    i += 1
# this variable is the int version of the years variable
years_int = [int(i) for i in years]

# Manipulating the dataset    
df=df[(df["Country Name"]=="United Arab Emirates")|
          (df["Country Name"]=="India")|
          (df["Country Name"]=="United Kingdom")]
df_subset = df[['Country Name']+years]
df_subset  = df_subset.T
df_subset.columns = df_subset.iloc[0]
df_subset = df_subset.iloc[1:]
df_subset = df_subset/100000000000

#ploting
plt.rcParams['font.size'] = 11
#ax1.figure(figsize=(10, 6), layout='constrained')
ax1.plot(years,df_subset["India"],label= "India")
ax1.plot(years,df_subset["United Arab Emirates"],label= "United Arab Emirates")
ax1.plot(years,df_subset["United Kingdom"],label= "United Kingdom")
ax1.set_title("GDP of Countries from 1975 to 2016")
ax1.set_ylabel("GDP per 100 Billion USD")
ax1.set_xlabel("Years")
xtick_locations = [0,10,20,30,40]
xtick_labels = [years_int[i] for i in xtick_locations]
ax1.set_xticks(xtick_locations, xtick_labels)
ax1.grid(True)
ax1.legend()

''' axes two '''

years,i = [],1
# To populate the years list
for i in range(15):
    years.append(str(2000+i))
    i += 1

df_NR = pd.read_csv('natural_resource.csv')

df_NR=df_NR[(df_NR["Country Name"]=="United Arab Emirates")|
          (df_NR["Country Name"]=="India")|
          (df_NR["Country Name"]=="United Kingdom")]
df_subset = df_NR[['Country Name']+years]
df_subset  = df_subset.T
df_subset.columns = df_subset.iloc[0]
df_subset = df_subset.iloc[1:]

x = np.arange(len(df_subset["India"]))
width = .20

plt.rcParams['font.size'] = 8
#ax2.figure(figsize = (11,6), layout = "constrained")
ax2.set_title("Cars sold in each Country")
ax2.bar(x - width / 2, df_subset["India"], width, label="India")
ax2.bar(x + width / 2, df_subset["United Arab Emirates"], width, label="United Arab Emirates")
ax2.bar(x - (width / 2) * 3, df_subset["United Kingdom"],width, label = "United Kingdom")

ax2.set_xlabel("YEARS")
ax2.set_ylabel("Natural Resource Rent")
ax2.set_xticks(x,labels = df_subset.index,rotation = 45)
#ax2.rcParams['font.size'] = 18
ax2.legend()
#ax2.show()
#ax2.close()

""" axes three """
plt.rcParams['font.size'] = 10
df_LF = pd.read_csv('labour_force.csv')
df_LF=df_LF[(df_LF["Country Name"]=="United Arab Emirates")|
          (df_LF["Country Name"]=="India")|
          (df_LF["Country Name"]=="United Kingdom")]


ax3.pie(df_LF["2021"], labels=df_LF["Country Name"] , autopct='%1.1f%%', wedgeprops={'linewidth': 5, 'edgecolor': 'white'})



ax3.set_title('Labor force participation rate')

# show the plot

""" axes four and five """

df_IM = pd.read_csv('import.csv')
df_EX = pd.read_csv('export.csv')


df_IM=df_IM[(df_IM["Country Name"]=="United Arab Emirates")|
          (df_IM["Country Name"]=="India")|
          (df_IM["Country Name"]=="United Kingdom")]

df_EX = df_EX[(df_EX["Country Name"]=="United Arab Emirates")|
          (df_EX["Country Name"]=="India")|
          (df_EX["Country Name"]=="United Kingdom")]

ax4.scatter(df_IM.iloc[0][45:-12], df_EX.iloc[0][45:-12], label = 'United Arab Emirates' , color = 'g')
ax4.scatter(df_IM.iloc[1][45:-12], df_EX.iloc[1][45:-12], label = 'United Kingdom', color ='b')
ax4.scatter(df_IM.iloc[2][45:-12], df_EX.iloc[2][45:-12], label = "India",color = 'r')

# add labels and title
ax4.set_xlabel('Imports')
ax4.set_ylabel('Exports')
ax4.set_title('Imports and Exports (2000 to 2010)')
ax4.legend(fontsize = 6)

ax5.scatter(df_IM.iloc[0][-12:-2], df_EX.iloc[0][-12:-2], label = 'United Arab Emirates' , color = 'g')
ax5.scatter(df_IM.iloc[1][-12:-2], df_EX.iloc[1][-12:-2], label = 'United Kingdom', color ='b')
ax5.scatter(df_IM.iloc[2][-12:-2], df_EX.iloc[2][-12:-2], label = "India",color = 'r')

# add labels and title
ax5.set_xlabel('Imports')
ax5.set_ylabel('Exports')
ax5.set_title('Imports and Exports (2010 to 2020)')
ax5.legend(fontsize = 6)


fig.suptitle("Factors that affect GDP")

#saving the graph as an png
fig.savefig('scatter_plot.png', dpi=300)
plt.show()



















