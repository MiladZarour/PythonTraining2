
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
