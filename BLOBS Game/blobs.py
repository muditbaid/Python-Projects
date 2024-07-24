# Name: Mudit Baid
# UGA ID: 811464288
from games import *
import utils

class BLOBS(Game):
    ''' This game consists of 5x5 board similar to the game Othello. Each player has
    his own colour X and O. The objective is to have maximum number of your colour on the board
    at the end of the game.
    '''
    def __init__(self, h=5, v=5):
        ''' Initialize size of the board and the initial board having the respective positions of X and O.
        Moves are all the possible moves on the board.
        '''
        self.h = h
        self.v = v
        board = {(1,1):'X',(h,1):'O',(h,v):'X',(1,v):'O'}
        moves = moves = [(x, y) for x in range(1, h + 1)
                 for y in range(1, v + 1) if (x,y)]
        self.initial = GameState(to_move='X', utility=0, board=board, moves=moves)
        
    def actions(self, state):
        ''' There are two separate functions defined to give possible moves for the two different types of actions.
        It returns all the possible moves for all the indices of the player in turn.
        '''
        board = state.board.copy()
        player = state.to_move
        
        n =   self.neighbors_to_move(state,player)
        moves = []
        for m in n.values():
            moves.extend(m)
        moves = list(set(moves))
        return moves

    def result(self, state, move):
        ''' It takes the action to perform as input and changes the state accordingly.
        '''
        board = state.board.copy()
        
        n = self.actions(state)
        # if the move is not in available moves, then dont make any change in state.
        if move not in n:
            return state  # Illegal move has no effect
        
        ''' If the chosen move is not an adjacent position of any of the indices of the player, 
        then move existing player to the position of the move.
        '''
        if move not in self.neighbors_to_place(state,state.to_move):

            # neighbors_to_place returns a dictionary containing the position of the player and moves associated with it.
            # p stores the position of the colour ('X' or 'O') to slide to the chosen position. 
            slides = self.neighbors_to_move(state,state.to_move)
            p = tuple
            for key, values in slides.items():
                if move in values:
                    p = key
                    break
            board[move] = state.to_move
            board.pop(p)
        else:
            board[move] = state.to_move
        
        moves = state.moves

        return GameState(to_move=('O' if state.to_move == 'X' else 'X'),
                     utility=self.compute_utility(board, move, state.to_move),
                     board=board, moves=moves)


    def utility(self, state, player):
        """Return the value to player; 1 for win, -1 for loss, 0 otherwise."""
        return state.utility if player == 'X' else -state.utility

    def terminal_test(self, state):
        """A state is terminal if it is won or there are no empty squares."""
        if state.utility != 0:
            return True

    # Returns a list of adjacent positions; Action 1
    def neighbors_to_place(self,state,player):
        board = state.board.copy()
        rows,cols = self.h,self.v
        indices = [key for key,value in board.items() if value == player]
        moves = []
        for index in indices:
            row,col = index
            proximity = [(row-1,col),(row+1,col),(row,col-1),(row,col+1)]
            for p in proximity:
                if board.get(p, 0) != 'X' and board.get(p,0) != 'O':
                    if 1<=p[0]<=5 and 1<=p[1]<=5 and p not in moves:
                        moves.append(p) 
        return moves            
    
    # Returns a dictionary containing the position of the colour and moves associatd with it; Move 2
    def neighbors_to_move(self,state,player):
        board = state.board.copy()
        rows,cols = self.h,self.v
        indices = [key for key,value in board.items() if value == player]
        moves = {}
        for index in indices:
            row,col = index
            moves[index] = []
            for r in range(row - 2,row + 2 + 1):
                for c in range(col -2,col + 2 + 1):
                    if (r,c) == (row,col):
                        continue
                    if 1<=r<=5 and 1<=c<=5:
                        if (r in [row,row-1,row+1]) or (c in [col,col-1,col+1]) or (r == c):
                            if (board.get((r,c),0)!='X' and board.get((r,c),0) !='O') and (r,c) not in moves:
                                moves[(row,col)].append((r,c))
        return moves
          
    def display(self, state):
        board = state.board
        for x in range(1, self.h + 1):
            for y in range(1, self.v + 1):
                print(board.get((x, y), '.'), end=' ')
            print()

    def compute_utility(self, board, move, player):
        """If 'X' wins with this move, return 1; if 'O' wins return -1; else return 0."""
        
        x = list(board.values()).count('X')
        o = list(board.values()).count('O')
        if len(board)==25:
            if x>o:
                return +1
            else:
                return -1
        else:
            return 0

# Evaluation function returns difference between count of X's and O's
def eval_function(state):
    board = state.board
    x_count = list(board.values()).count('X')
    o_count = list(board.values()).count('O')
    return x_count - o_count

# Added cutoff in minimax function from games.py.
def minimax_cutoff_decision(state, game, cutoff_depth):
    player = game.to_move(state)

    def max_value(state, depth):
        if depth == 0 or game.terminal_test(state):
            return eval_function(state)
        v = -float('inf')
        for a in game.actions(state):
            v = max(v, min_value(game.result(state, a), depth - 1))
        return v

    def min_value(state, depth):
        if depth == 0 or game.terminal_test(state):
            return eval_function(state)
        v = float('inf')
        for a in game.actions(state):
            v = min(v, max_value(game.result(state, a), depth - 1))
        return v

    return max(game.actions(state), key=lambda a: min_value(game.result(state, a), cutoff_depth))

# Giving a depth of 3 as cutoff
def minmax_cutoff_player(game,state):
    return minimax_cutoff_decision(state,game,3)

def alpha_beta_pruning_player(game,state):
    return alpha_beta_cutoff_search(state,game,3)
