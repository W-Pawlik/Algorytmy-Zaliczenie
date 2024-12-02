class HashTable:
    def __init__(self, size=10):
        self.size = size  
        self.table = [[] for _ in range(self.size)] 

    def hash_function(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value  
                return
        self.table[index].append([key, value])

    def get(self, key):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None  

    def remove(self, key):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                self.table[index].remove(pair)
                return True
        return False  

    def display(self):
        for i, bucket in enumerate(self.table):
            print(f"Bucket {i}: {bucket}")


hash_table = HashTable(size=5)
hash_table.put("a", 1)
hash_table.put("b", 2)
hash_table.put("c", 3)
hash_table.put("aa", 10)  
hash_table.display()

print("Get 'a':", hash_table.get("a"))
print("Get 'b':", hash_table.get("b"))
print("Remove 'a':", hash_table.remove("a"))
hash_table.display()
print("Get 'a':", hash_table.get("a"))
