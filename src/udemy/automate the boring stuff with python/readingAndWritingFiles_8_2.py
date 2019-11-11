helloFile = open('E:\\softwares\\softwares_installation\\eclipse\\workSpace\\LearningPython\\src\\udemy\\files\\hello.txt')
print(helloFile.read())
helloFile.close()


helloFile = open('E:\\softwares\\softwares_installation\\eclipse\\workSpace\\LearningPython\\src\\udemy\\files\\hello.txt')
content = helloFile.readlines()
print(content)
helloFile.close()

helloFile = open('E:\\softwares\\softwares_installation\\eclipse\\workSpace\\LearningPython\\src\\udemy\\files\\hello2.txt', 'w')
helloFile.write('Hello World!')
helloFile.close()

helloFile = open('E:\\softwares\\softwares_installation\\eclipse\\workSpace\\LearningPython\\src\\udemy\\files\\hello2.txt', 'a')
helloFile.write('Hello World!')
helloFile.close()

# helloFile = open('hello.txt','a')
# helloFile.write("are you in library?")
# helloFile.close()


