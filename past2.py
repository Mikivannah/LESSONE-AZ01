import pandas as pd
df = pd.read_csv('World-happiness-report-2024.csv')


# выведим содержимое одного выбранного столбца
print(df['Country name'].head(5)) # вывело 5 превых строк
print(df['Country name']) # вывело 5 превых и 5 последних строк

# выведим значение конкретных столбцов ( 5 первых ...)
print(df[['Country name', 'Regional indicator']])

# выведим значение конкретной строке индекса 56
print(df.loc[56])

print("___________________________________________")
# выведим значение конкретной строке индекса 56 конкретного столбца
print(df.loc[56, 'Healthy life expectancy'])

