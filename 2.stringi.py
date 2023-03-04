nazwa ='Jakub Filip Kostanski'
nazwa_ze_zmiana = nazwa.replace('i', 'DUZE_I',1) #co na co zamienia, ile razy
print(nazwa_ze_zmiana)

print(nazwa.replace(' ','')) #zmien spacje na nic
print(nazwa.replace(' ','\n')) #zmien spacje na \n MOJ PRZYKLAD

nazwa_podzielona = nazwa.split()    #zmiana na liste po spacji
print(nazwa_podzielona)
for slowo in nazwa_podzielona:
    print(slowo)


