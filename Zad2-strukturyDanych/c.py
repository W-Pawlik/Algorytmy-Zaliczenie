class SinglyLinkedListArray:
    def __init__(self):
        self.list = [] 
        self.head = None  

    def insert(self, data):
        node = {'data': data, 'next': None}  
        if self.head is None:  
            self.head = len(self.list)
        else:  
            current = self.head
            while self.list[current]['next'] is not None:
                current = self.list[current]['next']
            self.list[current]['next'] = len(self.list)
        self.list.append(node)

    def display(self):
        current = self.head
        while current is not None:
            print(self.list[current]['data'], end=" -> ")
            current = self.list[current]['next']
        print("None")

    def delete(self, data):
        if self.head is None:  
            return
        if self.list[self.head]['data'] == data:  
            self.head = self.list[self.head]['next']
            return
        current = self.head
        while current is not None and self.list[current]['next'] is not None:
            next_node = self.list[current]['next']
            if self.list[next_node]['data'] == data:
                self.list[current]['next'] = self.list[next_node]['next']
                return
            current = next_node

class DoublyLinkedListArray:
    def __init__(self):
        self.list = []  
        self.head = None  
        self.tail = None  

    def insert(self, data):
        node = {'data': data, 'next': None, 'prev': None} 
        if self.head is None:  
            self.head = len(self.list)
            self.tail = len(self.list)
        else:  
            node['prev'] = self.tail
            self.list[self.tail]['next'] = len(self.list)
            self.tail = len(self.list)
        self.list.append(node)

    def display_forward(self):
        current = self.head
        while current is not None:
            print(self.list[current]['data'], end=" -> ")
            current = self.list[current]['next']
        print("None")

    def display_backward(self):
        current = self.tail
        while current is not None:
            print(self.list[current]['data'], end=" -> ")
            current = self.list[current]['prev']
        print("None")

    def delete(self, data):
        if self.head is None: 
            return
        if self.list[self.head]['data'] == data:  
            if self.head == self.tail:  
                self.head = None
                self.tail = None
            else:
                self.head = self.list[self.head]['next']
                self.list[self.head]['prev'] = None
            return
        current = self.head
        while current is not None:
            if self.list[current]['data'] == data:
                prev_node = self.list[current]['prev']
                next_node = self.list[current]['next']
                if prev_node is not None:
                    self.list[prev_node]['next'] = next_node
                if next_node is not None:
                    self.list[next_node]['prev'] = prev_node
                if current == self.tail:  
                    self.tail = prev_node
                return
            current = self.list[current]['next']

print("---SinglyLinkedList---")
sll_array = SinglyLinkedListArray()
sll_array.insert(1)
sll_array.insert(2)
sll_array.insert(3)
sll_array.display()
sll_array.delete(2)
sll_array.display()

print("---DoublyLinkedList---")
dll_array = DoublyLinkedListArray()
dll_array.insert(1)
dll_array.insert(2)
dll_array.insert(3)
dll_array.display_forward()
dll_array.display_backward()
dll_array.delete(2)
dll_array.display_forward()
dll_array.display_backward()


