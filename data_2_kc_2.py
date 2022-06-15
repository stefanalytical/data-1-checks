import pandas as pd
import requests
import json

r = requests.get('https://www.balldontlie.io/api/v1/players')
x = r.json()
df = pd.json_normalize(x, 'data')
print(df)

print(df.columns)

df.drop(['id', 'height_inches', 'height_feet', 'team.id', 'weight_pounds'], axis = 1, inplace=True)
print(df)

fixed_columns = {
    'team.abbreviation':'team_abbreviation',
    'team.city':'city',
    'team.conference':'conference',
    'team.division':'division',
    'team.full_name':'team_full_name',
    'team.name':'team_name',
    
}

df.rename(columns=fixed_columns,inplace=True)
print(df.columns)

