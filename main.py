import pandas as pd

# пример  структуры Series
data = [1,2,3,4,5]
series = pd.Series(data)
print(series)

# пример структуры DataFrame
data = {
    'Name' : ['Tom', 'Jack', 'Steve', 'Ricky'],
    'Age' : [28,34,29,42],
    'Citi' : ['London', 'Manchester', 'Liverpool', 'Bristol']
}
df = pd.DataFrame(data)
print(df)

