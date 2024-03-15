# Get the 250 movies details from imdb website

from selenium import webdriver
from selenium.webdriver.common.by import By

driver= webdriver.Firefox()
url="https://www.imdb.com/chart/top/"
driver.get(url)

movies= driver.find_elements(By.XPATH,'//div[@class="sc-b0691f29-0 jbYPfh cli-children"]')

title= []
release_year=[]
duration= []
movie_type= []
ratings= []
number_of_ratings= []
for movie in movies:
    title.append(movie.text.split('\n')[0])
    release_year.append(movie.text.split('\n')[1])
    duration.append(movie.text.split('\n')[2])
    movie_type.append(movie.text.split('\n')[3])
    ratings.append(movie.text.split('\n')[4])
    number_of_ratings.append(movie.text.split('\n')[5])
            
# save this data into dataframe
import pandas as pd

df= pd.DataFrame({
    'title':title,
    'release_year':release_year,
    'duration':duration,
    'movie_type':movie_type,
    'ratings':ratings,
    'number_of_ratings':number_of_ratings
})

# export dataframe to csv file
df.to_csv('top 250 movies.csv',index=False)

driver.close()