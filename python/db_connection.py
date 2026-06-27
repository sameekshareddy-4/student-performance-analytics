import mysql.connector
import pandas as pd

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sam4",
    database="student_performance_db"
)

print("Connected Successfully!")

query = "SELECT * FROM Students"

df = pd.read_sql(query, connection)

print(df)

connection.close()
print(df.head())
print(df.tail())
print(df.columns)
print(df.shape)
print(df.info())
print(df.describe())