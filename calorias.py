import pandas as pd

#podemos crear una serie simple desde un diccionario.

calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories)

print(myvar)
