import pandas as pd
import numpy as np

diabetes = pd.read_csv('diabetes.csv')

print(diabetes.head())
print(diabetes.dtypes)
print(len(diabetes.columns))
## 9
print(len(diabetes))
## 768

print(diabetes.isnull().sum())
print(diabetes.describe())

diabetes[['Glucose','BloodPressure','SkinThickness','Insulin','BMI']] = diabetes[['Glucose','BloodPressure','SkinThickness','Insulin','BMI']].replace(0,np.NaN)
print(diabetes.isnull().sum())
print(diabetes[diabetes.isnull().any(axis=1)])
print(diabetes.dtypes)
print(diabetes.Outcome.unique())