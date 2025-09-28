#
# ps9pr2.py (Problem Set 9, Problem 2)
#
# A Connect-Four Player class 
#  

from ps9pr1 import Board

# write your class below.
class Player:
    '''player class'''
    def __init__(self, checker):
        assert(checker == 'X' or checker == 'O')
        self.checker = checker
        self.num_moves = 0
    def  __repr__(self):
        
        s = ''
        s += "Player " + self.checker
        return s
    
    
    
    def opponent_checker(self):
        '''returns the checker of the opponent'''
        if self.checker == 'X':
            return 'O'
        else:
            return 'X'
        
        
    def next_move(self, b):
        '''tracks the moves a player makes'''
        self.num_moves+=1 
        
        while True:
            col = int(input("Enter a column: "))
            if b.can_add_to(col) == True:
                return col
            else:
                print("Try Again")
        
        

