import os
oldFile = 'demo3.txt'
newFile = "rename_demo.txt"

with open(oldFile,'r') as f:
    content=f.read()

with open(newFile,'w') as f:
    f.write(content)

os.remove(oldFile)