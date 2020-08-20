# Set of functions for the game

# Display the board after taking input, list type data, index based printing

def display_board(board):

    #print("\n"*50)

    print('  |   |')
    print(''+ board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('  |   |')
    print('---------')
    print('  |   |')
    print(''+ board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('  |   |')
    print('---------')
    print('  |   |')
    print(''+ board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('  |   |')

# Function to assign marker to player and return the values
def marker_choose():

    marker = '' 

    while not (marker =='X' or marker =='O'):

        marker = input('Player 1, Choose your marker: ').upper()

    if marker=='X':
        return ('X', 'O')
    else:
        return ('O', 'X')    

#marker_choose()            
   

#test_board = ['#','X','O','X','O','X','O','X','O','X']
#display_board(test_board)

# Function to take in board object, the postion and the marker for assignment

def place_marker(board, position, marker):

    if space_check(board, position):
        board[position]= marker
        return True
    else:
        return False

   
# Test 
#place_marker(test_board, 3, '$')
#display_board(test_board)   

# To check if either of the player has won the game

def win_check(board, mark): 

    bol1 = (board[7]== mark and board[8]==mark and board[9]==mark)
    bol2 = (board[4]== mark and board[5]==mark and board[6]==mark)
    bol3 = (board[1]== mark and board[2]==mark and board[3]==mark) 
    bol4 = (board[7]== mark and board[4]==mark and board[1]==mark) 
    bol5 = (board[8]== mark and board[5]==mark and board[2]==mark)
    bol6 = (board[9]== mark and board[6]==mark and board[3]==mark)
    bol7 = (board[7]== mark and board[5]==mark and board[3]==mark) 
    bol8 = (board[1]== mark and board[5]==mark and board[9]==mark)

    return (bol1 or bol2 or bol3 or bol4 or bol5 or bol6 or bol7 or bol8)

#test 
#bol9 = win_check(test_board, 'X')

#print(bol9)

# Who plays first using random

import random

def choose_first():
    if random.randint(0,1)==0:
        return 'Player 2'
    else:
        return 'Player 1'    

#choice = choose_first()
#print(choice)

# Space Check

def space_check(board, position):
    if board[position] ==' ':
        return True
    else:
        return False


# Full Board Check

def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True        

   

def player_choice(board):

    position = 0

    while position not in [1,2,3,4,5,6,7,8,9] and not space_check(board, position):
        position = int(input('Enter your next position 1-9 : '))

    return position

def replay():
    
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')        
    
# Game logic
# 
print("Welcome to TIC TAC TOE")

while True:

    #Game play starts

    #Set the board

    the_board = [' ']*10
    player1_marker, player2_marker = marker_choose()

    # Who will go first

    turn = choose_first()
    print(turn + 'will go first')

    play_game = input("Ready to play? Y or N? ")
    if play_game.lower() == 'y':
        pass
        game_on = True
    else:
        game_on = False

    while game_on:

        # Player 1 turn

        if turn == "Player 1":

            display_board(the_board)  # Show Board

            # Choose Position

            position = player_choice(the_board)

            # Placing the marker on the position

            place_marker(the_board,position, player1_marker)


            # WIn check

            if win_check(the_board, player1_marker):
                display_board(the_board)
                print('Congratulation ! Player 1 has won')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('Tie game')
                    game_on = False
                else:
                    turn = 'Player 2'

        else:

            display_board(the_board)  # Show Board

            # Choose Positionx

            position = player_choice(the_board)

            # Placing the marker on the position

            place_marker(the_board, position, player2_marker)

            # WIn check

            if win_check(the_board, player2_marker):
                display_board(the_board)
                print('Congratulation ! Player 2 has won')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('Tie game')
                    game_on = False
                else:
                    turn = 'Player 1'

    if not replay():
        break
                        









