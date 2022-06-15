import requests
import pandas as pd
import json

# Get data from web API and normalize into Pandas data frame
r = requests.get('https://www.balldontlie.io/api/v1/players')
x = r.json()
df = pd.json_normalize(x, 'data')
print(df)


# Two descriptive statistics
freq = df['team.conference'].value_counts().idxmax()
print('Most Common Team Conference: ' + str(freq))

teams = df['height_feet'].isna().sum()
print('Number of Players With Unreported Heights (NaN): ' + str(teams))


# Perform query to only display Grizzlies
query = df[df['team.name'] == 'Grizzlies']
print(f'Below is a queried subset showing only Grizzlies:\n{query}\n')


# Second and third columns of my data frame
dfcol = df.iloc[:,[1,2]]
print(f'Below are the 2nd and 3rd Columns:\n{dfcol}\n')


# First four rows of my data frame
dfrow = df.iloc[0:4]
print(f'Below are the first 4 rows:\n{dfrow}')