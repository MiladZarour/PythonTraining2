
from hashlib import new


courses = ['History', 'Math', 'Physics', 'CompSci']  # List

print(courses)
print(len(courses))
print(courses[0])
print(courses[1])
print(courses[2])
print()
print(courses[-1])
print(courses[3])
# the first index is inclusive , but then the third index is not including it
print(courses[0:2])
print(courses[2:])  # from the third index until the end (SLICING)

courses.append('Art')
print(courses)
courses.insert(0, 'Art')
print(courses)
courses_2 = ['Bole', 'Manufacture']
courses.insert(0, courses_2)
print(courses)
print()
print(courses[0])
courses_3 = ['Nadol', 'Lamo']
courses.extend(courses_3)
print(courses)
courses.remove('Nadol')
print(courses)
popped = courses.pop()
print(popped)
print(courses)

print()
print(courses)
courses.reverse()
print(courses)
courses = ['History', 'Math', 'Physics', 'CompSci']  # List
print(courses)
courses.sort()  # Sorting Alphabatical
print(courses)
print()

num = [1, 5, 2, 4, 3]
print(num)
num.sort()
print(num)
num.sort(reverse=True)
print(num)
courses = ['History', 'Math', 'Physics', 'CompSci']  # List
print(courses)
sorted(courses)
# didn't printed when it sorted , cause it's need a variable to store the sorted list
print(courses)
sorted_courses = sorted(courses)
print(sorted_courses)
print()
print(min(num))
print(max(num))
print(sum(num))
print()
print(courses.index('CompSci'))
# print(courses.index('Art')) ValueError: 'Art' is not in list
print('Math' in courses)
print('Art' in courses)
print('CompSci' in courses)
print()
for item in courses:
    print(item)
print()
for index, course in enumerate(courses):
    print(index, course)
print()
for index, course in enumerate(courses, start=1):
    print(index, course)
print()

course_str = ' - '.join(courses)
print(course_str)
new_list = course_str.split(' - ')
print(new_list)

print()
list_1 = ['History', 'Math', 'Physics', 'CompSci']
list_2 = list_1

print(list_1)
print(list_2)

list_1[0] = 'Art'
print(list_1)
print(list_2)

# Immutable
tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
tuple_2 = tuple_1
print(tuple_1)
print(tuple_2)

# tuple_1[0] = 'Art' TypeError: 'tuple' object does not support item assignment
# print(tuple_1)
# print(tuple_2)
print()

# Sets
cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
print(cs_courses)  # the order will change when i compile each time
cs_courses_1 = {'History', 'Math', 'Physics', 'CompSci', 'Math'}
# the order will change when i compile each time, and now without the second Math
print(cs_courses_1)
print('Math' in cs_courses_1)
cs_courses_2 = {'History', 'Math', 'Physics', 'Art'}
print(cs_courses_1.intersection(cs_courses_2))
print(cs_courses_1.difference(cs_courses_2))
