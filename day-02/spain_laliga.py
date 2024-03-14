from selenium import webdriver
driver = webdriver.Chrome()
url= "https://www.adamchoi.co.uk/overs/detailed"

# open url with webdriver
driver.get(url)

# click on all matches button
all_matches_button = driver.find_element(by='xpath',value= '//label[contains(@analytics-event,"All matches")]')
all_matches_button.click()

# selection with drop down menu
from selenium.webdriver.support.ui  import Select
dropdown= Select(driver.find_element(by='id',value='country'))
dropdown.select_by_visible_text('Spain')

dropdown_league = Select(driver.find_element(by='id',value="league"))
dropdown_league.select_by_visible_text('La Liga')

# wait for 3 seconds
import time
time.sleep(5)

# select table data for Spain and La Liga
matches= driver.find_elements(by='xpath', value='//tr')

# create empty list
date= []
home_team= []
score= []
away_team= []

for match in matches:
    date.append(match.find_element(by='xpath',value='./td[1]').text)
    home_team.append(match.find_element(by='xpath',value="./td[2]").text)
    score.append(match.find_element(by='xpath',value="./td[3]").text)
    away_team.append(match.find_element(by='xpath',value="./td[4]").text)

# store data into dataframe 
import pandas as pd
df_spain_laliga= pd.DataFrame({
    'date':date,
    'home_team':home_team,
    'score':score,
    'away_team':away_team
})

df_spain_laliga.to_csv('/home/datajap/spain laliga.csv')