import math

#zadanie 1:
print(math.exp(10))

print(math.pow(math.log(5+math.pow(math.sin(8),2)),1.0/6.0))

print(math.floor(3.15))

print(math.ceil(4.80))

#zadanie 2:
imie="JAKUB "
nazwisko="LIPNICKI"

print(imie.capitalize() + nazwisko.capitalize())

#zadanie 3:
tekst="la la lea la la la la"
print(tekst.count("la"))

# zadanie 4:
p="Jakub"
print(p[1], p[4])

#zadanie 5:
a1="zmienna/ testowa"
print(a1.split("/ ")[0])

#zadanie 6:
j="string"
k=2.4
l=0xff
print(j)
print(k)
print(l)

#zadanie 7:
list=['koszykowka', 'pilkanozna']
list.reverse()
print(list)
list.append('siatkowka')
print(list)

#zadanie 8:
slownik={'szk':'szok', 'ndw':'niedowierzanie', 'skn':'skandal'}
print(slownik['szk'])

#zadanie 9:
gry_slownik={'rpg':'witcher', 'mmo':'league', 'adventure':'uncharted'}
print(gry_slownik['rpg'])

print(len(gry_slownik))

#zadanie 10:
zdanie=input("Podaj jakies zdanie")
print(zdanie.count('a'))

#zadanie 11:
a=3
b=3
c=3

if (a>b) & (a>c):
    print("Liczba:", a,"jest najwieszka")
elif (b>a) & (b>c):
    print("Liczba:", b,"jest najwieskza")
elif (c>a) & (c>b):
    print("Liczba:", c,"jest najwieksza")
else:
    print("Liczby sa rowne")

#zadanie 12:
liczby=[2,5.4,5,5.5]
for x in liczby:
    print(pow(x,2))

#zadanie 13:
i=0
lista13=[]
while(i<10):
    a13=int(input("Podaj liczbe: "))
    if a13%2==0:
        lista13.append(a13)
    i+=1
print(lista13)









