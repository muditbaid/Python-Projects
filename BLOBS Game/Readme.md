### BLOBS Game

This is a Python implementation of the BLOBS game, which is similar to Othello. The objective is to have the maximum number of your color ('X' or 'O') on the board at the end of the game.

## Rules

- The game is played on a 5x5 board.
- Players take turns to make moves.
- Players can either place their color on an empty square or slide their color to an adjacent empty square.
- The game ends when no more moves can be made or the board is filled.

2. Run the game:

```
from games import *
from assignment3 import *

1. Random vs Random
BLOBS().play_game(random_player,random_player)

2. Random vs Minimax with cutoff
BLOBS().play_game(random_player,minmax_cutoff_player)

3. Random vs 
```

## Game Features

- Interactive command-line interface.
- Two player modes: `query_player` and `random_player`.
- Minimax-based player (`minmax_cutoff_player`) with a cutoff depth of 3.

## Functions

### `__init__(self, h=5, v=5)`

- Initializes the game with a 5x5 board.
- Sets the initial state with predefined positions of 'X' and 'O'.
- Generates all possible moves on the board.

### `actions(self, state)`

- Returns a list of all possible moves for the current player.
- Combines the results from two separate functions based on the type of action.

### `result(self, state, move)`

- Updates the game state based on the chosen move.
- Handles both placing the color and sliding the color to an adjacent empty square.

### `utility(self, state, player)`

- Returns the utility value for the player; 1 for a win, -1 for a loss, and 0 otherwise.

### `terminal_test(self, state)`

- Checks if the current state is a terminal state, i.e., if the game is won or there are no empty squares left.

### `neighbors_to_place(self, state, player)`

- Returns a list of adjacent positions where a player can place their color (Action 1).

### `neighbors_to_move(self, state, player)`

- Returns a dictionary containing the position of the color and the associated moves where a player can slide their color (Move 2).

### `display(self, state)`

- Displays the current state of the board.

### `compute_utility(self, board, move, player)`

- Computes the utility value based on the move made by the player.

### `eval_function(state)`

- Returns the difference between the count of 'X's and 'O's on the board.

### `minimax_cutoff_decision(state, game, cutoff_depth)`

- Implements the minimax decision-making process with a specified depth cutoff.

### `minmax_cutoff_player(game, state)`

- Returns the best move for the player using the minimax algorithm with a cutoff depth of 3.

### `alpha_beta_pruning_player(game, state)`

- Returns the best move for the player using the alpha-beta pruning algorithm with a cutoff depth of 3.

### `alpha_beta_cutoff_search(state, game, d=4, cutoff_test=None, eval_fn=None)`

- Searches the game to determine the best action, utilizing alpha-beta pruning.
- This version allows for search cutoff and employs an evaluation function.
- Parameters:
  - `state`: The current state of the game.
  - `game`: The game being played.
  - `d`: The maximum depth of the search tree (default is 4).
  - `cutoff_test`: A function to determine whether to cut off the search (default is None).
  - `eval_fn`: An evaluation function to assess the state (default is None).
- Returns the best action based on the search.
