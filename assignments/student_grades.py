# Assignment 1 - Student Grades System

name = input("Enter student name: ")
score = int(input("Enter student score: "))

if score >= 70:
    grade = "A"
elif score >= 60:
    grade = "B"
elif score >= 50:
    grade = "C"
elif score >= 45:
    grade = "D"
elif score >= 40:
    grade = "E"
else:
    grade = "F"

print("Student:", name)
print("Score:", score)
print("Grade:", grade)