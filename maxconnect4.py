#Resha Adhikari  1001739209     #3/8/2022
#python 3.9.10 not omega compatible
#code given as sample code is used, with only additional modification
#added new function called EvalFunc, Minimax and MinFunc and MaxFunc, remaining is same as given by professor
#alpha beta pruning and depth limited min max used
#very simple eval function used, but works perfectly

#References: https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning code from wikipedia
#            https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-4-alpha-beta-pruning/
#            https://stackabuse.com/minimax-and-alpha-beta-pruning-in-python/


#Run in command line:   python maxconnect4.py interactive input1.txt human-next 4  (example for interactive mode)
#                  :  python maxconnect4.py one-move input1.txt output1.txt 5      (example for one-move mode)


import sys
from MaxConnect4Game import *
import math
import copy
import time
from copy import deepcopy
COLUMN=7  
PIECE=42

def EvalFunc(currentGame):
    currentGame.countScore()
    return (currentGame.player1Score-currentGame.player2Score)
    #returns positive when player1Score>player2score
    #returns negative when player2score>player1score
    #returns 0 when player1score equal to player2score
    

def Minimax(currentGame):
   # print(state)
    Games = []  #contains all the possible games
    neg= -math.inf
    pos= math.inf
    count=0
    MinMaxGames = []   #MinMaxGames contains array of all the best moves
    finalSelection = []  #array of final selected column/position
    
    #create a new board that represents the next possible states in the board itself
    #for that we need to change the player's turn
    if currentGame.currentTurn == 1: #change turn to next player
        next_turn = 2
    elif currentGame.currentTurn==2:
        next_turn = 1
        
    #now that the turn is changed to next player, we are ready to build a new game
    while count<COLUMN: 
        newGame = maxConnect4Game() #create a new game with same attributes
        count=count+1 #increase counter
        newGame.currentTurn = next_turn #turn implemented
        newGame.gameBoard = deepcopy(currentGame.gameBoard) #newGame has the currentGame deep copied
        if newGame.playPiece(count-1):  #returns 1 if correclty placed in empty position
            Games.append((count-1, newGame)) #Game array contains all the possible new games with the counter
            #we do counter-1 bc we previously incremented counter
   
    count=0
    #From all the possible games in the Games array, we need to minimax the game array, so we can choose the perfect state
    for each in Games: #each is a double array type with index and game object
        Minimumvalue = MinFunc(each[1], neg, pos, deepcopy(currentGame.depthLimt))  #each[1] is the position of the object game
        #call the Min function from MinMax
        #Make double array named that has address of object_game(minmaxed) and minimum value)  
        MinMaxGames.append((each[0], Minimumvalue))  #each[0] is just an index

        #MinMaxGames contains array of all the best moves
   # print(MinMaxGames)    
    
    #to finalize the AI move, we make a new array and store the index and position there
    for index, obj_position in MinMaxGames:
        if count == 0:
            AIDecision = ((index, obj_position))
            count = count+ 1
            continue
        if obj_position > AIDecision[1]:
            AIDecision = ((index, obj_position))
        count=count+1
    #AIDecison[0] is the column chosen 
    chosenColumn= AIDecision[0]    
    
    return chosenColumn  #returns the column chosen by AI


 
def MaxFunc(currentGame, alpha, beta, depth):
    value = -math.inf
    Games=[]
    count=0
    if depth==1 or currentGame.checkPieceCount() == PIECE-1:
        utility_score=EvalFunc(currentGame)
        return utility_score
    else:    
        if currentGame.currentTurn == 1: #change player's turn
            next_turn= 2
        else:
            next_turn = 1
        #create a array that stores future possible game moves with next turn
        while count<COLUMN: 
            newGame = maxConnect4Game() #create a new game with same attributes
            count=count+1 #increase counter
            newGame.currentTurn = next_turn #turn implemented
            newGame.gameBoard = deepcopy(currentGame.gameBoard) #newGame has the currentGame deep copied
            if newGame.playPiece(count-1):  #returns 1 if correclty placed in empty position
                Games.append((count-1, newGame)) #Game array contains all the possible new games with the counter
            #we do count-1 bc we previously incremented counter
   
        for each in Games:
           
            temp= MinFunc(each[1], alpha, beta, deepcopy(depth - 1))
            value = max(value,temp)
            if value >= beta:
                return value
            alpha = max(alpha, value)
    return value

def MinFunc(currentGame, alpha, beta, depth):
    value= math.inf  
    Games = []  #contains all the possible games
    count=0
    if depth==1 or currentGame.checkPieceCount() == 41:
    #if it is terminal node, we just send the utility score of terminal node
        utility_score= EvalFunc(currentGame)
        return utility_score 
    else:
        if currentGame.currentTurn == 1: #change player's turn
            next_turn= 2
        else:
            next_turn = 1
        
        while count<COLUMN: 
            newGame = maxConnect4Game() #create a new game with same attributes
            count=count+1 #increase counter
            newGame.currentTurn = next_turn #turn implemented
            newGame.gameBoard = deepcopy(currentGame.gameBoard) #newGame has the currentGame deep copied
            if newGame.playPiece(count-1):  #returns 1 if correclty placed in empty position
                Games.append((count-1, newGame)) #Game array contains all the possible new games with the counter
            #we do count-1 bc we previously incremented counter        
     
        for each in Games:
        #loop through each value in array to get the value smaller than alpha        
            temp=MaxFunc(each[1], alpha, beta, deepcopy(depth - 1))
            #the return of these values is then compared to value(inf)
            value = min(value,temp)
            if value <= alpha: #basic alpha beta pruning
                return value
            beta = min(beta, value) #beta is the smallest val
    return value

    
def oneMoveGame(currentGame):
    if currentGame.pieceCount == PIECE:    # Is the board full already?
        print ('BOARD FULL\n\nGame Over!\n')
        sys.exit(0)

    # currentGame.aiPlay() # Make a move (only random is implemented)
    # currentGame.currentTurn = 2
    depth= deepcopy(currentGame.depthLimit) 
    selectedColumn = Minimax(currentGame)

    # currentGame.currentTurn = 1
    currentGame.playPiece(selectedColumn)
    print('\n\nmove %d: Player %d, column %d\n' % (currentGame.checkPieceCount(), currentGame.currentTurn, selectedColumn+1))

    print ('Game state after move:')
    currentGame.printGameBoard()

    currentGame.countScore()
    print('Score: Player 1 = %d, Player 2 = %d\n' % (currentGame.player1Score, currentGame.player2Score))

    currentGame.printGameBoardToFile()
    currentGame.gameFile.close()    


def interactiveGame(currentGame, firstMovePlayer):
        
    while not currentGame.pieceCount==PIECE:
        if firstMovePlayer == 'human-next':
            currentGame.currentTurn=1
            print("It is your turn")
            userInput= input('Enter a column number[1-7]: ')
            userInput= int(userInput)
            
            while userInput<1 or userInput>7:
                userInput= input('Input out of range. Enter a column number[1-7]: ')
                userInput= int(userInput)
            while not currentGame.playPiece(userInput-1):
                    userInput=input("Column is full, try again: ")
                    userInput= int(userInput)
                    if userInput<1 or userInput>COLUMN:
                        while userInput<1 or userInput>7:
                            userInput= input('Input out of range. Enter a column number[1-7]: ')
                            userInput= int(userInput)
              #  continue
            currentGame.countScore()
            print('\n\Human nmove %d: Player %d, column %d\n' % (currentGame.checkPieceCount(), currentGame.currentTurn, userInput + 1))
            currentGame.printGameBoard()
            print('Score: Player 1 = %d, Player 2 = %d\n' % (currentGame.player1Score, currentGame.player2Score))
            currentGame.gameFile = open('human.txt', 'w')
            currentGame.gameFile.close()
            if currentGame.pieceCount!=PIECE:
                print('\n\nAI turn now...computing...')
                start_time= time.time()
                print('Start time: ', start_time)
                currentGame.currentTurn = 2
                column=Minimax(currentGame)
                currentGame.playPiece(column)
                currentGame.countScore()
                print('move %d: Player %d, column %d\n' % (currentGame.checkPieceCount(), currentGame.currentTurn, column + 1))
                currentGame.printGameBoard()
                print('Score: Player 1 = %d, Player 2 = %d\n' % (currentGame.player1Score, currentGame.player2Score))
                currentGame.gameFile=open('computer.txt', 'w')
                currentGame.gameFile.close()  
                current_time=time.time()
                print("End time", current_time)
                print("AI execution time:", current_time-start_time, "seconds")
        elif firstMovePlayer=='computer-next':
            currentGame.currentTurn=2
            print("It is AI's turn")
            start_time= time.time()
            print('Start time: ', start_time)
            print('AI turn now...computing...')
            column= Minimax(currentGame)
            currentGame.playPiece(column)
            currentGame.countScore()
            print('move %d: Player %d, column %d\n' % (currentGame.checkPieceCount(), currentGame.currentTurn, column + 1))
            currentGame.printGameBoard()
            print('Score: Player 1 = %d, Player 2 = %d\n' % (currentGame.player1Score, currentGame.player2Score))
            currentGame.gameFile=open('computer.txt', 'w')
            currentGame.gameFile.close()
            current_time=time.time()
            print("End time", current_time)
            print("AI execution time:", current_time-start_time)
            if currentGame.pieceCount!=PIECE:
                currentGame.currentTurn=1
                print("It is your turn now")
                userInput= input('Enter a column number[1-7]: ')
                userInput= int(userInput)
                while userInput<1 or userInput>7:
                    userInput= input('Input out of range. Enter a column number[1-7]: ')
                    userInput= int(userInput)
                while not currentGame.playPiece(userInput-1):
                    userInput=input("Column is full, try again: ")
                    userInput= int(userInput)
                    if userInput<1 or userInput>COLUMN:
                        while userInput<1 or userInput>7:
                            userInput= input('Input out of range. Enter a column number[1-7]: ')
                            userInput= int(userInput)
                    
              #  continue
                currentGame.countScore()
                print('\n\Human nmove %d: Player %d, column %d\n' % (currentGame.checkPieceCount(), currentGame.currentTurn, userInput + 1))
                currentGame.printGameBoard()
                print('Score: Player 1 = %d, Player 2 = %d\n' % (currentGame.player1Score, currentGame.player2Score))
                currentGame.gameFile = open('human.txt', 'w')
                currentGame.gameFile.close()
                
            
            
    print('Board full, game over')
    currentGame.countScore()
    if (currentGame.player1Score>currentGame.player2Score):
        print('CONGRATULATIONS, you won against AI')
    elif (currentGame.player1Score<currentGame.player2Score):
        print('You lost, AI won. Thank you for playing')
    else:
        print("It's a Tie! Thank you for playing")
    sys.exit(0)
                  
            


def main(argv):
    # Make sure we have enough command-line arguments
    if len(argv) != 5:
        print ('Four command-line arguments are needed:')
        print('Usage: %s interactive [input_file] [computer-first/human-first] [depth]' % argv[0])
        print('or: %s one-move [input_file] [output_file] [depth]' % argv[0])
        sys.exit(2)

    game_mode, inFile = argv[1:3]

    if not game_mode == 'interactive' and not game_mode == 'one-move':
        print('%s is an unrecognized game mode' % game_mode)
        sys.exit(2)

    currentGame = maxConnect4Game() # Create a game

    currentGame.depthLimt = int(argv[4])

    if game_mode == 'one-move':
        # Try to open the input file
        try:
            currentGame.gameFile = open(inFile, 'r')
        except IOError:
            sys.exit("\nError opening input file.\nCheck file name.\n")

        # Read the initial game state from the file and save in a 2D list
        file_lines = currentGame.gameFile.readlines()
        currentGame.gameBoard = [[int(char) for char in line[0:7]] for line in file_lines[0:-1]]
        currentGame.currentTurn = int(file_lines[-1][0])
        currentGame.gameFile.close()
    else:
        isFileFound = 1
        # Try to open the input file
        try:
            currentGame.gameFile = open(inFile, 'r')
        except IOError:
            isFileFound = 0

        if isFileFound:
            # Read the initial game state from the file and save in a 2D list
            file_lines = currentGame.gameFile.readlines()
            currentGame.gameBoard = [[int(char) for char in line[0:7]] for line in file_lines[0:-1]]
            currentGame.currentTurn = int(file_lines[-1][0])
            currentGame.gameFile.close()

    print ('\nMaxConnect-4 game\n')
    print ('Game state before move:')
    currentGame.printGameBoard()    

    # Update a few game variables based on initial state and print the score
    currentGame.checkPieceCount()
    currentGame.countScore()
    print('Score: Player 1 = %d, Player 2 = %d\n' % (currentGame.player1Score, currentGame.player2Score))

    if game_mode == 'interactive':  
        firstMovePlayer = argv[3]
        if not firstMovePlayer == 'computer-next' and not firstMovePlayer == 'human-next':
            print('%s is an unrecognized player name' % firstMovePlayer)
            sys.exit(2)
        
        interactiveGame(currentGame, firstMovePlayer) # Be sure to pass whatever else you need from the command line
    else: # game_mode == 'one-move'
        # Set up the output file
        outFile = argv[3]
        try:
            currentGame.gameFile = open(outFile, 'w')
        except:
            sys.exit('Error opening output file.')
        oneMoveGame(currentGame) # Be sure to pass any other arguments from the command line you might need.


if __name__ == '__main__':
    main(sys.argv)
