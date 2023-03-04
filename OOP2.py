class Czlowiek:
    def __init__(self, imie, nazwisko, wiek):
        self.imie = imie        #po lewej strony nazwy dla klasy
        self.nazwisko = nazwisko
        self.wiek = wiek
        self.wyplata = 5000
        self.ID = 12345

    def zwieksz_wyplate(self, o_ile):
        self.wyplata += o_ile

    def zmien_id(self, nowe_id):
        print('sprawdzam dostepnosc nowego ID')
        self.ID = nowe_id

class Data:
    def __init__(self):
        self.dzien = 1
        self.miesiac = 1
        self.rok = 1990
        self.dzien_tygodnia = 'monday'

    def dodaj_dni(self, ile):
        pass

czlowiek1 = Czlowiek('Jakub','Kostanski','31')
print(czlowiek1.nazwisko)
print(czlowiek1.ID)
czlowiek1.zmien_id(987)
print(czlowiek1.ID)


