import os
from datetime import datetime
from xmlrpc.client import DateTime

size = 'The Size of the file is: '
# print(dir(os)) # PRINING EVERYTHING
print(os.getcwd())
os.chdir('C:/Users/Milad Zarour/Desktop')
print(os.getcwd())
print(os.listdir())

# os.mkdir('OS-Demo-2/Sub-Dir-1') It cannot create subfolder
os.mkdir('OS-Demo-10')  # this is the right

os.makedirs('OS-Demo-2/Sub-Dir-1')
print(os.listdir())
print()

os.rename('text.txt', 'demo.txt')
print(os.listdir())
os.rename('demo.txt', 'text.txt')
print(os.listdir())
print()

os.rmdir('OS-Demo-10')
os.removedirs('OS-Demo-2/Sub-Dir-1')
print(os.listdir())
print()
print(os.stat('text.txt'))
print(os.stat('text.txt').st_size)  # 36
mod_size = str(os.stat('text.txt').st_size)
mod_time = os.stat('text.txt').st_mtime  # st_mtime=1651137289
print(datetime.fromtimestamp(mod_time))  # 2022-04-28 11:14:49.164686
print(size + mod_size)  # The Size of the file is: 36
print()

# os.walk() # three values of tuples
for dirpath, dirnames, filenames in os.walk('C:/Users/Milad Zarour/Desktop'):
    print('Current Path:', dirpath)
    print('Directories:', dirnames)
    print('Files:', filenames)
    print()

print(os.environ.get('HOME'))  # C:\Users\Milad Zarour
# file_path = os.environ.get('HOME') + 'testing.txt'
file_path = os.path.join(os.environ.get('HOME'), 'testing2.txt')
print(file_path)
