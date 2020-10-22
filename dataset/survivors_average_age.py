# Show the average age of the survivors
import math
import pandas as pd

data = pd.read_csv("data/titanic.csv")

data_filtered = data[data["Survived"] == 1]
avg_age = math.floor(data_filtered["Age"].mean())

print("Average age of the survivors: " + str(avg_age))

print("These are all the survivors that had the same age of the average")

array = ["Name", "Sex", "Age"]

passengersWithSameAge = data.loc[data["Age"] == avg_age, array]

print(passengersWithSameAge)





data_filtered2 = data[data["Survived"] == 0]
avg_age2 = math.floor(data_filtered2["Age"].mean())

print("Average age of the deads: " + str(avg_age2))

print("These are all the deads that had the same age of the average ")

passengersWithSameAge = data.loc[data["Age"] == avg_age2, array]

print(passengersWithSameAge)

