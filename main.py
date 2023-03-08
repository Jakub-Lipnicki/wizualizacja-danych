a='napis'
print(a)
print(type(a))
b=5
print(a+str(b))

c=5
d=5.3

print(c, d)

e=c+d
print(e)

f = 2+3j
print(f)
print(type(f))

print(c-d)
print(c//d)
print(c%d)
print(c**d)
print(c+2)

c+=2
print(c)

#dodanie elementu do listy na danej pozycji
#usuniecie lementu z danej pozycji
#usuniecie elementu o danej wartosci
#dodac sekwencje do listy
#odwrocic liste
#posortowac elementy w lisie

listy=['2',3,5,6.5,[2,3,4]]
print(listy)
#1
listy.insert(0,5)
print(listy)
#2
listy.pop(0)
print(listy)
#3
listy.remove('2')
print(listy)
#4
test=[21,34,12]
listy.extend(test)
print(listy)
#5
listy.reverse()
print(listy)
#6
lista=[5,3,6,4,2]
lista.sort()
print(lista)

slownik = {1: 'a', 2: 2, 3:'klucz' }
print(slownik)
print(slownik[3])
slownik['nowy']='wartosc'
print(slownik)

slownik.pop(2)
print(slownik)

del slownik[3]
print(slownik)

print(slownik.keys())
print(slownik.values())



