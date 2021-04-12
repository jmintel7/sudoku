#Rules
# 1. 1-9 in a cell
# 2. 1-9 in a row
# 3. 1-9 in column
# 4 no repetition in row column, row or cell
no_of_checks = 0
board=[
    [0,0,0,8,5,9,0,0,0],
    [0,0,5,0,1,0,2,0,0],
    [0,8,0,3,0,6,0,7,0],
    [6,0,2,0,0,0,3,0,7],
    [7,9,0,0,0,0,0,4,5],
    [5,0,3,0,0,0,1,0,8],
    [0,2,0,4,0,5,0,6,0],
    [0,0,9,0,7,0,8,0,0],
    [0,0,0,6,9,1,0,0,0]
]

def print_board(board):

    for rcount, row in enumerate(board):
        if (rcount) % 3 == 0 and rcount != 0:
            print('- - - - - - - - - - - - ')
        for ccount, cell in enumerate(row):

            cell = str(cell)
            if ccount == 8:
                print(cell)
            elif (ccount+1)%3==0:
                print(cell+' | ',end='')
            else:
                print(cell + ' ', end='')

def find_empty(boa):
    for i, row in enumerate(boa):
        for j, cell in enumerate(row):
            if cell == 0:
                return (i,j)
    return None

def valid(boa, num, row, col):

    #check row
    for i, cell in enumerate(boa[row]):
        if i == col:
            continue
        if cell == num:
            return False

    #check col
    for i in range(len(boa)):
        if i == row:
            continue
        if num == boa[i][col]:
            return False

    box_x = (row//3) * 3
    box_y = (col//3) * 3
    #check cell
    for i in range(box_x,box_x+3):
        for j in range(box_y,box_y+3):
            if (i==row) and (j==col):
                continue
            if num == boa[i][j]:
                return False
    return True

def fill(board):
    global no_of_checks
    find = find_empty(board)
    # print(f'find: {find}')
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        no_of_checks += 1
        if valid(board, i, row, col):
            board[row][col] = i

            if fill(board):
                return True

            board[row][col] = 0

    return False



print_board(board)
fill(board)
print('Solution')
print('----------------------------------------------')
print_board(board)
print(f'No of checks done: {no_of_checks}')

