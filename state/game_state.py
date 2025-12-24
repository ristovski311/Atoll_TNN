#
# Funkcije za stanja
#



# Definisanje stanja TODO

# Stanje - graf
# Kljucevi su tuple objekti sa koordinatama tog polja u tabli (A, 1) je na primer u koloni A prvo polje za igru
# Polja koja su hardcode ostrva su recimo (A, 0), (B, 0)... ali i cela LEFT i RIGHT kolona
# Od sredisnjeg slova (ako su slova od A do I, to je slovo E, pogledaj sliku na slajdovima) krece drugacije indeksiranje
# svako slovo posle sredisnjeg ima pocetni indeks za 1 veci od prethodnog
# pa tako F ima prvo polje (F, 2), G ima (G, 3) - ovo su polja na kojima korisnik ima pravo da satavi kamen
# a polja koja su hardcode ostrva su idalje na vrhu kolone (open, bolje se vidi sa slike) -  (F, 1), (G, 2) ... 

# Svaki kljuc ima tuple sa 2 stvari -> prva je stanje polja, GREEN RED ili None (None je slobodno)
# druga stvar je lista suseda tog polja, bice nam lakse za search kasnije, verovatno A*

# mockup:

# graph = {
#     ('A',1): ('RED', [('A', 0), ('A', 2), ('B', 1), ('B', 2), ('LEFT', 1)]),
#     ('A',2): (None, [('A', 1), ('A', 3), ('B', 2), ('B', 3), ('LEFT', 2)]),
#     ...
#     ('B', 1) : (None, [...])
# }

game_state = dict()

# Funkcija za pravljenje inicijalnog stanja TODO

def create_initial_state(board_size: int):
    # Ovo nam odredjuje broj kolona i broj "vrsta"
    board_diameter = 2 * board_size - 1
    column_letters = [chr(ord('A') + i) for i in range(board_diameter)]
    column_letters = ['LEFT'] + column_letters + ['RIGHT']
    game_state = {
        (let, num): (None, []) for let in column_letters for num in range(board_diameter)
    }
    return game_state
    
# Funkcija za prikaz proizvoljnog stanja TODO    

def display_arbitrary_state():
    print("Prikaz proizvoljnog stanja")