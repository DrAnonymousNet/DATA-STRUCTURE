from LinkedList import CircularList 

l = CircularList()
for i in range(4):
    l.add_last(i)
    l.add_First(i +1)
print(l)
l.chopOffStart(2)

print(l)
l.removeIndex(5)
print(l)
l.removeItem(4)
print(l)

from random import randint
for i in range(20):
	l.add_last(randint(1,20))
	
l.josephus(l, 3)
