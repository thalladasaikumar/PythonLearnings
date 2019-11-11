import shutil

emptyFile = open('emptyFile.txt','a')
emptyFile.write("This is an empty file previously\n")
emptyFile.close()

shutil.copy('emptyFile.txt', r'E:\softwares\softwares_installation\eclipse\workSpace\LearningPython\src\udemy\files') # to copy files

#shutil.copytree() #to copy folders.


import os

src = os.getcwd()
dst = 'E:\\softwares\\softwares_installation\\eclipse\\workSpace\\LearningPython\\src\\udemy\\files'
if os.path.exists(os.path.join(dst,'emptyFile.txt')):
    os.remove(os.path.join(dst,'emptyFile.txt'))
    shutil.move(r'E:\softwares\softwares_installation\eclipse\workSpace\LearningPython\src\udemy\automate the boring stuff with python\emptyFile.txt', dst) # to move files
# there is no rename instead use the move function.

if not os.path.exists('emptyFolder'):
    os.mkdir(os.path.join(os.getcwd(),'emptyFolder'))
    os.rmdir('emptyFolder')
if not os.path.exists('emptyFolder'):
    os.mkdir(os.path.join(os.getcwd(),'emptyFolder'))
    shutil.rmtree('emptyFolder')

import send2trash
if not os.path.exists('emptyFolder'):
    os.mkdir(os.path.join(os.getcwd(),'emptyFolder'))
send2trash.send2trash('emptyFolder')

os.walk(os.getcwd())
for folderName, subFolders, fileNames in os.walk(os.getcwd()):
    print('The folder is :'+folderName)
    print('The subFolders in '+folderName+' are :'+str(subFolders))
    print('The filenames in '+folderName+' are :'+str(fileNames))
    print()