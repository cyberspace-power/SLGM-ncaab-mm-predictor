import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


def prepare_webpage(driver, year):
    driver.get("https://247sports.com/Season/" + year + "-Basketball/CompositeTeamRankings/")

    # Click "load more" until all teams loaded
    flag = True
    while flag:
        time.sleep(5)
        try:  # If element exists, click button
            click_button = driver.find_element(By.CSS_SELECTOR, '.rankings-page__showmore > a:nth-child(1)')
            click_button.click()
        except NoSuchElementException:  # If element does not exist, terminate while loop
            flag = False
    time.sleep(3)


def get_recruit_data(driver):
    features = {'teamName': [], 'year': [], '3_star_recruits': [], '4_star_recruits': [], '5_star_recruits': []}
    for i in range(2011, 2022):
        print(i)
        prepare_webpage(driver, str(i))

        # Remove any non-D1 teams:
        rows = driver.find_elements(By.CLASS_NAME, 'rankings-page__list-item')
        new_rows = []
        for j in range(len(rows)):
            try:
                rows[j].find_element(By.CLASS_NAME, 'rankings-page__name-link')
                new_rows.append(rows[j])
            except NoSuchElementException:
                continue

        team_names = []
        three_stars = []
        four_stars = []
        five_stars = []
        for row in new_rows:
            team_names.append(row.find_element(By.CLASS_NAME, 'rankings-page__name-link').text)
            star_recruits = row.find_element(By.CLASS_NAME, 'star-commits-list').find_elements(By.TAG_NAME, 'div')
            try:
                three_stars.append(int(star_recruits[2].text))
            except ValueError:
                three_stars.append(0)
            try:
                four_stars.append(int(star_recruits[1].text))
            except ValueError:
                four_stars.append(0)
            try:
                five_stars.append(int(star_recruits[0].text))
            except ValueError:
                five_stars.append(0)

        year_list = [str(i)] * len(team_names)  # Create list of the year n times

        features['teamName'] += team_names
        features['year'] += year_list
        features['3_star_recruits'] += three_stars
        features['4_star_recruits'] += four_stars
        features['5_star_recruits'] += five_stars

        if len(features['teamName']) != len(features['year']) or len(features['year']) != len(
                features['3_star_recruits']) or len(features['4_star_recruits']) != len(
                features['3_star_recruits']) or len(features['5_star_recruits']) != len(features['4_star_recruits']):
            print(str(i) + ": " + str(len(features['teamName'])) + ' ' + str(len(features['year'])) + ' ' + str(
                len(features['3_star_recruits'])) + ' ' + str(len(features['4_star_recruits'])) + ' ' + str(
                len(features['5_star_recruits'])))

    df = pd.DataFrame(features)
    print(df)
    df.to_csv("./../Data/Recruiting1.csv", index=False, header=True)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    drive = webdriver.Firefox()
    get_recruit_data(drive)
    drive.close()
