import datetime


def dodaj_date(func):
    def inner():
        teraz = datetime.datetime.now()
        print('aktualnie mamy', teraz.strftime('%H:%M:%S'))
        print('dodaje date')
        func()
    return inner()

@dodaj_date
def przywitanie():
    print('hejka!')

przywitanie

