import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('songs_normalize.csv')
dict1 = df.groupby('artist').count().to_dict(orient='dict')
dict1 = dict1['song']
sorted_values = sorted(dict1.values())
sorted_dict = {}

for i in sorted_values:
    for k in dict1.keys():
        if dict1[k] == i:
            sorted_dict[k] = dict1[k]
top_ten = list(sorted_dict.items())
top_ten = top_ten[-10:]
artists = []
numbers = []
for value in top_ten:
    artists.append(value[0])
    numbers.append(value[1])
plt.bar(artists, numbers)
plt.xticks(rotation=45, ha='right', size = 7)
plt.title("Top 10 Artists with Highest Number of Times Charted")
plt.xlabel('Artist')
plt.ylabel('Number of Times Charted')
plt.show()
