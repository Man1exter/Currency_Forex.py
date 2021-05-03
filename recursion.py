# T(n) = 6T(n/3) + n
# T(n) = T(n/2) + n
# T(n) = 2T(n/2) + n

# 1. Wypisujemy A, B, f(n)
# 2. Obliczamy n^(log(b)a)
# 3. Porównujemy f(n) z n^(log(b)a)
# 4. Jeśli rząd wskazuje iż:
     # a. f(n) > n^(log(b)a) to wynik będzie równy T(n)=O(f(n))
     # b. f(n) < n^(log(b)a) to wynik będzie równy T(n)=O(n^(log(b)a))
     # c. f(n) = n^(log(b)a) to wynik będzie równy T(n)=O(n^(log(b)a) * log n) => T(n)=O(f(n) * log n)


def f1():
    pass

def f2():
    pass

def f3():
    pass