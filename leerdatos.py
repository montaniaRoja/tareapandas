import pandas as pd

df = pd.read_csv('data.csv')

print(df)

filtered_df = df[df['Duration'] > 60]

# Mostrar el DataFrame filtrado
print(filtered_df)

filtered_df.to_csv('filtered_data.csv', index=False)

# Contar el número de filas donde la columna 'Duration' es mayor que 60
num_rows = (df['Duration'] > 60).sum()

print(f"El número de filas donde la duración es mayor que 60 es: {num_rows}")

#imprimir la informacion de la tabla

print(df.info())