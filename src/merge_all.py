import pandas as pd

df1 = pd.read_csv("SLGM-ncaab-mm-predictor/Data/combined.csv").set_index(["teamName", "year"]).sort_index()

df2 = pd.read_csv("cleaned_team_results_2013-2021_encoded.csv").set_index(["teamName", "year"]).sort_index()

df3 = pd.read_csv("cleaned_team_features_final.csv").set_index(["teamName", "year"]).sort_index()

df4 = pd.read_csv("SLGM-ncaab-mm-predictor/Data/transfers_2013-2021.csv").set_index(["teamName", "year"]).sort_index()

df1 = df1[['prev_3s_recruits', 'prev_4s_recruits',
       'prev_5s_recruits', 'curr_3s_recruits', 'curr_4s_recruits',
       'curr_5s_recruits']]

m = df1.merge(df2, on = ['teamName', 'year'], how = 'right')

print(df1)
print(df2)
print(df3)
print(df4)

print("once merge")
print(m)
print()

m = m.merge(df3, on = ['teamName', 'year'], how = 'left')
print("twice merge")
print(m)


m = m.merge(df4, on = ['teamName', 'year'], how = 'left')
m['stars'] = m['stars'].fillna(0)

m.drop(['wins', 'totalGames', 'OE', 'DE'], axis=1, inplace=True)
m['label'] = m['NIT'].copy()

m['label'] = 1 - m['label']

print("thrice merge")
print(m)

m['sos'] = m['sos']/100
m['returningMins%'] = m['returningMins%']/100

print("four merge")
print(m)

def z_score_standardization(series):
    return (series - series.mean()) / series.std()

m['adjTempo'] = z_score_standardization(m['adjTempo'])
m['stars'] = z_score_standardization(m['stars'])
m['overall efficiency'] = z_score_standardization(m['overall efficiency'])
m['seed_points'] = z_score_standardization(m['seed_points'])

print("five merge")
print(m)
m.to_csv("all_combined.csv")
