from multiprocessing.sharedctypes import Value
from turtle import st


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
del student['age']
phone = student.pop('phone')
print(student)
print(phone)
print(len(student))  # we have two keys that's why is 2
print(student.values())
print(student.keys())
print(student.items())
print()

for key in student:
    print(key)
print()
for key, value in student.items():
    print(key, value)
