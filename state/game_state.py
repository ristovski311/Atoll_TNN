#
# Funkcije za stanja
#

# mock-up stanje 
# prvo pristupamo stanju preko "indeksa" slova state[A]
# tako dobijamo listu polja koja su oznacena sa A, odozgo na dole
# nakon toga jos jednim indeksiranjem toga nekim brojem (broj ide od 1 pa do nekog broja)
# dobijemo konkretno polje, na primer state[A][1] je prvo polje na vrhu kolone A
# na taj nacin dobijamo mogucnost da imamo polje state[A][0] koje je obojeno inicijalno polje koje pripada nekom igracu.
# dodavanjem "LEFT" i "RIGHT" kolona mozemo da dodamo i one 2 samo obojene kolone skroz levo i skroz desno
# koje predstavljaju ostrvca igraca

### Mora da se razmisli jer ne krecu sve kolone od indeksa 1 ^^^
### slovo na polovini table ima indekse od 0, ali posle toga indeksi se smanjuju


# Ove liste sadrze tuple-ove tipa (stanje_polja,). Namerno ga ostavljamo da bude tuple ako u buducnosti moramo da dodamo
# novu informaciju u polje 
# Sva polja u levoj i desnoj koloni su tipa (RED_ili_GREEN, 0), dakle ili pripadaju crvenom ili zelenom igracu a duzina puta je 0 njima

game_state = {
    'LEFT': [()],
    'A': [()],
    'B': [],
    'C': [],
    'D': [],
    'E': [],
    'F': [],
    'G': [],
    'H': [],
    'I': [],
    'RIGHT': []
}

# Definisanje stanja TODO

    #Stanje 


# Funkcija za pravljenje inicijalnog stanja TODO

def create_initial_state():
    print("Kreiranje pocetnog stanja!")
    
# Funkcija za prikaz proizvoljnog stanja TODO    

def display_arbitrary_state():
    print("Prikaz proizvoljnog stanja")