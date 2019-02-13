from functools import reduce

class ActionChecker:

  @classmethod
  def correct_action(self, players, player_pos, sb_amount, action, amount=None):
    if self.is_allin(players[player_pos], action, amount):
      amount = players[player_pos].stack + players[player_pos].paid_sum()
    elif self.__is_illegal(players, player_pos, sb_amount, action, amount):
      action, amount = "fold", 0
    return action, amount


  @classmethod
  def is_allin(self, player, action, bet_amount):
    if action == 'call':
      return bet_amount >= player.stack + player.paid_sum()
    elif action == 'raise':
      return bet_amount == player.stack + player.paid_sum()
    else:
      return False


  @classmethod
  def need_amount_for_action(self, player, amount):
    return amount - player.paid_sum()


  @classmethod
  def agree_amount(self, players):
    last_raise = self.__fetch_last_raise(players)
    return last_raise["amount"] if last_raise else 0


  @classmethod
  def legal_actions(self, players, player_pos, sb_amount,street):
    raise_amount,raise_limit = self.round_raise_amount(sb_amount,street)
    current_amount = self.agree_amount(players)
    player_raised_number = self.__player_raise_number(players,player_pos,street)
    if current_amount < raise_limit and player_raised_number < 4:
      return [
          { "action" : "fold"  },
          { "action" : "call" },
          { "action" : "raise"}
      ]
    else:
      return [
        {"action": "fold"},
        {"action": "call"}
      ]

  @classmethod
  def _is_legal(self, players, player_pos, sb_amount, action, amount=None):
    return not self.__is_illegal(players, player_pos, sb_amount, action, amount)

  @classmethod
  def __is_illegal(self, players, player_pos, sb_amount, action, amount=None):
    if action == 'fold':
      return False
    elif action == 'call':
      return self.__is_short_of_money(players[player_pos], amount)\
          or self.__is_illegal_call(players, amount)
    elif action == 'raise':
      return self.__is_short_of_money(players[player_pos], amount) \
          or self.__is_illegal_raise(players, amount, sb_amount)

  @classmethod
  def __is_illegal_call(self, players, amount):
    return amount != self.agree_amount(players)

  @classmethod
  def __is_illegal_raise(self, players, amount, sb_amount):
    return self.__min_raise_amount(players, sb_amount) > amount

  @classmethod
  def __min_raise_amount(self, players, sb_amount):
    raise_ = self.__fetch_last_raise(players)
    return raise_["amount"] + raise_["add_amount"] if raise_ else sb_amount*2

  @classmethod
  def __is_short_of_money(self, player, amount):
    return player.stack < amount - player.paid_sum()

  @classmethod
  def __fetch_last_raise(self, players):
    all_histories = [p.action_histories for p in players]
    all_histories = reduce(lambda acc, e: acc + e, all_histories)  # flatten
    raise_histories = [h for h in all_histories if h["action"] in ["RAISE", "SMALLBLIND", "BIGBLIND"]]
    if len(raise_histories) == 0:
      return None
    else:
      return max(raise_histories, key=lambda h: h["amount"])  # maxby

  @classmethod
  def round_raise_amount(self, sb_amount,street):
    if street == 0 or street == 1:
      return sb_amount * 2, sb_amount * 2 * 4
    else:
      return sb_amount * 4 ,sb_amount * 4 * 4

  @classmethod
  def __player_raise_number(self,players,player_pos,street):
    raised_number = 0
    histories = players[player_pos].round_action_histories
    for rounds in histories:
      if rounds == None:
        return raised_number
      else:
        for action in rounds:
          if action["action"] == "RAISE":
            raised_number += 1
    return raised_number