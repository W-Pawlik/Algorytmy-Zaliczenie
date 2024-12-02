class StackArray:
    def __init__(self):
        self.stack = [] 

    def push(self, data):
        """Dodaj element na stos"""
        self.stack.append(data)

    def pop(self):
        """Usuń element ze szczytu stosu"""
        if not self.is_empty():
            return self.stack.pop()
        return "Stos jest pusty"

    def peek(self):
        """Zobacz element na szczycie stosu bez usuwania"""
        if not self.is_empty():
            return self.stack[-1]
        return "Stos jest pusty"

    def is_empty(self):
        """Sprawdź, czy stos jest pusty"""
        return len(self.stack) == 0

    def display(self):
        """Wyświetl zawartość stosu"""
        print("Stos:", self.stack)

class Node:
    def __init__(self, data):
        self.data = data  
        self.next = None 


class StackList:
    def __init__(self):
        self.top = None  

    def push(self, data):
        """Dodaj element na stos"""
        new_node = Node(data)
        new_node.next = self.top  
        self.top = new_node  

    def pop(self):
        """Usuń element ze szczytu stosu"""
        if self.top is None:  
            return "Stos jest pusty"
        temp = self.top
        self.top = self.top.next  
        return temp.data

    def peek(self):
        """Zobacz element na szczycie stosu bez usuwania"""
        if self.top is not None:
            return self.top.data
        return "Stos jest pusty"

    def is_empty(self):
        """Sprawdź, czy stos jest pusty"""
        return self.top is None

    def display(self):
        """Wyświetl zawartość stosu"""
        current = self.top
        print("Stos:", end=" ")
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


print("---StackArray---")
stack_array = StackArray()
stack_array.push(10)
stack_array.push(20)
stack_array.push(30)
stack_array.display()
print("Pop:", stack_array.pop())
stack_array.display()
print("Peek:", stack_array.peek())


print("---StackList---")
stack_list = StackList()
stack_list.push(10)
stack_list.push(20)
stack_list.push(30)
stack_list.display()
print("Pop:", stack_list.pop())
stack_list.display()
print("Peek:", stack_list.peek())