import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import codecademylib3_seaborn
import glob
files = glob.glob('states*.csv')
df_lst = []
for file in files:
  data = pd.read_csv(file)
  df_lst.append(data)

us_census = pd.concat(df_lst)


us_census['Income'] = us_census['Income'].replace('[\$,]',"", regex=True)
us_census['Income'] = pd.to_numeric(us_census['Income'])
print(us_census.head())

split_df = us_census['GenderPop'].str.split("_")
us_census['male_pop'] = pd.to_numeric(split_df.str.get(0).str[:-1])
us_census['female_pop'] = pd.to_numeric(split_df.str.get(1).str[:-1])
us_census = us_census.drop(columns = ['GenderPop'])
us_census.columns = [x.lower() for x in us_census.columns]
print(us_census.head())

plt.scatter(us_census.female_pop, us_census.income)
plt.show()



us_census['female_pop'] = us_census['female_pop'].fillna(us_census['totalpop'] - us_census["male_pop"])

print(us_census.female_pop)
print(us_census['female_pop'].isna().sum())

print(us_census.duplicated().sum())
us_census = us_census.drop_duplicates()

plt.scatter(us_census.female_pop, us_census.income)
plt.show()

races = us_census[['hispanic', 'white', 'black', 'native', 'asian', 'pacific']]

for col in races:
  races[col] = races[col].str[:-1].replace('[M,]',"", regex=True).astype(float)
  print(races.head())

print(races.isna().sum())

races['pacific'] = races['pacific'].fillna(races['pacific'].mean())

for col in races:
  plt.scatter(races[col], us_census.income)
  plt.show()

