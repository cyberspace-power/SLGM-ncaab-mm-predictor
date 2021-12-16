import pandas as pd
# import numpy as np

results_table = pd.read_csv("./../Data/team_results_2013-2021.csv")
bart_names = list(dict.fromkeys(results_table['teamName'].to_list()))  # list of Barttovik school names
print(len(bart_names))
results_table = results_table.set_index(["teamName", "year"]).sort_index()
results_table['prev_3s_recruits'] = 0
results_table['prev_4s_recruits'] = 0
results_table['prev_5s_recruits'] = 0
results_table['curr_3s_recruits'] = 0
results_table['curr_4s_recruits'] = 0
results_table['curr_5s_recruits'] = 0


recruit_table = pd.read_csv("./../Data/recruiting.csv").set_index(["teamName", "year"]).sort_index()
# print(recruit_table)

for team in bart_names:
    # Print Teams and years:
    '''a = results_table.loc[(team, slice(None)), :]
    if len(a) < 9:
        print(team + ": " + str(len(a)), end='')
        print(a)'''

    for year in range(2012, 2022):
        try:
            if year != 2012:
                rec_array_curr = recruit_table.loc[(team, year), :].to_numpy()
                results_table.loc[(team, year), "curr_3s_recruits"] = rec_array_curr[0]
                results_table.loc[(team, year), "curr_4s_recruits"] = rec_array_curr[1]
                results_table.loc[(team, year), "curr_5s_recruits"] = rec_array_curr[2]
            if year != 2021:
                rec_array_prev = recruit_table.loc[(team, year), :].to_numpy()
                results_table.loc[(team, year + 1), "prev_3s_recruits"] = rec_array_prev[0]
                results_table.loc[(team, year + 1), "prev_4s_recruits"] = rec_array_prev[1]
                results_table.loc[(team, year + 1), "prev_5s_recruits"] = rec_array_prev[2]
        except KeyError:
            continue

print(results_table)
results_table.to_csv("./../Data/recruiting_2013-2021.csv", index=True, header=True)
