#---Sudoku Solver---
def row_(board):                #creates new list of list of rows from sudoku board
    start = 0; row_ = []
    for i in range(9):
        row_.append(array(board)[start:start+9])
        start += 9
    return row_
    
def column_(board):             #creates new list of list of columns from sudoku board
    start = 0; col_ = []
    for i in range(9):
        col_.append(array(board)[start:81:9])
        start += 1
    return col_
        
def block_(board):              #creates new list of list of 3x3 section/block from sudoku board
    start = 0; blk_ = []
    for i in range(9):
        blk_.append(array(board)[start:start+3]+
                  array(board)[start+9:start+12]+
                  array(board)[start+18:start+21])
        start += 3
        if start in (9,36):
            start += 18
    return blk_

def complete(board):
    # Iterates through rows, columns, and blocks to find if numbers 1-9 are found
    incorrect = False
    for key in range(9):
        for number in [1,2,3,4,5,6,7,8,9]:
            if number not in row_(board)[key]:
                #print('Row', key+1, 'is missing number', number)
                #warning: removing comment above, will display all missing rows, interrupt console with ctrl+c
                incorrect = True
                
            if number not in column_(board)[key]:
                #print('Column', key+1, 'is missing number', number)
                #warning: removing comment above, will display all missing rows, interrupt console with ctrl+c
                incorrect = True
                
            if number not in block_(board)[key]:
                #print('Block', key+1, 'is missing number', number)
                #warning: removing comment above, will display all missing rows, interrupt console with ctrl+c
                incorrect = True
    if incorrect:
        return False
    else:
        return True

def display(board):
    count = 0
    #print('-'*77)
    print('+-------'*3 + '+')
    for a in array(board):
        #print(a, end = ' '*(8-len(str(a))))
        if count in range(0,82,9):
            print('|', end= ' ')
        print(a, end = ' ')
        count += 1
        if count in range(0,82,3):
            print('|', end = ' ')
        if count in range(0,82,9):
            print('')
        if count in range(0,82,27):
            #print('-'*77)
            print('+-------'*3 + '+')
        
def array(board):                   #creates an arrow of the board
    array = []
    for key in board:
        array.extend(key)
    return array

def scan(board):                    #scans rows/columns/blocks for empty squares and inserts numbers 1 to 9 if only one number is possible in that square
    R = row_(board); C = column_(board); B = block_(board)
    for row in range(9):
        for col in range(9):
            store = ''
            num = board[row][col]
            if num == 0:
                for missing in [1,2,3,4,5,6,7,8,9]:
                    if missing not in R[row] and\
                       missing not in C[col] and\
                       missing not in B[col//3 + row//3 *3]:
                        store += str(missing)
                board[row].insert(board[row].index(num),store)
                board[row].remove(num)
    
    for row in board:
        for number in row:
            if len(str(number)) > 1:
                row.insert(row.index(number),0)
                row.remove(number)

            elif isinstance(number, str):
                row.insert(row.index(number),int(number))
                row.remove(number)
    return board

recursion = 0

def solve(board):                   #solves the sudoku with recursion, if number of recrusions reach 25, deem it unsolvable
    global recursion
    if recursion > 25:
        recursion = 0
        return print('UNSOLVABLE!\n')
    if complete(scan(board)) == False:
        recursion += 1
        solve(scan(board))
    else:
        display(board)
        print('Recursions:',recursion,'\nThe Sudoku is Solved, CONGRATULATIONS!\n')


print('EASY DIFFICULTY')
solve([[6,0,3,0,4,2,0,0,1],
       [0,0,9,8,0,0,0,7,2],
       [0,8,0,1,0,9,0,0,0],
       [0,0,1,2,6,0,0,0,8],
       [0,0,0,9,5,8,0,0,0],
       [5,0,0,0,1,7,3,0,0],
       [0,0,0,3,0,4,0,1,0],
       [8,2,0,0,0,1,7,0,0],
       [1,0,0,7,2,0,8,0,4]])

print('MEDIUM DIFFICULTY')
solve([[0,0,0,0,0,0,0,9,0],
       [0,4,0,0,7,0,1,6,0],
       [2,9,0,0,1,0,0,3,4],
       [0,0,9,0,0,6,0,1,0],
       [7,0,0,0,4,0,0,0,3],
       [0,8,0,5,0,0,7,0,0],
       [9,7,0,0,2,0,0,4,1],
       [0,5,4,0,6,0,0,8,0],
       [0,1,0,0,0,0,0,0,0]])

print('MEDIUM DIFFICULTY')      
solve([[0,0,0,9,6,2,7,3,0],
       [0,0,0,0,0,5,0,0,0],
       [0,2,8,3,0,0,0,0,0],
       [6,7,2,0,0,0,8,9,0],
       [0,0,1,0,4,0,0,0,7],
       [0,0,0,0,2,0,1,6,0],
       [1,5,0,0,0,6,0,0,0],
       [0,0,0,7,5,0,0,1,0],
       [3,9,6,0,1,0,0,0,0]])

print('MEDIUM DIFFICULTY')      
solve([[0,0,0,3,0,2,0,0,4],
       [0,0,0,0,0,4,0,7,0],
       [4,1,0,0,0,0,0,9,5],
       [0,6,9,0,4,8,0,2,0],
       [0,0,0,0,2,0,0,0,0],
       [0,5,0,1,9,0,3,4,0],
       [6,4,0,0,0,0,0,1,8],
       [0,8,0,7,0,0,0,0,0],
       [2,0,0,4,0,1,0,0,0]])

print('MEDIUM DIFFICULTY UNSOLVABLE')
solve([[3,0,0,0,4,0,0,0,2],
       [0,0,0,0,0,0,4,0,9],
       [0,4,1,0,6,8,0,3,0],
       [0,0,0,9,8,0,5,7,0],
       [8,0,0,0,0,0,0,0,1],
       [0,6,9,0,2,5,0,0,0],
       [0,7,0,6,3,0,9,2,0],
       [4,0,3,0,0,0,0,0,0],
       [6,0,0,0,5,0,0,0,7]])

print('HARD DIFFICULTY UNSOLVABLE')
solve([[7,0,0,0,0,1,4,6,0],
       [0,0,0,3,0,0,0,0,0],
       [0,0,0,0,0,9,0,2,3],
       [0,1,0,0,6,3,0,0,0],
       [9,0,0,4,0,5,0,0,7],
       [0,0,0,7,9,0,0,5,0],
       [6,4,0,5,0,0,0,0,0],
       [0,0,0,0,0,2,0,0,0],
       [0,8,2,9,0,0,0,0,5]])


