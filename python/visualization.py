import pandas as pd
import matplotlib.pyplot as plt

# Load merged dataset
df = pd.read_csv("data/final_dataset.csv")

print(df.head())
print(df.columns)

# Average marks by branch
branch_avg = df.groupby("branch")["marks"].mean()

plt.figure(figsize=(8,5))

plt.bar(
    branch_avg.index,
    branch_avg.values
)

plt.title("Average Marks by Branch")
plt.xlabel("Branch")
plt.ylabel("Average Marks")

plt.savefig("docs/branch_average.png")

plt.show()

subject_avg = df.groupby("subject_name")["marks"].mean()

plt.figure(figsize=(10,5))

plt.bar(
    subject_avg.index,
    subject_avg.values
)

plt.title("Average Marks by Subject")
plt.xlabel("Subject")
plt.ylabel("Average Marks")

plt.xticks(rotation=30)

plt.savefig("docs/subject_average.png")

plt.show()

plt.figure(figsize=(8,5))

plt.hist(
    df["marks"],
    bins=10
)

plt.title("Distribution of Marks")
plt.xlabel("Marks")
plt.ylabel("Number of Students")

plt.savefig("docs/marks_distribution.png")

plt.show()

gender = df["gender"].value_counts()

plt.figure(figsize=(6,6))

plt.pie(
    gender.values,
    labels=gender.index,
    autopct="%1.1f%%"
)

plt.title("Gender Distribution")

plt.savefig("docs/gender_distribution.png")

plt.show()

top = df.sort_values(
    "marks",
    ascending=False
).head(10)

plt.figure(figsize=(10,5))

plt.bar(
    top["student_name"],
    top["marks"]
)

plt.xticks(rotation=40)

plt.title("Top 10 Students")

plt.savefig("docs/top_students.png")

plt.show()
