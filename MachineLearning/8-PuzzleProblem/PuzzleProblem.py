import PuzzleBoard
from PuzzleBoard import *



"""
    Name: PuzzleProblem
    Description: This function maintains the initial and goal states for the 8-Puzzle Problem and contains methods for generating successors
                 of a given PuzzleBoard, and checking if a PuzzleBoard's configuration matches the goal state.
"""
class PuzzleProblem():

    #The initial state of the 8-Puzzle Problem
    initState = []
    
    #The goal state to reach for the 8-Puzzle Problem
    goalState = []



    """
        Name: isGoalState
        Description: This function checks if the given PuzzleBoard's state matches the goal state.

        Parameter: state            The state of the passed PuzzleBoard as its configuration.
        Return: true or false
    """
    def isGoalState(self, state):

        #If the passed PuzzleBoard's heuristic value is 0, the goal has been reached
        if (state.getHeuristicValue() == 0):
            return True

        #Else, it does not match the goal state
        else:
            return False



    """
        Name: getInitialState
        Description: Getter function for the initial state for the 8-Puzzle Problem.
    """
    def getInitialState(self):
        return self.initState


        
    """
        Name: getSuccessors
        Description: This function generates the successors for the given PuzzleBoard as all of the valid moves that can be made.
                     The valid moves generate new PuzzleBoards to be returned in a list.
        
        Parameter: currentBoard             The current PuzzleBoard to generate successors with
        Return: successorStates
    """
    def getSuccessors(self, currentBoard):
        
        #The list of possible valid successor states for the given board
        successorStates = []

        #Get the passed board's current layout and ID
        currentLayout = currentBoard.getBoardLayout()
        currentID = currentBoard.getID()

        #Boolean to check if a successor board formed by a move is valid
        validSuccessor = False

        #Get the goal state configuration
        goalConfiguration = self.goalState.getBoardLayout()

        #Make a new successor board by shifting the hole left
        leftSuccessor = PuzzleBoard(currentLayout, currentID)
        validSuccessor = leftSuccessor.makeMove('L')

        #If the move is valid, add it to the list of possible successors
        if (validSuccessor == True):
            leftSuccessor.calculateHeuristicValue(goalConfiguration)
            successorStates.append(leftSuccessor)

        #Make a new successor board by shifting the hole right
        rightSuccessor = PuzzleBoard(currentLayout, currentID)
        validSuccessor = rightSuccessor.makeMove('R')

        #If the move is valid, add it to the list of possible successors
        if (validSuccessor == True):
            rightSuccessor.calculateHeuristicValue(goalConfiguration)
            successorStates.append(rightSuccessor)

        #Make a new successor board by shifting the hole up
        upSuccessor = PuzzleBoard(currentLayout, currentID)
        validSuccessor = upSuccessor.makeMove('U')

        #If the move is valid, add it to the list of possible successors
        if (validSuccessor == True):
            upSuccessor.calculateHeuristicValue(goalConfiguration)
            successorStates.append(upSuccessor)

        #Make a new successor board by shifting the hole down
        downSuccessor = PuzzleBoard(currentLayout, currentID)
        validSuccessor = downSuccessor.makeMove('D')

        #If the move is valid, add it to the list of possible successors
        if (validSuccessor == True):
            downSuccessor.calculateHeuristicValue(goalConfiguration)
            successorStates.append(downSuccessor)

        return successorStates



    """
        Name: setGoalState
        Description: Setter function for the 8-Puzzle Problem's goal state or configuration. 
    """
    def setGoalState(self, goalState):
        self.goalState = goalState



    """
        Name: setInitialState
        Description: Setter function for the 8-Puzzle Problem's initial state or configuration. 
    """
    def setInitialState(self, initState):
        self.initState = initState
