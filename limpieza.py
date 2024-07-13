import pandas as pd
import numpy as np

# Leer el archivo CSV en un DataFrame
df = pd.read_csv('data.csv')

# 1. Crear un DataFrame sin nulos
df_no_nulls = df.dropna()

# 2. Crear un DataFrame sin vacíos (celdas vacías representadas por cadenas vacías)
df_no_empties = df.replace('', np.nan).dropna()

# 3. Reemplazar los valores vacíos con el promedio de la columna correspondiente
df_fill_empties_with_mean = df.replace('', np.nan)
for column in df_fill_empties_with_mean.columns:
    if df_fill_empties_with_mean[column].dtype in [np.float64, np.int64]:
        mean_value = df_fill_empties_with_mean[column].mean()
        df_fill_empties_with_mean[column] = df_fill_empties_with_mean[column].fillna(mean_value)

# Guardar los DataFrames en nuevos archivos CSV
df_no_nulls.to_csv('data_no_nulls.csv', index=False)
df_no_empties.to_csv('data_no_empties.csv', index=False)
df_fill_empties_with_mean.to_csv('data_filled_with_mean.csv', index=False)

df = pd.read_csv('data.csv')
print(df.info())

df_mean = pd.read_csv('data_filled_with_mean.csv')
print(df_mean.info())

df_empties = pd.read_csv('data_no_empties.csv')
print(df_empties.info())

df_null = pd.read_csv('data_no_nulls.csv')
print(df_null.info())



