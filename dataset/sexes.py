# Show the average age of the survivors
import math

import pandas as pd

data = pd.read_csv("data/titanic.csv")

data_men = data[data["Sex"] == "male"]
data_women = data[data["Sex"] == "female"]

number_men = len(data_men.axes[0])
number_women = len(data_women.axes[0])

print("Number of men: " + str(number_men))
print("Number of women: " + str(number_women))

data_men_deads = data_men[data_men["Survived"] == 0]
data_women_deads = data_women[data_women["Survived"] == 0]

number_men_deads = len(data_men_deads.axes[0])
number_women_deads = len(data_women_deads.axes[0])

print("Number of men who died: " + str(number_men_deads))
print("Number of women who died: " + str(number_women_deads))

print("Number of men who survived " + str(number_men-number_men_deads))
print("Number of women who survived " + str(number_women-number_women_deads))

print("Percentage of men who died: " + str(math.floor(((number_men_deads / number_men) * 100))) + "%")
print("Percentage of women who died: " + str(math.floor(((number_women_deads / number_women) * 100))) + "%")
