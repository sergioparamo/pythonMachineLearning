#Obtenir el Nom, Sexe i Edat dels 5 primers passatgers

import pandas as pd

data = pd.read_csv("data/titanic.csv")

var = data.iloc[0:5, 3:6]


print(var)

