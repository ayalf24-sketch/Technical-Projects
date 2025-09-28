#
# ps9pr4.py (Problem Set 9, Problem 4)
#
# AI Player for use in Connect Four  
#

import random  
from ps9pr3 import *

class AIPlayer(Player):
    '''AI Player class which is a subclass of player'''
    def __init__(self, checker, tiebreak, lookahead):
        """ put your docstring here"""
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)
        super().__init__(checker)
        self.tiebreak = tiebreak
        self.lookahead = lookahead
    
    def  __repr__(self):
        '''returns the string representation of the ai'''
        s = ''
        s+= 'Player ' + str(self.checker) + ' (' + str(self.tiebreak) + ', ' + str(self.lookahead) + ')'
        return s
    
    def max_score_column(self, scores):
        '''returns what the max score is for a lst of scores and determines which index is chosen if a tiebreak is needed'''
        lst = []
        maxscore = max(scores)
        for i in range(len(scores)):
            if scores[i] == maxscore:
                lst += [i]
        if self.tiebreak == 'RANDOM':
            return random.choice(lst)
        elif self.tiebreak == 'RIGHT':
            return lst[-1]
        else:
            return lst[0]
    
    def scores_for(self, b):
        '''returns the scores for each col either -1,50,0, or 100'''
        scores =[50] * b.width
        for i in range(b.width):
            if b.can_add_to(i) == False:
                scores[i] = -1
            elif self.lookahead == 0:
                scores[i] = 50
            else:
                b.add_checker(self.checker, i)
                if b.is_win_for(self.checker):
                    scores[i] = 100
                elif b.is_win_for(self.opponent_checker()):
                    scores[i] = 0
                else:
                    opp = AIPlayer(self.opponent_checker(), self.tiebreak, self.lookahead-1)
                    oppscores = opp.scores_for(b)
                    maxscore = max(oppscores)
                    if maxscore == 0:
                        scores[i] = 100
                    elif maxscore == 100:
                        scores[i] = 0
                    else:
                        scores[i] = 50
                b.remove_checker(i)
        return scores
                        
        
    def next_move(self, b):
        '''returns the next col that the ai will put a checker on'''
        self.num_moves+=1 
        scores = self.scores_for(b)
        col = self.max_score_column(scores)
        return col



        
        
        
        
        
        
        
        
        
        
        
        
 
        
            
        
    
