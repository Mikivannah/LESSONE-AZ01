import pandas as pd
df = pd.read_csv('World-happiness-report-2024.csv')

print("вывелось 5 первых строк")
print(df.head()) # вывелось 5 первых строк

print("вывелось 5 последних строк")
print(df.tail()) # вывелось 5 последних строк

print("вывелось информацию о датафрейме")
print(df.info())

print("вывелось статистик информацию о датафрейме")
print(df.describe())


