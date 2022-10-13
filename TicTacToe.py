#---Tic Tac Toe---
board = [[1,2,3],[4,5,6],[7,8,9]]
from random import randrange

def display(board):             #Displays the new tic tac toe board after each move
    horz = ('+'+'-'*7)*3+'+' 
    vert = ('|'+' '*7)*3+'|'
    
    print(horz+'\n'+vert)
    
    print("|  ",board[0][0],"  |  ",board[0][1],"  |  ",board[0][2],"  |")    
    print(vert+'\n'+horz+'\n'+vert)
    
    print("|  ",board[1][0],"  |  ",board[1][1],"  |  ",board[1][2],"  |")    
    print(vert+'\n'+horz+'\n'+vert)
    
    print("|  ",board[2][0],"  |  ",board[2][1],"  |  ",board[2][2],"  |")    
    print(vert+'\n'+horz)

def open(board):                #Scans the board for empty/open squares
    empty = []
    for row in range(3):
        for i in range(3):
            if board[row][i] not in ("X","O"):
                empty.append(board[row][i])
    return empty

def comp(board):                #Computer player randomly selects a empty square (square 1 to 9)
    move = randrange(10)
    if move in open(board):
        for row in range(3):
            for i in range(3):
                if board[row][i] == move:
                    board[row][i] = "X"
    else:
        comp(board)

def me(board):                  #Human player is asked for input during their turn
    try:
        move = int(input("You are 'O', Enter your an integer between 1-9: "))
        if move > 0 and move < 10 and move in open(board):
            for row in range(3):
                for col in range(3):
                    if board[row][col] == move:
                        board[row][col] = "O"
        elif move <= 0 or move >= 10:
            print("Enter a number from 1 to 9!")
            me(board)
        else:
            print("That square is not empty!")
            me(board)
    except:
        print("Not an integer!")
        me(board)

def victory(board, sign):       #scans board if any player (X or O) has won
    for row in board:
        if row == [sign,sign,sign]:
            return True
    columns = []
    for i in range(3):
        col = []
        for row in range(3):
            col.append(board[row][i])
            if len(col) == 3:
                columns += [col]
    for c in columns:
        if c == [sign,sign,sign]:
            return True
    if board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
        return True
    elif board[0][2] == sign and board[1][1] == sign and board[2][0] == sign:
        return True
    else:
        return False

def turn(board):                #To start the game, Human player is asked who goes first
    try:
        s = int(input("Enter 1 to go first, Enter 2 to go second, Enter 0 to be assigned randomly: "))
        x = []
        if s in (0,1,2):
            if s == 0:
                x = randrange(1,3)
                if x == 1:
                    me(board)
                    return x
                if x == 2:
                    comp(board)
                    return x
            elif s == 1:
                me(board)
                return s
            elif s == 2:
                comp(board)
                return s
        else:
            print("Enter 0, 1, or 2!")
            turn(board)
    except:
        print("Enter an integer!")
        turn(board)
        
def tic_tac_toe(board):         #Tic Tac Toe function includes previous functions to run the game
    x = turn(board)
    display(board)
    if x == 1:
        while victory(board, "O") == False and victory(board, "X") == False and open(board) != []:
            comp(board)
            display(board)
            if victory(board, "O") == False and victory(board, "X") == False and open(board) != []:
                me(board)
                display(board)
        if victory(board, "O") == True:
            return print("O WON!")
        elif victory(board, "X") == True:
            return print("X WON!")
        elif open(board) == []:
            return print("DRAW!")
    elif x == 2:
        while victory(board, "O") == False and victory(board, "X") == False and open(board) != []:
            me(board)
            display(board)
            if victory(board, "O") == False and victory(board, "X") == False and open(board) != []:
                comp(board)
                display(board)
        if victory(board, "O") == True:
            return print("O WON!")
        elif victory(board, "X") == True:
            return print("X WON!")
        elif open(board) == []:
            return print("DRAW!")
        
tic_tac_toe(board)


