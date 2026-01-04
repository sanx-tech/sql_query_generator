
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    database="company_db"
)

cursor = conn.cursor()
cursor.execute("SELECT * FROM employees")

for row in cursor.fetchall():
    print(row)

conn.close() 