import pandas as pd
from selenium import webdriver

driver= webdriver.Chrome()
url= "https://www.adamchoi.co.uk/overs/detailed"
driver.get(url)
all_matches_button= driver.find_element('xpath',"//label[@analytics-event='All matches']")
all_matches_button.click()

matches= driver.find_elements(by='xpath',value='//tbody/tr')
date= []
home_team= []
score= []
away_team= []

for match in matches:
    date.append(match.find_element(by='xpath',value="./td[1]").text)
    home_team.append(match.find_element(by='xpath',value="./td[2]").text)
    score.append(match.find_element(by='xpath',value="./td[3]").text)
    away_team.append(match.find_element(by='xpath',value="./td[4]").text)


# store data into dataframe 
import pandas as pd
football_df= pd.DataFrame({
    'date':date,
    'home_team':home_team,
    'score':score,
    'away_team':away_team
})

# export dataframe into csv file
football_df.to_csv('football_data.csv',index=False)