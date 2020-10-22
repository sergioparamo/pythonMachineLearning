#Obtenir el Nom, Sexe i Edat de les persones amb menys de 30 anys.

import pandas as pd

data = pd.read_csv("data/titanic.csv")

array = ["Name","Sex","Age"]

var = data.loc[data["Age"] < 30, array]

print(var)
