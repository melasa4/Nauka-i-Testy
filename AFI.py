import string                   # Import biblioteki

                                # deklaracja słowników
lista = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8,
         'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16,
         'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24,
         'Z': 25}

listaOdw = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I',
         9: 'J', 10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q',
         17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y',
         25: 'Z'}

                                # wprowadzenie tekstu jawnego z jednoczesnym podniesieniem znakow do wielkich liter
TJ = input("Podaj tekst jawny ktory poddamy kodowaniu szyfrem afinicznym(bez polskich znaków):\n").upper()

                                # wprowadzenie zmiennych stalych szyfrowania y = a * x + b

a = int(input("Podaj stala licznbe do kodowania a:"))
b = int(input("podaj stala liczne do kodowania b:"))


                                # usuwanie wszystkich inncyh znakow takich jak spacje, przecinki i cyfry
TR = ""                        # deklaracja zmiennej tekstowej bez znaków innych niż litery
for k in TJ:
    if k in string.ascii_letters:
        TR += k
#print(TR)                      # sprawdzenie poprawnosci wykonania polecenie usunięcia innych znakow niz litera

m = len(TR)                    # deklaracja zmiennej potrzebnej do obliczen
print('ilość znakow w ciagu tekstu jawnego:',m)

                                # Obliczenie Indeksu Koodyscencji suma iloczynów podzielona przez iloczyn wszystkich liter w tekscie




TJB = ""                         #deklaracja zmiennej tekstu tajnego

i = 0                            #ustawienia 0 przy rozpoczeciu odliczania
                                 # wyciągnięcie liczby zamiast tekstu i wykonanie operacji matematycznej z kodowaniem
while i < m:
    if TR[i] in lista.keys():    # pobiesz kolejna litere ze slowa Tekstu jawnego
        x = lista.get(TR[i])     # przypisz do litery liczbe podana w slowniku
        y = a * x + b            # operacja szyfrowania
        y = y % 26               # operacja modulo 26
        # print(x,y)              # sprawdzenie poprawnie przeprowadzonych obliczen
        q = listaOdw.get(y)      # przypisanie szyfru do litery
        TJB += q                 # utowrzenie ciagu znakow tekstu tajnego
        i += 1
    else:
        print("Nie ma takiego numeru")

print("Tekst Tajny:", TJB)

IC = (TJB.count("A")*(TJB.count("A")-1)+TJB.count("B")*(TJB.count("B")-1)+TJB.count("C")*(TJB.count("C")-1)+TJB.count("D")*(TJB.count("D")-1)+TJB.count("E")*(TJB.count("E")-1)+
      TJB.count("F")*(TJB.count("F")-1)+TJB.count("G")*(TJB.count("G")-1)+TJB.count("H")*(TJB.count("H")-1)+TJB.count("I")*(TJB.count("I")-1)+TJB.count("J")*(TJB.count("J")-1)+
      TJB.count("K")*(TJB.count("K")-1)+TJB.count("L")*(TJB.count("L")-1)+TJB.count("M")*(TJB.count("M")-1)+TJB.count("N")*(TJB.count("N")-1)+TJB.count("O")*(TJB.count("O")-1)+
      TJB.count("P")*(TJB.count("P")-1)+TJB.count("Q")*(TJB.count("Q")-1)+TJB.count("R")*(TJB.count("R")-1)+TJB.count("S")*(TJB.count("S")-1)+TJB.count("T")*(TJB.count("T")-1)+
      TJB.count("U")*(TJB.count("U")-1)+TJB.count("V")*(TJB.count("V")-1)+TJB.count("W")*(TJB.count("W")-1)+TJB.count("X")*(TJB.count("X")-1)+TJB.count("Y")*(TJB.count("Y")-1)+
      TJB.count("Z")*(TJB.count("Z")-1))/(m*(m-1))

print(IC)                       #wynik obliczinego Indeksu kodestencji





