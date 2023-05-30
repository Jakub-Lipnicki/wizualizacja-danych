import matplotlib.pyplot as plt
import math
import numpy as np
import pandas as pd
import seaborn as sns




# plt.plot([1,3*3,math.sqrt(5),pow(7,2),21])
# plt.show()

x = np.array([1,2,3,4])
y = x**2
#
# plt.plot(x, y, 'ro-')
# plt.axis([0, 6, 0, 20])
# plt.show()
#
# plt.plot(x,y, 'r')
# plt.plot(x,y,'o')
# plt.axis([0, 6, 0, 20])
# plt.show()

x = np.arange(0, 5, 0.2)

# plt.plot(x, x, 'r--', x, x**2, 'bo', x, x**3, 'g^')
# plt.legend(labels=['liniowy', 'kwadratowy', 'szescienny'])
# plt.show()

# plt.plot(x, x, 'r--', label='liniowy')
# plt.plot(x, x**2, 'or--', label='kwadratowa')
# plt.plot(x, x**3, 'g^', label='szescienna')
# plt.legend()
# plt.show()


#wykres funkcji sinus na przedziale x<0,10> wartosci zmieniaja sie co 0.1
#
# x = np.arange(0, 10.1, 0.1)
# y = np.sin(x)
# plt.plot(x, y, 'b-', label='sinus')
# plt.xlabel('wartosci x')
# plt.ylabel('wartosci y')
# plt.legend()
# plt.title('wykres sinusa')
# plt.show()
#
# data = {'a': np.arange(50),
#         'c': np.random.randint(0, 50, 50),
#         'd': np.random.randn(50)
# }
# data['b'] = data['a'] + 10 * np.random.rand(50)
# data['d'] = np.abs(data['d']) * 100
#
# plt.scatter('a', 'b', c='c', s='d', data=data, cmap='plasma')
# plt.xlabel('klucz a')
# plt.ylabel('klucz b')
# plt.show()

x1 = np.arange(0, 5, 0.2)
x2 = np.arange(0, 5, 0.2)

y1 = np.sin(x1)
y2 = np.cos(x2)

# plt.subplot(4, 1, 1)
# plt.plot(x1, y1)
# plt.title('wykres sinx')
# plt.xlabel('x')
# plt.ylabel('sinx')
# plt.subplot(4, 1, 4)
# plt.plot(x2, y2, 'r')
# plt.title('wykres cosx')
# plt.xlabel('x')
# plt.ylabel('cosx')
# plt.subplots_adjust(hspace=0.5)
#
# plt.show()
#
# fig, axs = plt.subplots(3, 2)
#
# axs[0, 0].plot(x1, y1)
# axs[0, 0].set_title('sinus')
# axs[0, 0].set_xlabel('x')
# axs[0, 0].set_ylabel('y')
#
# axs[1, 1].plot(x2, y2)
# axs[1, 1].set_title('cosinus')
# axs[1, 1].set_xlabel('x')
# axs[1, 1].set_ylabel('y')
#
# axs[2, 0].plot(x1, y1, 'r')
# axs[2, 0].set_title('sinus')
# axs[2, 0].set_xlabel('x')
# axs[2, 0].set_ylabel('y')
#
# fig.delaxes(axs[0, 1])
# fig.delaxes(axs[1, 0])
# fig.delaxes(axs[2, 1])
#
# plt.show()

# data = {'kraj':['Belgia', 'Idie', 'Brazylia', 'Polska'],
#         'Stolica':['Bruksela', 'New Delhi', 'Brasilia', 'Warsaw'],
#         'Kontynent':['europa', 'azja', 'am.south', 'europa'],
#         'Populacja':[11190846, 1303171035, 207847584, 38675912]}
# df = pd.DataFrame(data)
# print(df)
# grupa = df.groupby('Kontynent')
# etykiety = list(grupa.groups.keys())
# wartosci = list(grupa.agg('Populacja').sum())
#
# plt.bar(x=etykiety, height=wartosci, color=['yellow', 'red', 'green'])
# plt.xlabel("etykiety")
# plt.ylabel("wartosci")
# plt.show()
#
# grupa = df.groupby('Kontynent').agg({'Populacja':['sum']})
# print(grupa)
# # grupa.plot(kind='bar', xlabel='KKontynenty', ylabel='Populacja', legend=True, rot=0, title='Populacja na kontynentach')
# # #zapisanie wyk do pliku
# wykres = grupa.plot.bar()
# wykres.set_ylabel('Populacja')
# wykres.set_xlabel('Kontynent')
# wykres.tick_params(axis='x', labelrotation=0)
# wykres.legend()
# wykres.set_title('jaki tatauht')
# # plt.savefig('wykres.png')
# plt.show()

#
# ts = pd.Series(np.random.randn((1000)))
# ts = ts.cumsum()
# ts.plot()
# plt.show()

# df = pd.read_csv('zamowienia.csv.csv', header=0, sep=';', decimal='.')
# printf(df)
# groupa = df.groupby('Imie i nazwisko').agg({'Wartość zamówienia': ['sum']})
# grupa.plot(kind='pie', subplots=True, autopct='%.2f%%', fontsize=20, figsize=(6, 6), colors=['red', 'green'])
#
# plt.legend(loc='lower right')
# plt.title('Tytul')
# plt.show()
#

#PROSTY WYKRES LINIOWY
# plt.plot([1,2,0,3,4,30])
# plt.ylabel('jakieś liczby')
# plt.show()

#przekazujemy dwa wektory wartości, najpierw dla wektora x,
#następnie dla wektora y
#dodatkowo mamy tutaj przekazywany parametr w postaci stringa,
#który określa styl wykresu
# plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro-')
# #tutaj określamy listę parametrów w postaci [xmin, xmax, ymin, ymax]
# plt.axis([0, 6, 0, 20])
# plt.show()
#
# #możemy też ustawić różne kolory dla poszczególnych elementów nakładając na siebie dwa wykresy
# plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'r')
# plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'o')
# plt.axis([0, 6, 0, 20])
# plt.show()
#
# #bazowy wektor wartości
# t = np.arange(0., 5., 0.2)
# #za pomocą pojedynczego wywołania funkcji plot() możemy
# #wygenerować wiele wykresów na jednym płótnie (ang. canvas)
# #każdorazowo podając niezbędne wartości: wartości dla osi x,
# #wartości dla osi y, styl wykresu, ...
# plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
# plt.legend(labels=['liniowa', 'kwadratowa', 'szescienna'])
# plt.show()
#
#
# x = np.linspace(0, 2, 100)
# #wykresy mogą być też dodawane do płótna definicja po definicji zamiast w pojedynczym wywołaniu funkcji
# #plot()
# #tutaj użyty został również parametr label, który
# #określa etykietę danego wykresu w legendzie
# plt.plot(x, x, label="liniowa")
# plt.plot(x, x**2, label="kwadratowa")
# plt.plot(x, x**3, label="sześcienna")
# #etykiety osi
# plt.xlabel('etykieta x')
# plt.ylabel("etykieta y")
# #tytuł wykresu
# plt.title("Prosty wykres")
# #włączamy pokazanie legendy
# plt.legend()
# plt.savefig('wykres matplot.png')
# plt.show()
# im1 = Image.open('wykres matplot.png')
# im1 = im1.convert('RGB')
# im1.save('nowy.jpg')

#zad1
# Na wykresie wyświetl wykres liniowy funkcji f(x) = 1/x dla x ϵ [1, 20]. Dodaj etykietę do linii wykresu i
# wyświetl legendę. Dodaj odpowiednie etykiety do osi wykresu (‘x’, ’f(x)’) oraz ustaw zakres osi na (0,
# 1) oraz (1, długość wektora x).
x = np.arange(1, 21, 1)
plt.plot(x, 1/x, label='f(x) = 1/x')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.axis([0, 20, 0, 1])
plt.legend()
plt.title('Wykres funkcji f(x) = 1/x dla x[1,20]')
plt.show()
# zad2
#zmodyfikuj wykres z zad 1 tak aby wygladal jak na zrzucie z ekranu
x = np.arange(1, 21, 1)
plt.plot(x, 1/x, 'g>:', label='f(x) = 1/x' )
plt.xlabel('x')
plt.ylabel('f(x)')
plt.axis([0, 20, 0, 1])
plt.legend()
plt.title('Wykres funkcji f(x) = 1/x dla x[1,20]')
plt.show()
# zad3
#Na jednym wykresie wygeneruj wykresy funkcji sin(x) oraz cos(x) dla x ϵ [0, 30] z krokiem 0.1.
# Dodaj etykiety i legendę do wykresu.
x = np.arange(0, 30, .1)
plt.plot(x, np.sin(x), 'b', label='sin(x)')
plt.plot(x, np.cos(x), 'r', label='cos(x)')
plt.xlabel('x')
plt.ylabel('sin(x) cos(x)')
plt.legend(loc='upper right')
plt.title('Wykres sin(x), cos(x)')
plt.show()
# zad4
#Korzystając ze zbioru danych Iris (https://archive.ics.uci.edu/ml/datasets/iris) wygeneruj wykres
# punktowy, gdzie wektor x to wartość ‘sepal length’ a y to ‘sepal width’, dodaj paletę kolorów c na
# przykładzie listingu 6 a parametr s niech będzie wartością absolutną z różnicy wartości
# poszczególnych elementów wektorów x oraz y.
df = pd.read_csv('iris.data', header=0, sep=',', decimal='.')
print(df)
# przygotowanie wektora kolorów
colors = np.random.randint(0, 50, len(df.index))
# przygotowanie wektora z rozmiarami 'kropek'
scale = np.abs(df['sepal length'] - df['sepal width'])
plt.scatter(df['sepal length'], df['sepal width'], c=colors, s=scale)
plt.xlabel('sepal length')
plt.ylabel('sepal width')
plt.show()
#zad5
#Korzystając z biblioteki pandas wczytaj zbiór danych z narodzinami dzieci przedstawiony w lekcji 8.
# Następnie na jednym płótnie wyświetl 3 wykresy (jeden wiersz i 3 kolumny). Dodaj do wykresów
# stosowne etykiety. Poustawiaj różne kolory dla wykresów.
# 1 wykres – wykres słupkowy przedstawiający ilość narodzonych dziewczynek i chłopców w całym
# okresie.
# 2 wykres – wykres liniowy, gdzie będą dwie linie, jedna dla ilości urodzonych kobiet, druga dla
# mężczyzn dla każdego roku z osobna. Czyli y to ilość narodzonych kobiet lub mężczyzn (dwie linie), x
# to rok.
# 3 wykres – wykres słupkowy przedstawiający sumę urodzonych dzieci w każdym roku
xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx, header=0)
print(df)
plt.subplot(1, 3, 1)
grouped = df.groupby('Plec')
etykiety = list(grouped.groups.keys())
wartosci = list(grouped.agg('Liczba').sum())
plt.bar(x=etykiety, height=wartosci, color=['green', 'red'])
plt.xlabel('Płeć')
plt.ylabel('Liczba narodzonych dzieci')
# wykres 2
plt.subplot(1, 3, 2)
x = df['Rok'].unique()
kobiety = df[(df.Plec == 'K')].groupby('Rok').agg({'Liczba':['sum']}).values
mezczyzni = df[(df.Plec == 'M')].groupby('Rok').agg({'Liczba':['sum']}).values
plt.plot(x, kobiety, label="Kobiety")
plt.plot(x, mezczyzni, label="Mężczyźni")
plt.xlabel('Rok')
#
# # wykres 3
plt.subplot(1, 3, 3)
x = df['Rok'].unique()
y = df.groupby('Rok').agg('Liczba').sum()
plt.bar(x, y)
plt.xlabel('Rok')
# wyświetlamy cały wykres
plt.subplots_adjust(wspace=0.85)
plt.show()


