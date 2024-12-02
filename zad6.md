### **Dowód poprawności wyszukiwania liniowego**

Musimy pokazać:

1. **Własność poprawności**: Jeśli element `target` istnieje w tablicy, algorytm zwróci poprawny indeks tego elementu.
2. **Własność zakończenia**: Algorytm zawsze się kończy.

---

### **1. Poprawność (częściowy dowód przez indukcję)**

#### Założenia:

- Niech `arr` będzie tablicą o rozmiarze `n`.
- `target` jest wartością, którą szukamy.

#### **Krok bazowy (i = 0):**

- Algorytm zaczyna od indeksu `i = 0`.
- Jeśli `arr[0] == target`, algorytm natychmiast zwraca `0`, co jest poprawnym wynikiem.

#### **Krok indukcyjny:**

- Zakładamy, że algorytm działa poprawnie dla `i = 0, 1, ..., k-1` (wszystkie elementy od `0` do `k-1` zostały poprawnie sprawdzone).
- Musimy pokazać, że działa poprawnie dla `i = k`.

1. Jeśli `arr[k] == target`, algorytm zwróci `k`, co jest poprawnym wynikiem.
2. Jeśli `arr[k] != target`, algorytm przechodzi do kolejnego indeksu. Z założenia indukcyjnego, algorytm sprawdzi następne elementy poprawnie.
3. Jeśli algorytm dotrze do końca tablicy (`k = n-1`) i nie znajdzie `target`, zwróci `-1`, co jest zgodne z definicją (element nie istnieje).

#### **Wniosek:**

Na podstawie indukcji algorytm poprawnie znajdzie `target` w tablicy, jeśli `target` istnieje, lub zwróci `-1`, jeśli `target` nie istnieje.

---

### **2. Zakończenie**

- Algorytm ma pętlę, która iteruje maksymalnie przez `n` elementów tablicy.
- W każdej iteracji wykonuje stałą liczbę operacji (`arr[i] == target`).
- Po sprawdzeniu wszystkich elementów (lub znalezieniu `target`) algorytm kończy się.

#### **Wniosek:**

Algorytm zawsze się kończy, ponieważ tablica ma skończony rozmiar, a każda iteracja przesuwa się o jeden krok w kierunku końca.

---

### **3. Całkowity dowód poprawności**

#### **Przypadek 1: `target` istnieje w `arr`.**

- Algorytm przejdzie przez tablicę, aż znajdzie `target` na jakimś indeksie `i`.
- W momencie znalezienia `arr[i] == target`, zwróci poprawny indeks `i`.

#### **Przypadek 2: `target` nie istnieje w `arr`.**

- Algorytm przeszuka całą tablicę i nie znajdzie `target`.
- Po zakończeniu pętli zwróci `-1`.

---

### **4. Poprawność na przykładzie**

Dane: `arr = [5, 10, 15, 20], target = 15`.

1. Iteracja 0: `arr[0] != 15`.
2. Iteracja 1: `arr[1] != 15`.
3. Iteracja 2: `arr[2] == 15` → zwraca `2`.

Poprawność:

- `15` znajduje się w tablicy na pozycji `2`, co jest poprawnym wynikiem.

---

### **Podsumowanie**

Dowiedliśmy, że algorytm wyszukiwania liniowego spełnia dwa warunki:

1. **Poprawność**: Znajduje `target` w tablicy (lub zwraca `-1`, jeśli `target` nie istnieje).
2. **Zakończenie**: Algorytm zawsze kończy działanie.

Algorytm wyszukiwania liniowego jest więc **poprawny i kompletny**.
