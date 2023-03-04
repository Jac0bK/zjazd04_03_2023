#program ktory sprawdzi czy dane slowo to palindrom
#program ktory dziala na liscie slow

slowo = input('Wpisz slowo ')

#liczba_iteracji = len(slowo)//2

#for i in range(liczba_iteracji):
#    if slowo[i] != slowo[-1 -1]
if slowo == slowo[::-1]:            #https:/www.w3schools.com/python/python
    print('TAK', 'palindrom')
else:
    print('Nie, nie palindrom')
