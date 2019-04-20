from pypokerengine.players import BasePokerPlayer
import random as rand
import pprint

class RandomPlayer(BasePokerPlayer):

    # def __init__(self):
    #   BasePokerPlayer.__init__(self)
    #   self.round_count = 0

    def declare_action(self, valid_actions, hole_card, round_state):
        # print("Random Player")
        # print("Valid Actions : ")
        # pprint.pprint(valid_actions)
        r = rand.random()
        if r <= 0.5:
            call_action_info = valid_actions[1]
        elif r<= 0.9 and len(valid_actions ) == 3:
            call_action_info = valid_actions[2]
        else:
            call_action_info = valid_actions[0]
        action = call_action_info["action"]
        print("Taken Actions : ")
        pprint.pprint(action)
        return action  # action returned here is sent to the poker engine

    def receive_game_start_message(self, game_info):
        # print("\n\n")
        # pprint.pprint(game_info)
        # print("---------------------------------------------------------------------")
        pass

    def receive_round_start_message(self, round_count, hole_card, seats):
        # print("My ID : "+self.uuid+", round count : "+str(round_count)+", hole card : "+str(hole_card))
        # pprint.pprint(seats)
        # print("-------------------------------")
        pass

    def receive_street_start_message(self, street, round_state):
        pass

    def receive_game_update_message(self, action, round_state):
        pass

    def receive_round_result_message(self, winners, hand_info, round_state):
        # print("My ID (round result) : "+self.uuid)
        # pprint.pprint(round_state)
        # print("\n\n")
        # self.round_count = self.round_count + 1
        # print("Random Player")
        # pprint.pprint(hand_info)
        # print('\n')
        pass

def setup_ai():
    return RandomPlayer()