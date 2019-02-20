import random

team_name = 'POC'
strategy_name = 'Score check'
strategy_description = 'If we have the same score, we will randomly choose. On the first turn, we will collude. If our score is less than -99, we will always betray. If our score is greater than 299, we will always collude. If our score is greater than the their score, we will always betray.Score check'

def move(my_score, my_hist, their_score, their_hist):
	a = ['c', 'b']
	if my_score > their_score:	
		return 'b'
	elif my_score <= -100:
		return 'b'
	elif my_score >= 300:
		return 'c'
	elif my_score == their_score:
		return random.choice(a)
	else:
		return 'c'
