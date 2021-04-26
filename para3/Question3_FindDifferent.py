import random
list = []
for i in range(10):
    list.append(str(i))
for i in range(3):
    print(list.pop( random.randint(0,len(list)) ),end="")