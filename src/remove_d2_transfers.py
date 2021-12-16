import pandas as pd

# Get transfer school names:
transfer_df = pd.read_csv("./../Data/transfers_2013-2021.csv")
transfer_names = list(dict.fromkeys(transfer_df['teamName'].to_list()))
print(len(transfer_df))

# Get barttovik school names:
results_table = pd.read_csv("./../Data/team_results_2013-2021.csv")
bart_names = list(dict.fromkeys(results_table['teamName'].to_list()))  # list of Barttovik school names

for name in transfer_names:
    index_names = transfer_df[~transfer_df['teamName'].isin(bart_names)].index
    transfer_df.drop(index_names, inplace=True)
print(len(transfer_df))

transfer_df.to_csv("./../Data/transfers1_2013-2021.csv", index=False, header=True)
