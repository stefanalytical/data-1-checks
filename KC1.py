import requests
import pandas as pd
import json

# Get data from web API and normalize into Pandas Dataframe
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
print('Below is a queried subset showing only Grizzlies:')
print(query)