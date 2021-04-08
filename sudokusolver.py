from random import randint

grid = [[0, 2, 0,  0, 0, 9,  5, 0, 0],
        [9, 0, 0,  7, 0, 0,  3, 2, 0],
        [6, 0, 0,  4, 5, 0,  1, 0, 0],

        [8, 0, 1,  5, 0, 0,  0, 6, 2],
        [3, 4, 0,  6, 0, 0,  0, 1, 0],
        [2, 5, 6,  1, 0, 0,  4, 3, 0],

        [1, 0, 0,  0, 0, 4,  0, 0, 8],
        [0, 0, 4,  8, 3, 5,  2, 0, 0],
        [5, 0, 8,  0, 0, 0,  7, 4, 0]]

#------fucntion to print grid------#
def print_grid():
    print("____________________________")
    for i in range(0, 3):
        print(grid[i])
        print("----------------------------")
        print(grid[i+1])
        print("----------------------------")
        print(grid[i+2])
        print("____________________________")


def verify(i, j, k):
    col = []

    for f in range(0, 9):
        col.append(grid[f][j])

    for a in grid[i]:
        if a == k:
            return False

    for c in col:
        if c == k:
            return False

    if i % 3 == 1:
        if j % 3 == 1:
            if k in [grid[i][j-1], grid[i][j+1], grid[i-1][j-1], grid[i-1][j], grid[i-1][j+1]]:
                return False

        elif j % 3 == 0:
            if k in [grid[i][j+2], grid[i][j+1], grid[i-1][j+2], grid[i-1][j], grid[i-1][j+1]]:
                return False

        elif j % 3 == 2:
            if k in [grid[i][j-1], grid[i][j-2], grid[i-1][j-1], grid[i-1][j], grid[i-1][j-2]]:
                return False

    if i % 3 == 2:
        if j % 3 == 1:
            if k in [grid[i][j-1], grid[i][j+1], grid[i-1][j-1], grid[i-1][j], grid[i-1][j+1], grid[i-2][j-1], grid[i-2][j], grid[i-2][j+1]]:
                return False

        elif j % 3 == 0:
            if k in [grid[i][j+2], grid[i][j+1], grid[i-1][j+2], grid[i-1][j], grid[i-1][j+1], grid[i-2][j+2], grid[i-2][j], grid[i-2][j+1]]:
                return False

        elif j % 3 == 2:
            if k in [grid[i][j-1], grid[i][j-2], grid[i-1][j-1], grid[i-1][j], grid[i-1][j-2], grid[i-2][j-1], grid[i-2][j], grid[i-2][j-2]]:
                return False


def next_empty():
    list1=[]
    for i in range(0, 9):
        for j in range(0, 9):
            if grid[i][j] == 0:
                return i, j
    for q in grid:
        for w in q:
            list1.append(w)
    c=0
    for o in list1:
        if o == 0:
            c+=1
    
    if c == 0:
        print('All filled')
        return False


# Solving the grid
print("------------------------------START--------------------------------")

def solve(m, n):
        for k in range(1,9):
            ver = verify(m, n, k)

            if ver != False:
                grid[m][n] = k
                a, b = next_empty()
                solve(a, b)
                
            if next_empty()== False:
                print('\t\tBREAKING\t\t')
                break


solve(0, 0)
print_grid()
