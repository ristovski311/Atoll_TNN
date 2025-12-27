#
# Funkcije za poteze
#



# Funkcija za ispravnost unosa poteza (slobodno dodati dodatne f-je ako su potrebne) TODO
def is_move_valid(game_state,position):
    if position not in game_state:
        return False

    # 2. da li je slobodno
    if game_state[position][0] is not None:
        return False

    return True
    

# Funkcija za unos poteza TODO
def input_a_move(game_state):
    while True:
        user_input = input("Unesi potez (npr. C 3): ").strip().upper()

        try:
            col, row = user_input.split()
            row = int(row)
            position = (col, row)
        except ValueError:
            print("Neispravan format.")
            continue

        if is_move_valid(game_state, position):
            return position
        else:
            print("Potez nije dozvoljen. Polje ne postoji ili je zauzeto.")

def choose_game_mode():
    while True:
        print("Izaberite režim igre:")
        print("1 - Čovek protiv Čoveka")
        print("2 - Čovek protiv Računara")
        choice = input("Vaš izbor (1 ili 2): ").strip()

        if choice == "1":
            return "HUMAN_HUMAN"
        elif choice == "2":
            return "HUMAN_AI"
        else:
            print("Neispravan izbor. Pokušajte ponovo.")


def choose_first_player():
    while True:
        choice = input("Ko igra prvi? (H = Human, A = AI): ").strip().upper()
        if choice == "H":
            return "HUMAN"
        elif choice == "A":
            return "AI"
        else:
            print("Neispravan izbor. Unesite H ili A.")

def choose_first_symbol():
    """
    Omogućava izbor koji simbol ide prvi: X ili O
    """
    while True:
        choice = input("Koji simbol igra prvi? (X/O): ").strip().upper()
        if choice in ["X", "O"]:
            return choice
        else:
            print("Neispravan izbor. Unesite X ili O.")


### !!! 
# Nije potrebno praviti funkcije za odigravanje poteza.
# Unos poteza i odigravanje je razlicita stvar i guess?
# To je deo faze 2 !!!
