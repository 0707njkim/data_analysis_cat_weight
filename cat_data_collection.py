import pandas as pd
import sqlite3

df = pd.read_csv (r'C:\Users\nicol\Desktop\Projects\Data_Analysis_Cat_Weight\cats.csv')

conn = sqlite3.connect('content.sqlite')
cur = conn.cursor()
cur.execute('''DROP TABLE IF EXISTS Weights''')
cur.execute('''CREATE TABLE IF NOT EXISTS Weights
    (id INTEGER PRIMARY KEY, sex TEXT, body_weight INTEGER)''')


sum = 0
count = df.shape[0]
print("Count is:", count)
for index, line in df.iterrows():
    print(index)
    sex = line[1]
    body_weight = line[2]
    print("Sex:",sex)
    print("Body Weight:", body_weight)
    cur.execute('''INSERT INTO Weights (sex, body_weight) VALUES (?, ?)''', (sex, body_weight))

conn.commit()
cur.close()
