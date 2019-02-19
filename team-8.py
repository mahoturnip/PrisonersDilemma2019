####
#     Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'POC'
team_strategy = 'If they colluded last time, we betray. If they betraed last time, we collude. Else, collude'
strategy_description = 'Opposite'

def move(my_score, my_hist, their_score, their_hist):
  if my_hist >= 1 and their_hist[-1] == 'b':
    return 'c'
  elif my_hist >= 1 and their_hist[-1] == 'c':
    return 'b'
  elif my_score >= 500 and their_score < my_score:
    return 'b'
  elif my_score <= 0 and their_score  >= 0:
    return 'c'
  else:
    return 'c' 

team_name = 'Vengeful Twoface'
team_strategy =  'heads collude, tails betray, but if they betrayed last, I betray no matter what'
strategy_description = 'The world is cruel. And the only morality in a cruel world is chance.'
    


def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    Make my move.
    Returns 'c' or 'b'. 
    '''

    # my_history: a string with one letter (c or b) per round that has been played with this opponent.
    # their_history: a string of the same length as history, possibly empty.
    # The first round between these two players is my_history[0] and their_history[0].
    # The most recent round is my_history[-1] and their_history[-1].

    # Analyze my_history and their_history and/or my_score and their_score.
    # Decide whether to return 'c' or 'b'.

    # collude on the first move:
    if len(my_history) == 0:
      return 'c'
    # make sure that there's enough history
    elif len(my_history) >= 1 and their_history[-1] == 'b':
      return 'b'
    else:
      choices = ['c','b']
      return random.choice(choices)

def test_move(my_history, their_history, my_score, their_score, result):
    '''calls move(my_history, their_history, my_score, their_score)
    from this module. Prints error if return value != result.
    Returns True or False, dpending on whether result was as expected.
    '''
    real_result = move(my_history, their_history, my_score, their_score)
    if real_result == result:
        return True
    else:
        print("move(" +
            ", ".join(["'"+my_history+"'", "'"+their_history+"'",
                       str(my_score), str(their_score)])+
            ") returned " + "'" + real_result + "'" +
            " and should have returned '" + result + "'")
        return False

if __name__ == '__main__':
     
    # Test 1: Collude on the first move
    if test_move(my_history='',
              their_history='', 
              my_score=0,
              their_score=0,
              result='c'):
         print 'Turn 1 test passed'
     # Test 2: if they betrayed last time, i should betray this time
    if test_move(my_history='bcbc',
              their_history='cccb', 
              # Note the scores are for testing move()
              # The history and scores don't need to match unless
              # that is relevant to the test of move(). Here,
              # the simulation (if working correctly) would have awarded 
              # 300 to me and -750 to them. This test will pass if and only if
              # move('bbb', 'ccc', 0, 0) returns 'b'.
              my_score=0, 
              their_score=0,
              result='b'):       
      print 'vengeance test successful.'
