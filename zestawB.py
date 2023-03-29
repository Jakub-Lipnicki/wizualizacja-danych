import math





# # zad 2:
# lista1 = [2,3,1.2,4,2.32,1.23]
# lista2 = [x for x in lista1 if x != int(x)]
# print(lista1)
# print(lista2)

# # zad 3:
# lista3 = [2,1,3,5.5,13,12]
# print(lista3)
# suma=0
# for x in lista3:
#     suma = x + suma
# lista3.append(suma)
# print(lista3)

# # zad 4:
# wynik = pow(math.sin(56), 2)+ pow((pow(4,2)/25 + math.log(85,3)), 1/4)
# print(wynik)

# zad 5:
try:
    n1 = int(input("podaj calkowita liczbe n1: "))
except ValueError:
    print("podana wartosc musi byc liczbą!")
wynik = 0
for x in range (1,n1+1):
    wynik += x
print(wynik)
plik = open("zadanie5.txt", "a+")
plik.writelines(str(wynik))
plik.seek(0)
for line in plik:
    print(line)
plik.close()


