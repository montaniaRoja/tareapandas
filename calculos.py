import pandas as pd

# Leer el archivo CSV en un DataFrame
df = pd.read_csv('data.csv')

# Calcular el promedio, el mínimo y el máximo de la columna 'Calories'
average_calories = df['Calories'].mean()
min_calories = df['Calories'].min()
max_calories = df['Calories'].max()

print(f"Promedio de calorías: {average_calories}")
print(f"Calorías mínimas: {min_calories}")
print(f"Calorías máximas: {max_calories}")
