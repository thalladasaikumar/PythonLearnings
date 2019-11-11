import os
print(os.sep) # prints os specific file separator
print(os.getcwd()) # current working directory 
filePath = os.path.join('folder1','folder2','folder3','images.png') # applies for different operating systems
print(filePath)
print(os.getpid())


print(os.path.isfile(os.path.join(r'C:\Users\thall\Downloads', '10931559670001014620003346548.pdf')))

print(os.path.getsize(os.path.join(r'C:\Users\thall\Downloads', '10931559670001014620003346548.pdf')))

# finding total size of all files under downloads folder.
totalSize = 0
for eachfile in os.listdir(r'C:\Users\thall\Downloads'):
    if os.path.isfile(os.path.join(r'C:\Users\thall\Downloads', eachfile)):
        totalSize = totalSize + os.path.getsize(os.path.join(r'C:\Users\thall\Downloads', eachfile))
print(totalSize)