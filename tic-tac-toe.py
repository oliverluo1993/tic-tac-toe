#!/Users/rustam/anaconda/bin/python
import sys 

# Library

def BestMove( Board, Symbol ):
# if there are no winning moves returns 0
# else updates the Board and returns the BestPosition
# ZZZ: now the algorithm is quite dumb. 
# to make it smarter we need to count how many branches lead to win from the current state

 # ZZZ! important to make sure that each copy of BestMove gets its own ScratchBoard
 ScratchBoard = Board[:]
 BestPosition = 0

 for TrialPosition in range(0, BoardSize2):
  if ScratchBoard[TrialPosition] == 0:

   ScratchBoard[TrialPosition] = Symbol

   myState=WLT( ScratchBoard )

   if (myState == Symbol): # Symbol wins!
    BestPosition = TrialPosition
    break # do not consider any other (possibly winning) moves

   # let the opponent choose its best move
   BestMove ( ScratchBoard, InvertSymbol(Symbol) )
   myState=WLT( ScratchBoard )

   if (myState == InvertSymbol(Symbol) ): # Inverted symbol (opponent) wins!
    # reject this move simply by going to the next TrialPosition
    # so that the next BestMove is never called and 
    # this branch in the decision tree is terminated
    continue

   # step deeper in the recursive tree,
   # this is where the magic happens: this copy of the BestMove returns
   # non-zero value if Symbol wins in the end AND
   # InvertedSymbol does not win at any stage
   if BestMove ( ScratchBoard, Symbol ) > 0:
    BestPosition = TrialPosition

 if BestPosition > 0:
  Board[BestPosition] = Symbol

 return BestPosition 


def WLT( Board ):
# returns 0-3 for undecided, X wins, O wins, tie, respectively


def InvertSymbol( Symbol ):
 if Symbol==1:
  return 2
 elif Symbol==2:
  return 1
 else:
  sys.exit("Incorrect symbol")

BoardSize=3
BoardSize2=BoardSize*BoardSize

OurTurn = 1 # random 0 or 1
OurSymbol = 1 # random: 1 or 2
OppSymbol = InvertSymbol(OurSymbol)

# how to best represent the board? X -> 1, O -> 2, empty cell -> 0
Board = []
for element_in_borad in range(0, BoardSize2):
    Board.append(0)

# Draw the board
def draw( borad_size ):
  board = ""
  for i in range( 2 * board_size - 1):
    if i%2 == 0:
      board += "|    " * (board_size + 1)
    else:
      board += " --- " * ( borad_size)
      board += "\n"

  print(board)


# start the main loop
while True:
  
  # Let user to decide the borad size and draw the board
  board_size = input("Please choose the board size: ")
  draw(board_size)


 if OurTurn:
  BestMove( Board, OurSymbol )
  OurTurn = False
 else:
  GetInput( Board, OppSymbol )
  OurTurn = True

 State = WLT( Board )
 DisplayBoard ( Board )

 if State > 0 :
  break

## end of the main loop

if State==1:
 print("X wins!")
elif State==2:
 print("O wins!")
else:
 print("Tie")





