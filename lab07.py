import numpy as np
import pandas as pd

#df = pd.read_csv('australian.txt', header=None, sep=' ', )
#print(df)

#xlsx = pd.ExcelFile('Wynik.xlsx')
#df = pd.read_excel(xlsx)
#print(df)

#s = pd.Series([1,3,5,np.nan, 6,8])
#print(s)

s = pd.Series([10, 12, 8, 14], index=['a','b','c','d'])
#print(s)
#
data = {'Kraj': ['Belgia', 'Indie', 'Brazylia'],'Stolica': ['Bruksela', 'New Delhi', 'Brasilia'],'Populacja': [11190846, 1303171035, 207847528]}
df = pd.DataFrame(data)
print(df)
# print(df.dtypes)df = pd.read_csv('dane.csv', header=0, sep=";",decimal=',')print(df)df.to_csv('plik.csv', index=False)

# daty = pd.date_range('20210324', periods=5)
# print(daty)
#
# df = pd.DataFrame(np.random.randn(5,4), index=daty, columns=list('ABCD'))
# print(df)

# df = pd.read_csv('dane.csv', header=0, sep=";",decimal=',')
# print(df)
# df.to_csv('plik.csv', index=False)

# xlsx=pd.ExcelFile('dane.xlsx')
# df = pd.read_excel(xlsx, header=0)
# print(df)
# df.to_excel('wyniki.xlsx',sheet_name='arkuszpierwszy')
# print(s['c'])
# print(s.c)
#
# # pojedynczy elemenet ramki danych, tak jak przy cięciu tablic, oparte na indeksach
# print(df[0:1])
# print("")
# # kolumna po etykiecie
# print(df['Populacja'])
#
# # pobieranie pojedynczej wartości po indeksie wiersza i kolumny
# print(df.iloc[0, 0])
# # pobieranie wartości po indeksie wiersza i etykiecie kolumny
# print(df.loc[0, "Kraj"])
# print(df.at[0, "Kraj"])
#
# # podobnie jak wprzypadku serii można odwoływać się do kolumn jak do pól klasy
# # dodatkowo print jest wywoływany jak w pętli dla każdego elementu danej kolumny
# print('kraj: ' + df.Kraj)
#
# # Pandas posiada również funkcje pozwalające na losowe pobieranie elementów lub# w odniesieniu do procentowej wielkości całego zbioru
# #
# # jeden losowy element
# print(df.sample())
#
# #n losowych elementów
# print(df.sample(2))
# # ilość elementów procentowo, uwaga na zaokrąglenie
# print(df.sample(frac=0.5))


# zad 1
xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx, header=0)
print(df)

# zad 2
print(df[df.Liczba > 1000])
print('')
print(df[df.Imie == 'JAKUB'])
print('')
print(df.Liczba.sum())
print('')
grupa = df[df.Rok < 2006]
print(grupa.Liczba.sum())
grupa = df[df.Rok < 2006].groupby('Rok').agg({'Liczba': ['sum']})
print(grupa)
print('')
print('')
print("Chłopiec")
print(df[df['Plec'] == 'M'].groupby(['Imie']).agg({'Liczba': ['sum']}).sort_values(('Liczba', 'sum'),
                                                                                   ascending=False).iloc[0])
print("Dziewczynka")
print(df[df['Plec'] == 'K'].groupby(['Imie']).agg({'Liczba': ['sum']}).sort_values(('Liczba', 'sum'),
                                                                                   ascending=False).iloc[0])

print(df.sort_values('Liczba', ascending=False).groupby(['Rok', 'Plec']).nth(0))
# print(df.sort_values('Liczba', ascending=False).groupby(['Rok', 'Plec']).first())

new_df = df.sort_values('Liczba', ascending=False).groupby(['Rok', 'Plec'])
for index, group in enumerate(new_df, start=1):
    print(f"{index} {group[0]}")
    print(f" {group[1].iloc[0]['Imie']}", end='')
    print(f" {group[1].iloc[0]['Liczba']}")
print('')
#ZAD3
df = pd.read_csv('zamowienia.csv', header=0, sep=';', decimal='.')
print(df)
print(df['Sprzedawca'].unique())
print('')
print(df.sort_values('Utarg', ascending=False).head(5))
print('')
print(df.groupby('Sprzedawca').size())
print('')
print(df.groupby('Kraj').agg({'Utarg': ['sum']}))
print(df.groupby('Kraj').size())
print('')
print(df[(df['Kraj'] == 'Polska') & (df['Data zamowienia'] >= '2005-01-01') & (df['Data zamowienia'] <= '2005-12-31')].
      agg({'Utarg': ['sum']}))
print('')
print(df[df['Data zamowienia'].str[:4] == '2004'].agg({'Utarg': ['mean']}))
rok_2004 = df[((df[ 'Data zamowienia'] >= '2004-01-01') & (df['Data zamowienia'] <= '2004-12-31'))]
rok_2004.to_csv("zamowienia_2004.csv", index=False)

## print("Chłopiec")
## print(df[df['Plec'] == 'M'].groupby(['Imie']).agg({'Liczba': ['sum']}).sort_values(('Liczba', 'sum'),
##                                                                                    ascending=False).iloc[0])
## print("Dziewczynka")
## print(df[df['Plec'] == 'K'].groupby(['Imie']).agg({'Liczba': ['sum']}).sort_values(('Liczba', 'sum'),
#                                                                                    ascending=False).iloc[0])
# print(df[df['Liczba']>100])
#
# print(df[df['Imie']=='JAKUB'])
#
# print(df.loc[df['Rok'] == 2001, 'Liczba'].sum())
#
# a = df.loc[(df['Rok'] == 2002), 'Liczba'].sum()
# b = df.loc[(df['Rok'] == 2001), 'Liczba'].sum()
# print(a+b)
#
# print("Chlopcy: ",df.loc[(df['Plec'] == 'M'), 'Liczba'].sum())
# print("Dziewoje: ",df.loc[(df['Plec'] == 'K'), 'Liczba'].sum())
#
# print(df[df['Imie']=='JAKUB'])



















