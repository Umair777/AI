import pandas as pd
import matplotlib.pyplot as plt
from nba_api.stats.static import teams
from nba_api.stats.endpoints import leaguegamefinder
import requests

dict_={'a':[11,21,31],'b':[12,22,32]}

df=pd.DataFrame(dict_)

def one_dict(list_dict):
    print('==========')
    keys=list_dict[0].keys()
    print('Print Keys:')
    print(keys)
    out_dict={key:[] for key in keys}
    print('Initialized output dictionary:')
    print(out_dict)
    for dict_ in list_dict:
        for key, value in dict_.items():
            out_dict[key].append(value)
    return out_dict


nba_teams = teams.get_teams()
threenba_teams = nba_teams[0:3]
print(threenba_teams)
print(type(threenba_teams))
dict_nba_team=one_dict(threenba_teams)
print(type(dict_nba_team))
df_teams=pd.DataFrame(dict_nba_team)
print("NBA Teams DataFrame:")
print(df_teams.head())
df_warriors=df_teams[df_teams['nickname']=='Warriors']
print("Golden State Warriors DataFrame:")
print(df_warriors)

# id_warriors = df_warriors[['id']].values[0][0]
# print("Warriors Team ID:", id_warriors)


filename = "https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%205/Labs/Golden_State.pkl"
def download(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, "wb") as f:
            f.write(response.content)    


download(filename, "Golden_State.pkl")
file_name = "Golden_State.pkl"
games = pd.read_pickle(file_name)
print(games.head())

games_home=games[games['MATCHUP']=='GSW vs. TOR']
games_away=games[games['MATCHUP']=='GSW @ TOR']

print(games_home['PLUS_MINUS'].mean())
print(games_away['PLUS_MINUS'].mean())


fig, ax = plt.subplots()

games_away.plot(x='GAME_DATE',y='PLUS_MINUS', ax=ax)
games_home.plot(x='GAME_DATE',y='PLUS_MINUS', ax=ax)
ax.legend(["away", "home"])
plt.savefig("warriors_home_away.png")
plt.show()



'''Outside:
[{'id': 1610612737, 'full_name': 'Atlanta Hawks', 'abbreviation': 'ATL', 'nickname': 'Hawks', 'city': 'Atlanta', 'state': 'Georgia', 'year_founded': 1949}, {'id': 1610612738, 'full_name': 'Boston Celtics', 'abbreviation': 'BOS', 'nickname': 'Celtics', 'city': 'Boston', 'state': 'Massachusetts', 'year_founded': 1946}, {'id': 1610612739, 'full_name': 'Cleveland Cavaliers', 'abbreviation': 'CLE', 'nickname': 'Cavaliers', 'city': 'Cleveland', 'state': 'Ohio', 'year_founded': 1970}]
<class 'list'>
==========
Print Keys:
dict_keys(['id', 'full_name', 'abbreviation', 'nickname', 'city', 'state', 'year_founded'])
Initialized output dictionary:
{'id': [], 'full_name': [], 'abbreviation': [], 'nickname': [], 'city': [], 'state': [], 'year_founded': []}
<class 'dict'>
NBA Teams DataFrame:
           id            full_name abbreviation   nickname       city          state  year_founded
0  1610612737        Atlanta Hawks          ATL      Hawks    Atlanta        Georgia          1949
1  1610612738       Boston Celtics          BOS    Celtics     Boston  Massachusetts          1946
2  1610612739  Cleveland Cavaliers          CLE  Cavaliers  Cleveland           Ohio          1970
Golden State Warriors DataFrame:
Empty DataFrame
Columns: [id, full_name, abbreviation, nickname, city, state, year_founded]
Index: []
  SEASON_ID     TEAM_ID TEAM_ABBREVIATION              TEAM_NAME  ... BLK   TOV  PF PLUS_MINUS
0     22019  1610612744               GSW  Golden State Warriors  ...   3  11.0  21        3.2
1     22019  1610612744               GSW  Golden State Warriors  ...   7  20.0  20       -8.0
2     22019  1610612744               GSW  Golden State Warriors  ...   4  13.0  22        8.0
3     22019  1610612744               GSW  Golden State Warriors  ...   3  20.0  25       10.0
4     22019  1610612744               GSW  Golden State Warriors  ...   3  13.0  15       -8.0

[5 rows x 28 columns]
'''