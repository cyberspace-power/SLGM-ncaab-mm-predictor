import pandas as pd


bart_pd = pd.read_csv("./../Data/team_results_2013-2021.csv")
bart_names = bart_pd['teamName'].to_list()

file_name = input("Enter the file name (from the data folder) that you want to check the team names of: ")
file_name = "./../Data/" + file_name

df = pd.read_csv(file_name)
df_names = df['teamName'].to_list()

nonmatching_names = []
for name in df_names:
    if name not in bart_names and name not in nonmatching_names:
        nonmatching_names.append(name)

if len(nonmatching_names) == 0:
    print("All school names match!")
else:
    for name in nonmatching_names:
        print(df[df['teamName'] == name])
