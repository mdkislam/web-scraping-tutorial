from selenium import webdriver
from selenium.webdriver.common.by import By
import numpy as np
import pandas as pd
import time

driver= webdriver.Firefox()
url= "https://www.audible.in/adblbestsellers"
driver.get(url=url)

page_elements= driver.find_element(By.XPATH,'//ul[contains(@class,"pagingElements")]')
pages= page_elements.find_elements(By.TAG_NAME,'li')
next_page= driver.find_element(By.XPATH,'//span[contains(@class,"nextButton")]')
last_page= int(pages[-2].text)

current_page= 1

title= []
writter= []
narrator= []
length= []
release_date= []
language= []
stars= []
num_rating= []
price= []

while current_page <= last_page:
    time.sleep(3)
    products= driver.find_elements(By.XPATH,'//div[@class="adbl-impression-container "]//span//ul//li[contains(@class,"productListItem")]')

    for product in products:
        title.append(product.text.splitlines()[1].split('. ')[1])
        writter_line=[line for line in product.text.splitlines() if line.startswith('Written by:')][0]
        writter.append(writter_line.split(': ')[1])
        narrator_line=[line for line in product.text.splitlines() if line.startswith('Narrated by:')][0]
        narrator.append(narrator_line.split(': ')[1])
        length_line= [line for line in product.text.splitlines() if line.startswith('Length:')][0]
        length.append(length_line.split(': ')[1])
        release_date_line= [line for line in product.text.splitlines() if line.startswith('Release Date')][0]
        release_date.append(release_date_line.split(': ')[-1])
        language_line=[line for line in product.text.splitlines() if line.startswith('Language:')][0]
        language.append(language_line.split(': ')[-1])
        stars_line= next((line for line in product.text.splitlines() if line.endswith('stars')),None)
        if stars_line:
            stars.append(stars_line.split(' ')[0])
        else:
            stars.append(np.nan)
        rating_line= next((line for line in product.text.splitlines() if line.endswith('ratings')),None)
        if rating_line:
            num_rating.append(rating_line.split(' ')[0])
        else:
            num_rating.append(np.nan)
        price_line= [line for line in product.text.splitlines() if line.startswith('Regular price:')][0]
        price.append(price_line.split(': ')[-1])

    current_page += 1
    try:
        next_page= driver.find_element(By.XPATH,'//span[contains(@class,"nextButton")]')
        next_page.click()
    except:
        pass
driver.close()


df= pd.DataFrame({
    'book title': title,
    'writter': writter,
    'narrator':narrator,
    'audio_length': length,
    'release_date': release_date,
    'book language': language,
    'review stars': stars,
    'num of ratings': num_rating,
    'price':price
})

df.to_csv('best selling books.csv')
