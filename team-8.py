import random

team_name = 'POC'
team_strategy = 'If we have the same score, we will randomly choose. On the first turn, we will collude. If our score is less than -99, we will always betray. If our score is greater than 299, we will always collude. If our score is greater than the their score, we will always betray.'
strategy_description = 'Score check'

def move(my_score, my_hist, their_score, their_hist):
	a = ['c', 'b']
	if int(my_score) > int(their_score):	
		return 'b'
	elif int(my_score) <= -100:
		return 'b'
	elif int(my_score) >= 300:
		return 'c'
	elif int(my_score) == int(their_score):
		return random.choice(a)
	else:
		return 'c'
