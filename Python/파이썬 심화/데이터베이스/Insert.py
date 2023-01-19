import sqlite3

conn = sqlite3.connect('파이썬 심화/SQL_DDL.db')

cur = conn.cursor()

INSERT_SQL = "INSERT INTO item(code , name , price) VALUES (?,?,?)"

data = (
    ('A0002','에어컨 20평형 ' , 350000),
    ('A0003' , '최신형 노트북',800000),
    ('A0004', '가성비 노트북' , 650000)

)

cur.executemany(INSERT_SQL,data)

conn.commit()

conn.close()