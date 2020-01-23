import os

filepath='../eyeballs'
fileNams=os.listdir(filepath)
print(len(fileNams))
for name in fileNams:
    print(name)
    open(filepath + name, 'ab').write(b'camare')
