from games import *

import utils

class BLOBS(Game):
    def __init__(self, h=5, v=5):
        self.h = h
        self.v = v
        board = {(1,1):'X',(h,1):'O',(h,v):'X',(1,v):'O'}
        moves = moves = [(x, y) for x in range(1, h + 1)
                 for y in range(1, v + 1) if (x,y) not in board.keys()]
        self.initial = GameState(to_move='X', utility=0, board=board, moves=moves)
        
    def actions(self, state):
        board = state.board.copy()
        player = state.to_move
        
        if self.neighbors_to_place(state,player)!=[]:
            moves = self.neighbors_to_place(state,player)

        else:
            moves = self.neighbors_to_move(state,player)
        
        return moves

    def result(self, state, move):
        
        board = state.board.copy()
        print('123',move)
        print('345',state.moves,end='\n')
        n = self.actions(state)
        if move not in n:
            return state  # Illegal move has no effect
        
        # if self.neighbors_to_place(state,state.to_move) == []:
        #     board[move] = 
        board[move] = state.to_move
        moves = state.moves
        moves.remove(move)  # Remove the chosen move from the available moves
        print(moves)

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
        
    def neighbors_to_move(self,state,player):
        board = state.board.copy()
        rows,cols = self.h,self.v
        indices = [key for key,value in board.items() if value == player]
        moves = []
        for index in indices:
            row,col = index
            for r in range(row - 2,row + 2 + 1):
                for c in range(col -2,col + 2 + 1):
                    if (r,c) == (row,col):
                        continue
                    if 1<=r<=5 and 1<=c<=5:
                        if (r == row) or (c == col) or (r == c):
                            if (board.get((r,c),0)!='X' and board.get((r,c),0) !='O') and (r,c) not in moves:
                                moves.append((r,c))
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



# if __name__== '__main__':
#     othello = BLOBS()
    
#     othello.play_game(query_player,random_player)