import pandas as pd

# load the datasets
PATH = 'E:/projects/active/olympics-economics/data/'
medals_total = pd.read_csv(PATH + 'kaggle-olympics2024.csv')
gdp = pd.read_csv(PATH + 'world_bank-gdp_per_capita-2023.csv')


# Merge data based on country_code
df = pd.merge(medals_total, gdp, on='country_code', how='left')

# check if data available
def null_gdp(year):
    col = 'gdp' + str(year)
    countries = df.country[df[col].isnull()].values
    return countries

year = int(input("Enter a year from 2020 to 2023: \n")) 

if year:
    print(
        "checking...\nThere is no GDP data for:\n", 
        null_gdp(year)
        )
else:
    print("No year provided!")