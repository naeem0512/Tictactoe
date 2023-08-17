#Printing the game board
#Take player input /
#Check for win or tie /
#Switch players
#Check for win or tie again

import random
import time

board  = [" - ", " - ", " - ",
          " - ", " - ", " - ",
          " - ", " - ", " - "]

current_player = 'X'
winner = None
game_running: bool = True

def print_game_board(board):
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('----------------')
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('----------------')
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])



def player_input(board):
    global current_player
    while True:
        inp = int(input('Enter a number between 1-9: '))
        if 9 >= inp >= 1:
            if inp != board[inp - 1]:
                board[inp-1] = current_player
                break
            else:
                print("Enter number within range or choose an unreserved position")
        else:
            print('Select a number between 1-9')

def check_horizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != ' - ':
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != ' - ':
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != ' - ':
        winner = board[6]
        return True

def check_vertical(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != ' - ':
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != ' - ':
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != ' - ':
        winner = board[2]
        return True

def check_diagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != ' - ':
        winner = board[0]
        return True
    elif board[6] == board[4] == board[2] and board[6] != ' - ':
        winner = board[6]
        return True

def check_tie(board):
    global game_running
    if ' - ' not in board:
        print_game_board(board)
        print("It's a tie")
        game_running = False

def check_win(board):
    global game_running
    if check_diagonal(board) or check_horizontal(board) or check_vertical(board):
        print(f"The winner is {winner}")
        print_game_board(board)
        game_running = False

def switch_player():
    global current_player
    if current_player == 'X':
        current_player = 'O'
    else:
        current_player = 'X'

def computer(board):
    while current_player == "O":
        position = random.randint(0,8)
        if board[position] == ' - ':
            board[position] = 'O'
            switch_player()



while game_running:
    print_game_board(board)
    player_input(board)
    check_win(board)
    check_tie(board)
    switch_player()
    time.sleep(1)
    computer(board)