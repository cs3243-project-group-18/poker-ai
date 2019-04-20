from pypokerengine.api.game import setup_config, start_poker
from raise_player import Group18Player
from randomplayer import RandomPlayer
# from honest_player import DumbHonestPlayer
# from honest_player import SmartHonestPlayer
# from reinforced_player import RLPlayer
# from self_player import SelfPlayer

config = setup_config(max_round=10, initial_stack=10000, small_blind_amount=10)

config.register_player(name="f1", algorithm=RandomPlayer())
config.register_player(name="FT2", algorithm=Group18Player())

game_result = start_poker(config, verbose=1)
