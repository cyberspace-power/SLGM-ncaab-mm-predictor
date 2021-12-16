import pandas as pd


bart_pd = pd.read_csv("./../Data/team_results_2013-2021.csv")
bart_names = list(dict.fromkeys(bart_pd['teamName'].to_list()))

file_name = input("Enter the file name (from the data folder) that you want to check the team names of: ")
file_name = "./../Data/" + file_name

df = pd.read_csv(file_name)
df_names = df['teamName'].to_list()

# Check bart_names -> file_to_check
nonmatching_names = []
for name in df_names:
    if name not in bart_names and name not in nonmatching_names:
        nonmatching_names.append(name)

if len(nonmatching_names) == 0:
    print("barttovik -> " + file_name + ": All school names match!")
else:
    for name in nonmatching_names:
        # print("barttovik -> " + file_name + ": " + str(df[df['teamName'] == name]))
        print("barttovik -> " + file_name + ": " + name)

# file_to_check -> Check bart_names
nonmatching_names = []
for name in bart_names:
    if name not in df_names and name not in nonmatching_names:
        nonmatching_names.append(name)

if len(nonmatching_names) == 0:
    print(file_name + " -> barttovik: All school names match!")
else:
    for name in nonmatching_names:
        # print(file_name + " -> barttovik: " + str(bart_pd[bart_pd['teamName'] == name]))
        print(file_name + " -> barttovik: " + name)
