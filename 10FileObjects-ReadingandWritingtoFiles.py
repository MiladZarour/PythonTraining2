# File Objects

# f = open('test.txt', 'w') writing to a file
# f = open('test.txt', 'a') appending to a file
# f = open('test.txt', 'r+') read and write to a file

# reading the content of the file and store it in the variable f
# f = open('10test.txt', 'r')

# print('name of the file : ' + f.name)
# print('mode of the file : ' + f.mode)

# f.close()


# with open('10test.txt', 'r') as f:
# f_contents = f.read()
# f_contents = f.readlines()
# f_contents = f.readline()
# print(f_contents)

# f_contents = f.readline()
# print(f_contents)

# f_contents = f.readline()
# print(f_contents, end='')  # that end='' it will delete the extra new line

# f_contents = f.readline()
# print(f_contents, end='')  # that end='' it will delete the extra new line

# print(f.closed)
# print(f.read()) ValueError: I/O operation on closed file.
# print(f.name)
# print(f.mode)
# print(f_contents) this variable still accessable !

# with open('10test.txt', 'r') as f:

#     for line in f:
#         print(line, end='')

with open('10test.txt', 'r') as f:

    f_contents = f.read()
    print(f_contents, end='')


print()
with open('10test.txt', 'r') as f2:

    f_contents2 = f2.read(100)
    print(f_contents2, end='')

print()
with open('10test.txt', 'r') as f3:

    size_to_read = 10
    f_contents3 = f3.read(size_to_read)

    while len(f_contents3) > 0:
        print(f_contents3, end='**')
        f_contents3 = f3.read(size_to_read)

print()
print('------f_contents4 and f4------')
with open('10test.txt', 'r') as f4:

    size_to_read = 10
    f_contents4 = f4.read(size_to_read)
    print(f_contents4, end='')
    # while len(f_contents4) > 0:
    #     print(f_contents4, end='**')
    #     f_contents4 = f4.read(size_to_read)

    print(f4.tell())

print()
print('------f_contents5 and f5------')
with open('10test.txt', 'r') as f5:

    size_to_read = 10
    f_contents5 = f5.read(size_to_read)
    print(f_contents5, end='')

    f_contents5 = f5.read(size_to_read)
    print(f_contents5, end='')

    # while len(f_contents5) > 0:
    #     print(f_contents5, end='**')
    #     f_contents5 = f5.read(size_to_read)

    print(f5.tell())

print()
print('------f_contents6 and f6------')
with open('10test.txt', 'r') as f6:

    size_to_read = 10
    f_contents6 = f6.read(size_to_read)
    print(f_contents6, end='')

    f6.seek(0)

    f_contents6 = f6.read(size_to_read)
    print(f_contents6, end='')
