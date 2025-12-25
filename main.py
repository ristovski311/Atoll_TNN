from state.game_state import *
from config.game_config import *
from gameplay.game_moves import *
from gui.game_display import *
from auxilary.misc import *

state = create_initial_state(board_size=game_config["board_size"])
# display_graph(state)

arb = create_arbitrary_state([('A', 3), ('B', 5)], [('E', 3), ('I', 5)])
#display_graph(arb)
