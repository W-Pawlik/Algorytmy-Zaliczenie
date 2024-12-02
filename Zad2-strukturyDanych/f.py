class Heap:
    def __init__(self, is_min_heap=True):
        self.heap = []  
        self.is_min_heap = is_min_heap  
    def compare(self, parent, child):
        if self.is_min_heap:
            return parent > child  
        else:
            return parent < child  

    def insert(self, value):
        self.heap.append(value)
        self.heapify_up(len(self.heap) - 1)

    def extract(self):
        if not self.heap:
            return "Kopiec jest pusty"
        root = self.heap[0]
        self.heap[0] = self.heap[-1]  
        self.heap.pop()  
        if self.heap:
            self.heapify_down(0)
        return root

    def heapify_up(self, index):
        parent_index = (index - 1) // 2
        while index > 0 and self.compare(self.heap[parent_index], self.heap[index]):
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            index = parent_index
            parent_index = (index - 1) // 2

    def heapify_down(self, index):
        size = len(self.heap)
        while True:
            smallest_largest = index
            left_child = 2 * index + 1
            right_child = 2 * index + 2

            if left_child < size and self.compare(self.heap[smallest_largest], self.heap[left_child]):
                smallest_largest = left_child

            if right_child < size and self.compare(self.heap[smallest_largest], self.heap[right_child]):
                smallest_largest = right_child

            if smallest_largest == index:
                break

            self.heap[index], self.heap[smallest_largest] = self.heap[smallest_largest], self.heap[index]
            index = smallest_largest

    def display(self):
        print("Kopiec:", self.heap)


min_heap = Heap(is_min_heap=True) 
min_heap.insert(10)
min_heap.insert(5)
min_heap.insert(20)
min_heap.insert(2)
min_heap.display()
print("Extract:", min_heap.extract())
min_heap.display()

max_heap = Heap(is_min_heap=False)  
max_heap.insert(10)
max_heap.insert(5)
max_heap.insert(20)
max_heap.insert(2)
max_heap.display()
print("Extract:", max_heap.extract())
max_heap.display()
