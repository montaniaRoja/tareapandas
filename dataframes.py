import pandas as pd

data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}

df = pd.DataFrame(data)

print(df)

print("Localizar e imprimir la columna 1")

print(df.loc[1])

#tambien podemos etiquetar los index

df = pd.DataFrame(data, index=["day1", "day2", "day3"])

print(df)

print(df.info())
