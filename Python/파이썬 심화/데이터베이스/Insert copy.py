import sqlite3

conn = sqlite3.connect('파이썬 심화/SQL_DDL.db')

cur = conn.cursor()

SELECT_SQL = "SELECT * FROM Item"

cur.execute(SELECT_SQL)

rows = cur.fetchall()

for row in rows:
    print(row)

conn.close()