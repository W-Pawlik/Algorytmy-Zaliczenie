class NodeS:
    def __init__(self, data):
        self.data = data  
        self.next = None 


class SinglyLinkedList:
    def __init__(self):
        self.head = None  

    def insert_at_end(self, data):
        new_node = NodeS(data)
        if not self.head:  
            self.head = new_node
            return
        current = self.head
        while current.next: 
            current = current.next
        current.next = new_node

    def display(self):
        current = self.head
        while current: 
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def delete(self, data):
        if not self.head: 
            return
        if self.head.data == data:  
            self.head = self.head.next
            return
        current = self.head
        while current.next and current.next.data != data:
            current = current.next
        if current.next: 
            current.next = current.next.next


class NodeD:
    def __init__(self, data):
        self.data = data  
        self.next = None  
        self.prev = None  


class DoublyLinkedList:
    def __init__(self):
        self.head = None  

    def insert_at_end(self, data):
        new_node = NodeD(data)
        if not self.head:  
            self.head = new_node
            return
        current = self.head
        while current.next:  
            current = current.next
        current.next = new_node
        new_node.prev = current

    def display_forward(self):
        current = self.head
        while current:  
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def display_backward(self):
        current = self.head
        if not current: 
            print("None")
            return
        while current.next:  
            current = current.next
        while current: 
            print(current.data, end=" -> ")
            current = current.prev
        print("None")

    def delete(self, data):
        if not self.head:  
            return
        if self.head.data == data:  
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            return
        current = self.head
        while current and current.data != data:
            current = current.next
        if current:  
            if current.next:
                current.next.prev = current.prev
            if current.prev:
                current.prev.next = current.next

print("---SinglyLinkedList---")
sll = SinglyLinkedList()
sll.insert_at_end("a")
sll.insert_at_end(2)
sll.insert_at_end(3)
sll.display()
sll.delete(2)
sll.display()

print("---DoublyLinkedList---")
dll = DoublyLinkedList()
dll.insert_at_end(1)
dll.insert_at_end(2)
dll.insert_at_end(3)
dll.display_forward()
dll.display_backward()
dll.delete(2)
dll.display_forward()
dll.display_backward()


