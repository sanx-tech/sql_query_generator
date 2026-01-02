
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sandywork777",
    database="company_db"
)

cursor = conn.cursor()
cursor.execute("SELECT * FROM employees")

for row in cursor.fetchall():
    print(row)

conn.close() 