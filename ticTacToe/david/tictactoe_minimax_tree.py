#!/bin/python3
#
# Tictactoe program that uses a minimax tree with alpha-beta pruning.
# Details at https://www.hackerrank.com/challenges/tic-tac-toe/
#
# By: Davíð Guðni Halldórsson
#

import random
import time

class Node(object):
    def __init__(self, board, pos=-1):
        self.children = []
        self.board = board
        self.coord = self.__posToCoord__(pos)
        self.done = False
        self.reward = 0

    def __posToCoord__(self, pos):
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


class MiniMax(object):
    def __init__(self):
        self.root = Node(['_', '_', '_', '_', '_', '_', '_', '_', '_'])
        self.__build__()
        self.__findNodeValues__()

    #
    # Creates the nodes of the tree. Builds all possible states of
    # the tictactoe board. It uses alpha-beta pruning which reduces
    # the amount of nodes by half.
    #
    def __build__(self):
        self.__buildHelper__(self.root, True)

    def __buildHelper__(self, node, maxPlayer):
        # Return if board is full
        if '_' not in node.board:
            node.done = True
            node.reward = 0
            return

        # Try all squares at the board
        for i in range(9):
            if node.board[i] == '_':
                board = node.board.copy()
                if maxPlayer:
                    board[i] = 'X'
                else:
                    board[i] = 'O'

                child = Node(board, i)
                reward = self.__checkForWinner__(board)
                if reward == 1:
                    child.done = True
                    child.reward = 1
                    node.children.append(child)

                    # pruning
                    if maxPlayer:
                        return
                elif reward == -1:
                    child.done = True
                    child.reward = -1
                    node.children.append(child)

                    # pruning
                    if not maxPlayer:
                        return
                else:
                    node.children.append(child)
                    self.__buildHelper__(child, not maxPlayer)

    #
    # Inspects the board for a winner and returns the appropriate reward.
    #
    def __checkForWinner__(self, board):
        if board[0] == 'X' and board[1] == 'X' and board[2] == 'X':
            return 1
        if board[3] == 'X' and board[4] == 'X' and board[5] == 'X':
            return 1
        if board[6] == 'X' and board[7] == 'X' and board[8] == 'X':
            return 1
        if board[0] == 'X' and board[3] == 'X' and board[6] == 'X':
            return 1
        if board[1] == 'X' and board[4] == 'X' and board[7] == 'X':
            return 1
        if board[2] == 'X' and board[5] == 'X' and board[8] == 'X':
            return 1
        if board[0] == 'X' and board[4] == 'X' and board[8] == 'X':
            return 1
        if board[2] == 'X' and board[4] == 'X' and board[6] == 'X':
            return 1

        if board[0] == 'O' and board[1] == 'O' and board[2] == 'O':
            return -1
        if board[3] == 'O' and board[4] == 'O' and board[5] == 'O':
            return -1
        if board[6] == 'O' and board[7] == 'O' and board[8] == 'O':
            return -1
        if board[0] == 'O' and board[3] == 'O' and board[6] == 'O':
            return -1
        if board[1] == 'O' and board[4] == 'O' and board[7] == 'O':
            return -1
        if board[2] == 'O' and board[5] == 'O' and board[8] == 'O':
            return -1
        if board[0] == 'O' and board[4] == 'O' and board[8] == 'O':
            return -1
        if board[2] == 'O' and board[4] == 'O' and board[6] == 'O':
            return -1

        return 0

    #
    # Propagates the terminal values to the top of the tree
    #
    def __findNodeValues__(self):
        self.__findNodeValuesHelper__(self.root, True)

    def __findNodeValuesHelper__(self, node, maxState):
        if node.done: return

        for child in node.children:
            self.__findNodeValuesHelper__(child, not maxState)

        if maxState:
            node.done = True
            maxVal = -9
            for child in node.children:
                if child.reward > maxVal:
                    maxVal = child.reward

            node.reward = maxVal
        else:
            node.done = True
            minVal = 9
            for child in node.children:
                if child.reward < minVal:
                    minVal = child.reward

            node.reward = minVal

    #
    # Returns the size of the tree
    #
    def size(self):
        return self.__sizeHelper__(self.root)

    def __sizeHelper__(self, node):
        size = 1
        for child in node.children:
            size += self.__sizeHelper__(child)
        return size


#
# Returns the best child of node depending on if we are
# maximizing or minimizing.
#
def pickNode(node, maxState):
    if not node.children: return None

    val = 0
    if maxState:
        val = -9
        for child in node.children:
            if child.reward > val:
                val = child.reward
    else:
        val = 9
        for child in node.children:
            if child.reward < val:
                val = child.reward

    nodes = []
    for child in node.children:
        if child.reward == val:
            nodes.append(child)

    rand = random.randrange(0,len(nodes))
    bestNode = nodes[rand]
    return bestNode

#
# Reads previous actions from a file and gets to that state in
# the tree. Then finds the best action to perform with regards
# to which player it is.
# Prints out the coordinates of the players next action.
#
def play(player, board, node):
    file = open('turns.txt', 'a+')
    file.seek(0)
    turns = file.read()

    if turns == '':
        if player == 'X':
            node = pickNode(node, True)
        elif player == 'O':
            for child in node.children:
                if child.board == board:
                    node = child
                    break
            node = pickNode(node, False)

    else:
        turns = turns.split(' ')
        for turn in turns:
            for child in node.children:
                if child.board == list(turn):
                    node = child
                    break

        for child in node.children:
            if child.board == board:
                node = child
                break

        if player == 'X':
            node = pickNode(node, True)
        elif player == 'O':
            node = pickNode(node, False)

    file.seek(2)
    file.write(''.join(board) + ' ')
    file.write(''.join(node.board) + ' ')
    file.close()

    x, y = node.coord
    print(str(x) + ' ' + str(y))


def main():
    #t = time.time()
    minimax = MiniMax() # Construct the minimax tree
    #print('--- %s seconds to build minimax tree ---' % (time.time() - t))
    #print('--- %d nodes in the tree ---' % (minimax.size()))

    player = input()
    board = input()
    board += input()
    board += input()
    board = list(board)

    play(player, board, minimax.root) # Determine the next action


if __name__ == "__main__":
    main()



