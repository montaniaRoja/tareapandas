import pandas as pd

a = [1, 7, 2]

myvar = pd.Series(a)

print(myvar)

#los valores son etiquetados con su numero de indice

print(myvar[0])

#con el arguemento index, se pueden crear etiquetas personalizadas

myvar = pd.Series(a, index=["indice 0", "indice 1", "indice 2"])

print(myvar)

print(myvar["indice 0"])
