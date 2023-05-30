import numpy as np

# zad 1:
# arange stwórz tablicę numpyskładającą się z 20 kolejnych wielokrotności liczby 4.
a = np.arange(4, 4 * 21, 4)
print(a)

# zad 2:
# Stwórz listę składającą się z wartości zmiennoprzecinkowych a następnie zapisz do innej zmiennej jej kopię przekonwertowaną na typ int32
lista = [2.1, 3.4, 9.9]
tab = np.array(lista)
kopia = tab.astype(np.int32)
print(kopia)

# zad 3:
# Napisz funkcję, która będzie:
# •Przyjmowała jeden parametr ‘n’ w postaci liczby całkowitej
# •Zwracała tablicę Numpy o wymiarach n*n kolejnych potęg liczby 2
def tab_pow(n):
    potega = np.arange(n**2).reshape(n, n)
    return potega
n = 8
wynik = tab_pow(n)
print(wynik)

#zad 4:
# Napisz funkcję, która będzie przyjmowała 2 parametry:
# liczbę, która będzie podstawą operacji potęgowania oraz ilość kolejnych potęg do wygenerowania.
# Korzystając z funkcji logspace generuj tablicę jednowymiarową kolejnych potęg podanej liczby, np. generuj(2,4) -> [2,4,8,16]

def zad4(a, b):
    potega = np.power(a, np.arange(1, b+1))
    return potega











# a = np.array([[0, 1, 5], [3,4, 5], [4, 7, 2]])
# print(a)
# print(a.shape)
#
# a = np.arange(2, 5, 0.1)
# print(a)
#
# print(type(a))
#
# print(a.dtype)
#
# a = np.arange(2, dtype='int64')
# print(a.dtype)
#
# b = a.astype('float')
# print(b)
# print(b.dtype)
#
# print(b.shape)
#
# print(a.ndim)
#
# m = np.array([np.arange(2), np.arange(2)])
# print(m.shape)

# print(type(m))
#
# zera = np.zeros((5, 5))
# jedynki = np.ones((4, 4))
# print(zera)
# print(jedynki)
# print(zera.dtype)
#
# pusta = np.empty((2, 2))
# print(pusta)
#
#
# macierz = np.array([[12, 11], [2, 1]])
# print(macierz)
#
# poz_1 = macierz[1, 1]
# poz_2 = macierz[0][1]
# print(poz_2)
# print(poz_1)
#
# liczby_lin = np.linspace(1,2,5,endpoint=False)
# print(liczby_lin)
#
# z = np.indices((5, 3))
# print(z)
# print(z[0][1][2])
#
# mat_diag = np.diag([a for a in range(5)], 1)
# print(mat_diag)
#
# z = np.fromiter(range(5), dtype='int32')
# print(z)

# znaki = b'ogolna'
# z1 = np.frombuffer(znaki, dtype='S1')
# print(z1)
# z2 = np.frombuffer(znaki, dtype='S2')
# print(z2)
#
# znaki = 'ogolna'
# z3 = np.array(list(znaki))
# z4 = np.array(list(znaki), dtype='S1')
# z5 = np.array(list(b'ogolna'))
# z6 = np.fromiter(znaki,dtype='S1')
# print(z3)
# print(z4)
# print(z5)
# print(z6)

# a = np.arange(10)
# print(a)
# s = slice(2,7,2)
# print(a[s])
# s = range(2,7,2)
# print(a[s])
#
# print(a[2:7:2])
#
# print(a[1:])
# print(a[2:5])

# mat = np.arange(25)
# print(mat)
# mat = mat.reshape((5,5))
# print(mat)
# print(mat[1:])
# print(mat[: ,1:2])
# print(mat[:,4:5])
# print(mat[2:6, 1:3])
# print(mat[:, range(2,6,2)])
# print(mat[:, [2,4]])

# x = np.array([[0,1,2], [3,4,5], [6,7,8], [9,10,11]])
# print(x)
# rows = np.array([[0, 0], [3, 3]])
# cols = np.array([[0, 2], [0, 2]])
# y = x[rows,cols]
# print(y)



