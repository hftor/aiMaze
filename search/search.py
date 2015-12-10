# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    path = []
    discovered = []
    startState = problem.getStartState(), None, 0

    depthFirstSearchHelper(path, discovered, startState, problem)
    return path

#
# Recursive helper function for the depthFirstSearch.
#
def depthFirstSearchHelper(path, discovered, v, problem):
    vPoint = v[0]
    vDirection = v[1]
    discovered.append(vPoint)

    if problem.isGoalState(vPoint):
        path.append(vDirection)

    for w in problem.getSuccessors(vPoint):
        wPoint = w[0]
        wDirection = w[1]

        if wPoint not in discovered:
            if not path:
                depthFirstSearchHelper(path, discovered, w, problem)
                if path:
                    path.insert(0, wDirection)

def breadthFirstSearch(problem):
    q = util.Queue() # Stores all visited nodes that have not been expanded
    parent = { }     # Stores parents of all visited nodes

    startState = problem.getStartState(), None, 0
    q.push(startState)

    while not q.isEmpty():
        current = q.pop()

        # If we have reached the goal state we track the parent dict from goal to start
        if problem.isGoalState(current[0]):
            path = []
            path.insert(0, current[1])

            p = parent[current[0]]
            while p[1] is not None:
                path.insert(0, p[1])
                p = parent[p[0]]

            return path

        # Expand all adjacent nodes of current
        for n in problem.getSuccessors(current[0]):
            # Only visit n if it is unvisited
            if n[0] not in parent:
                parent[n[0]] = current
                q.push(n)


def uniformCostSearch(problem):
	"""Search the node of least total cost first."""
	"*** YOUR CODE HERE ***"

	queue = util.PriorityQueue()
	path = []
	visited = []

	# startState:
	#((position), Direction, Cost)
	#(  (1,2)   ,   None   ,  0  )
	startState = problem.getStartState(), None, 0


	# startStateTupe:
	#(((position), Direction, Cost), Parent)
	#((  (1,2)   ,   None   ,  0  ), (None))
	startStateTuple = startState, None

	queue.push(startStateTuple, 0)

	while(not queue.isEmpty()):
		currentNode = queue.pop()

		currentNodePosition = currentNode[0][0]
		currentNodeCost     = currentNode[0][2]

		# check if the new node is a goal state
		if(problem.isGoalState(currentNodePosition)):
			queue.push(currentNode, 0)
			goalNode = currentNode
			break

		# mark the currentNode as visited
		visited.append(currentNodePosition)

		# go through all nodes of currentNode successors
		for n in problem.getSuccessors(currentNodePosition):
			possition = n[0]
			cost      = n[2]

			# Create a new tuple to keep track of the parent node
			newTuple = n, currentNode

			# If that node has not been visited, we will expand
			if(possition not in visited):
				queue.push(newTuple, currentNodeCost + cost)

	# Reconstruct the path
	path.append(goalNode[1][0][1])
	while goalNode[1][0][1] != None:
		path.insert(0, goalNode[1][0][1])
		goalNode = goalNode[1]

	return path


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
	"""Search the node that has the lowest combined cost and heuristic first."""
	"*** YOUR CODE HERE ***"
	queue = util.PriorityQueue()
	path = []
	visited = []

	# startState:
	#((position), Direction, Cost)
	#(  (1,2)   ,   None   ,  0  )
	startState = problem.getStartState(), None, 0


	# startStateTupe:
	#(((position), Direction, Cost), Parent)
	#((  (1,2)   ,   None   ,  0  ), (None))
	startStateTuple = startState, None

	queue.push(startStateTuple, heuristic(startState[0], problem))

	while(not queue.isEmpty()):
		currentNode = queue.pop()

		currentNodePosition = currentNode[0][0]
		currentNodeCost     = currentNode[0][2]

		# check if the new node is a goal state
		if(problem.isGoalState(currentNodePosition)):
			queue.push(currentNode, 0)
			goalNode = currentNode
			break

		# mark the currentNode as visited
		visited.append(currentNodePosition)

		# go through all nodes of currentNode successors
		for n in problem.getSuccessors(currentNodePosition):
			possition = n[0]
			cost      = n[2]

			# Create a new tuple to keep track of the parent node
			newTuple = n, currentNode

			# If that node has not been visited, we will expand
			if(possition not in visited):
				queue.push(newTuple, currentNodeCost + cost + heuristic(possition, problem))

	# Reconstruct the path
	path.append(goalNode[1][0][1])
	while goalNode[1][0][1] != None:
		path.insert(0, goalNode[1][0][1])
		goalNode = goalNode[1]

	return path


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
