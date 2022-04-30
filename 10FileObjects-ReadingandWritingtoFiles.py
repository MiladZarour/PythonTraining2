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

import chunk


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

print()
print('------f_contents7 and f7------')
with open('10test2.txt', 'w') as f7:  # using the open with write mode , it will create the file
    # pass
    f7.write('Testttt')
    f7.write('Testttt')

print()
print('------f_contents8 and f8------')
with open('10test3.txt', 'w') as f8:
    # pass
    f8.write('Testttt')
    # it will overwrite the 10test3.txt file, and it's begin from the first letter
    f8.seek(0)
    f8.write('R')

print()
print('------rf and wf------')
with open('10test.txt', 'r') as rf:
    with open('10test_copy.txt', 'w') as wf:
        for line in rf:
            wf.write(line)

print()
print('------SO IMPORTANT, you can not copy image, and to use that you need to open the file in binary mode------')
print('------This code will give you an error, do not run it------')
''' return codecs.charmap_decode(input,self.errors,decoding_table)[0]
UnicodeDecodeError: 'charmap' codec can't decode byte 0x8d in position 291: character maps to <undefined>'''
# with open('10france.jpg', 'r') as rf:
#     with open('10france_copy.jpg', 'w') as wf:
#         for line in rf:
#             wf.write(line)

print()
print('------SO IMPORTANT, you can not copy image, and to use that you need to open the file in binary mode------')
print('------you can run this code...------')
print('------you need to added b letter------')

with open('10france.jpg', 'rb') as rf:
    with open('10france_copy.jpg', 'wb') as wf:
        for line in rf:
            wf.write(line)

print()
print('------Chunk_size------')

with open('10BBC.jpg', 'rb') as rf:
    with open('10BBC_copy.jpg', 'wb') as wf:
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)
