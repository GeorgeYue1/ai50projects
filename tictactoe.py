"""
Tic Tac Toe Player
"""
import copy
import math

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
    totalTurns = 0

    for i in range(3):
        for j in range(3):
            if(board[i][j] != EMPTY):
                totalTurns += 1
    if totalTurns%2 == 0:
        return X
    return O
    raise NotImplementedError
    

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    moves = []
    for i in range(3):
        for j in range(3):
            if(board[i][j] == EMPTY):
                moves.append((i,j))
    return moves
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i,j = action
    b = copy.deepcopy(board)
    if b[i][j] != EMPTY:
        raise NameError
    b[i][j] = player(board)
    return b
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if board[0][0] == board[0][1] and board[0][0] == board[0][2] and board[0][0] != EMPTY:
        return board[0][0]
    if board[1][0] == board[1][1] and board[1][0] == board[1][2] and board[1][0] != EMPTY:
        return board[1][0]
    if board[2][0] == board[2][1] and board[2][0] == board[2][2] and board[1][0] != EMPTY:
        return board[2][0]
    if board[0][0] == board[1][0] and board[0][0] == board[2][0] and board[0][0] != EMPTY:
        return board[0][0]
    if board[0][1] == board[1][1] and board[0][1] == board[2][1] and board[0][1] != EMPTY:
        return board[0][1]
    if board[0][2] == board[1][2] and board[0][2] == board[2][2] and board[0][2] != EMPTY:
        return board[0][2]
    if board[0][0] == board[1][1] and board[0][0] == board[2][2] and board[0][0] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] and board[0][2] == board[2][0] and board[0][2] != EMPTY:
        return board[0][2]
    return None
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True
    for i in range(3):
        for j in range(3):
            if(board[i][j] == EMPTY):
                return False
    return True
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    if winner(board) == O:
        return -1 
    else: 
        return 0
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    turn = player(board)
    if(turn == X):
        value, action = MaxValue(board)
        return action
    value, action = MinValue(board)
    return action  
    raise NotImplementedError

def MaxValue(board):
    if terminal(board):
        return utility(board), None
    v = -2
    bestAction = (0,0)
    for action in actions(board):
        value, a = MinValue(result(board,action))
        if(v < value):
            v = value
            bestAction = action
    return v, bestAction

def MinValue(board):
    if terminal(board):
        return utility(board), None
    v = 2
    bestAction = (0,0)
    for action in actions(board):
        value, a = MaxValue(result(board,action))
        if(v > value):
            v = value
            bestAction = action
    return v, bestAction