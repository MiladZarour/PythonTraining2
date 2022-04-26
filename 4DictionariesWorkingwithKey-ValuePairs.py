student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
print(student)
print(student['name'])
print(student['age'])
print(student['courses'])
# print(student['phone']) KeyError: 'phone'
print(student.get('name'))
print(student.get('phone'))
print(student.get('phone', 'Hej! its Not Found'))
