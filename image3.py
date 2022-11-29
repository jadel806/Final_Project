import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_csv('songs_normalize.csv')
y = df['popularity']
x = df['acousticness']
plt.plot(x, y , 'o')

m, b = np.polyfit(x, y, 1)


plt.plot(x, m*x+b)
plt.title("Popularity vs Acoutsticness Correlation")
plt.ylabel('Popularity')
plt.xlabel('Acousticness')


plt.show()