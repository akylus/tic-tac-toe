import random
from printBoard import printBoard
from winChecker import winChecker,winnerPrinter
from thinking_process import think,randomMove

#-----------------------------------------------------------------------------------------------
print('+--------------------------------------------------------------------')
print('| Welcome to Akylus\' Tic-Tac-Toe.')
print('| This is a basic render of the game and is not very smart as of now.')
print('| But feel free to play and give your opinion.')
print('+--------------------------------------------------------------------')
print()
print('Game works like this. Below is the code you need to put for that corresponding box.')
print('top-L','|','top-M','|','top-R')
print('---------------------')
print('mid-L','|','mid-M','|','mid-R')
print('---------------------')
print('low-L','|','low-M','|','low-R')
print()
#-----------------------------------------------------------------------------------------------

ipvalues = [
    'top-L', 'top-M', 'top-R',
    'mid-L', 'mid-M', 'mid-R',
    'low-L', 'low-M', 'low-R'
]
board = {
    'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
    'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
    'low-L': ' ', 'low-M': ' ', 'low-R': ' '
}

print('Choose: X or O?')
while(1):
    player = input().upper()
    if(player != 'X' and player != 'O'):
        print('Enter X or O only! Try Again.')
    else:
        break

if(player == 'X'):
    cpu = 'O'
else:
    cpu = 'X'

while(1):
    print("Enter move:")
    while(1):
        temp = input()
        temp = temp[:4] + temp[-1].capitalize()
        if(temp not in ipvalues):
            print('Enter valid input! Try Again.')
        elif(board[temp] != ' '):
            print('Already placed. Try again.')
        else:
            break

    board[temp] = player
    if(winnerPrinter(board,player,cpu)):
        break
    
    board[think(board,temp,player)] = cpu
    if(winnerPrinter(board,player,cpu)):
        break

    printBoard(board)
