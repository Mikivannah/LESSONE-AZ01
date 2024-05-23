
import pandas as pd
df = pd.read_csv('hh.csv')


# добавляем новый столбец
df['tEST'] = [new for new in range(29)]
print(df)
print("___________________________")
# удаляем столбец (или строку)
df.drop('tEST', axis=1, inplace=True) # обрати внимание на параметр axis=1 - удаляем столбец
print(df)


# удаляем строку
df.drop([28], axis=0, inplace=True) # обрати внимание на параметр axis=0 - удаляем строку в столбе целиком по индексу 28
print(df)