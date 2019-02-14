import random
team_name = 'POC'
team_strategy = 'If they colluded last time, we betray. If they betraed last time, we collude. Else, collude'
strategy_description = 'Opposite'

def move(my_score, my_hist, their_score, their_hist):
  if my_hist >= 1 and their_hist[-1] == 'b':
    return 'c'
  elif my_hist >= 1 and their_hist[-1] == 'c':
    return 'b'
  else:
    return 'c' 
