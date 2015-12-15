#!/bin/python
import random


class Node:

	def __init__(self, gameState, i, j):
		self.state       = gameState
		self.value       = 0
		self.children    = []
		self.xCoordinate = i
		self.yCoordinate = j
		self.hasValue    = False

def formNewState(world, i, j, player):
	newState = []

	for k in range(3):
		if(k == i):
			# get the row
			row = world[i]
			# convert to list
			l = list(row)
			# change the world accordingly
			l[j] = player
			newState.append("".join(l))
		else:
			newState.append(world[k])
	new_list = list(newState)
	return new_list

def isWinState(world):

	winner = None
	# horizontal checks
	if(world[0][0] == world[0][1] == world[0][2] == "X"):
		winner = "X"
	elif(world[1][0] == world[1][1] == world[1][2] == "X"):
		winner = "X"
	elif(world[2][0] == world[2][1] == world[2][2] == "X"):
		winner = "X"

	# vertical checks
	elif(world[0][0] == world[1][0] == world[2][0] == "X"):
		winner = "X"
	elif(world[0][1] == world[1][1] == world[2][1] == "X"):
		winner = "X"
	elif(world[0][2] == world[1][2] == world[2][2] == "X"):
		winner = "X"

	# diagonal checks
	elif(world[0][0] == world[1][1] == world[2][2] == "X"):
		winner = "X"
	elif(world[0][2] == world[1][1] == world[2][0] == "X"):
		winner = "X"

	if(world[0][0] == world[0][1] == world[0][2] == "O"):
		winner = "O"
	elif(world[1][0] == world[1][1] == world[1][2] == "O"):
		winner = "O"
	elif(world[2][0] == world[2][1] == world[2][2] == "O"):
		winner = "O"

	# vertical checks
	elif(world[0][0] == world[1][0] == world[2][0] == "O"):
		winner = "O"
	elif(world[0][1] == world[1][1] == world[2][1] == "O"):
		winner = "O"
	elif(world[0][2] == world[1][2] == world[2][2] == "O"):
		winner = "O"

	# diagonal checks
	elif(world[0][0] == world[1][1] == world[2][2] == "O"):
		winner = "O"
	elif(world[0][2] == world[1][1] == world[2][0] == "O"):
		winner = "O"
	return winner

def setValue(player):
	if(player == "X"):
		return 1
	else:
		return -1

def isDraw(newWorld):
	count = 0
	for i in range(3):
		for j in range(3):
			if(newWorld[i][j] == "_"):
				count += 1
	return count == 0

def nextPlayer(player):
	if player == "X":
		return "O"
	else:
		return "X"

def initializePossibleMoves(board, node, player):
	for i in range(3):
		for j in range(3):
			if board[i][j] == "_":
				newBoard = formNewState(board, i, j, player)
				newNode  = Node(newBoard, i, j)
				node.children.append(newNode)


def getValueByDFS(board, player, alpha, beta):
	winner = isWinState(board)
	if(winner):
		return setValue(winner)
	elif(isDraw(board)):
		return 0
	else:
		if(player == "X"):
			currentBest = -10
		else:
			currentBest = 10
		for i in range(3):
			for j in range(3):
				if board[i][j] == "_":
					newBoard = formNewState(board, i, j, player)
					if(player == "X"):
						currentBest = max(currentBest, getValueByDFS(newBoard, nextPlayer(player), alpha, beta))
						alpha = max(alpha, currentBest)
					else:
						currentBest = min(currentBest, getValueByDFS(newBoard, nextPlayer(player), alpha, beta))
						beta = min(beta, currentBest)

					if(beta <= alpha):
						break
		return currentBest

def nextMove(childrenNodes, player):
	if(player == "X"):
		currentBest = childrenNodes[0]
		for c in childrenNodes:
			if c.value > currentBest.value:
				currentBest = c
		print(currentBest.xCoordinate, currentBest.yCoordinate)
	else:
		currentBest = childrenNodes[0]
		for c in childrenNodes:
			if c.value < currentBest.value:
				currentBest = c
		print(currentBest.xCoordinate, currentBest.yCoordinate)

def main():
	player = input()
	row1 = input()
	row2 = input()
	row3 = input()

	board = []
	board.append(row1)
	board.append(row2)
	board.append(row3)

	node = Node(board, None, None)
	
	initializePossibleMoves(board, node, player)
	for c in node.children:
		c.value = getValueByDFS(c.state, nextPlayer(player), -10, 10)

	nextMove(node.children, player)

if __name__ == '__main__':
	main()






