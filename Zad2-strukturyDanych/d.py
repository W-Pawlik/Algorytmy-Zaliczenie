class QueueArray:
    def __init__(self):
        self.queue = []  

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)  
        return "Kolejka jest pusta"

    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        return "Kolejka jest pusta"

    def is_empty(self):
        return len(self.queue) == 0

    def display(self):
        print("Kolejka:", self.queue)

class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None  


class QueueList:
    def __init__(self):
        self.front = None  
        self.rear = None  

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:  
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node  
            self.rear = new_node

    def dequeue(self):
        if self.front is None:  
            return "Kolejka jest pusta"
        temp = self.front
        self.front = self.front.next  
        if self.front is None:  
            self.rear = None
        return temp.data

    def peek(self):
        if self.front is not None:
            return self.front.data
        return "Kolejka jest pusta"

    def is_empty(self):
        return self.front is None

    def display(self):
        current = self.front
        print("Kolejka:", end=" ")
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


print("---QueueArray---")

qa = QueueArray()
qa.enqueue(10)
qa.enqueue(20)
qa.enqueue(30)
qa.display()
print("Dequeue:", qa.dequeue())
qa.display()
print("Peek:", qa.peek())

print("---QueueList---")
ql = QueueList()
ql.enqueue(10)
ql.enqueue(20)
ql.enqueue(30)
ql.display()
print("Dequeue:", ql.dequeue())
ql.display()
print("Peek:", ql.peek())