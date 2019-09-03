from printBoard import printBoard
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

def winnerPrinter(board,player,cpu):
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