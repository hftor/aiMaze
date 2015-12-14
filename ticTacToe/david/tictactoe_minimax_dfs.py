#!/bin/python3
#
# Tictactoe program that uses a minimax tree with alpha-beta pruning.
# Details at https://www.hackerrank.com/challenges/tic-tac-toe/
#
# By: Davíð Guðni Halldórsson
#

INF = 9999

class Node(object):
    def __init__(self, board, coord, player):
        self.done = False
        self.board = board
        self.coord = coord
        if player == 'X':
            self.value = INF
        elif player == 'O':
            self.value = -INF


#
# Takes a node as a parameter, if its board has a winner or a draw it is
# marked done and given appropriate value according to the results.
#
def checkForWinner(node):
    if node.board[0] == 'X' and node.board[1] == 'X' and node.board[2] == 'X':
        node.done = True
        node.value = 1
        return
    if node.board[3] == 'X' and node.board[4] == 'X' and node.board[5] == 'X':
        node.done = True
        node.value = 1
        return
    if node.board[6] == 'X' and node.board[7] == 'X' and node.board[8] == 'X':
        node.done = True
        node.value = 1
        return
    if node.board[0] == 'X' and node.board[3] == 'X' and node.board[6] == 'X':
        node.done = True
        node.value = 1
        return
    if node.board[1] == 'X' and node.board[4] == 'X' and node.board[7] == 'X':
        node.done = True
        node.value = 1
        return
    if node.board[2] == 'X' and node.board[5] == 'X' and node.board[8] == 'X':
        node.done = True
        node.value = 1
        return
    if node.board[0] == 'X' and node.board[4] == 'X' and node.board[8] == 'X':
        node.done = True
        node.value = 1
        return
    if node.board[2] == 'X' and node.board[4] == 'X' and node.board[6] == 'X':
        node.done = True
        node.value = 1
        return

    if node.board[0] == 'O' and node.board[1] == 'O' and node.board[2] == 'O':
        node.done = True
        node.value = -1
        return
    if node.board[3] == 'O' and node.board[4] == 'O' and node.board[5] == 'O':
        node.done = True
        node.value = -1
        return
    if node.board[6] == 'O' and node.board[7] == 'O' and node.board[8] == 'O':
        node.done = True
        node.value = -1
        return
    if node.board[0] == 'O' and node.board[3] == 'O' and node.board[6] == 'O':
        node.done = True
        node.value = -1
        return
    if node.board[1] == 'O' and node.board[4] == 'O' and node.board[7] == 'O':
        node.done = True
        node.value = -1
        return
    if node.board[2] == 'O' and node.board[5] == 'O' and node.board[8] == 'O':
        node.done = True
        node.value = -1
        return
    if node.board[0] == 'O' and node.board[4] == 'O' and node.board[8] == 'O':
        node.done = True
        node.value = -1
        return
    if node.board[2] == 'O' and node.board[4] == 'O' and node.board[6] == 'O':
        node.done = True
        node.value = -1
        return

    if '_' not in node.board:
        node.done = True
        node.value = 0
        return


#
# Takes a player as a parameter and returns the opposite player.
#
def notPlayer(player):
    if player == 'X':
        return 'O'
    elif player == 'O':
        return 'X'


#
# Takes a position in a list and maps it to coordinates in a 3x3 two dimensional array.
#
def posToCoord(pos):
    if pos == 0:
        return (0,0)
    if pos == 1:
        return (0,1)
    if pos == 2:
        return (0,2)
    if pos == 3:
        return (1,0)
    if pos == 4:
        return (1,1)
    if pos == 5:
        return (1,2)
    if pos == 6:
        return (2,0)
    if pos == 7:
        return (2,1)
    if pos == 8:
        return (2,2)
    return (-1,-1)


#
# Takes a list of nodes as a parameter and returns the coordinates of the
# node that has the highest value.
#
def maximize(choices):
    maxVal = -INF
    maxNode = None
    for node in choices:
        if node.value > maxVal:
            maxVal = node.value
            maxNode = node

    return maxNode.coord


#
# Takes a list of nodes as a parameter and returns the coordinates of the
# node that has the lowest value.
#
def minimize(choices):
    minVal = INF
    minNode = None
    for node in choices:
        if node.value < minVal:
            minVal = node.value
            minNode = node

    return minNode.coord


#
# Takes a node, player, alpha and beta as parameters. It uses recursion to find
# all possible board moves from the board of the node and propagates those values
# up to the original node with regards to the player. The alpha and beta parameters
# assist with pruning the tree, using a method called alpha-beta pruning.
#
def minimax(node, player, alpha, beta):
    checkForWinner(node)

    if node.done:
        return node.value

    node.done = True
    for i in range(0,9):
        if node.board[i] == '_':
            modBoard = node.board.copy()
            modBoard[i] = player
            val = minimax(Node(modBoard, posToCoord(i), player), notPlayer(player), alpha, beta)

            if player == 'X':
                node.value = max(node.value, val)
                alpha = max(alpha, node.value)
            elif player == 'O':
                node.value = min(node.value, val)
                beta = min(beta, node.value)

            if beta <= alpha:
                break

    return node.value


#
# Takes a player and a board as parameters. It finds all possible moves for the
# board with regards to the player. Then uses the minimax function to get the
# reward for each action. Finally it maximizes or minimizes (depending on the player)
# the choices and returns the best move for the player.
#
def getCoord(player, board):
    choices = []
    for i in range(0,9):
        if board[i] == '_':
            modBoard = board.copy()
            modBoard[i] = player
            choices.append(Node(modBoard, posToCoord(i), player))

    for node in choices:
        node.value = minimax(node, notPlayer(player), -INF, INF)

    if player == 'X':
        return maximize(choices)
    elif player == 'O':
        return minimize(choices)


def main():
    player = input()
    board = input()
    board += input()
    board += input()
    board = list(board)

    x,y = getCoord(player, board)

    print(x, y)

if __name__ == "__main__":
    main()

