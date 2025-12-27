from state.game_state import *
from config.game_config import *
from gameplay.game_moves import *
from gui.game_display import *
from auxilary.misc import *

state = create_initial_state(board_size=game_config["board_size"])
# display_graph(state)

arb = create_arbitrary_state([('A', 3), ('B', 5)], [('E', 3), ('I', 5)])
#display_graph(arb)

game_mode = choose_game_mode()

first_player_type = choose_first_player()

first_symbol = choose_first_symbol()

position = input_a_move(state)

draw(state)

