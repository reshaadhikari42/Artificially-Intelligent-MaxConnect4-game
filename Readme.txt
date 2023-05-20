
python 3.9.10 not omega compatible
Artificical Intelligenct MaxConnect4 game created using eval function and alpha beta pruning minmax
This command line program is programmed in such a way that no matter what move you make, you will not be able to win the game
The game is programmed to process the future moves(depth that you require) and then take the decision
very simple eval function used, but works perfectly

References: https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning code from wikipedia
            https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-4-alpha-beta-pruning/
           https://stackabuse.com/minimax-and-alpha-beta-pruning-in-python/

#Run in command line:  python maxconnect4.py interactive input1.txt computer-next/human-next 4  -> 4 is the # of depth it processes before making the move
                    :  python maxconnect4.py one-move input1.txt output1.txt 5      (example for one-move mode) -> 5 is the # of depth it processes before making the move
                    
#Interactive mode
-Argument interactive specifies that the program runs in interactive mode.
-Argument [input_file] specifies an input file that contains an initial board state. This way we can start the program from a non-empty board state. If the input file does not exist, the program should just create an empty board state and start again from there.
-Argument [computer-first/human-first] specifies whether the computer should make the next move or the human.
-Argument [depth] specifies the number of moves in advance that the computer should consider while searching for its next move. In other words, this argument specifies the depth of the search tree. Essentially, this argument will control the time takes for the computer to make a move.

#one move mode
-Read the input file and initialize the board state and current score, as in interactive mode.
-Print the current board state and score. If the board is full, exit.
-Choose and make the next move.
-Print the current board state and score.
-Save the current board state to the output file IN EXACTLY THE SAME FORMAT THAT IS USED FOR INPUT FILES.
-Exit
                    
This is a command line game so instead of red and green marbles, I have used the digit 1 and 2 instead of the  marbles. The game does not end when one player connects four digits, but instead the game completes when the entire board is filled and the player with the higher score wins - which is the game since its artificially intelligent!

If you try depth of more than or equalo to 10, the game takes a while to process(more than a minute). 
