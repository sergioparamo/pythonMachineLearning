#Obtenir el nom de la persona més gran

import pandas as pd

data = pd.read_csv("data/titanic.csv")

OldestPerson = data.loc[data["Age"]==data["Age"].max()]

print(OldestPerson["Name"].values)
