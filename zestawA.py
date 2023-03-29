import math

# # zad 1:
# try:
#     a=int(input("Podaj liczbe calkowita a: "))
# except ValueError:
#     print("podana wartosc musi byc liczba calkowita!")
# try:
#     b=int(input("Podaj liczbe calkowita b: "))
# except ValueError:
#     print("podana wartosc musi byc liczba calkowita!")
# try:
#     b=int(input("Podaj liczbe calkowita c: "))
# except ValueError:
#     print("podana wartosc musi byc liczba calkowita!")
#
# wynik = (a**2)+(a*b)+(b**2)
#
# plik = open("zadanie1.txt", 'a+')
# plik.write(str(wynik))
# plik.seek(0)
# for line in plik:
#     print(line, end='')
# plik.close()

# # zad 2:
#
# lista1=[x for x in range(0,11)]
# lista2=[x+2*3 for x in range(0,11)]
# print(lista1)
# print(lista2)
# def zad2(lista1, lista2):
#     lista3=[x for x in range(0,11)]
#     for x in range(0,11):
#         lista3[x] = lista1[x]+lista2[x]
#     return print(lista3)
#
# zad2(lista1, lista2)






# # zazd 4:
# a=5
# lista4=[3,9,2,1,int(a),6,8,4,12,-3]
#
# lista5 = [x for x in lista4 if x>a]
# print(lista5)

# zad 5:
wynik5 = pow((math.exp(3)+pow(math.cos(39),2)),1/3) + pow(2/7,3) + math.pi

print("%.2f" % wynik5)









