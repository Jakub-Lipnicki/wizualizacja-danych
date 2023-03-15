import random

# #zadanie 1:
# a=[1-x for x in range (1,10)]
# print(a)
# b=[4**i for i in range(8)]
# print(b)
# c=[x for x in b if x % 2 ==0]
# print(c)

# #zadanie 2:
# lista1=[]
# for i in range(10):
#     lista1.append(random.randint(1,100))
# print(lista1)
# listaparz=[j for j in lista1 if j % 2 ==0]
# print(listaparz)

# #zadanie 3:
# produkty={'jajka':'sztuka', 'mleko':'karton', 'sok':'butelka', 'baton':'sztuka'}
# print(produkty)
# onlySztuki=[i for i in produkty if produkty[i] == 'sztuka']
# print(onlySztuki)

# #zadanie 4:
# a4=3
# b4=4
# c4=5
# def czyTrukjkat(a4, b4, c4):
#     if(a4**2+b4**2==c4**2) or (b4**2+c4**2==a4**2) or (c4**2+a4**2==b4**2) :
#         return "moze byc"
#     else:
#         return 0
# print(czyTrukjkat(a4,b4,c4))

# #zadanie 5:
# def poleTrapezu(a5=4,b5=1,h5=3):
#     return ((a5+b5)*h5)/2
# print(poleTrapezu())

# #zadanie 6:
# #a=wartosc poczatkowa b=wielkosc ile=ile elementow ma mnozyc
# def iloczynCiagu(a6=1,b6=4,ile=10):
#     wartPocz = a6
#     wynik = 1
#     for a6 in range(0,ile):
#         wynik = wartPocz*(wartPocz+b6)
#         wartPocz += b6
#     return wynik
#
# print(iloczynCiagu())

# #zadanie 7:



# #zadanie 8:
# listaZak={'mleko':'3.20', 'chleb':'3.1', 'karma':'9.99', 'maslo':'4'}
# def listaZakupow(** listaZak):
#     print(listaZak['mleko'])
#
# listaZakupow(listaZak)
