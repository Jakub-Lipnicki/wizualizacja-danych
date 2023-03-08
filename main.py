#a='napis'
#print(a)
#print(type(a))
#b=5
#print(a+str(b))

#c=5
#d=5.3
#print(c, d)

#e=c+d
#print(e)

#f = 2+3j
#print(f)
#print(type(f))

#print(c-d)
#print(c//d)
#print(c%d)
#print(c**d)
#print(c+2)

#c+=2
#print(c)

#dodanie elementu do listy na danej pozycji
#usuniecie lementu z danej pozycji
#usuniecie elementu o danej wartosci
#dodac sekwencje do listy
#odwrocic liste
#posortowac elementy w lisie

#listy=['2',3,5,6.5,[2,3,4]]
#print(listy)
#1
#listy.insert(0,5)
#print(listy)
#2
#listy.pop(0)
#print(listy)
#3
#listy.remove('2')
#print(listy)
#4
#test=[21,34,12]

#listy.extend(test)
#print(listy)
#5
#listy.reverse()
#print(listy)
#6
#lista=[5,3,6,4,2]
#lista.sort()
#print(lista)

#slownik = {1: 'a', 2: 2, 3:'klucz' }
#print(slownik)
#print(slownik[3])
#slownik['nowy']='wartosc'
#print(slownik)

#slownik.pop(2)
#print(slownik)

#del slownik[3]
#print(slownik)


#print(slownik.keys())
#print(slownik.values())

#print('a = %(zm)d' %{'zm': 12})
#print('a = {}'.format(12))

#napis=input("wpr liczbe: ")
#print(napis)
#print(type(napis))

#napis=int(napis)
#print(type(napis))

#instrukcja warunkowa

#if warunek:
    # instrukcja
#elif warunek:
    # insturkcja
#else:
    #ins

#a = input("podaj a: ")
#b = input("podaj b: ")

#a=int(a)
#b=int(b)
#c = int(input("podaj c: "))
#d = int(input("podaj d: "))

#if (a>b) & (c>d):
#    print("a wieksze od b i c wieksze od d")
#else:
#    print("a nie jest wieskze od b lub c nie jest wiekseze od d")

#if(c==d):
#    print("rowne")
#else:
#    print("nierowne")

# for element in sekwencja:
    #instrukcje
# else:
    #insturkcje po petli:

#for x in range(1,6,1):
#    print(x)
#else:
#    print("koniec petli for")

list =[3,5,2,5,3,7]

#for x in list:
#    print(x)
#else:
#    print("sposob 1")

#for x in range(0,len(list), 1):
#    print(list[x])
#else:
 #   print("drugi sposob")

# petla while
# while warunek :
#   instukacje
# else:
#   insturkcje

#licznik=0
#while licznik !=len(list):
#   print(list[licznik])
#    licznik+=1

#liczby=[2,5,6,7,3,4]

#a = int(input("podaj a: "))
#licznik = 0

#while licznik != len(liczby):
#    if liczby[licznik]-a == 0:
#        print("prawda")
#        licznik += 1
#    else:
#        licznik+=1

#petla z liczbami ktora bedzie zawierala jeeden element kilka razy 4 elementy o wartosci '2' uzywajac petli while usunac wszystkie lementy z listy rowne 2

list=[1,2,2,2,2]
licznik=0
while licznik != list.count(2):
    print(list)
    list.remove(2)
else:
    print(list)
