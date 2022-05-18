import csv
import os 
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('parsing/2022-05-17-ETH-USD.csv', header=1)

print (df)
df.plot(y ="Price")
plt.show()


exit()