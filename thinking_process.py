import random
indi = [['top','mid','low'],['L','M','R']]
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


def think(board,xMove,player):
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