from collections import namedtuple
total_students=int(input())
attributes=input().split()
Student=namedtuple('Student',attributes)
total_marks=0
for _ in range(total_students):
    student_data = input().split()
    student = Student(*student_data)
    total_marks += int(student.MARKS)

average_marks = total_marks / total_students
print('{:.2f}'.format(average_marks))