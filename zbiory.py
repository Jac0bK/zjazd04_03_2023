# załóżmy, że pesel ma 4 cyfry
# stwórzmy zbiór NFZ – ludzie, w bazie pacjentów NFZ
# stwórzmy zbiór chorzy_rok – ludzie chorzy w ostatnim roku
# stwórzmy zbiór chorzy_miesiac – ludzie chorzy w ostatnim miesiącu
# stwórzmy zbiór krzyki – wszystkich ludzi mieszkających na krzykach
# stwórzmy zbiór centrum – wszystkich ludzi mieszkających

NFZ = {1234, 3476, 4544, 3423, 3254, 8769, 5436, 2345, 6532, 1243, 6435, 1298, 6732, 7688, 7648, 2345, 2356}
chorzy_rok = set([1234, 3476, 4544, 3423, 3254, 8769, 5436])
chorzy_miesiac = {1234, 3476, 3098, 4544, 3423}
krzyki = {4544, 3423, 3254, 8769, 5436, 2345, 6532, 1243}
centrum = {7648, 2345, 2356, 3987, 1234, 3476, 3254}
zbior_pusty = set()

# intersection - czesc wspolna
# union - suma
#a.union(b)
# difference - roznica dwoch zbiorow
#a.difference(b)
'''''
# sprawdzmy ile osob chorowalo w ostatnim roku na krzykach
print('chorzy w ostatnim roku z krzykow to:', krzyki.intersection(chorzy_rok))
print('liczba =', len(krzyki.intersection(chorzy_rok)))

#ile osob mieszka w sumie w centrum i na krzykach
print(krzyki.union(centrum))
print('liczba =', len(krzyki.union(centrum)))


#sprawdzamy poprawnosc dancyh:
print('\nPoprawnosc danych')
#kazdy kto chorowal w ostatnim miesiacu, jednoczesnie chorowal w ostatnim roku

if len(chorzy_miesiac.difference(chorzy_rok)) == 0:
    print('OK')
else:
    print('problem', chorzy_miesiac.difference(chorzy_rok))

#nikt nie powinien mieszkac jednoczesnie w centrum i na krzykach
# - jesli tak trzba usunac
# zbior.remove(element)

if len(krzyki.intersection(centrum)) != 0:
    x = input('usunac z centrum (C), czy z krzykow (K) ?')
    duplikaty = krzyki.intersection(centrum)
    if x.lower() =='k':
       krzyki = krzyki.difference(duplikaty)

    elif x.lower() == 'c':
       for pesel in duplikaty:
           centrum.remove(pesel)
    else:
       print('zly wybor')
'''''
#kazdy chory,zdrowy, z krzykow, z centrum, powinien byc w bazie NFZ

wszyscy = chorzy_rok.union(chorzy_miesiac.union(krzyki.union(centrum)))

#print(wszyscy)

poza_NFZ = wszyscy.difference(NFZ)

if len(poza_NFZ) != 0:
    print(poza_NFZ)
    NFZ = NFZ.union(poza_NFZ)
print(NFZ)






#lista = [1,2,3,3,3,3,4,4,4,5] jak usunac duplikaty
#lista = list(set(lista))
#print(lista)

