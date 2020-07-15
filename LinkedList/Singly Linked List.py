class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.lenght = 0

    def add_first(self, item):
        if self.head is None:
            self.head = Node(item)
            self.tail= self.head
            self.lenght +=1
            return
        curr_node = self.head
        self.head =Node(item, curr_node)

        self.lenght +=1

    def remove_first(self):
        if self.head is None:
            return
        self.head = self.head.next
        self.lenght -=1

    def add_last(self,item):
        new_node = Node(item)
        if self.head is None:
            self.head = new_node
            self.lenght +=1
            return
        curr_node = self.head
        while curr_node.next != None:
            curr_node = curr_node.next
        curr_node.next = new_node
        self.tail = curr_node.next
        self.lenght += 1

    def remove_last(self):
        if self.head.next is None:
            self.head = None
        curr_node = self.head
        while curr_node.next.next != None:
            curr_node = curr_node.next

        curr_node.next = None
        self.lenght -= 1

    def insert(self, item, index):
        counter = 0
        new_node = Node(item)
        curr_node = self.head
        prev_node = None
        while counter < index:
            counter += 1
            prev_node = curr_node
            curr_node = curr_node.next

        new_node.next =curr_node
        if curr_node == self.head:
            self.head = new_node
        if prev_node is not None:
            prev_node.next = new_node
        self.lenght += 1

    def __delete__(self, instance):
        self.head = None
        return
    def remove_index(self, index):
        counter = 0
        if index > self.lenght-1:
            raise IndexError("OUT OF RANGE")
        if index == 0:
            self.head = self.head.next
            self.lenght -= 1
            return
        curr_node = self.head
        prev_node = None
        while counter < index:
            prev_node = curr_node
            curr_node = curr_node.next
            counter += 1
        prev_node.next = curr_node.next

        self.lenght -=1

    def remove_item(self, item):

        if self.head.data == item:
            self.head = self.head.next
            self.lenght -= 1
            return
        curr_node = self.head
        prev_node = None
        while curr_node != None and curr_node.data != item:
            prev_node = curr_node
            curr_node = curr_node.next

        if curr_node is None:
            raise ValueError("Item not found")
        prev_node.next = curr_node.next

        self.lenght -=1

    def chopOffStart(self, num):
        counter =  0
        curr_node = self.head
        while counter < num :
            curr_node = curr_node.next
            counter += 1
        self.head = curr_node
        self.lenght -= num

    def chopOffEnd(self, num):
        counter =  0
        curr_node = self.head
        while counter < num :
            prev_node = curr_node
            curr_node = curr_node.next
            counter += 1

        prev_node.next = None
        prev_node = self.tail

        self.lenght = num
    def get_item(self , index):
        counter = 0
        if index > self.lenght - 1:
            raise IndexError("OUT OF RANGE")
        if index == 0:
            return self.head
        curr_node = self.head
        prev_node = None
        while counter < index:
            prev_node = curr_node
            curr_node = curr_node.next
            counter += 1
        return curr_node

    def evenToString(self):
        curr_node = self.head


        counter = 0
        print("[" , self.head , end="")
        while curr_node != None:
            if counter % 2 == 0 and counter > 0:
                print("," , curr_node.data, end = "")
            curr_node = curr_node.next
            counter += 1
        return "]"

    def count(self, item):
        curr_node = self.head
        counter = 0

        while curr_node != None:
            if curr_node.data == item:
                counter +=1
            curr_node = curr_node.next
        return counter
    def deleteEvenIndex(self):
        curr_node = self.head
        prev_node = curr_node
        self.head = self.head.next
        counter = 0
        while curr_node != None:
            if counter % 2 == 0:
                prev_node.next = curr_node.next
                prev_node = curr_node.next
            curr_node = curr_node.next
            counter +=1
        self.lenght -= self.lenght // 2

    def combine(self , lst):
        curr_node = self.get_item(self.lenght-1)
        curr_node.next = lst.head
        self.lenght += lst.lenght

    def __eq__(self, lst):
        curr_node = self.head
        curr_node_1 = lst.head

        while (curr_node != None and curr_node_1 !=None) and curr_node.data == curr_node_1.data:
            curr_node = curr_node.next
            curr_node_1 = curr_node_1.next

        if curr_node is None:
            return True
        elif curr_node is not None:
            return False




    def clear(self):
        self.head = None
        self.lenght = 0
    def __repr__(self):
        if self.lenght == 0:
            return "[]"
        curr_node = self.head
        print("[" , self.head.data , end= "")
        while curr_node.next != None:
            curr_node = curr_node.next
            print("," , curr_node.data, end= "")


        return "]"

    def __len__(self):
        return self.lenght
