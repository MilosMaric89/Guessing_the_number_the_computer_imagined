import random

class Igrac:
    broj_poena = 0

    def __init__(self, ime):
        self.ime = ime

    def dodaj_poen(self):
        self.broj_poena+=1

    def prikaz_poena(self):
        if self.broj_poena in [1,21,31,41,51,61,71,81,91,101]:
            print(f"Igrac {self.ime} ima {self.broj_poena} poen.")
        else:
            print(f"Igrac {self.ime} ima {self.broj_poena} poena.")

def broj_pokusaja(x):
    if x>2:
        print(f"Ostalo je jos {x-1} pokusaja.")
    elif x==2:
        print(f"Ostalo je jos {x-1} pokusaj.")

def provera():
    while True:
        x = input("Unesi ceo broj iz opsega od 1 do 20: ")
        if not x.isdecimal():
            print("Nisi uneo broj. Pokusaj ponovo. ")
            continue
        elif int(x) <= 0 or int(x) > 20:
            print("Uneo si broj koji ne pripada opsegu. Pokusaj ponovo.")
            continue
        else:
            return int(x)

ime = input("Unesi svoje ime: ")
igrac = Igrac(ime)

print("--------------------------")

while True:
    broj = random.randint(1,20)
    for i in range(5, 0, -1):
        unos = provera()

        if unos == broj:
            print("Bravo! Pogodio si broj.")
            igrac.dodaj_poen()
            break
        elif unos<broj:
            print("Uneo si broj koji je manji od zamisljenog broja.")
            broj_pokusaja(i)
        elif unos>broj:
            print("Uneo si broj koji je veci od zamisljenog broja.")
            broj_pokusaja(i)

    print(f"Racunar je zamislio broj {broj}.")
    igrac.prikaz_poena()
    pitanje = input("Da li zelis ponovo da igras? 'da' za nastavak, 'ne' za izlaz iz igrice:").lower()

    while pitanje not in ("da", "ne"):
        pitanje = input("Uneo si pogresno slovo, pokusaj ponovo: ")

    if pitanje == "ne":
        break

