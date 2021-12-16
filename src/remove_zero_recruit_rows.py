import pandas as pd

df = pd.read_csv("./../Data/recruiting.csv")
print("Old length: " + str(len(df)))
df = df[(df['3_star_recruits'] != 0) | (df['4_star_recruits'] != 0) | (df['5_star_recruits'] != 0)]
print("New length: " + str(len(df)))
# df.to_csv("./../Data/Recruiting1.csv", index=False, header=True)
