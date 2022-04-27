def hello_func():
    pass


def hello_func_1():
    print('Hello Function.')


def hello_func_2():
    return 'Hello Function.'


def hello_func_3(greeting):
    return '{} Function.'.format(greeting)


def hello_func_3(greeting, name='You'):
    return '{}, {}'.format(greeting, name)


def student_info(*args, **kwargs):
    print(args)
    print(kwargs)


# DRY: Don't Repeat Yourself
print(hello_func)
print(hello_func())
hello_func()
print()

print(hello_func_1)
print(hello_func_1())  # Hello Function and None !
print()
hello_func_1()  # here is prining Hello Function cause it have print('Hello Function.')
hello_func_1()
hello_func_1()
hello_func_1()
print()

print(hello_func_2)  # <function hello_func_2 at 0x000001360635B0A0>
hello_func_2()  # printing nothing
print(hello_func_2())  # printing Hello Function cause return 'Hello Function.'
print()

print(len('Test'))
print(hello_func_2().upper())
print(hello_func_2().lower())
print()

hello_func_3('Hiii')  # printing nothing cause it's not a print....
print(hello_func_3('Hiii'))  # prining Hi Function from the return....
print()

hello_func_3('KLM')  # printing nothing cause it's not a print....
print(hello_func_3('KLM'))  # prining Hi Function from the return....
print(hello_func_3('KLM', name='Corey'))
print()

student_info('Math', 'Art', name='John', age=22)
print()

courses = ['Math', 'Art']
info = {'name': 'John', 'age': 22}

# (['Math', 'Art'], {'name': 'John', 'age': 22})
# {}
student_info(courses, info)
print()

#('Math', 'Art')
#{'name': 'John', 'age': 22}
student_info(*courses, **info)
