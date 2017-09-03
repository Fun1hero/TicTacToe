from __future__ import print_function
from IPython.display import clear_output
import random

def display_board(board):
    clear_output()
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

def player_input():
    marker = ''
    
    while not (marker == 'O' or marker == 'X'):
        marker = raw_input('Player 1: Do you want to be X or O: ').upper()
    if marker == 'X':
        return('X','O')
    else:
        return('O','X')
    
def place_marker(board, marker, position):
        board[position] = marker

def win_check(board,mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal

def choose_first():
    if int(random.randint(0,1)) == 0:
        return 'Player 1'
    else:
        return 'Player 2'

def space_check(board, position):
    return board[position] == ' '

def is_taken(board, position):
    if board[position] == 'X':
        print('This spot is already taken! Choose free one.')
        return False
    elif board[position] == 'O':
        print('This spot is already taken! Choose free one.')
        return False
    else:
        return True   
    #return board[position] != 'X' or board[position] != 'O'

def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

def played_choise(board):
    position = ' '
    
    while position not in '1 2 3 4 5 6 7 8 9'.split() or not space_check(board, int(position)):
        position = raw_input('Choose your next position(1-9): ')
        if position != '' and position.isdigit() and int(position) in [i for i in range(1,9)]:
            if is_taken(board, int(position)):
                return int(position)
            
def replay():
    return raw_input('Do you want to play again?(Yes/no)').lower().startswith('y')

def game_step(turn, the_board, player_marker):
    global game_on
    print(turn, game_on)
    display_board(the_board)
    position = played_choise(the_board)
    place_marker(the_board, player_marker, position)
            
    if win_check(the_board, player_marker):
        display_board(the_board)
        print('Congratulations,' + turn + ', has won the game!')
        game_on = False
    else:
        if full_board_check(the_board):
            display_board(the_board)
            print('The game is draw!')
    return the_board

#ALL STUFF---------------------------------------------------------///////////////////////////////////////
print('Welcome to TicTacToe game!')


while True:
    the_board = [' ']*10
    
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')
    
    game_on = True
    
    while game_on:
        if turn == 'Player 1':
            game_step(turn, the_board, player1_marker)
            turn = 'Player 2'
        else:
            game_step(turn, the_board, player2_marker)
            turn = 'Player 1'
    if not replay():
        break