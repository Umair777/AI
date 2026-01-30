import pandas as pd
import matplotlib.pyplot as plt
from nba_api.stats.static import teams

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
id_warriors=df_warriors[['id']].values[0][0]
print("Warriors Team ID:", id_warriors)


