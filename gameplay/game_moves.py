#
# Funkcije za poteze
#

import copy
from state import game_state
from config import game_config 

# Funkcija za ispravnost unosa poteza
def is_move_valid(game_state,position):
    if position not in game_state:
        return False

    # 2. da li je slobodno
    if game_state[position][0] is not None:
        return False

    return True
    

# Funkcija za unos poteza - ova f-ja se koristi u CLI, ne koristimo je u GUI
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

# Funkcija za postavljanje polja
def set_a_cell(state, position, current_player):
    state[position][0] = current_player
    return state

# Vraca novo stanje koje je nastalo odigravanjem poteza
def get_next_state(current_state, move, player):
    new_state = copy.deepcopy(current_state)

    if move in new_state:
        new_state[move][0] = player

    return new_state

# Vraca listu koordinata svih slobodnih polja
def get_all_possible_moves(current_state):
    return [coords for coords, info in current_state.items() if info[0] is None]

# Generise listu svih mogucih stanja za sledeci potez
def get_all_possible_states(current_state, player):
    moves = get_all_possible_moves(current_state)
    return [get_next_state(current_state, m, player) for m in moves]


#
# Faza 3 - MINMAX
#


def max_value(state, depth, current_player, maximizing_player, alpha, beta):
    #Max nivo
    
    # Provera kraja
    winner = game_state.check_win_condition(state, game_config.game_config["board_size"])
    if winner == maximizing_player:
        return (None, 10000)
    elif winner is not None:
        return (None, -10000)
    
    # Provera dubine
    if depth == 0:
        return (None, game_state.calculate_heur(maximizing_player, state))
    
    # Generiši stanja
    moves = get_all_possible_moves(state)
    
    if not moves:
        return (None, game_state.calculate_heur(maximizing_player, state))
    
    best_move = None
    best_value = float('-inf')
    next_player = 'RED' if current_player == 'GREEN' else 'GREEN'
    
    for move in moves:
        new_state = get_next_state(state, move, current_player)
        _, value = min_value(new_state, depth - 1, next_player, maximizing_player, alpha, beta)
        
        if value > best_value:
            best_value = value
            best_move = move
        
        alpha = max(alpha, best_value)
        if beta <= alpha:
            break  # Odsecanje
    
    return (best_move, best_value)


def min_value(state, depth, current_player, maximizing_player, alpha, beta):
    #Min nivo
    
    # Provera kraja
    winner = game_state.check_win_condition(state, game_config.game_config["board_size"])
    if winner == maximizing_player:
        return (None, 10000)
    elif winner is not None:
        return (None, -10000)
    
    # Provera dubine
    if depth == 0:
        return (None, game_state.calculate_heur(maximizing_player, state))
    
    # Generiši stanja
    moves = get_all_possible_moves(state)
    
    if not moves:
        return (None, game_state.calculate_heur(maximizing_player, state))
    
    best_move = None
    best_value = float('inf')
    next_player = 'RED' if current_player == 'GREEN' else 'GREEN'
    
    for move in moves:
        new_state = get_next_state(state, move, current_player)
        _, value = max_value(new_state, depth - 1, next_player, maximizing_player, alpha, beta)
        
        if value < best_value:
            best_value = value
            best_move = move
        
        beta = min(beta, best_value)
        if beta <= alpha:
            break  # Odsecanje
    
    return (best_move, best_value)


def minimax(state, depth, current_player, maximizing_player):
    alpha = float('-inf')
    beta = float('inf')
    
    is_maximizing = (current_player == maximizing_player)
    
    if is_maximizing:
        return max_value(state, depth, current_player, maximizing_player, alpha, beta)
    else:
        return min_value(state, depth, current_player, maximizing_player, alpha, beta)