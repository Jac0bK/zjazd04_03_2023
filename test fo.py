napis = 'Kamil ma psa'
lista_zwierzat = ['pies', 'drugi pies', 'tu tez pies']

print(napis[2:6])
print(lista_zwierzat[2])
print(lista_zwierzat[2][3:7])
#slicing [2] [3:7]
print(lista_zwierzat[2][-3])

#od do, co ile (20, 4, -3)
for i in range(20, 4, -3):
    print(i)

for i in range(4):          # i jest iteratorem, mozemy go uzyc tak jak chcemy
    print('okrazenie' ,i+1, 'litera' ,i+4, 'to' , napis[i+3], '\n')

for litera in napis:   #petla po strinug (napis0
    print(litera)
for zwierze in lista_zwierzat:    #petla po liscie
    print(zwierze)
