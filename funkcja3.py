from funkcja2 import *


while True:
    wyplata = input('ile zarabiasz? ')
    try:
        wyplata = float(wyplata)
        break
    except ValueError:
        print('złe dane, podaj liczbe')

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
