from cmath import pi
from email import message
from pyexpat import native_encoding


message_1 = "Hello's World"  # m = 'Hello\'s World'
message_2 = """Hi How are you"""

print(message_1)
print(len(message_1))
print(len(message_1[10]))
# print(len(message_1[13])) ERROR
# from the letter in the index 0 all the way upp the unincluding index 5
print(len(message_1[0:5]))  # == print(len(message_1[:5]))
print(len(message_1[6:]))
print()

print(message_2)
print(message_2.upper())
print(message_2.lower())
print(len(message_2))

print()

print(message_2.count('Hello'))
print(message_2.count('Hi'))
print(message_2.count('H'))

print()

print(message_2.find('Hi'))
print(message_2.find('How'))
print(message_2.find('are'))
print(message_2.find('you'))

print()
message_3 = message_2.replace('you', 'Me')

print(message_2)  # didn't replace it !
print(message_3)

greeting = 'Hello'
name = 'Milad'
message_4 = greeting + name
print(message_4)
message_4 = greeting + ', ' + name
print(message_4)
message_5 = greeting + ', ' + name + '. Welcome!'
print(message_5)

print()

# greeting + ', ' + name + '. Welcome!'
message_6 = 'message_6 = {}, {}. Welcome!'.format(greeting, name)
print(message_6)

message_7 = f'message_7 = {greeting}, {name}. Welcome!'
print(message_7)

message_8 = f'message_8 = {greeting}, {name.upper()}. Welcome!'
print(message_8)
print()
print(dir(name))
print()
print(help(str))
print()
print(help(str.lower))
