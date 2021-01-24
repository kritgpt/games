# initial board has position numbers to introduce to user
# board properties
boardSize = 3
board = list(range(1, boardSize ** 2 + 1))
d_s = [i for i in range(0, boardSize ** 2, boardSize + 1)]  # diagonal slash 😛 the key with ?
d_b = [i for i in range(boardSize - 1, boardSize ** 2-1, boardSize-1)]  # diagonal backslash the one above enter!
# number of players
pnum = 2


# function to show board
def printBoard(brd):
    print()
    print(
        brd[0], ' | ', brd[1], ' | ', brd[2],
        "\n---------\n",
        brd[3], ' | ', brd[4], ' | ', brd[5],
        "\n---------\n",
        brd[6], ' | ', brd[7], ' | ', brd[8],
        sep='')


# function to clear out board


def bClear():
    for q in range(len(board)):
        board[q] = ' '


# list of players(empty initially)
l = []
for j in range(pnum):  # create an element for each player
    l.append('')

# -----------defining class player------------ #

sym = ['O', 'X']  # symbols O and X


class player:
    def __init__(self, nm, scr, symb):
        self.nm = nm
        self.scr = scr
        self.symb = symb


# ----------------function for each turn---------------- #
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
        # except:
        #      print("\n\tPlease enter a valid position number\n")
        #      continue
    printBoard(board)


# -----------------------winning code----------------------- #


winState = False


def fWin(k):
    for i in range(0, boardSize ** 2, boardSize):
        c1 = c2 = c3 = c4 =True
        init_r = board[i]
        for j in range(i + 1, i + boardSize):
            if board[j] != init_r or board[j] == " ":
                c1 = False
                break
        init_c = board[i // boardSize]
        for j in range(i // boardSize + boardSize, boardSize ** 2, boardSize):
            if board[j] != init_c or board[j] == " ":
                c2 = False
                break
        init_d = [board[d_s[0]], board[d_b[0]]]
        for j in range(boardSize):
            c3 = False if board[d_s[j]] != init_d[0] or board[d_s[j]] == " " else True
            c4 = False if board[d_b[j]] != init_d[1] or board[d_b[j]] == " " else True
        # j = int(i / 3)
        # c1 = board[i] != ' ' and board[i] == board[i + 1] == board[i + 2]
        # c2 = board[j] != ' ' and board[j + 3] == board[j] == board[j + 6]
        # c3 = board[4] != ' ' and (board[0] == board[4] == board[8]
        #                           or board[2] == board[4] == board[6])

        # ✨I didn't really want to specify the exact index numbers so that I can maybe extend the grid to 4*4 or 5*5 in the future (based on user preference), but I also didn't know how else to do this
        if c1 or c2 or c3:
            print('\n\n\n\t--------you won, ', l[k].nm, '--------')
            global winState
            winState = True
            break


# ------------------------game starts------------------------ #

# introduce game to player
print(
    "These are the position numbers for each position. Enter the number for whichever position you want to put you symbol in when prompted"
)
printBoard(board)

# player n enters info
for i in range(pnum):
    print("Enter your name, Player ", i + 1, "(", sym[i], ")", end=' : ')
    nme = input()
    l[i] = player(nme, 0, sym[i])

bClear()
# game starts
print("\nWelcome to TicTacPy! \n")

k = 0
while True:
    if winState:  # ✨ should I instead do a thing where it just switched to the next symbol after each move instead of all this?
        break
    else:
        pTurn(k)
        if k == 0:
            k = 1
        elif k == 1:
            k = 0
