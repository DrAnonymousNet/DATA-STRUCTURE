class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.isempty():
            return self.queue.pop(0)
        raise IndexError("Dequeue from empty queue")

    def isempty(self):
        return len(self.queue) == 0

    def peek(self):
        if not self.isempty():
            return self.queue[0]
        raise IndexError("Peek from empty queue")

    def __len__(self):
        return len(self.queue)

    @property
    def __str__(self):
        return self.queue

    def __repr__(self):
        return self.queue


def hotPotato(num):
    queue = Queue()

    for i in range(20):
        queue.enqueue(i)

    n = 0
    while (len(queue) > 1):
        if n == num:
            print(str(queue.dequeue()) + " REMOVED")
            n = 0

        elif n != num:
            queue.enqueue(queue.dequeue())
            n += 1
    print(queue.queue)

hotPotato(2)
