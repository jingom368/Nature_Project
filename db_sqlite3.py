import sqlite3
import pandas as pd
import openpyxl

conn = sqlite3.connect("db.sqlite3")

cur = conn.cursor()
cur.execute('SELECT * FROM mainpage_apply')
rows = cur.fetchall()

cur2 = conn.cursor()
cur2.execute('SELECT * FROM mainpage_contact')
rows2 = cur2.fetchall()

cols = [column[0] for column in cur.description]
cols2 = [column[0] for column in cur2.description]

for row in rows:
    df = pd.DataFrame.from_records(data=rows, columns=cols)

for row in rows2:
    df_2 = pd.DataFrame.from_records(data=rows2, columns=cols2)

df.to_excel('oumtt_apply.xlsx')
df_2.to_excel('oumtt_contact.xlsx')