import os
import shutil

source = 'C:/Users/Sanjay/Downloads'
destination = 'C:/Users/Sanjay/Desktop'

files = os.listdir(source)

for i in files:
    name,ext = os.path.splitext(i)

print(name, ext)