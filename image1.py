import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('songs_normalize.csv')

df_sort_genres=pd.DataFrame(df.assign(genres=df.genre.str.split(",")).explode('genre'))
df_sort_genres=pd.DataFrame(df.assign(genres=df.genre.str.split(",")).explode('genres'))

all_genres=pd.DataFrame(df_sort_genres['genres'].value_counts()[:]).reset_index()


all_genres.set_index("index", inplace = True)

all_genres.loc['pop']['genres'] = all_genres.iloc[0][0] + all_genres.iloc[2][0]
all_genres.loc['rock']['genres'] = all_genres.iloc[5][0] + all_genres.iloc[6][0]
all_genres.loc['R&B']['genres'] = all_genres.iloc[3][0] + all_genres.iloc[13][0]
all_genres.loc['metal']['genres'] = all_genres.iloc[17][0] + all_genres.iloc[7][0]
all_genres.loc['Dance/Electronic']['genres'] = all_genres.iloc[4][0] + all_genres.iloc[9][0]
all_genres.loc['latin']['genres'] = all_genres.iloc[8][0] + all_genres.iloc[12][0]
all_genres.loc['Folk/Acoustic']['genres'] = all_genres.iloc[20][0] + all_genres.iloc[11][0]
all_genres.loc['country']['genres'] = all_genres.iloc[14][0] + all_genres.iloc[15][0]
all_genres.loc['easy listening']['genres'] = all_genres.iloc[24][0] + all_genres.iloc[18][0]


data = all_genres.drop(labels=[' pop',' R&B', ' rock', ' Dance/Electronic', ' metal', ' latin', ' Folk/Acoustic', ' country', ' easy listening'], axis=0)


data.rename(columns = {'index':'Genres','genres':'Total_Count'}, inplace = True)
plt.bar(data.index, data['Total_Count'])
plt.title("Number of Songs in Each Genre")
plt.xlabel('Genre')
plt.ylabel('Number of Songs')
plt.xticks(rotation=45, ha='right', size = 7)
plt.show()

