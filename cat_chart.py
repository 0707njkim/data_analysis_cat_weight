import pandas as pd
import sqlite3

conn = sqlite3.connect('content.sqlite')
cur = conn.cursor()

cur.execute('''SELECT AVG(body_weight) FROM Weights WHERE sex="F"''')
for avg in cur:
    f_avg = avg[0]
f_avg = round(f_avg, 3)

cur.execute('''SELECT AVG(body_weight) FROM Weights WHERE sex="M"''')
for avg in cur:
    m_avg = avg[0]
m_avg = round(m_avg, 3)

cur.execute('''SELECT id, sex, body_weight from Weights''')
weights = dict()
for weight_row in cur :
    weights[weight_row[0]] = (weight_row[1], weight_row[2])


fhand = open('cat_chart.js','w')
fhand.write("cat_chart = [ ['Sex', 'Body Weight in kg']")
fhand.write(",\n['Female', '"+str(f_avg)+"'"+"]")
fhand.write(",\n['Male', '"+str(m_avg)+"']")
fhand.write("\n];\n")
fhand.close()


conn.commit()
cur.close()
print("Output has been printed to cat_chart.js")
