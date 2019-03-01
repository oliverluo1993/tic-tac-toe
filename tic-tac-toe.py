#!/Users/rustam/anaconda/bin/python
import sys 
import math

# This global variable keeps track of recursion depth
Depth = 0

# Library

# This recursive function updates one position in the Board
# and returns the best outcome for Symbol player
def BestMove( Board, Symbol ):
# Now the algorithm is quite dumb. It works only if it can reach the 
# bottom of the tree. To make it smarter we need to estimate how many 
# branches lead to win from the current state.

 global Depth
 BestOutcome = 0 # loss(0), tie(1), win(2)
 BestPosition = -1 # this is a local variable to keep current best move
 TrialOutcome = -1

 ScratchBoard=Board.copy()
 for TrialPosition in range(BoardSize2):

  # return the scratch board to its original state 
  # that is, the state before the last trial move
  ScratchBoard=Board.copy()

  if ScratchBoard[TrialPosition] == 0:

   ScratchBoard[TrialPosition] = Symbol
   myState=WLT( ScratchBoard, BoardSize )

   if (myState == Symbol): # Symbol wins!
    BestPosition = TrialPosition
    BestOutcome = 2
    break # do not consider any other (possibly winning) moves
   elif (myState == 3 and BestOutcome == 0): # It's a tie
    BestPosition = TrialPosition
    BestOutcome = 1
    continue

   # let the opponent choose its best move
   Depth += 1
   BestMove ( ScratchBoard, InvertSymbol(Symbol) )
   myState=WLT( ScratchBoard, BoardSize )
   Depth -= 1

   if (myState == InvertSymbol(Symbol) ): # Inverted symbol (opponent) wins!
    # reject this move simply by going to the next TrialPosition
    # so that the next BestMove is never called and 
    # this branch in the decision tree is terminated
    continue
   elif (myState == 3 and BestOutcome == 0): # It's a tie
    BestPosition = TrialPosition
    BestOutcome = 1
    continue

   # Step deeper in the recursive tree.
   # This is where the magic happens: 
   # if this BestMove returns a better outcome than the 
   # current best we accept the 
   Depth += 1
   TrialOutcome = BestMove ( ScratchBoard, Symbol )
   Depth -= 1
   if TrialOutcome > BestOutcome:
    BestPosition = TrialPosition
    BestOutcome = TrialOutcome

  #if (Depth==0):
  # print( (Depth+1)*"!", Symbol, TrialPosition, BestPosition, BestOutcome, ScratchBoard)

 # done with the main trial loop

 if BestOutcome > 0:
  Board[BestPosition] = Symbol
 else:
  # This handles an "impossible-to-win" situation:
  # We make a move into the first empty cell
  # in hope that the opponent does not make their best move
  for TrialPosition in range(0, BoardSize2):
   if Board[TrialPosition] == 0:
    Board[TrialPosition] = Symbol
    break

 #if (Depth==0):
 # print( (Depth+1)*">", Symbol, BestOutcome, BestPosition, Board)

 return BestOutcome


def WLT( Board, BoardSize ):
# returns 0-3 for undecided, X wins, O wins, tie, respectively
    state = 0

    # Check rows
    for irow in range(BoardSize):
      found_same = True
      symbol_col_1 = Board[irow * BoardSize]
      for icol in range(1, BoardSize):
        if symbol_col_1 != Board[irow * BoardSize + icol]:
          found_same = False
          break

      if found_same:
        return symbol_col_1

    # Check columns
    for icol in range(BoardSize):
      found_same = True
      symbol_row_1 = Board[icol]
      for irow in range(1, BoardSize):
        if symbol_row_1 != Board[irow * BoardSize + icol]:
          found_same = False
          break

      if found_same:
        return symbol_row_1

    # Check the fisrt Diagonals
    found_same = True
    symbol_diag_1 = Board[0]
    for i_element in range(1, BoardSize):
      if symbol_diag_1 != Board[i_element * BoardSize + i_element]:
        found_same = False
        break

    if found_same:
      return symbol_diag_1

    # Check the 2nd Diagonals
    found_same = True
    vairbale_one = BoardSize**2 - BoardSize
    symbol_diag_2 = Board[vairbale_one]
    for i_element in range(1, BoardSize):
      if symbol_diag_2 != Board[vairbale_one - BoardSize * i_element + i_element]:
        found_same = False
        break

    if found_same:
      return symbol_diag_2

    # Check tie
    for i_tie in range(BoardSize**2):
      if Board[i_tie] == 0:
          return state # Here the state is 0, which means undecided

    return 3 # return 3 means tie

def InvertSymbol( Symbol ):
 if Symbol==1:
  return 2
 elif Symbol==2:
  return 1
 else:
  sys.exit("Incorrect symbol")

def GetInput( Board, Symbol ):

 Accepted=False
 if Symbol == 1:
  CharSymbol = "X"
 else:
  CharSymbol = "Q"
 Prompt = "Enter position for %1s [0-%d]: " % (CharSymbol,BoardSize2-1)

 while not Accepted:
  
  InpPos = input(Prompt)
  try:
   int(InpPos)
   Accepted = int(InpPos) > -1 and int(InpPos) < BoardSize2
  except ValueError:
   Accepted = False

 Board[int(InpPos)] = Symbol


# Display the board
def drawBoard( Board ):
 BoardSize = int(math.sqrt(len(Board)))
 for row in range(BoardSize):
  for column in range(BoardSize):
   iBoard = Board[BoardSize * row + column]
   if iBoard == 0:
    Symbol = BoardSize * row + column
   elif iBoard == 1:
    Symbol = "X"
   else:
    Symbol = "Q"
   print(Symbol, end ="")
  print("")

### THe BEGINNING OF THE MAIN FUNCTION!!

BoardSize=3
BoardSize2=BoardSize*BoardSize

OurTurn = 1 # random 0 or 1
OurSymbol = 1 # random: 1 or 2
OppSymbol = InvertSymbol(OurSymbol)

# how to best represent the board? X -> 1, Q -> 2, empty cell -> 0
Board = []
for element_in_board in range(0, BoardSize2):
 Board.append(0)

# create initial Board
#Board[0]=1
#Board[6]=1
#Board[2]=2
#Board[3]=2
#Board[4]=2
#OurTurn = 1

# Draw empty board
if not OurTurn:
 drawBoard ( Board )

# start the main loop
while True:

 # Let user to decide the borad size and draw the board
 if OurTurn:
  print("Here is my move:")
  BestMove( Board, OurSymbol )
  OurTurn = False
 else:
  GetInput( Board, OppSymbol )
  OurTurn = True

 State = WLT( Board, BoardSize )
 drawBoard ( Board )

 if State > 0 :
  break

## end of the main loop

if State==1:
 print("X wins!")
elif State==2:
 print("Q wins!")
else:
 print("How unfortunate, it's a tie!")

