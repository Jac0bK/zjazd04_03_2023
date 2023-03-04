from funkcja2 import *

licznik = 0
while True:
    wyplata = input('ile zarabiasz? ')
    try:
        wyplata = float(wyplata)
        break
    except ValueError:
        print('złe dane, podaj liczbe')
        licznik += 1
    if licznik == 3:
        print('wyplata 2000PLN')
        wyplata = 2000
        break


while True:
    liczba_dzieci = input('ile masz dzieci? ')
    try:
        liczba_dzieci = int(liczba_dzieci)
        break
    except ValueError:
        print('złe dane, podaj liczbe')

try:
    print('kasa na dziecko =', wyplata / liczba_dzieci)
except ZeroDivisionError:
    print('cala kasa dla ciebie')
