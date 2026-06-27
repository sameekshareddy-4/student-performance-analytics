import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sam4",
    database="student_performance_db"
)

print("Connected Successfully!")