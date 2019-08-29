import random
def printBoard(board):
    print(board['top-L'],'|',board['top-M'],'|',board['top-R'])
    print('----------')
    print(board['mid-L'],'|',board['mid-M'],'|',board['mid-R'])
    print('----------')
    print(board['low-L'],'|',board['low-M'],'|',board['low-R'])

def winChecker(board):
    if(
        board['top-L'] + board['top-M'] + board['top-R'] == 'XXX' or
        #----------------------------------------------------------
        board['mid-L'] + board['mid-M'] + board['mid-R'] == 'XXX' or
        #----------------------------------------------------------
        board['low-L'] + board['low-M'] + board['low-R'] == 'XXX' or
        #----------------------------------------------------------
        board['top-L'] + board['mid-L'] + board['low-L'] == 'XXX' or
        #----------------------------------------------------------
        board['top-M'] + board['mid-M'] + board['low-M'] == 'XXX' or
        #----------------------------------------------------------
        board['top-R'] + board['mid-R'] + board['low-R'] == 'XXX' or
        #----------------------------------------------------------
        board['top-L'] + board['mid-M'] + board['low-R'] == 'XXX' or
        #----------------------------------------------------------
        board['low-L'] + board['mid-M'] + board['top-R'] == 'XXX'
    ):
        return 'X'
    elif(
        board['top-L'] + board['top-M'] + board['top-R'] == 'OOO' or
        #----------------------------------------------------------
        board['mid-L'] + board['mid-M'] + board['mid-R'] == 'OOO' or
        #----------------------------------------------------------
        board['low-L'] + board['low-M'] + board['low-R'] == 'OOO' or
        #----------------------------------------------------------
        board['top-L'] + board['mid-L'] + board['low-L'] == 'OOO' or
        #----------------------------------------------------------
        board['top-M'] + board['mid-M'] + board['low-M'] == 'OOO' or
        #----------------------------------------------------------
        board['top-R'] + board['mid-R'] + board['low-R'] == 'OOO' or
        #----------------------------------------------------------
        board['top-L'] + board['mid-M'] + board['low-R'] == 'OOO' or
        #----------------------------------------------------------
        board['low-L'] + board['mid-M'] + board['top-R'] == 'OOO'
    ):
        return 'O'
    elif(
        board['top-L'] != ' ' and board['top-M'] != ' ' and board['top-R'] != ' ' and
        #----------------------------------------------------------
        board['mid-L'] != ' ' and board['mid-M'] != ' ' and board['mid-R'] != ' ' and
        #----------------------------------------------------------
        board['low-L'] != ' ' and board['low-M'] != ' ' and board['low-R'] != ' '
    ):
        return 'draw'
    else:
        return 0

def randomMove(board):
    row = random.randint(0,2)
    column = random.randint(0,2)
    cpumove = indi[0][row] + '-' + indi[1][column]
    if(board[cpumove] == ' '):
        return cpumove
    else:
        while(board[cpumove] != ' '):
            row = random.randint(0,2)
            column = random.randint(0,2)
            cpumove = indi[0][row] + '-' + indi[1][column]
        return cpumove


def think(board,xMove):
    xMove = xMove.split('-')
    counter = 0
    if(board['top-L'] == player and board['mid-M'] == player):
        if(board['low-R'] == ' '):
            return('low-R')
    if(board['low-R'] == player and board['mid-M'] == player):
        if(board['top-L'] == ' '):
            return('top-L')
    if(board['top-L'] == player and board['low-R'] == player):
        if(board['mid-M'] == ' '):
            return('mid-M')
    if(board['top-R'] == player and board['mid-M'] == player):
        if(board['low-L'] == ' '):
            return('low-L')
    if(board['top-R'] == player and board['low-L'] == player):
        if(board['mid-M'] == ' '):
            return('mid-M')
    if(board['mid-M'] == player and board['low-L'] == player):
        if(board['top-R'] == ' '):
            return('top-R')
    for i in indi[1]:
        if(board[(xMove[0]+'-'+ i)] == player):
            counter += 1
    if(counter > 1):
        for i in indi[1]:
            if(board[(xMove[0]+'-'+ i)] == ' '):
                return (xMove[0]+'-'+i)
    else:
        for i in indi[0]:
            temp = i+'-'+ xMove[1]
            if(board[temp] == player):
                counter += 1
        if(counter > 1):
            for i in indi[0]:
                temp = i+'-'+ xMove[1]
                if(board[temp] == ' '):
                    return (temp)
            
    return randomMove(board)

def winnerPrinter(board):
    ans = winChecker(board)
    if(ans):
        printBoard(board)
        if(ans == player):
            print('You win!')
        elif(ans == cpu):
            print('Ha! I win.')
        elif(ans == 'draw'):
            print('Alas, it\'s a draw')
        return 1
    else:
        return 0


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
#-----------------------------------------------------------------------------------------------------
indi = [['top','mid','low'],['L','M','R']]
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
        if(temp not in ipvalues):
            print('Enter valid input! Try Again.')
        elif(board[temp] != ' '):
            print('Already placed. Try again.')
        else:
            break

    board[temp] = player
    if(winnerPrinter(board)):
        break
    
    board[think(board,temp)] = cpu
    if(winnerPrinter(board)):
        break

    printBoard(board)
    #hemanth was here.
