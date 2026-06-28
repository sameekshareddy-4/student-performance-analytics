CREATE DATABASE IF NOT EXISTS student_performance_db;

USE student_performance_db;

CREATE TABLE Students (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(100),
    branch VARCHAR(50),
    gender VARCHAR(10),
    age INT,
    section VARCHAR(10),
    semester INT,
    admission_year INT
);

CREATE TABLE Subjects (
    subject_id INT PRIMARY KEY,
    subject_name VARCHAR(100),
    credits INT
);

CREATE TABLE Marks (
    mark_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    subject_id INT,
    marks INT,
    FOREIGN KEY (student_id) REFERENCES Students(student_id),
    FOREIGN KEY (subject_id) REFERENCES Subjects(subject_id)
);