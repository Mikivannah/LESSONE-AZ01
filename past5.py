import  pandas as pd

data = {
    'Name' : ['Tom', 'Jack', 'Steve', 'Ricky'],
    'Age' : [28,34,29,42],
    'Citi' : ['London', 'Manchester', 'Liverpool', 'Bristol']
}

df = pd.DataFrame(data)

# сохранение изменений в файл
df.to_csv('OUTPUT.csv', index=False)
