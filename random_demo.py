from random import *

for i in range(10):
    print(random())

for i in range(10):
    print(randint(10,40))

for i in range(10):
    print(uniform(1,40))
    
for i in range(10):
    print(randrange(1,12,2))

list1 =['java','python','devops','aws']
for i in range(10):
    print(choice(list1))