from Nodes import Node

class DoubleList:
    def __init__(self):
        self.head = None
        self.length = 0

    def add_first(self, item):
        if self.head is None:
            self.head = Node(item , next= None , prev= None)
            self.length += 1
            return
        new_node = Node(item , self.head, None)
        self.head.prev = new_node
        self.head = new_node
        self.length += 1
        return

    def remove_last(self):
        if not self.head:
            return
        if self.head.next is None:
            self.head = None
            self.length -=1
            return
        curr_node = self.head
        while curr_node.next:
            curr_node = curr_node.next
        curr_node.prev.next = None
        curr_node = None
        self.length -= 1
    def add_last(self, item):
        if not self.head:
            self.add_first(item)
            return
        curr_node = self.head
        while curr_node.next:
            curr_node = curr_node.next
        new_node = Node(item , None , curr_node)
        curr_node.next = new_node
        self.length += 1

    def remove_first(self):
        if not self.head:
            return
        if not self.head.next:
            self.head = None
            self.length -= 1
            return
        self.head = self.head.next
        self.head.prev = None
        self.length -= 1
    def rotate(self):
        if not self.head or not self.head.next:
            return
        curr_node = self.head
        while curr_node.next:
            curr_node = curr_node.next
        curr_node.next = self.head
        curr_node.prev.next = None
        self.head.prev = curr_node
        curr_node.prev = None
        self.head = curr_node

    def remove_index_item(self, index):
        if index == self.length -1:
            self.remove_last()
            return
        elif index >= self.length:
            raise IndexError("OUT OF RANGE")

        elif index == 0:
            self.remove_first()

            return
        counter = 0
        curr_node = self.head
        while counter < index:
            curr_node = curr_node.next
            counter += 1
        curr_node.prev.next = curr_node.next
        curr_node.next.prev = curr_node.prev
        curr_node.prev = curr_node.next = None
        curr_node = None
        self.length -= 1

    def insert(self, item , index):
        if index == 0:
            self.add_first(item)
            return
        elif index == self.length:
            self.add_last(item)
            return
        elif index > self.length:
            raise IndexError("OUT OF RANGE")
        counter = 0
        curr_node = self.head
        while counter < index:
            curr_node = curr_node.next
            counter += 1
        new_node = Node(item , curr_node, curr_node.prev)
        curr_node.prev.next = new_node
        curr_node.prev =new_node
        self.length +=1

    def remove_node(self , node):
        if node == self.head:
            self.remove_first()
            return
        curr_node = self.head
        while curr_node:
            if curr_node == node:
                if curr_node.next:
                    curr_node.prev.next = curr_node.next
                    curr_node.next.prev = curr_node.prev
                    curr_node = None


                else:
                    curr_node.prev.next = None
                self.length -= 1
                return
            curr_node = curr_node.next
        if not curr_node:
            raise ValueError("NODE NOT FOUND")


    def get_index_item(self, index):
        if index >= self.length:
            raise IndexError("OUT OF RANGE")



        if index == 0:
            return self.head.data
        curr_node = self.head
        counter = 0
        while counter < index:
            curr_node = curr_node.next
            counter += 1
        return curr_node




    def remove_item(self, item):
        if self.head.data == item:
            self.remove_first()

            return
        curr_node = self.head
        while curr_node:
            if curr_node.data == item:
                self.remove_node(curr_node)
                return
            curr_node = curr_node.next

        if not curr_node:
            raise ValueError("Item Not Found")

    def clear(self):
        self.head =None
        self.length = 0

    def combine(self , lst):
        curr_node = self.get_index_item(self.length-1)
        curr_node.next = lst.head
        lst.head.prev = curr_node

        self.length += lst.length

    def __repr__(self):
        if self.length == 0:
            return "[]"
        curr_node = self.head
        print("[" , self.head.data , end= "")
        while curr_node.next != None:
            curr_node = curr_node.next
            print("," , curr_node.data, end= "")
        return " ]"
    def __len__(self):
        return self.length

    def __eq__(self, lst):
        curr_node = self.head
        curr_node_1 = lst.head

        while (curr_node != None and curr_node_1 != None) and curr_node.data == curr_node_1.data:
            curr_node = curr_node.next
            curr_node_1 = curr_node_1.next

        if curr_node is None:
            return True
        elif curr_node is not None:
            return False
