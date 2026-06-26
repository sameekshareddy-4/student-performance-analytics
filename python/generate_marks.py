import csv
import random
students = list(range(1001, 1051))
subjects = [
    "SUB101",
    "SUB102",
    "SUB103",
    "SUB104",
    "SUB105"
]
with open("../data/marks.csv","w",newline="") as file:
    writer = csv.writer(file)
    writer.writerow([
    "student_id",
    "subject_id",
    "marks"
])
    for student in students:
        for subject in subjects:
            marks = random.randint(35,98)
            writer.writerow([
    student,
    subject,
    marks
])
            