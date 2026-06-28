USE student_performance_db;

-- ==========================================================
-- STUDENT PERFORMANCE ANALYTICS SYSTEM
-- Version 1 SQL Analysis Queries
-- Author: Sameeksha Reddy
-- ==========================================================

-------------------------------------------------------------
-- 1. View All Students
-------------------------------------------------------------
SELECT * FROM Students;

-------------------------------------------------------------
-- 2. View All Subjects
-------------------------------------------------------------
SELECT * FROM Subjects;

-------------------------------------------------------------
-- 3. View All Marks
-------------------------------------------------------------
SELECT * FROM Marks;

-------------------------------------------------------------
-- 4. Total Number of Students
-------------------------------------------------------------
SELECT COUNT(*) AS Total_Students
FROM Students;

-------------------------------------------------------------
-- 5. Average Marks by Branch
-------------------------------------------------------------
SELECT
    s.branch,
    ROUND(AVG(m.marks),2) AS Average_Marks
FROM Students s
JOIN Marks m
ON s.student_id = m.student_id
GROUP BY s.branch
ORDER BY Average_Marks DESC;

-------------------------------------------------------------
-- 6. Average Marks by Subject
-------------------------------------------------------------
SELECT
    sub.subject_name,
    ROUND(AVG(m.marks),2) AS Average_Marks
FROM Subjects sub
JOIN Marks m
ON sub.subject_id = m.subject_id
GROUP BY sub.subject_name
ORDER BY Average_Marks DESC;

-------------------------------------------------------------
-- 7. Top 10 Students
-------------------------------------------------------------
SELECT
    s.student_name,
    s.branch,
    SUM(m.marks) AS Total_Marks
FROM Students s
JOIN Marks m
ON s.student_id = m.student_id
GROUP BY s.student_name, s.branch
ORDER BY Total_Marks DESC
LIMIT 10;

-------------------------------------------------------------
-- 8. Highest Marks in Each Subject
-------------------------------------------------------------
SELECT
    sub.subject_name,
    MAX(m.marks) AS Highest_Marks
FROM Subjects sub
JOIN Marks m
ON sub.subject_id = m.subject_id
GROUP BY sub.subject_name
ORDER BY Highest_Marks DESC;

-------------------------------------------------------------
-- 9. Lowest Marks in Each Subject
-------------------------------------------------------------
SELECT
    sub.subject_name,
    MIN(m.marks) AS Lowest_Marks
FROM Subjects sub
JOIN Marks m
ON sub.subject_id = m.subject_id
GROUP BY sub.subject_name
ORDER BY Lowest_Marks ASC;

-------------------------------------------------------------
-- 10. Student Count by Branch
-------------------------------------------------------------
SELECT
    branch,
    COUNT(*) AS Total_Students
FROM Students
GROUP BY branch
ORDER BY Total_Students DESC;

-------------------------------------------------------------
-- 11. Students Scoring Above 90
-------------------------------------------------------------
SELECT
    s.student_name,
    sub.subject_name,
    m.marks
FROM Students s
JOIN Marks m
ON s.student_id = m.student_id
JOIN Subjects sub
ON m.subject_id = sub.subject_id
WHERE m.marks >= 90
ORDER BY m.marks DESC;

-------------------------------------------------------------
-- 12. Students Scoring Below 40
-------------------------------------------------------------
SELECT
    s.student_name,
    sub.subject_name,
    m.marks
FROM Students s
JOIN Marks m
ON s.student_id = m.student_id
JOIN Subjects sub
ON m.subject_id = sub.subject_id
WHERE m.marks < 40
ORDER BY m.marks ASC;

-------------------------------------------------------------
-- 13. Branch Wise Highest Score
-------------------------------------------------------------
SELECT
    s.branch,
    MAX(m.marks) AS Highest_Score
FROM Students s
JOIN Marks m
ON s.student_id = m.student_id
GROUP BY s.branch
ORDER BY Highest_Score DESC;

-------------------------------------------------------------
-- 14. Branch Wise Lowest Score
-------------------------------------------------------------
SELECT
    s.branch,
    MIN(m.marks) AS Lowest_Score
FROM Students s
JOIN Marks m
ON s.student_id = m.student_id
GROUP BY s.branch
ORDER BY Lowest_Score ASC;

-------------------------------------------------------------
-- 15. Overall Dataset (Used for Python & Power BI)
-------------------------------------------------------------
SELECT
    s.student_name,
    s.branch,
    sub.subject_name,
    m.marks
FROM Students s
JOIN Marks m
ON s.student_id = m.student_id
JOIN Subjects sub
ON m.subject_id = sub.subject_id
ORDER BY s.student_name;


