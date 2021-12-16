import urllib.request as urllib
import json
import re
from bs4 import BeautifulSoup
import requests
import pandas as pd

years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]
baseurl = "https://barttorvik.com/"
teamurl = "_team_results.json"

teamNames = set()

for year in years:
    url = baseurl+str(year)+teamurl
    res = requests.get(url)
    res = res.json()
    for team in range(len(res)):
        teamName = res[team][1]
        teamNames.add(teamName)

print(len(teamNames))
print(teamNames)

features = {'teamName': [], 'year': [], 'returningMins%': [], 'wins': [], 'totalGames': [], 'OE': [], 'DE': [], 'sos': [], 'adjTempo': []}
idx =-1
teams = ['Alabama A&M', 'Prairie View A&M', 'Texas A&M', 'Florida A&M', 'Texas A&M Corpus Chris', 'William & Mary', 'North Carolina A&T']

urls = ['https://barttorvik.com/program-maps.php?tvalue=Alabama+A%26M&year=2022&sort=&t2value=None&avg=all&top=0&quad=4&venue=All&type=All&xax=37&yax=3',
        'https://barttorvik.com/program-maps.php?tvalue=Prairie+View+A%26M&year=2022&sort=&t2value=None&avg=all&top=0&quad=4&venue=All&type=All&xax=37&yax=3',
        'https://barttorvik.com/program-maps.php?tvalue=Texas+A%26M&year=2022&sort=&t2value=None&avg=all&top=0&quad=4&venue=All&type=All&xax=37&yax=3',
        'https://barttorvik.com/program-maps.php?tvalue=Florida+A%26M&year=2022&sort=&t2value=None&avg=all&top=0&quad=4&venue=All&type=All&xax=37&yax=3',
        'https://barttorvik.com/program-maps.php?tvalue=Texas+A%26M+Corpus+Chris&year=2022&sort=&t2value=None&avg=all&top=0&quad=4&venue=All&type=All&xax=37&yax=3',
        'https://barttorvik.com/program-maps.php?tvalue=William+%26+Mary&year=2022&sort=&t2value=None&avg=all&top=0&quad=4&venue=All&type=All&xax=37&yax=3',
        'https://barttorvik.com/program-maps.php?tvalue=North+Carolina+A%26T&year=2022&sort=&t2value=None&avg=all&top=0&quad=4&venue=All&type=All&xax=37&yax=3']
for team in teamNames:
    idx+=1
    print(team)
    print()
    baseurl = "https://barttorvik.com/program-maps.php?tvalue="+str(team)+"&year=2022&sort=&t2value=None&avg=all&top=0&quad=4&venue=All&type=All&xax=37&yax=3"
    baseurl = baseurl.replace(" ", "%20")
    # baseurl = baseurl.replace("&", "%26")
    # baseurl = urls[idx]
    web = urllib.urlopen(baseurl)
    soup = BeautifulSoup(web.read(), 'lxml')
    scripts = soup.find_all("script")
    if len(scripts)>=2:
        data  = soup.find_all("script")[1].string
        gdata = re.findall(r"var gdata = (.*?);", data)
        jsondata = json.loads(gdata[0])

        for i in range(len(jsondata)):
            if jsondata[i][30] == 2008 or jsondata[i][30] == 2009:
                continue
            features['teamName'].append(jsondata[i][0])
            features['year'].append(jsondata[i][30])
            features['returningMins%'].append(jsondata[i][37])
            features['wins'].append(jsondata[i][5])
            features['totalGames'].append(jsondata[i][6])
            features['OE'].append(jsondata[i][1])
            features['DE'].append(jsondata[i][2])
            features['sos'].append(jsondata[i][38])
            features['adjTempo'].append(jsondata[i][26])
    else:
        print("Not found ", team)


df = pd.DataFrame(features)
df.to_csv("./team features missing.csv")
