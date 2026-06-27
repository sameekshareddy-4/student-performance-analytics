print("Student Performance Analytics System")
import mysql.connector
import pandas as pd

# Connect to MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sam4",
    database="student_performance_db"
)

# SQL Query
query = "SELECT * FROM Students"

# Read SQL into DataFrame
df = pd.read_sql(query, connection)

# Display Data
# print(df)
print(df.head())

connection.close()