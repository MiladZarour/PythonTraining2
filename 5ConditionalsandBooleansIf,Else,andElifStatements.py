# Comparisons:
# Equal:            3 == 2
# Not Equal:        3 != 2
# Greater Than:     3 > 2
# Less Than:        3 < 2
# Greater or Equal  3 >= 2
# Less or Equal:    3 <= 2

from operator import truediv


language_1 = 'Python'
language_2 = 'Java'
language_3 = 'JavaScript'

# if language == 'Pytho': this will run the else statment
if language_1 == 'Python':
    print('Language is python')
elif language_1 == 'Java':
    print('Language is Java')
else:
    print('No Match')

if language_2 == 'Python':
    print('Language is python')
elif language_2 == 'Java':
    print('Language is Java')
else:
    print('No Match')


if language_3 == 'Python':
    print('Language is python')
elif language_3 == 'Java':
    print('Language is Java')
elif language_3 == 'JavaScript':
    print('Language is JavaScript')
else:
    print('No Match')
print()

# and
# or
# not

user = 'Admin'
logged_in = True

if user == 'Admin' and logged_in:
    print('Admin Page')
else:
    print('Bad Creds')

logged_in = False
if user == 'Admin' or logged_in:
    print('Admin Page')
else:
    print('Bad Creds')

if not logged_in:
    print('Please Log In')
else:
    print('Welcome')

logged_in = True
if not logged_in:
    print('Please Log In')
else:
    print('Welcome')
print()

a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)
print(id(a))
print(id(b))
print(a is b)  # these are two different objects in memory
print()

c = [1, 2, 3]
d = c
print(c == d)
print(id(c))
print(id(d))
print(c is d)  # these are the same objects in memory print(id(a) == id(b))
print(id(a) == id(b))
print()

# ******False Values:******
# 1-- False
# 2-- None
# 3-- Zero of any numeric type
# 4-- Any empty sequence. For example, '', (), [].
# 5-- Any empty mapping. For example, {}

condition = False
if condition:
    print('Evaluated to True')
else:
    print('Evaluared to False')

condition = None
if condition:
    print('Evaluated to True')
else:
    print('Evaluared to False')

condition = 0
if condition:
    print('Evaluated to True')
else:
    print('Evaluared to False')

condition = 10
if condition:
    print('Evaluated to True')
else:
    print('Evaluared to False')

condition = []
if condition:
    print('Evaluated to True')
else:
    print('Evaluared to False')

condition = ()
if condition:
    print('Evaluated to True')
else:
    print('Evaluared to False')

condition = ''
if condition:
    print('Evaluated to True')
else:
    print('Evaluared to False')

condition = {}
if condition:
    print('Evaluated to True')
else:
    print('Evaluared to False')
