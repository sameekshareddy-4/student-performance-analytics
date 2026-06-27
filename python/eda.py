import pandas as pd

df = pd.read_csv("data/final_dataset.csv")

print(df.head())

branch_avg = df.groupby("branch")["marks"].mean()

print(branch_avg)

subject_avg = df.groupby("subject_name")["marks"].mean()

print(subject_avg)

top_students = df.sort_values(
    "marks",
    ascending=False
)

print(top_students.head(10))

lowest = df.sort_values(
    "marks"
)

print(lowest.head(10))

print(df[df["marks"]>=90])

print(df[df["marks"]<40])

passed = df[df["marks"]>=40]

pass_percentage = (len(passed)/len(df))*100

print(pass_percentage)

distinction = df[df["marks"]>=75]

percentage = (len(distinction)/len(df))*100

print(percentage)

print(
df.groupby(
["branch","subject_name"]
)["marks"].mean()
)

best = df.loc[df["marks"].idxmax()]

print(best)

cse = df[df["branch"]=="CSE"]

print(
cse.groupby("subject_name")["marks"].mean()
)

print(
df.groupby("branch")["student_name"].count()
)

