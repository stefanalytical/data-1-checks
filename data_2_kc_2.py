import pandas as pd
import requests
import json

r = requests.get('https://www.balldontlie.io/api/v1/players')
x = r.json()
df = pd.json_normalize(x, 'data')
print(df)

# See all 14 columns and determine which can be dropped.
print(df.columns)

# Drop columns that are not needed.
df.drop(['id', 'height_inches', 'height_feet', 'team.id', 'team.city', 'team.name'], axis = 1, inplace = True)

# Rename and change column names to snake case.
fixed_columns = {
    'team.abbreviation':'team_abbreviation',
    'team.conference':'conference',
    'team.division':'division',
    'team.full_name':'team_full_name',

}

df.rename(columns = fixed_columns, inplace = True)
print(df)

# Count and display the number of cells thate are NaN.
nan = df.isnull().sum().sum()
print('Number of NaNs: ' + str(nan))

# Replace all NaN values with 0.
df['weight_pounds'] = df['weight_pounds'].fillna(0)
print(df)

# Count and display the number of cells thate are NaN again. Displays zero.
nan = df.isnull().sum().sum()
print('Number of NaNs: ' + str(nan))
