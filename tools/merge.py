import os
import pandas as pd

# load the datasets
os.chdir('data')
medals = pd.read_csv('kaggle-olympics2024.csv')
gdp = pd.read_csv('world_bank-gdp_per_capita-2023.csv')
population = pd.read_csv('world_bank-population-2023.csv')

df = pd.merge(pd.merge(medals, gdp, on='country_code', how='left'), population, on='country_code', how='left')

# === data pre-processing ===

df = df.drop(['rank', 'country_name', 'gdp2020', 'gdp2021', 'gdp2022'], axis=1)
df = df.rename(columns={'gdp2023': 'gdp'})

# add gdp for Qatar and Cuda 
df['gdp_year'] = int(2023)
df.at[87, 'gdp'] = 87480.41971 
df.at[87, 'gdp_year'] = int(2022)
df.at[31, 'gdp'] = 56495.85
df.at[31, 'gdp_year'] = int(2022)

# changes to apply
def billion_pop(x):
    return round((x / (10^6)), 1)

def round2(x):
    return round(x, 2)

df['population'] = df.population.apply(billion_pop)
df['gdp'] = df.gdp.apply(round2)

# switch the order of last two columns
columns = df.columns.tolist()
columns[-2], columns[-1] = columns[-1], columns[-2]
df = df.reindex(columns, axis=1)

# drop Refugee Olympic Team 
# (since we focus on countries not teams)
df = df.drop(85, axis=0)

# save the results 
os.chdir('../kaggle_ds')
df.to_csv('olympics-economics.csv', index=False)