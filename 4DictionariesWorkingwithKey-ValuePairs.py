student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
print(student)
print(student['name'])
print(student['age'])
print(student['courses'])
# print(student['phone']) KeyError: 'phone'
print(student.get('name'))
print(student.get('phone'))
print(student.get('phone', 'Hej! its Not Found'))
print()
student['phone'] = '555-555555'
print(student.get('phone'))
student['name'] = 'Jane'
print(student)
student.update({'name': 'Milad', 'age': 30, 'phone': '0762602923'})
print(student)
