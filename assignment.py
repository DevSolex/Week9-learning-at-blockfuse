import random

students = []
count = 0

while count < 1000:
    students_id = count + 1
    students_name = (f'student{count}')
    students_score = random.randint(0, 100)

    student = {
    'id': students_id,
    'name': students_name,
    'score': students_score
    }

    students.append(student)
    count += 1

print(students)
