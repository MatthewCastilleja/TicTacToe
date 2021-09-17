"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count = 0
    for r in range(3):
        for c in range(3):
            if board[r][c] == EMPTY:
                count += 1
    if count % 2 == 1:
        return X
    return O
            


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = []
    for r in range(3):
        for c in range(3):
            if board[r][c] == EMPTY:
                actions.append((r,c))
    return actions



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    
    i, j = action
    
    if not board[i][j] == EMPTY:
        return board
    
    
    new_board = [[],[],[]]
    for r in range(3):
        new_board[r] = copy.deepcopy(board[r])
        
    new_board[i][j] = player(board)
    return new_board
    


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    
    for i in range(3):
        if board[i][0] != EMPTY and board[i][0] == board[i][1] and board[i][0] == board[i][2]:
            return board[i][0]
        if board[0][i] != EMPTY and board[0][i] == board[1][i] and board[0][i] == board[2][i]:
            return board[0][i]
    
    if board[0][0] != EMPTY and board[0][0] == board[1][1] and board[0][0] == board[2][2]:
        return board[0][0]
        
    if board[0][2] != EMPTY and board[0][2] == board[1][1] and board[0][2] == board[2][0]:
        return board[2][0]
    
    return 'Nobody'


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if actions(board) and winner(board) == 'Nobody':
        return False
    return True
    
    


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    return 0



def minimax(board):
    """
    #Returns the optimal action for the current player on the board.
    """
    
    if player(board) == X:
        return Max_value(board, float('-inf'), float('inf'))[1]
    else:
        return Min_value(board, float('-inf'), float('inf'))[1]
    
    
    
def Max_value(board, max_value, min_value):
    """
    Returns the [score, move] list that is associated with the max score available
    """
    if terminal(board):
        return [utility(board), None]
    
    move = None
    current_max = float('-inf')
    for action in actions(board):
        
        test = Min_value(result(board, action), max_value, min_value)[0]
        max_value = max(max_value, test)
        
        if test > current_max:
            current_max = test
            move = action
        
        #If the current max value of this node's possible outcomes
        #is larger than the min value of the previous nodes's possible outcomes
        #then stop looking at this node
        if max_value >= min_value:
            break
    return [current_max, move]





def Min_value(board, max_value, min_value):
    if terminal(board):
        return [utility(board), None]
    
    move = None
    outcome_min = float('inf')
    for action in actions(board):
        outcome = Max_value(result(board, action), max_value, min_value)[0]
        min_value = min(min_value, outcome)
        
        if outcome < outcome_min:
            outcome_min = outcome
            move = action
        
        #If the current min value of this node's possible outcomes
        #is lower than the max value of the previous nodes's possible outcomes
        #then stop looking at this node 
        if max_value >= min_value:
            break
    return [outcome_min, move]
