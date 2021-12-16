import requests
from bs4 import BeautifulSoup
import pandas as pd

baseurl = "https://verbalcommits.com/transfers/"

years = [2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]

# transferStars = {'year', 'stars': [], 'new team': []}

transfersdf = pd.DataFrame()

for year in years:
    url = baseurl+str(year)

    page = requests.get(url).text
    soup = BeautifulSoup(page, 'html.parser')

    my_table = soup.find('table', class_='table full table-hover tablesorter')

    rows = my_table.tbody.find_all('tr')

    transfers = {'stars': [], 'new team': []}
    
    for row in rows:
        cells = row.find_all('td')
        stars = float(cells[0].text.strip())
        new_team = cells[9].text.strip()

        if new_team != '':
            transfers['stars'].append(stars)
            transfers['new team'].append(new_team)

    df = pd.DataFrame(transfers)
    df = df.groupby(['new team']).sum().reset_index()
    df['year'] = year
    print(df)
    transfersdf = transfersdf.append(df, ignore_index = True)

print(transfersdf)
transfersdf.to_csv("transfers.csv")
