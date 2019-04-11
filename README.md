[![Build Status](https://travis-ci.com/cs3243-project-group-18/poker-ai.svg?branch=master)](https://travis-ci.com/cs3243-project-group-18/poker-ai)
[![Maintainability](https://api.codeclimate.com/v1/badges/2899885f1128dc2d5b42/maintainability)](https://codeclimate.com/github/cs3243-project-group-18/poker-ai/maintainability)

# CS3243 Poker AI Project

### Create your own player

#### Example player

```

class Group18Player(BasePokerPlayer):

  def declare_action(self, valid_actions, hole_card, round_state):
    #Implement your code
    return action

  def receive_game_start_message(self, game_info):
    pass

  def receive_round_start_message(self, round_count, hole_card, seats):
    pass

  def receive_street_start_message(self, street, round_state):
    pass

  def receive_game_update_message(self, action, round_state):
    pass

  def receive_round_result_message(self, winners, hand_info, round_state):
    pass
```

### Example Game

The example game is in the example.py

### Information for the game
```valid_actions```: vaild action list


```
[
    { "action" : "fold"  },
    { "action" : "call" },
    { "action" : "raise" }
]
OR 
[
    {"action": "fold"},
    {"action": "call"}
]
```

In the limited version, user only allowed to raise for four time in one round game.    
In addition, in each street (preflop,flop,turn,river),each player only allowed to raise for four times.

Other information is similar to the PyPokerEngine,please check the detail about the parameter [link](https://github.com/ishikota/PyPokerEngine/blob/master/AI_CALLBACK_FORMAT.md)
