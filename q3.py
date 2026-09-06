students = {
    "Ngoni": 75,
    "Tacu": 82,
    "Shing": 68,
    "Peter": 90,
    "Mary": 78
}

for student, mark in students.items():
    print(student, mark)

highest = max(students, key=students.get)

print("Highest mark:", highest, students[highest])
