from bs4 import BeautifulSoup as bs
import pandas as pd
import re
import requests


def get_team_results():
    result_dict = {' R68': 'R64', ' R64': 'R64', ' R32': 'R32', ' Sweet Sixteen': 'S16',
                   ' Elite Eight': 'E8', ' Final Four': 'F4', ' Finals': 'F2', ' CHAMPS': 'CHMP'}
    features = {'teamName': [], 'year': [], 'seed_points': [], 'results': []}
    for i in range(2010, 2022):
        print(i)
        resp = requests.get('https://barttorvik.com/trank.php?year=' + str(i) + "#")
        soup = bs(resp.content, "html.parser")
        teams = soup.find_all(class_="teamname")
        for team in teams:
            team_data = re.split(r',|\s{2,}', team.find('a').get_text())
            #print(team_text)
            features['teamName'].append(team_data[0])
            features['year'].append(i)
            if len(team_data) == 1:  # This means that this team did not make the tournament
                features['seed_points'].append(0)
                features['results'].append("NIT")
            else:  # Team made the tournament
                seed = int(re.split(' ', team_data[1])[0])
                features['seed_points'].append(17-seed)  # Reverse order of seed (1 seed = 16 pts, 16 seed = 1 pt, etc.)
                features['results'].append(result_dict[team_data[2]])
    df = pd.DataFrame(features)
    df.to_csv('./../Data/Team_Results1.csv', index=False, header=True)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    get_team_results()
