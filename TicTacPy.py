#initial board has position numbers to introduce to user
board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
#number of players
pnum = 2

#function to show board
def printBoard(brd):
    print()
    print(
        brd[0],' | ',brd[1],' | ',brd[2],
        "\n---------\n",
        brd[3],' | ',brd[4],' | ',brd[5],
        "\n---------\n",
        brd[6],' | ',brd[7], ' | ',brd[8],
        sep='')
    
#function to clear out board
def bClear():
    for q in range(len(board)):
        board[q] = ' '


#list of players(empty initially)
l = []
for j in range(pnum):  #create an element for each player
    l.append('')

#-----------defining class player------------#

sym = ['O', 'X']  #symbols O and X


class player:
    def __init__(self, nm, scr, symb):
        self.nm = nm
        self.scr = scr
        self.symb = symb


#----------------function for each turn----------------#
def pTurn(k):
    while True:
        print(l[k].nm, ", enter box number ", end='')
        # try:
        pPos = int(input("")) - 1

        if board[pPos] != ' ':
            print(
                "\n\tInvalid turn. Box is already filled. Pick another box.\n")
            continue
        else:
            board[pPos] = l[k].symb
            fWin(k)
            break
        except:
             print("\n\tPlease enter a valid position number\n")
             continue

    printBoard(board)

#-----------------------winning code-----------------------#
winState = False


def fWin(k):
    for i in range(0, 9, 3):
        j = int(i / 3)
        c1 = board[i] != ' ' and board[i] == board[i + 1] and board[
            i + 1] == board[i + 2]
        c2 = board[j] != ' ' and board[j + 3] == board[j] == board[j + 6]
        c3 = board[4] != ' ' and (board[0] == board[4] == board[8]
                                  or board[2] == board[4] == board[6])  #✨I didn't really want to specify the exact index numbers so that I can maybe extend the grid to 4*4 or 5*5 in the future (based on user preference), but I also didn't know how else to do this
        if c1 == True or c2 == True or c3 == True:
            print('\n\n\n\t--------you won, ', l[k].nm, '--------')
            global winState
            winState = True
            break


#------------------------game starts------------------------#

#introduce game to player
print(
    "These are the position numbers for each position. Enter the number for whichever position you want to put you symbol in when prompted"
)
printBoard(board)

#player n enters info
for i in range(pnum):
    print("Enter your name, Player ", i + 1, "(", sym[i], ")", end='')
    nme = input()
    l[i] = player(nme, 0, sym[i])

bClear()
#game starts
print("\nWelcome to TicTacPy! \n")

k = 0
while True:
    if winState == True:        #✨ should I instead do a thing where it just switched to the next symbol after each move instead of all this?
        break
    else:
        pTurn(k)
        if k == 0:
            k = 1
        elif k == 1:
            k = 0
