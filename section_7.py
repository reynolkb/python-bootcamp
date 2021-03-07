# row1 = [' ',' ',' ']
# row2 = [' ','X',' ']
# row3 = [' ',' ',' ']

# def display(row1,row2,row3):
#     print(row1)
#     print(row2)
#     print(row3)

# display(row1,row2,row3)

# ---------------------------------------- Validating User Input ----------------------------------------
# def user_choice():

#     # variables

#     # initial choice
#     choice = 'WRONG'
#     # acceptable range
#     acceptable_range = range(0,10)
#     within_range = False

#     # two conditions to check
#     # digit or within_range == false

#     while choice.isdigit() == False or within_range == False:
#         choice = input('Please enter a number (0-10): ')

#         # digit check
#         if choice.isdigit() == False:
#             print("sorry that is not a digit")
        
#         # range check
#         if choice.isdigit() == True:
#             if int(choice) in acceptable_range:
#                 within_range = True
#             else:
#                 print("Sorry, you are out of acceptable range (0-10)")
#                 within_range = False

#     return int(choice)

# # print(user_choice())
# user_choice()

# ---------------------------------------- Simple User Interaction ----------------------------------------

# game_on = True
# game_list = [0,1,2]

# def display_game(game_list):
#     print("Here is the curent list: ")
#     print(game_list)

# def position_choice():

#     choice = 'wrong'

#     while choice not in ['0', '1', '2']:
#         choice = input("Pick a position (0,1,2): ")
#         if choice not in ['0','1','2']:
#             print('Sorry, invalid choice! ')
    
#     return int(choice)

# def replacement_choice(game_list, position):
#     user_placement = input("Type a string to place at position: ")
#     game_list[position] = user_placement
#     return game_list

# def gameon_choice():

#     choice = 'wrong'

#     while choice not in ['Y', 'N']:
#         choice = input("Keep playing? (Y or N) ")
#         if choice not in ['Y', 'N']:
#             print("Sorry, I don't understand, please choose Y or N")
    
#     if choice == "Y":
#         return True
#     else:
#         return False

# while game_on:
#     display_game(game_list)
#     position = position_choice()
#     game_list = replacement_choice(game_list, position)
#     display_game(game_list)
#     game_on = gameon_choice()

# ---------------------------------------- Milestone Project 1 ----------------------------------------
import os
clear = lambda: os.system('clear')
import random

def display_board(board):
    clear()
    print(board[7]+'|'+board[8]+'|'+board[9])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[1]+'|'+board[2]+'|'+board[3])

def player_input():
    '''
    OUTPUT = (Player 1 marker, Player 2 marker)
    '''

    marker = ''

    while marker != 'X' and marker != 'O':
        marker = input('Player1: Choose X or O: ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O','X')

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):
    # win tic tac toe?

    return (
        # all rows, and check to see if they all share the same marker?
        (board[1] == mark and board[2]  == mark and board[3] == mark) or
        (board[4] == mark and board[5]  == mark and board[6] == mark) or
        (board[7] == mark and board[8]  == mark and board[9] == mark) or
        # all columns, and check to see if they all match?
        (board[8] == mark and board[5]  == mark and board[2] == mark) or
        (board[9] == mark and board[6]  == mark and board[3] == mark) or
        (board[7] == mark and board[4]  == mark and board[1] == mark) or
        # 2 diagonals, check to see if they match
        (board[7] == mark and board[5]  == mark and board[3] == mark) or
        (board[9] == mark and board[5]  == mark and board[1] == mark)
    )

def choose_first():
    flip = random.randint(0,1)

    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'

def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    # board is full if we return true
    return True

def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input('Choose a position: (1-9) '))
    return position

def replay():
    choice = input("Play again? Enter Yes or No")

    return choice == 'Yes'

# while loop to keep running the game
print('Welcome to tic tac toe')

while True:
    # play the game

    ## set everything up (board, who's first, choose markers)
    the_board = [' ']*10
    player1_marker, player2_marker = player_input()

    turn = choose_first()
    print(turn + ' will go first')

    play_game = input('Ready to play? y or n')

    if play_game == 'y':
        game_on = True
    else:
        game_on = False

    ## game play
    while game_on:
        if turn == 'Player 1':
            # show the board
            display_board(the_board)
            # choose a position
            position = player_choice(the_board)
            # place the marker on the position
            place_marker(the_board, player1_marker, position)
            #check if they won
            if win_check(the_board, player1_marker):
                display_board(the_board)
                print('Player 1 has won!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('Tie Game!')
                    game_on = False
                else:
                    turn = 'Player 2'
        else:
            ### player two turn
            # show the board
            display_board(the_board)
            # choose a position
            position = player_choice(the_board)
            # place the marker on the position
            place_marker(the_board, player2_marker, position)
            #check if they won
            if win_check(the_board, player2_marker):
                display_board(the_board)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('Tie Game!')
                    game_on = False
                else:
                    turn = 'Player 1'

    if not replay():
        break
    # break out of the while loop on replay()