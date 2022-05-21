import csv
import os 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('parsing/2022-05-19-BTC-USD.csv', header=1, index_col='UnixTime', usecols=['Price','UnixTime'])
df.index = pd.to_datetime(df.index, unit='s')
df.index.names = ['Time']


dt = pd.to_datetime("2022-05-19 18:00:03")
idx = df.index[df.index.get_loc(dt, method='nearest')]

print (idx)
#print(df.loc['2022-05-19 18:00:00'] )
#print(fcl(df, '2022-05-19 18:00:01'))

#df.loc['2022-05-19 18:00:07' : '2022-05-19 19:00:07'] #get a subset dataframe


#print (df)
df.plot(y ="Price")
plt.show()


exit()