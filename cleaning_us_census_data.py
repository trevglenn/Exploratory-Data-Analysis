import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import seaborn as sns

import glob
 
files = glob.glob("states*.csv")
 
df_list = []
for filename in files:
  data = pd.read_csv(filename)
  df_list.append(data)

us_census = pd.concat(df_list)
print(us_census.head())

print(us_census.columns)
print(us_census.dtypes)

for index in range(0,len(us_census["Income"])):
    string = str(us_census['Income'].iat[index])
    replace_dol = string.replace('$', '')
    replace_com = replace_dol.replace(',', '')
    us_census['Income'].iat[index] = replace_com
us_census.Income = pd.to_numeric(us_census.Income)

print(us_census.GenderPop.head())

us_census['GenderPop'].head()

Men = []
Women = []
for index in range(0,len(us_census["GenderPop"])):
    string = str(us_census['GenderPop'].iat[index])
    replace = string.split('_')
    Men.append(replace[0])
    Women.append(replace[1])

us_census['Men'] = Men
us_census['Women'] = Women

for index in range(0,len(us_census["Men"])):
    string = str(us_census['Men'].iat[index])
    replace = string.replace('M', '')
    us_census['Men'].iat[index] = replace
    
for index in range(0,len(us_census["Women"])):
    string = str(us_census['Women'].iat[index])
    replace = string.replace('F', '')
    us_census['Women'].iat[index] = replace
    
us_census['Men'] = pd.to_numeric(us_census['Men'])
us_census['Women'] = pd.to_numeric(us_census['Women'])


us_census.head()
plt.figure(figsize=(10,8))
plt.scatter(us_census['Women'], us_census['Income'])
plt.xlabel('Number of Women')
plt.ylabel('Income')
plt.title("Women's Income in State")

plt.show()
plt.clf()

print(us_census['Women'])

us_census['Women'] = us_census['Women'].fillna(us_census['TotalPop'] - us_census['Men'])
print(us_census['Women'])

us_census.duplicated(subset = us_census.columns[1:])
census = us_census.drop_duplicates(subset = us_census.columns[1:])
census

plt.figure(figsize=(10,8))
plt.scatter(us_census['Women'], us_census['Income'])
plt.xlabel('Number of Women')
plt.ylabel('Income')
plt.title("Women's Income in State")

plt.show()
plt.clf()

print(census.columns)
for race in ['Hispanic', 'White', 'Black', 'Native', 'Asian', 'Pacific']:
    for index in range(0,len(us_census)):    
        string = str(us_census[race].iat[index])
        replace = string.replace('%', '')
        if (replace == "nan"):
            replace = ""
        us_census[race].iat[index] = replace
    us_census[race] = pd.to_numeric(us_census[race])
    
us_census['Pacific'] = us_census['Pacific'].fillna(100 - us_census['Hispanic'] - us_census['White'] - us_census['Black'] - us_census['Native'] - us_census['Asian'])

census = us_census.drop_duplicates(subset = us_census.columns[1:])
census

for race in ['Hispanic', 'White', 'Black', 'Native', 'Asian', 'Pacific']:
    plt.hist(census[race])
    plt.title("Histogram of the Percentage of {} People per State".format(race))
    plt.xlabel("Percentage")
    plt.ylabel("Frequency")
    plt.show()
    plt.clf()