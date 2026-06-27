import pandas as pd

df = pd.read_csv("data/final_dataset.csv")

print("="*50)
print("Student Performance Analysis")
print("="*50)

print("\nDataset Shape")
print(df.shape)

print("\nColumns")
print(df.columns)

print("\nData Types")
print(df.dtypes)

print("\nMissing Values")
print(df.isnull().sum())

print("\nStatistical Summary")
print(df.describe())

print("\nHighest Marks")
print(df["marks"].max())

print("\nLowest Marks")
print(df["marks"].min())

print("\nAverage Marks")
print(df["marks"].mean())

print("\nTop 10 Students")
print(
    df.groupby("student_name")["marks"]
      .mean()
      .sort_values(ascending=False)
      .head(10)
)

print("\nAverage Marks by Branch")
print(
    df.groupby("branch")["marks"].mean()
)

print("\nAverage Marks by Subject")
print(
    df.groupby("subject_name")["marks"].mean()
)