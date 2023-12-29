import pandas as pd
import numpy as np
import seaborn as sns
import statsmodels
import matplotlib.pyplot as plt
import math


## Read in Data
flight = pd.read_csv("flight.csv")
print(flight.head())

plt.hist(flight['coach_price'])
plt.show()
plt.clf()

## Task 1
## Coach ticket price should be $400

## Task 2
sns.histplot(flight.coach_price[flight.hours == 8])
plt.show()
plt.clf()
## $500 ticket price is more reasonable but closer to $475 would be better

## Task 3
sns.histplot(flight.delay[flight.delay < 24])
plt.show()
plt.clf()
## 10 hour delays is most common even over 0 hour delay, there is a relatively normal distribution from 5 hours to 15 hours delay peaking at 10 hours

## Task 4
sns.histplot(flight.coach_price, color='green', bins=20)
sns.histplot(flight.firstclass_price, color='gray', bins=20)
plt.xlabel('Price')
plt.title('Coach vs First Class')
plt.legend(['Coach', 'First Class'])
plt.show()
plt.clf()
## Task 5

sns.histplot(flight.coach_price[flight.inflight_meal == 'Yes'], color='red')

sns.histplot(flight.coach_price[flight.inflight_entertainment == 'Yes'], color='green')

sns.histplot(flight.coach_price[flight.inflight_wifi == 'Yes'])

plt.legend(['Meal', 'Entertainment', 'Wifi'])
plt.show()
plt.clf()
## Task 6
sns.boxplot(flight.hours, flight.passengers)
plt.show()
plt.clf()
## Task 7
ax1 = plt.subplot(2, 1, 1)
sns.histplot(flight.coach_price[flight.weekend == 'No'], color='green')
sns.histplot(flight.firstclass_price[flight.weekend == 'No'], color='red')
ax1.set_title('Weekdays')
ax1.set_xlabel('Price')
ax1.legend(['Coach', 'First Class'])

ax2=plt.subplot(2, 1, 2)
sns.histplot(flight.coach_price[flight.weekend == 'Yes'], color='green')
sns.histplot(flight.firstclass_price[flight.weekend == 'Yes'], color='red')
ax2.set_title('Weekends')
ax2.set_xlabel('Price')
ax2.legend(['Coach', 'First Class'])

plt.show()
plt.clf()

## Weekend flights for both are more expensive usually
## Task 8
days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

for day in days:
  sns.histplot(flight.coach_price[flight.redeye == 'Yes'], color='red')
  sns.histplot(flight.coach_price[flight.redeye == 'No'], color='blue')
  plt.legend(['Redeye', 'Non-Redeye'])
  plt.title(day)
  plt.show()
  plt.clf()



