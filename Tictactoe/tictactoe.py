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
    num_x = 0
    num_o = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == X:
                num_x += 1
            elif board[i][j] == O:
                num_o += 1
    if num_x > num_o:
        return O
    return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    result = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] is None:
                result.append((i, j))
    return result


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = copy.deepcopy(board)
    new_board[action[0]][action[1]] = player(board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(len(board)):
        if board[i][0] is not None and board[i][1] == board[i][0] and board[i][2] == board[i][1]:
            return board[i][0]
    for i in range(len(board[0])):
        if board[0][i] is not None and board[1][i] == board[0][i] and board[2][i] == board[1][i]:
            return board[0][i]
    if board[1][1] is not None:
        if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
            return board[1][1]
        if board[0][2] == board[1][1] and board[2][0] == board[1][1]:
            return board[1][1]
    return None



def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] is None:
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
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    next_move = None
    def max_value(board):
        if terminal(board):
            return (utility(board), None)
        v = float("-inf")
        next_action = None
        for action in actions(board):
            temp = min_value(result(board, action))[0]
            if temp > v:
                next_action = action
                v = temp
        return (v, next_action)

    def min_value(board):
        if terminal(board):
            return (utility(board), None)
        v = float("inf")
        next_action = None
        for action in actions(board):
            temp = max_value(result(board, action))[0]
            if temp < v:
                next_action = action
                v = temp
        return (v, next_action)
    p = player(board)
    if p == X:
        next_move = max_value(board)[1]
    if p == O:
        next_move = min_value(board)[1]
    return next_move



