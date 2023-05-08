
import pandas as pd
import numpy as np
from scipy import stats
from matplotlib import pyplot as plt
import seaborn as sns
from scipy.stats.mstats import winsorize



df1 = pd.read_csv('D:\FMT PART 2\Financial Data Visualization' +'/1989-1990 Financial ratios 1.csv', sep=",")
colNames = df1.columns
secNames = df1['FFI10_desc'].unique()     # sector names
df1['public_date'] = pd.to_datetime(df1['public_date'])      # convert date 
dates = df1.public_date.unique()    # dates

sns.set()    
#%%
'''
This part plots the cross section
Select the first/last month
'''
i = -1    # select the month
temp = df1[df1['public_date']==dates[i]].copy()    # return a copy not a view
temp['Industry'] = np.arange(1,11)    #Industry indicator
temp['Percent'] = temp['NFIRM']/temp['NFIRM'].sum()*100

# %matplotlib qt
dpi = 200       # resolution of the graph
fts = 12       # font size

# the number of firms
fts2 = 15
y_pos = temp['Industry']
plt.barh(y_pos, temp['NFIRM'])
plt.yticks(y_pos, temp['FFI10_desc'], fontsize = fts2)
plt.xticks(fontsize = fts2)

# a pie chart for percentage
plt.figure(dpi = dpi)
plt.pie(temp['Percent'], labels=temp['FFI10_desc'], autopct='%1.1f%%', shadow=True, radius=1.5)
plt.axis('equal')

#%%
'''
plot the time series jointly
%matplotlib qt
'''
dpi = 200       # resolution of the graph
lw = 1.5          # linewidth
fts = 12       # font size
lsty = ['solid','dotted', 'dashed', 'dashdot']          # line styles
cl = ['black','blue', 'red']        # line colors
x = 1989+1/12*np.arange(len(dates))
xtc = x[::60]

# plot the number of firms evolution
key = 'NFIRM'
plt.figure(dpi = dpi)
for i in range(len(secNames)):
    temp = df1[df1['FFI10_desc']==secNames[i]]    
    plt.plot(x, temp[key], label=secNames[i])
plt.xlabel(r'Year', fontsize =fts)    
plt.ylabel(r'Firm Number', fontsize =fts)
plt.yticks(fontsize=fts)
plt.xticks(xtc, fontsize=fts)
plt.legend(fontsize = fts, ncol=2)
plt.grid(True)

# plot the industry return dynamics with subplots
fts2 = 15
key = 'indret_vw'
for i in range(10):
    temp = df1[df1['FFI10_desc']==secNames[i]]
    plt.subplot(5,2,i+1)
    plt.plot(x, temp[key], label=secNames[i])
    plt.legend(fontsize = fts2)
    plt.yticks(fontsize=fts2)
    plt.xticks(xtc, fontsize=fts2)
    plt.annotate('Mean='+str(round(temp[key].mean()*12, 2)), xytext=[1989, temp[key].max()*0.9], xy=[1989, temp[key].max()*0.9], fontsize=fts2)     
    plt.annotate('S.D.='+str(round(temp[key].std()*np.sqrt(12), 2)), xytext=[1990, temp[key].max()*0.9], xy=[1990, temp[key].max()*0.9], fontsize=fts2)
    plt.grid(True)
    
#Plot the Weights of each industry​        
fts2 = 15
key = 'indret_vw'
fts2 = 12
for i in range(10):
    temp = df1[df1['FFI10_desc']==secNames[i]]
    y = temp[key]
    yW = winsorize(y, limits=[0, 0.01])
    plt.subplot(5,2,i+1)
    plt.plot(x, yW, label=secNames[i])
    plt.legend(fontsize = fts2)
    plt.yticks(fontsize=fts2)
    plt.xticks(xtc, fontsize=fts2)
    plt.annotate('Mean='+str(round(yW.mean(), 2)), xytext=[1989, yW.max()*0.9], xy=[1989, yW.max()*0.9], fontsize=fts2)     
    plt.annotate('S.D.='+str(round(yW.std(), 2)), xytext=[1990, yW.max()*0.9], xy=[1990, yW.max()*0.9], fontsize=fts2)
    plt.grid(True)
    

#Profitability Ratios 


# Return on Asset
fts2 = 12
for i in range(10):
    temp = df1[df1['FFI10_desc']==secNames[i]]
    y = temp['roa_Mean']
    yW = winsorize(y, limits=[0, 0.01])
    plt.subplot(5,2,i+1)
    plt.plot(x, yW, label=secNames[i])
    plt.legend(fontsize = fts2)
    plt.yticks(fontsize=fts2)
    plt.xticks(xtc, fontsize=fts2)
    plt.annotate('Mean='+str(round(yW.mean(), 2)), xytext=[1989, yW.max()*0.9], xy=[1989, yW.max()*0.9], fontsize=fts2)     
    plt.annotate('S.D.='+str(round(yW.std(), 2)), xytext=[1990, yW.max()*0.9], xy=[1990, yW.max()*0.9], fontsize=fts2)
    plt.grid(True)
    
#  Return on Equity 
fts2 = 12
for i in range(10):
    temp = df1[df1['FFI10_desc']==secNames[i]]
    y = temp['roe_Mean']
    yW = winsorize(y, limits=[0, 0.01])
    plt.subplot(5,2,i+1)
    plt.plot(x, yW, label=secNames[i])
    plt.legend(fontsize = fts2)
    plt.yticks(fontsize=fts2)
    plt.xticks(xtc, fontsize=fts2)
    plt.annotate('Mean='+str(round(yW.mean(), 2)), xytext=[1989, yW.max()*0.9], xy=[1989, yW.max()*0.9], fontsize=fts2)     
    plt.annotate('S.D.='+str(round(yW.std(), 2)), xytext=[1990, yW.max()*0.9], xy=[1990, yW.max()*0.9], fontsize=fts2)
    plt.grid(True)

# Net profit margin
fts2 = 15
for i in range(10):
    temp = df1[df1['FFI10_desc']==secNames[i]]
    y = temp['npm_Mean']
    yW = winsorize(y, limits=[0, 0.01])
    plt.subplot(5,2,i+1)
    plt.plot(x, yW, label=secNames[i])
    plt.legend(fontsize = fts2)
    plt.yticks(fontsize=fts2)
    plt.xticks(xtc, fontsize=fts2)
    plt.annotate('Mean='+str(round(yW.mean(), 2)), xytext=[1989, yW.max()*0.9], xy=[1989, yW.max()*0.9], fontsize=fts2)     
    plt.annotate('S.D.='+str(round(yW.std(), 2)), xytext=[1990, yW.max()*0.9], xy=[1990, yW.max()*0.9], fontsize=fts2)
    plt.grid(True)
    
    
#Efficiency 

#Asset turnover 
fts2 = 15
for i in range(10):
    temp = df1[df1['FFI10_desc']==secNames[i]]    
    y = temp['at_turn_Mean']
    yW = winsorize(y, limits=[0, 0.01])
    plt.subplot(5,2,i+1)
    plt.plot(x, yW, label=secNames[i])
    plt.legend(fontsize = fts2)
    plt.yticks(fontsize=fts2)
    plt.xticks(xtc, fontsize=fts2)
    plt.annotate('Mean='+str(round(yW.mean(), 2)), xytext=[1989, yW.max()*0.9], xy=[1989, yW.max()*0.9], fontsize=fts2)     
    plt.annotate('S.D.='+str(round(yW.std(), 2)), xytext=[1990, yW.max()*0.9], xy=[1990, yW.max()*0.9], fontsize=fts2)
    plt.grid(True)

#Inventory Turnover Ratio 
fts2 = 15
for i in range(10):
    temp = df1[df1['FFI10_desc']==secNames[i]]
    y = temp['inv_turn_Mean']
    yW = winsorize(y, limits=[0, 0.01])
    plt.subplot(5,2,i+1)
    plt.plot(x, yW, label=secNames[i])
    plt.legend(fontsize = fts2)
    plt.yticks(fontsize=fts2)
    plt.xticks(xtc, fontsize=fts2)
    plt.annotate('Mean='+str(round(yW.mean(), 2)), xytext=[1989, yW.max()*0.9], xy=[1989, yW.max()*0.9], fontsize=fts2)     
    plt.annotate('S.D.='+str(round(yW.std(), 2)), xytext=[1990, yW.max()*0.9], xy=[1990, yW.max()*0.9], fontsize=fts2)
    plt.grid(True)
#Net working Capital 
fts2 = 15
for i in range(10):
    temp = df1[df1['FFI10_desc']==secNames[i]]
    y = temp['sale_nwc_Mean']
    yW = winsorize(y, limits=[0, 0.01])
    plt.subplot(5,2,i+1)
    plt.plot(x, yW, label=secNames[i])
    plt.legend(fontsize = fts2)
    plt.yticks(fontsize=fts2)
    plt.xticks(xtc, fontsize=fts2)
    plt.annotate('Mean='+str(round(yW.mean(), 2)), xytext=[1989, yW.max()*0.9], xy=[1989, yW.max()*0.9], fontsize=fts2)     
    plt.annotate('S.D.='+str(round(yW.std(), 2)), xytext=[1990, yW.max()*0.9], xy=[1990, yW.max()*0.9], fontsize=fts2)
    plt.grid(True)
    
    
#Solvancy Ratios 
#Current Ratios 
fts2 = 15
for i in range(10):
    temp = df1[df1['FFI10_desc']==secNames[i]]    
    y = temp['curr_ratio_Mean']
    yW = winsorize(y, limits=[0, 0.01])
    plt.subplot(5,2,i+1)
    plt.plot(x, yW, label=secNames[i])
    plt.legend(fontsize = fts2)
    plt.yticks(fontsize=fts2)
    plt.xticks(xtc, fontsize=fts2)
    plt.annotate('Mean='+str(round(yW.mean(), 2)), xytext=[1989, yW.max()*0.9], xy=[1989, yW.max()*0.9], fontsize=fts2)     
    plt.annotate('S.D.='+str(round(yW.std(), 2)), xytext=[1990, yW.max()*0.9], xy=[1990, yW.max()*0.9], fontsize=fts2)
    plt.grid(True)
    
    
#Debt To Equity 

fts2 = 15
for i in range(10):
    temp = df1[df1['FFI10_desc']==secNames[i]]    
    y = temp['de_ratio_Mean']
    yW = winsorize(y, limits=[0, 0.01])
    plt.subplot(5,2,i+1)
    plt.plot(x, yW, label=secNames[i])
    plt.legend(fontsize = fts2)
    plt.yticks(fontsize=fts2)
    plt.xticks(xtc, fontsize=fts2)
    plt.annotate('Mean='+str(round(yW.mean(), 2)), xytext=[1989, yW.max()*0.9], xy=[1989, yW.max()*0.9], fontsize=fts2)     
    plt.annotate('S.D.='+str(round(yW.std(), 2)), xytext=[1990, yW.max()*0.9], xy=[1990, yW.max()*0.9], fontsize=fts2)
    plt.grid(True)
    




'''
This part does pair-wise scatter-plots for industry return and industry characteristics.
'''
y = df1['indret_vw']

# use only one x at a time
x = df1['de_ratio_Mean']
x = df1['curr_ratio_Mean']
x = df1['inv_turn_Mean']
x = df1['roa_Mean']
x = df1['sale_nwc_Mean']
x = df1['roe_Mean']
x = df1['npm_Mean']
x = df1['at_turn_Mean']

xW = winsorize(x, limits=[0.005, 0.005])

fts = 12
plt.figure(dpi = dpi)
plt.scatter(xW, y, c="g", label='Data')
m, b = np.polyfit(xW, y, 1)
plt.plot(xW, m*xW+b, label='Fitted', linewidth=lw, color='r')
plt.xlabel(x.name, fontsize =fts)    
plt.ylabel(y.name, fontsize =fts)
plt.yticks(fontsize=fts)
plt.xticks(fontsize=fts)
plt.legend(fontsize = fts)
# this depends on the x
#plt.annotate('Intercept='+str(round(m*100, 2))+'%', xytext=[xW.max()*0.5, y.max()*0.9], xy=[xW.max()*0.5, y.max()*0.9], fontsize=fts)     
#plt.annotate('Slope='+str(round(b*100, 2))+'%', xytext=[xW.max()*0.75, y.max()*0.9], xy=[xW.max()*0.8, y.max()*0.9], fontsize=fts)
#use this when x is negative, and comment the other
plt.annotate('Intercept='+str(round(m*100, 2))+'%', xytext=[xW.min()*0.3, y.max()*0.9], xy=[xW.min()*0.3, y.max()*0.9], fontsize=fts)     
plt.annotate('Slope='+str(round(b*100, 2))+'%', xytext=[xW.min()*0.5, y.max()*0.9], xy=[xW.min()*0.5, y.max()*0.9], fontsize=fts)
plt.grid(True)

#%%









#%%

import pandas as pd
import numpy as np
from scipy import stats
from matplotlib import pyplot as plt
import seaborn as sns
from scipy.stats.mstats import winsorize


df1 = pd.read_csv('D:\FMT PART 2\Financial Data Visualization' +'/2021-2022 Financial Ratios.csv', sep=",")
colNames = df1.columns
secNames = df1['FFI10_desc'].unique()     # sector names
df1['public_date'] = pd.to_datetime(df1['public_date'])      # converting the date 
dates = df1.public_date.unique()    #naming the dataframe as dates

sns.set()     
#%%
'''
This part plots the cross section
Select the first/last month
'''
i = -1    # select the month
temp = df1[df1['public_date']==dates[i]].copy()    # return a copy not a view
temp['Industry'] = np.arange(1,11)    #Industry indicator
temp['Percent'] = temp['NFIRM']/temp['NFIRM'].sum()*100

# %matplotlib qt
dpi = 200       # resolution of the graph
fts = 12       # font size

# the number of firms
fts2 = 15
y_pos = temp['Industry']
plt.barh(y_pos, temp['NFIRM'])
plt.yticks(y_pos, temp['FFI10_desc'], fontsize = fts2)
plt.xticks(fontsize = fts2)

# a pie chart for percentage
plt.figure(dpi = dpi)
plt.pie(temp['Percent'], labels=temp['FFI10_desc'], autopct='%1.1f%%', shadow=True, radius=1.5)
plt.axis('equal')

#%%
'''
plot the time series jointly
%matplotlib qt
'''
dpi = 200       # resolution of the graph
lw = 1.5          # linewidth
fts = 12       # font size
lsty = ['solid','dotted', 'dashed', 'dashdot']          # line styles
cl = ['black','blue', 'red']        # line colors
x = 2021+1/12*np.arange(len(dates))
xtc = x[::60]

# plot the number of firms evolution
key = 'NFIRM'
plt.figure(dpi = dpi)
for i in range(len(secNames)):
    temp = df1[df1['FFI10_desc']==secNames[i]]    
    plt.plot(x, temp[key], label=secNames[i])
plt.xlabel(r'Year', fontsize =fts)    
plt.ylabel(r'Firm Number', fontsize =fts)
plt.yticks(fontsize=fts)
plt.xticks(xtc, fontsize=fts)
plt.legend(fontsize = fts, ncol=2)
plt.grid(True)

# plot the industry return dynamics with subplots
fts2 = 15
key = 'indret_vw'
for i in range(10):
    temp = df1[df1['FFI10_desc']==secNames[i]]
    plt.subplot(5,2,i+1)
    plt.plot(x, temp[key], label=secNames[i])
    plt.legend(fontsize = fts2)
    plt.yticks(fontsize=fts2)
    plt.xticks(xtc, fontsize=fts2)
    plt.annotate('Mean='+str(round(temp[key].mean()*12, 2)), xytext=[2021, temp[key].max()*0.9], xy=[2021, temp[key].max()*0.9], fontsize=fts2)     
    plt.annotate('S.D.='+str(round(temp[key].std()*np.sqrt(12), 2)), xytext=[2022, temp[key].max()*0.9], xy=[2022, temp[key].max()*0.9], fontsize=fts2)
    plt.grid(True)
    
#Plot the Weights of each industry​        
fts2 = 15
key = 'indret_vw'
fts2 = 12
for i in range(10):
    temp = df1[df1['FFI10_desc']==secNames[i]]
    y = temp[key]
    yW = winsorize(y, limits=[0, 0.01])
    plt.subplot(5,2,i+1)
    plt.plot(x, yW, label=secNames[i])
    plt.legend(fontsize = fts2)
    plt.yticks(fontsize=fts2)
    plt.xticks(xtc, fontsize=fts2)
    plt.annotate('Mean='+str(round(yW.mean(), 2)), xytext=[2021, yW.max()*0.9], xy=[2021, yW.max()*0.9], fontsize=fts2)     
    plt.annotate('S.D.='+str(round(yW.std(), 2)), xytext=[2022, yW.max()*0.9], xy=[2022, yW.max()*0.9], fontsize=fts2)
    plt.grid(True)    

#Profitability Ratios 


# Return on Asset
fts2 = 12
for i in range(10):
    temp = df1[df1['FFI10_desc']==secNames[i]]
    y = temp['roa_Mean']
    yW = winsorize(y, limits=[0, 0.01])
    plt.subplot(5,2,i+1)
    plt.plot(x, yW, label=secNames[i])
    plt.legend(fontsize = fts2)
    plt.yticks(fontsize=fts2)
    plt.xticks(xtc, fontsize=fts2)
    plt.annotate('Mean='+str(round(yW.mean(), 2)), xytext=[2021, yW.max()*0.9], xy=[2021, yW.max()*0.9], fontsize=fts2)     
    plt.annotate('S.D.='+str(round(yW.std(), 2)), xytext=[2022, yW.max()*0.9], xy=[2022, yW.max()*0.9], fontsize=fts2)
    plt.grid(True)
    
#  Return on Equity 
fts2 = 12
for i in range(10):
    temp = df1[df1['FFI10_desc']==secNames[i]]
    y = temp['roe_Mean']
    yW = winsorize(y, limits=[0, 0.01])
    plt.subplot(5,2,i+1)
    plt.plot(x, yW, label=secNames[i])
    plt.legend(fontsize = fts2)
    plt.yticks(fontsize=fts2)
    plt.xticks(xtc, fontsize=fts2)
    plt.annotate('Mean='+str(round(yW.mean(), 2)), xytext=[2021, yW.max()*0.9], xy=[2021, yW.max()*0.9], fontsize=fts2)     
    plt.annotate('S.D.='+str(round(yW.std(), 2)), xytext=[2022, yW.max()*0.9], xy=[2022, yW.max()*0.9], fontsize=fts2)
    plt.grid(True)

# Net profit margin
fts2 = 15
for i in range(10):
    temp = df1[df1['FFI10_desc']==secNames[i]]
    y = temp['npm_Mean']
    yW = winsorize(y, limits=[0, 0.01])
    plt.subplot(5,2,i+1)
    plt.plot(x, yW, label=secNames[i])
    plt.legend(fontsize = fts2)
    plt.yticks(fontsize=fts2)
    plt.xticks(xtc, fontsize=fts2)
    plt.annotate('Mean='+str(round(yW.mean(), 2)), xytext=[2021, yW.max()*0.9], xy=[2021, yW.max()*0.9], fontsize=fts2)     
    plt.annotate('S.D.='+str(round(yW.std(), 2)), xytext=[2022, yW.max()*0.9], xy=[2022, yW.max()*0.9], fontsize=fts2)
    plt.grid(True)
    
    
#Efficiency 

#Asset turnover 
fts2 = 15
for i in range(10):
    temp = df1[df1['FFI10_desc']==secNames[i]]    
    y = temp['at_turn_Mean']
    yW = winsorize(y, limits=[0, 0.01])
    plt.subplot(5,2,i+1)
    plt.plot(x, yW, label=secNames[i])
    plt.legend(fontsize = fts2)
    plt.yticks(fontsize=fts2)
    plt.xticks(xtc, fontsize=fts2)
    plt.annotate('Mean='+str(round(yW.mean(), 2)), xytext=[2021, yW.max()*0.9], xy=[2021, yW.max()*0.9], fontsize=fts2)     
    plt.annotate('S.D.='+str(round(yW.std(), 2)), xytext=[2022, yW.max()*0.9], xy=[2022, yW.max()*0.9], fontsize=fts2)
    plt.grid(True)

#Inventory Turnover Ratio 
fts2 = 15
for i in range(10):
    temp = df1[df1['FFI10_desc']==secNames[i]]
    y = temp['inv_turn_Mean']
    yW = winsorize(y, limits=[0, 0.01])
    plt.subplot(5,2,i+1)
    plt.plot(x, yW, label=secNames[i])
    plt.legend(fontsize = fts2)
    plt.yticks(fontsize=fts2)
    plt.xticks(xtc, fontsize=fts2)
    plt.annotate('Mean='+str(round(yW.mean(), 2)), xytext=[2021, yW.max()*0.9], xy=[2021, yW.max()*0.9], fontsize=fts2)     
    plt.annotate('S.D.='+str(round(yW.std(), 2)), xytext=[2022, yW.max()*0.9], xy=[2022, yW.max()*0.9], fontsize=fts2)
    plt.grid(True)
#Net working Capital 
fts2 = 15
for i in range(10):
    temp = df1[df1['FFI10_desc']==secNames[i]]
    y = temp['sale_nwc_Mean']
    yW = winsorize(y, limits=[0, 0.01])
    plt.subplot(5,2,i+1)
    plt.plot(x, yW, label=secNames[i])
    plt.legend(fontsize = fts2)
    plt.yticks(fontsize=fts2)
    plt.xticks(xtc, fontsize=fts2)
    plt.annotate('Mean='+str(round(yW.mean(), 2)), xytext=[2021, yW.max()*0.9], xy=[2021, yW.max()*0.9], fontsize=fts2)     
    plt.annotate('S.D.='+str(round(yW.std(), 2)), xytext=[2022, yW.max()*0.9], xy=[2022, yW.max()*0.9], fontsize=fts2)
    plt.grid(True)
    
    
#Solvancy Ratios 
#Current Ratios 
fts2 = 15
for i in range(10):
    temp = df1[df1['FFI10_desc']==secNames[i]]    
    y = temp['curr_ratio_Mean']
    yW = winsorize(y, limits=[0, 0.01])
    plt.subplot(5,2,i+1)
    plt.plot(x, yW, label=secNames[i])
    plt.legend(fontsize = fts2)
    plt.yticks(fontsize=fts2)
    plt.xticks(xtc, fontsize=fts2)
    plt.annotate('Mean='+str(round(yW.mean(), 2)), xytext=[2021, yW.max()*0.9], xy=[2021, yW.max()*0.9], fontsize=fts2)     
    plt.annotate('S.D.='+str(round(yW.std(), 2)), xytext=[2022, yW.max()*0.9], xy=[2022, yW.max()*0.9], fontsize=fts2)
    plt.grid(True)
    
    
#Debt To Equity 

fts2 = 15
for i in range(10):
    temp = df1[df1['FFI10_desc']==secNames[i]]    
    y = temp['de_ratio_Mean']
    yW = winsorize(y, limits=[0, 0.01])
    plt.subplot(5,2,i+1)
    plt.plot(x, yW, label=secNames[i])
    plt.legend(fontsize = fts2)
    plt.yticks(fontsize=fts2)
    plt.xticks(xtc, fontsize=fts2)
    plt.annotate('Mean='+str(round(yW.mean(), 2)), xytext=[2021, yW.max()*0.9], xy=[2021, yW.max()*0.9], fontsize=fts2)     
    plt.annotate('S.D.='+str(round(yW.std(), 2)), xytext=[2022, yW.max()*0.9], xy=[2022, yW.max()*0.9], fontsize=fts2)
    plt.grid(True)
    




'''
This part does pair-wise scatter-plots for industry return and industry characteristics.
'''
y = df1['indret_vw']

# use only one x at a time
x = df1['de_ratio_Mean']
x = df1['curr_ratio_Mean']
x = df1['inv_turn_Mean']
x = df1['roa_Mean']
x = df1['sale_nwc_Mean']
x = df1['roe_Mean']
x = df1['npm_Mean']
x = df1['at_turn_Mean']

xW = winsorize(x, limits=[0.005 , 0.005])

fts = 12
plt.figure(dpi = dpi)
plt.scatter(xW, y, c="g", label='Data')
m, b = np.polyfit(xW, y, 1)
plt.plot(xW, m*xW+b, label='Fitted', linewidth=lw, color='r')
plt.xlabel(x.name, fontsize =fts)    
plt.ylabel(y.name, fontsize =fts)
plt.yticks(fontsize=fts)
plt.xticks(fontsize=fts)
plt.legend(fontsize = fts)
# this depends on the x
#plt.annotate('Intercept='+str(round(m*100, 2))+'%', xytext=[xW.max()*0.5, y.max()*0.9], xy=[xW.max()*0.5, y.max()*0.9], fontsize=fts)     
#plt.annotate('Slope='+str(round(b*100, 2))+'%', xytext=[xW.max()*0.75, y.max()*0.9], xy=[xW.max()*0.8, y.max()*0.9], fontsize=fts)
#plt.grid(True)
plt.annotate('Intercept='+str(round(m*100, 2))+'%', xytext=[xW.max()*0.5, y.max()*0.9], xy=[xW.max()*0.5, y.max()*0.9], fontsize=fts)     
plt.annotate('Slope='+str(round(b*100, 2))+'%', xytext=[xW.max()*0.75, y.max()*0.9], xy=[xW.max()*0.8, y.max()*0.9], fontsize=fts)
#use this when x is negative, and comment the other