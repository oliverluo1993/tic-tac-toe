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

   myState=WLT( ScratchBoard, len(Board) )

   if (myState == Symbol): # Symbol wins!
    BestPosition = TrialPosition
    break # do not consider any other (possibly winning) moves

   # let the opponent choose its best move
   BestMove ( ScratchBoard, InvertSymbol(Symbol) )
   myState=WLT( ScratchBoard, len(Board) )

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

# Display the board
def drawBoard( Board, BoardSize ):
  for row in range(BoardSize):
    for column in range(BoardSize):
      print(Board[BoardSize * row + column], end =" ")
    print("\n ")

### THe BEGINNING OF THE MAIN FUNCTION!!

BoardSize=3
BoardSize2=BoardSize*BoardSize

OurTurn = 1 # random 0 or 1
OurSymbol = 1 # random: 1 or 2
OppSymbol = InvertSymbol(OurSymbol)

# how to best represent the board? X -> 1, O -> 2, empty cell -> 0
Board = []

for element_in_borad in range(0, BoardSize2):
    Board.append(0)

# start the main loop
while True:
  
  # Let user to decide the borad size and draw the board

  if OurTurn:
    BestMove( Board, OurSymbol )
    OurTurn = False
  else:
    GetInput( Board, OppSymbol )
    OurTurn = True

  State = WLT( Board, BoardSize )
  drawBoard ( Board, BoardSize )

  if State > 0 :
    break

## end of the main loop

if State==1:
  print("X wins!")
elif State==2:
  print("O wins!")
else:
  print("Tie")





