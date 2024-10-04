import pandas as pd

# load the datasets
PATH = 'E:/projects/active/olympics-economics/data/'
medals_total = pd.read_csv(PATH + 'kaggle-olympics2024.csv')
country_code = pd.read_csv(PATH + 'iban-country_codes.csv')
gdp = pd.read_csv(PATH + 'world_bank-gdp_per_capita-2023.csv')


# Merge based on country_code
df = pd.merge(medals_total, gdp, on='country_code', how='left')

# check
countries = df.country_code[df['gdp2020'].isnull()]
print(countries)