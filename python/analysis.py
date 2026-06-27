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

#Display Data

print(df)
print(df.head())
print(df.tail())
print(df.shape)
print(df.columns)
print(df.dtypes)
print(df.info())
print(df.describe())
print(len(df))
print(df["branch"].unique())
print(df["branch"].value_counts())

print(df["student_name"])
print(df[["student_name","branch"]])
print(df[df["branch"]=="CSE"])
print(df[df["gender"]=="Female"])
print(df[df["age"]>20])

print(
df[
(df["gender"]=="Female") &
(df["branch"]=="CSE")
]
)
print(
df[
(df["gender"]=="Female") |
(df["branch"]=="AIML")
]
)

print(df.sort_values("age",ascending=False))
print(df.groupby("branch").size())
print(
df.groupby("branch")["age"].mean()
)
print(
df.groupby("branch")["age"].agg(
["mean","max","min"]
)
)

connection.close()