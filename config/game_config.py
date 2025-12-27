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



# Funkcija za odredjivanje covek vs covek ili covek vs racunar
def choose_game_mode():
    global game_config
    
    while True:
        print("Izaberite režim igre:")
        print("1 - Čovek protiv Čoveka")
        print("2 - Čovek protiv Računara")
        choice = input("Vaš izbor (1 ili 2): ").strip()

        if choice == "1":
            game_config["computer_plays"] = False
            break
        elif choice == "2":
            game_config["computer_plays"] = True
            break
        else:
            print("Neispravan izbor. Pokušajte ponovo.")
    
# Funkcija za postavljanje da li racunar igra prvi ili covek igra prvi ako je tip igre: covek vs racunar
def choose_first_player():
    global game_config
    
    while True:
        choice = input("Ko igra prvi? (H = Human, A = AI): ").strip().upper()
        if choice == "H":
            game_config["computer_plays_first"] = False
            break
        elif choice == "A":
            game_config["computer_plays_first"] = True
            break
        else:
            print("Neispravan izbor. Unesite H ili A.")

# Funkcija za odredjivanje da li X ili O igra prvi (X - black tj green / O - white tj red, konfuzno i know...)
def choose_first_symbol():
    """
    Omogućava izbor koji simbol ide prvi: X ili O
    """
    while True:
        choice = input("Koji simbol igra prvi? (X/O): ").strip().upper()
        if choice == "X":
            game_config["green_plays_first"] = True
            break
        elif choice == "O":
            game_config["green_plays_first"] = False
            break
        else:
            print("Neispravan izbor. Unesite X ili O.")
    
# Funkcija za postavljanje velicine table (dozvoljeno je samo 5/7/9)
def choose_board_size():
    global game_config
    
    while True:
        choice = input("Izaberite velicinu table? (5/7/9): ").strip().upper()
        if choice in ["5", "7", "9"]:
            game_config["board_size"] = int(choice)
            break
        else:
            print("Unesite dozvoljenu veličinu! 5, 7 ili 9:")