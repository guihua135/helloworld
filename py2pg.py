import psycopg2

conn = psycopg2.connect(database="db1", user="postgres", password="123", host="127.0.0.1", port="5432")

print("connect to database successfully")
cur = conn.cursor()

"""
cur.execute('''CREATE TABLE COMPANY
       (ID INT PRIMARY KEY     NOT NULL,
       NAME           TEXT    NOT NULL,
       AGE            INT     NOT NULL,
       ADDRESS        CHAR(50),
       SALARY         REAL);''')
print("Table created successfully")

cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (1, 'Paul', 32, 'California', 20000.00 )");
cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (2, 'Allen', 25, 'Texas', 15000.00 )");
cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )");
cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )");
print("insert data successfully")

"""

cur.execute("select id, name, age, address, salary from company FOR UPDATE")
rows = cur.fetchall()
for row in rows:
    if str(row[1]) == 'Allen':
        cur.execute("update company set salary = 20000 where name = 'Allen'")
    print(str(row[0])+";"+row[1]+";"+str(row[2])+";"+row[3]+";"+str(row[4]))

#测试一下提交
#conn.commit()
conn.close()
