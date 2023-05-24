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



