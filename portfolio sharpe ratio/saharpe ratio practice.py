# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 19:57:07 2020

@author: admin
"""

###Refer:https://towardsdatascience.com/calculating-sharpe-ratio-with-python-755dcb346805


aapl = pd.read_csv(‘AAPL_CLOSE’, index_col=’Date’, parse_dates=True)

#calculate a normalized return
for stock_df in (aapl, cisco, ibm, amzn):
    stock_df[‘Norm return’] = stock_df[‘Adj. Close’] / stock_df.iloc[0][‘Adj. Close’]

##assume our portfolio will consist of: 35% for Apple, 25% for Cisco, and 20% each for IBM and Amazon.
for stock_df, allocation in zip((aapl, cisco, ibm, amzn),[.35,.25,.2,.2]):
    stock_df[‘Allocation’] = stock_df[‘Norm return’] * allocation

for stock_df in (aapl, cisco, ibm, amzn):
stock_df[‘Position’] = stock_df[‘Allocation’]*10000

#In order to get all our positions in one single table, we can isolate the column “Position” from each stock and merge it in a new dataframe called “portf_val”. We then rename the columns to match each stock.
all_pos = [aapl[‘Position’], cisco[‘Position’], ibm[‘Position’], amzn[‘Position’]]
portf_val.columns = [‘AAPL Pos’,’CISCO Pos’,’IBM Pos’,’AMZN Pos’]
portf_val = pd.concat(all_pos, axis=1)
#We can also create a column to show the sum of all positions, which is our Total Position.
portf_val[‘Total Pos’] = portf_val.sum(axis=1)
portf_val.head()

#From here we can actually draw a few charts to have an idea of what happened to our portfolio value during all the days in our data.
import matplotlib.pyplot as plt
plt.style.use(‘fivethirtyeight’)
portf_val[‘Total Pos’].plot(figsize=(10,8))

#How about our individual stocks? How did they perform?
portf_val.drop(‘Total Pos’, axis=1).plot(figsize=(10,8))

#cumulative return.
cumulative_return = 100 * ( portf_val [ ‘Total Pos’ ] [-1 ] / portf_val [ ‘Total Pos’] [ 0 ] -1)
print(‘Your cumulative return was {:.2f}% ‘.format(cumulative_return))

#add the percentage change in each day — hence the 1 in the formula below. The daily return will be important to calculate the Sharpe ratio.
portf_val[‘Daily Return’] = portf_val[‘Total Pos’].pct_change(1)

#calc Sharpe
Sharpe_Ratio = portf_val[‘Daily Return’].mean() / portf_val[‘Daily Return’].std()