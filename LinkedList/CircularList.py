from Nodes import Node

class CircularList:
    def __init__(self):
        self.head = None
        self.length = 0

    def tail_node(self):
        curr_node = self.head
        while curr_node.next.next != self.head:

            curr_node = curr_node.next
        return curr_node

    def add_First(self, item):
        if self.head is None:
            self.head = Node(item)
            self.head.next = self.head
            self.length += 1
            return
        prev_node = self.tail_node().next
        new_node = Node(item, self.head)
        self.head = new_node
        prev_node.next  = self.head
        self.length += 1

    def add_last(self , item):

        if self.head is None:
            self.head = Node(item)
            self.head.next = self.head
            self.length += 1
            return
        curr_node = self.head
        while curr_node.next != self.head:
            curr_node = curr_node.next
        curr_node.next = Node(item , self.head)
        self.length += 1

    def remove_last(self):
        if self.head is None:
            return
        elif self.head == self.head.next:
            self.head = None
            self.length -= 1
            return
        curr_node = self.tail_node()
        curr_node.next.next = None
        curr_node.next = self.head
        self.length -= 1

    def remove_first(self):
        if self.head is None:
            return
        elif self.head.next == self.head:
            self.head = None
            self.length -= 1
            return
        curr_node = self.tail_node()
        curr_node.next.next = self.head.next
        self.head = self.head.next
        self.length -=1

    def remove_node(self, node):
        if node == self.head:
            prev_node = self.tail_node().next
            prev_node.next = self.head.next

            self.head = self.head.next
            self.length -= 1
            return
        curr_node = self.head
        while curr_node.next != node:
            curr_node = curr_node.next
        curr_node.next = node.next
        self.length -= 1
    @staticmethod
    def josephus(l, step):

        counter = 1
        curr_node = l.head
        while l.length != 1:
            if counter == step:
                counter = 0
                print(str(curr_node.data) + " killed")
                l.remove_node(curr_node)
                curr_node  = prev_node
                if l.length == 1:
                    print(str(curr_node.data) + " Survived")
                    return
                continue
            prev_node = curr_node
            curr_node = curr_node.next
            counter += 1
        print(l)



    def insert(self , item , index):
        if self.head is None and index > 0:
            raise IndexError("OUT OF RANGE")
        elif index == 0  and self.head is None:
            self.add_First(item)
            return
        elif index == 0 and self.head.next is not None:
            prev_node = self.tail_node().next
            self.head = Node(item, self.head)
            prev_node.next = self.head
            self.length += 1
            return
        elif index == self.length:
            self.add_last(item)
            return
        counter = 0

        curr_node = self.head
        while counter < index and curr_node.next != self.head:
            prev_node = curr_node
            curr_node = curr_node.next
            counter += 1

        curr_node = Node(item , curr_node)
        prev_node.next = curr_node
        self.length += 1

    def remove_index(self, index):
        if index == 0 and self.head.next != self.head:
            self.remove_first()
            return
        elif index >= self.length-1:
            return
        elif index == self.length-1:
            self.remove_last()
            return
        curr_node = self.head
        counter = 0
        while counter < index:
            prev_node = curr_node
            curr_node = curr_node.next
            counter += 1
        prev_node.next = curr_node.next
        self.length -= 1

    def remove_item(self , item):
        if self.head.data == item:
            self.remove_first()
            return
        elif self.tail_node().next.data == item:
            self.remove_last()
            return
        curr_node = self.head
        while curr_node.next != self.head and curr_node.data != item:
            prev_node = curr_node
            curr_node = curr_node.next
        if curr_node.next == self.head:
            return
        prev_node.next = curr_node.next
        self.length -= 1

    def chop_off_start(self, index):
        if index  == 0:
            self.remove_first()
            return
        counter = 0
        curr_node = self.head
        while counter < index:
            curr_node =curr_node.next
            counter += 1

        prev_node =self.tail_node().next
        prev_node.next = curr_node.next
        self.head = curr_node.next
        self.length -= index

    def combine(self , lst):
        curr_node = self.get_item(self.lenght-1)
        curr_node.next = lst.head
        self.lenght += lst.lenght

    def rotate(self):
        if self.head.next == self.head:
            return
        curr_node = self.head
        while curr_node.next != self.head:
            curr_node = curr_node.next
        self.head = curr_node

    def clear(self):
        self.head = None
        self.length = 0

    def get_node_item(self, node):
        if self.head == node:
            return self.head
        curr_node = self.head

        while curr_node != Node:
            curr_node = curr_node.next

        if curr_node:
            return curr_node
        raise ValueError("Node Not Found")

    def __repr__(self):
        if self.length == 0:
            return "[]"
        curr_node = self.head
        print("[" , self.head.data , end= "")
        while curr_node.next != self.head:
            curr_node = curr_node.next
            print("," , curr_node.data, end= "")
        return " ]"
    def __len__(self):
        return self.length



    def __eq__(self, lst):
        if self.length != lst.length:
            return False
        curr_node = self.head
        curr_node_1 = lst.head

        while curr_node.next != self.head  and curr_node.data == curr_node_1.data:
            if curr_node.data != curr_node_1.data:
                return False
            curr_node = curr_node.next
            curr_node_1 = curr_node_1.next

        return True
