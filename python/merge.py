import os

print(os.getcwd())
import pandas as pd
import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sam4",
    database="student_performance_db"
)

students = pd.read_sql("SELECT * FROM Students", connection)
subjects = pd.read_sql("SELECT * FROM Subjects", connection)
marks = pd.read_sql("SELECT * FROM Marks", connection)

connection.close()

student_marks = pd.merge(
    students,
    marks,
    on="student_id"
)

print(student_marks.head())

final_df = pd.merge(
    student_marks,
    subjects,
    on="subject_id"
)

print(final_df.head())

result = final_df[[
    "student_name",
    "branch",
    "subject_name",
    "marks"
]]

print(result.head(10))

print(result.groupby("branch")["marks"].mean())
print(result.groupby("subject_name")["marks"].mean())
top_students = result.sort_values(
    "marks",
    ascending=False
)

print(top_students.head(10))
result.to_csv(
    r"C:\Users\samee\OneDrive\Desktop\Internships\student-performance-analytics\data\final_dataset.csv",
    index=False
)

print("Dataset Saved Successfully!")