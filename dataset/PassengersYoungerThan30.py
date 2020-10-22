#Obtenir el nombre de persones amb menys de 30 anys.


import pandas as pd

data = pd.read_csv("data/titanic.csv")

#filtered_data = data[data["Age"]<30.00]
#var = filtered_data.iloc[0:1000,3:4]
#print(filtered_data.Name.to_string(index=False))

var = data.loc[data["Age"] < 30, "Name"]
print(var)




