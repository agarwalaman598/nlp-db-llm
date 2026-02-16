CREATE DATABASE college;
USE college;

CREATE TABLE students(
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50),
    branch VARCHAR(50),
    year INT,
    cgpa FLOAT
);

INSERT INTO students(name,branch,year,cgpa) VALUES
('Aman','CSE',2,8.2),
('Riya','IT',3,7.9),
('Karan','ECE',1,6.5),
('Neha','CSE',4,9.1),
('Rahul','ME',2,7.1);
