#
# Konfiguracioni file, informacije o igri
#



game_config = {
    "board_size": 5, # Omoguciti da korisnik bira velicinu ovog parametra, 5/7/9 su mogucnosti 
    "computer_plays": False,
    "computer_plays_first": False, 
    "green_plays_first": True, #Zeleni igrac je X (Crni igrac u tekstu na slajdu), po default-u on igra prvi
}



#
# Funkcije za postavljanje konfiguracije igre
#


def choose_game_mode(game_mode_code):
    global game_config

    match game_mode_code:
        case "1":
            game_config["computer_plays"] = False
            return True
        case "2":
            game_config["computer_plays"] = True
            return True
        case _: 
            print("Neispravan izbor. Pokušajte ponovo.")
            return False
        

def choose_a_player(player_code):
    global game_config

    match player_code:
        case "H":
            game_config["computer_plays_first"] = False
            return True
        case "A":
            game_config["computer_plays_first"] = True
            return True
        case _:
            print("Neispravan izbor. Unesite H ili A.")
            return False


def choose_first_symbol(first_symbol):
    global game_config
    
    match first_symbol:
        case "X":
            game_config["green_plays_first"] = True
            return True
        case "O":
            game_config["green_plays_first"] = False
            return True
        case _:
            print("Neispravan izbor. Unesite X ili O.")
            return False


def choose_board_size(board_size):
    if board_size in ["5", "7", "9"]:
        game_config["board_size"] = int(board_size)
        return True
    else:
        print("Unesite dozvoljenu veličinu! 5, 7 ili 9.")
        return False

# Funkcija za odredjivanje covek vs covek ili covek vs racunar
def choose_game_mode_cli():
    global game_config
    
    while True:
        print("Izaberite režim igre:")
        print("1 - Čovek protiv Čoveka")
        print("2 - Čovek protiv Računara")
        choice = input("Vaš izbor (1 ili 2): ").strip()

        if choose_game_mode(choice):
            break
    
# Funkcija za postavljanje da li racunar igra prvi ili covek igra prvi ako je tip igre: covek vs racunar
def choose_first_player_cli():
    global game_config
    
    while True:
        choice = input("Ko igra prvi? (H = Human, A = AI): ").strip().upper()
        
        if choose_a_player(choice):
            break

# Funkcija za odredjivanje da li X ili O igra prvi (X - black tj green / O - white tj red, konfuzno i know...)
def choose_first_symbol_cli():
    """
    Omogućava izbor koji simbol ide prvi: X ili O
    """
    while True:
        choice = input("Koji simbol igra prvi? (X/O): ").strip().upper()
        
        if choose_first_symbol(choice):
            break
    
# Funkcija za postavljanje velicine table (dozvoljeno je samo 5/7/9)
def choose_board_size_cli():
    global game_config
    
    while True:
        choice = input("Izaberite velicinu table? (5/7/9): ").strip().upper()
        
        if choose_board_size(choice):
            break