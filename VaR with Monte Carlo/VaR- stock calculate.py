# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 21:15:16 2020

@author: admin
"""

#####VaR with Monte Carlo


import sys as sy
import numpy as np
import pandas as pd
import tushare as ts
import pyecharts as pye
from sklearn import datasets as ds
import matplotlib as mpl
from matplotlib import pyplot as plt
import seaborn as sns
import pyecharts as pye


#First, let’s get market prices of AAPL from Quandl again, and compute the returns.
end = datetime.datetime.now()
start = end - datetime.timedelta(365)
AAPL = quandl.get('EOD/AAPL', start_date=start, end_date=end)

rets_1 = (AAPL['Close']/AAPL['Close'].shift(1))-1 #credit default rate可以在这里替代


mean = np.mean(rets_1)
std = np.std(rets_1)
Z_99 = scipy.stats.norm.ppf(1-0.99)
price = AAPL.iloc[-1]['Close']
print(mean, std, Z_99, price)

# compute the parametric and historical VAR numbers so we have a basis for comparison.

ParamVAR = price*Z_99*std
HistVAR = price*np.percentile(rets_1.dropna(), 1)

print('Parametric VAR is {0:.3f} and Historical VAR is {1:.3f}'.format(ParamVAR, HistVAR))

#For Monte Carlo simulation, we simply apply a simulation using the assumptions of normality, 
#and the mean and std computed above.

np.random.seed(42)
n_sims = 1000000
sim_returns = np.random.normal(mean, std, n_sims)
SimVAR = price*np.percentile(sim_returns, 1)
print('Simulated VAR is ', SimVAR)

