def linear_search(arr, target):
    """
    Algorytm wyszukiwania liniowego.
    :param arr: Przeszukiwana lista
    :param target: Szukana wartość
    :return: Indeks elementu, jeśli znaleziony, lub -1, jeśli nie znaleziony
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i 
    return -1  

data = [10, 20, 30, 40, 50]
to_find = 30

result = linear_search(data, to_find)
if result != -1:
    print(f"Element {to_find} znaleziony na indeksie {result}")
else:
    print(f"Element {to_find} nie znaleziony w liście")
