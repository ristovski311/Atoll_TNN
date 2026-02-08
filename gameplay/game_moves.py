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
    new_state = current_state.copy()
    new_state[move] = [player, current_state[move][1]]
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

# Koristimo memoizaciju za poboljsanje performansi
memo = {}

# Pomocna funkcija koja odredjuje koliko protivnikovih polja je oko trenutnog polja
def get_move_score(state, move, opponent_color):
    neighbors = state[move][1]
    score = 0
    for n in neighbors:
        if state[n][0] == opponent_color:
            score += 1
    return score

def max_value(state, depth, current_player, maximizing_player, alpha, beta):
    # Memoizacija
    state_key = frozenset((coords, info[0]) for coords, info in state.items())
    if state_key in memo:
        cached_depth, cached_value, cached_move = memo[state_key]
        if cached_depth >= depth:
            return cached_move, cached_value

    # Uslovi za kraj
    winner = game_state.check_win_condition(state)
    if winner == maximizing_player:
        return (None, 10000 + depth)
    elif winner is not None:
        return (None, -10000 - depth)
    
    if depth == 0:
        return (None, game_state.calculate_heur(maximizing_player, state))

    moves = [coords for coords, info in state.items() if info[0] is None]
    if not moves:
        return (None, game_state.calculate_heur(maximizing_player, state))

    # Sortiramo tako da potezi sa više protivnika u okruženju budu prvi
    opponent = "RED" if current_player == "GREEN" else "GREEN"
    moves.sort(key=lambda m: get_move_score(state, m, opponent), reverse=True)

    best_move = None
    best_value = float('-inf')
    next_player = "RED" if current_player == "GREEN" else "GREEN"

    for move in moves:
        state[move][0] = current_player
        
        _, value = min_value(state, depth - 1, next_player, maximizing_player, alpha, beta)
        
        state[move][0] = None
        
        if value > best_value:
            best_value = value
            best_move = move
        
        alpha = max(alpha, best_value)
        if beta <= alpha:
            break
    
    memo[state_key] = (depth, best_value, best_move)
    return (best_move, best_value)


def min_value(state, depth, current_player, maximizing_player, alpha, beta):
    state_key = frozenset((coords, info[0]) for coords, info in state.items())
    if state_key in memo:
        cached_depth, cached_value, cached_move = memo[state_key]
        if cached_depth >= depth:
            return cached_move, cached_value

    winner = game_state.check_win_condition(state)
    if winner == maximizing_player:
        return (None, 10000 + depth)
    elif winner is not None:
        return (None, -10000 - depth)
    
    if depth == 0:
        return (None, game_state.calculate_heur(maximizing_player, state))

    moves = [coords for coords, info in state.items() if info[0] is None]
    if not moves:
        return (None, game_state.calculate_heur(maximizing_player, state))

    opponent = "RED" if current_player == "GREEN" else "GREEN"
    moves.sort(key=lambda m: get_move_score(state, m, opponent), reverse=True)

    best_move = None
    best_value = float('inf')
    next_player = "RED" if current_player == "GREEN" else "GREEN"

    for move in moves:
        state[move][0] = current_player
        _, value = max_value(state, depth - 1, next_player, maximizing_player, alpha, beta)
        state[move][0] = None
        
        if value < best_value:
            best_value = value
            best_move = move
        
        beta = min(beta, best_value)
        if beta <= alpha:
            break
            
    memo[state_key] = (depth, best_value, best_move)
    return (best_move, best_value)

def minimax(state, depth, current_player, maximizing_player):
    alpha = float('-inf')
    beta = float('inf')
    
    is_maximizing = (current_player == maximizing_player)
    
    if is_maximizing:
        return max_value(state, depth, current_player, maximizing_player, alpha, beta)
    else:
        return min_value(state, depth, current_player, maximizing_player, alpha, beta)
    
  

