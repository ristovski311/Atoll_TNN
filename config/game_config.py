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



# Funkcija za odredjivanje covek vs covek ili covek vs racunar TODO

def set_computer_as_player():
    print("Postavlja da racunar igra")
    
# Funkcija za postavljanje da li racunar igra prvi ili covek igra prvi ako je tip igre: covek vs racunar TODO

def set_computer_turn():
    print("Postavlja da li racunar igra prvi ili drugi")
    
# Funkcija za odredjivanje da li X ili O igra prvi (X - black tj green / O - white tj red, konfuzno i know...) TODO

def set_green_turn():
    print("Postavlja da li green tj X igra prvi ili drugi")
    
# Funkcija za postavljanje velicine table (dozvoljeno je samo 5/7/9) TODO

def set_table_size():
    print("Postavlja velicinu table za igru")