
# A Connect Four Board class

class Board:
    """ a data type for a Connect Four board with arbitrary dimensions
    """   
    def __init__(self, height, width):
        self.width = width
        self.height = height
        self.slots = [[' '] * self.width for row in range(self.height)]


    def __repr__(self):
        """ Returns a string that represents a Board object.
        """
        s = ''       

        
        for row in range(self.height):
            s += '|'  

            for col in range(self.width):
                s += self.slots[row][col] + '|'

            s += '\n'  

        s+= '-'*((self.width*2)+1) + '\n'
        for i in range(self.width):
           s+= ' ' + str(i%10)+ ''
        
        return s

    def add_checker(self, checker, col):
        """ adds the specified checker (either 'X' or 'O') to the
            column with the specified index col in the called Board.
            inputs: checker is either 'X' or 'O'
                    col is a valid column index
        """
        assert(checker == 'X' or checker == 'O')
        assert(col >= 0 and col < self.width)
        
        
        row = 0
        while row < self.height-1 and self.slots[row+1][col] == ' ':
            row += 1
        self.slots[row][col] = checker
    
        
    
    
    def reset(self):
        '''resets every board value back to blank'''
        for r in range(self.height):
            for c in range(self.width):
                self.slots[r][c] = ' '
    
    def add_checkers(self, colnums):
        """ takes a string of column numbers and places alternating
            checkers in those columns of the called Board object,
            starting with 'X'.
            input: colnums is a string of valid column numbers
        """
        checker = 'X'   # start by playing 'X'

        for col_str in colnums:
            col = int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker, col)

            if checker == 'X':
                checker = 'O'
            else:
                checker = 'X'

    def can_add_to(self, col):
        '''checks if a col is possible to be added to'''
        if col > self.width -1 or col < 0:
            return False
        elif self.slots[0][col] != ' ':
            return False
        else:
            return True
    
    def is_full(self):
        '''uses can add to to see if the board is full or not'''
        for c in range(self.width):
            if self.can_add_to(c) == True:
                return False
        return True
    
    def remove_checker(self, col):
        '''removes the top checker in a col'''
        for row in range(self.height):
            if self.slots[row][col] != ' ':
                self.slots[row][col] = ' '
                break
    
    def is_horizontal_win(self, checker):
        '''Checks for a horizontal win for the specified checker.'''
        for row in range(self.height):
            for col in range(self.width - 3):
                # Check if the next four columns in this row
                # contain the specified checker.
                if self.slots[row][col] == checker and \
                   self.slots[row][col + 1] == checker and \
                   self.slots[row][col + 2] == checker and \
                   self.slots[row][col + 3] == checker:
                    return True
        return False
    
        # if we make it here, there were no horizontal wins
        return False
    
    def is_vertical_win(self,checker):
        '''checks for a vertical win'''
        for row in range(self.height-3):
            for col in range(self.width):
                if self.slots[row][col] == checker and \
                   self.slots[row +1][col] == checker and \
                   self.slots[row+2][col] == checker and \
                   self.slots[row+3][col] == checker:
                    return True
        return False
    def is_down_diagonal_win(self,checker):
        '''checks for down diagonal win from left to right'''
        for row in range(self.height-3):
            for col in range(self.width-3):
                if self.slots[row][col] == checker and \
                   self.slots[row +1][col+1] == checker and \
                   self.slots[row+2][col+2] == checker and \
                   self.slots[row+3][col+3] == checker:
                    return True
        return False
    def is_up_diagonal_win(self,checker):
        '''checks for if theres a potential win from up to right'''
        for row in range(self.height-3):
            for col in range(self.width-3):
                if self.slots[row+3][col] == checker and \
                   self.slots[row+2][col+1] == checker and \
                   self.slots[row+1][col+2] == checker and \
                   self.slots[row][col+3] == checker:
                    return True
        return False
    def is_win_for(self, checker):
        """ checks if theres a potential win in any direction"""
        assert(checker == 'X' or checker == 'O')
        
        if self.is_down_diagonal_win(checker) == True or self.is_horizontal_win(checker) == True or self.is_up_diagonal_win(checker) == True or self.is_vertical_win(checker) == True:
            return True
        return False
        
        

