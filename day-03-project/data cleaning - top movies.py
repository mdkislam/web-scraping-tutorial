# import pandas library
import pandas as pd

# read csv file into dataframe
df= pd.read_csv('top 250 movies.csv')

# remove the anomaly from title column:
# get movies title only from '1. The Shawshank Redemption'
df.title.str.split('.').str.get(1)  # movie title dataframe

# output has extra space in the begining:- ' The Shawshank Redemption'
df.title.str.split('.').str.get(1).str.strip() 
# strip method is used for removing extra space from any string.

# update the data  into title column:
df['title']= df.title.str.split('.').str.get(1).str.strip()

# convert duration into minutes:
def convert_to_minutes(mixed_duration):
    parts=mixed_duration.split(' ')
    hours= 0
    minutes= 0

    if 'h' in parts[0]:
        hours= int(parts[0].replace('h',''))
    if 'm' in parts[-1]:
        minutes=int(parts[-1].replace('m',''))

    return hours * 60 + minutes

# apply funtion to the durtion column:
df['duration'].apply(convert_to_minutes)

df['length_in_minutes']= df['duration'].apply(convert_to_minutes)
# remove the duration column:
df.drop(columns='duration',inplace=True)
# remove extra () from number_of_ratings column:
df['number_of_ratings'] = df['number_of_ratings'].str.extract(r'\(([\d.]+[A-Za-z])\)')

# export the cleaned df to csv files:
df.to_csv('top moves cleaned.csv',index=False)