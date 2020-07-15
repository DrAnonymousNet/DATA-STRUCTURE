class Node:

    def __init__(self, data, next = None):
        self.data = data
        self.next = next
    def __repr__(self):
        return self.data
    def __str__(self):
        return str(self.data)
