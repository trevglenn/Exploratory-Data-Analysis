import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Import data
students = pd.read_csv('students.csv')

# Print first few rows of data
print(students.head())
# Print summary statistics for all columns
print(students.describe(include = 'all'))
# Calculate mean
math_mean = students.math_grade.mean()
print(math_mean)
# Calculate median
math_med = students.math_grade.median()
print(math_med)
# Calculate mode
math_mode = students.math_grade.mode()
print(math_mode)
# Calculate range
math_range = students.math_grade.max() - students.math_grade.min()
print(math_range)
# Calculate standard deviation
math_std = students.math_grade.std()
print(math_std)
# Calculate MAD
math_mad = students.math_grade.mad()
print(math_mad)
# Create a histogram of math grades
sns.histplot(x = 'math_grade', data = students)

plt.show()
plt.clf()

# Create a box plot of math grades
sns.boxplot(x = 'math_grade', data = students)

plt.show()
plt.clf()

# Calculate number of students with mothers in each job category
print(students.Mjob.value_counts())
#most is other with 141. second is services with 103
# Calculate proportion of students with mothers in each job category
print(students.Mjob.value_counts(normalize=True))
##8.61% in health
# Create bar chart of Mjob
sns.countplot(x = 'Mjob', data = students)

plt.show()
plt.clf()

# Create pie chart of Mjob
students.Mjob.value_counts().plot.pie()

plt.show()