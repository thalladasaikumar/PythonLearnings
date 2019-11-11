for i in [0,1,2,3,4]:
    print(i)
    
print(list(range(4)))

print(list(range(0,100,2))) #prints all numbers of 2 difference up to 100


cat = ['fat', 'orange', 'loud']

size, color, disposition = cat
print(size)
print(color)
print(disposition)

cat.append('Zophiee')
print(cat)

cat.sort(key=None, reverse=False)
print(cat)

cat.sort(key=None, reverse=True)
print(cat)