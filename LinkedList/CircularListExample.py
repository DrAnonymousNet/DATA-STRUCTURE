from LinkedList import CircularList 

l = CircularList()
for i in range(4):
    l.add_last(i)
    l.add_First(i +1)
print(l)
l.chop_off_start(2)

print(l)
l.remove_index(5)
print(l)
l.remove_item(4)
print(l)
l.rotate()
print(l)
l.clear()
print(l)
l.add_last(1)


m= CircularList()
m.add_last(1)


print(l == m)

from random import randint
for i in range(20):
	l.add_last(randint(1,20))
	
l.josephus(l, 3)
