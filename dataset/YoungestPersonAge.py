#Obtenir l'edat de la persona més jove

import pandas as pd

data = pd.read_csv("data/titanic.csv")

column = data["Age"]
YoungestPerson = column.min()

print(YoungestPerson)


