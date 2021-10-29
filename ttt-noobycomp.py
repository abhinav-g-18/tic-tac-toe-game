import random
import os
from time import sleep

def clear():
    os.system('cls')

def display_board(board):

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

def players():
    players_in ='Undefined'

    while players_in.lower()[0] not in ['y','n'] :
        players_in = input('Do you wish to play with computer? Enter Yes or No\t')

        if players_in.lower()[0]=='y':
            play_with = choose_player('Computer')
            second_play = 'Computer'

        elif players_in.lower()[0]=='n':
            play_with = choose_player('Player')
            second_play = 'Player'

        else:
            print('Enter a valid input from Yes or No')
    return (play_with,second_play)

def choose_player(play):
    if play == 'Computer':
        if random.randint(0, 1) == 0:
            return 'Computer'
        else:
            return 'Player 1'

    else:
        if random.randint(0, 1) == 0:
            return 'Player 2'
        else:
            return 'Player 1'

def player_input():
    marker = ''
    while marker not in ('X','O'):
        marker = input('Player 1: Do you want to be X or O?\t').upper()
        if marker not in ('X','O'):
            print('Enter valid marker X or O')
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

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

def space_check(board, position):
    if position > 9 or position <1:
        return False
    return board[position] == ' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

def check_posi():
    check="unchecked"
    while check.lower()[0] not in ['y','n'] :
        check=input('Do you wish to check the positions in the board yes or no\t')
        if check.lower()[0]=="y":
            display_board(['#','1','2','3','4','5','6','7','8','9'])
            break
        elif check.lower()[0]=="n":
            break
        else:
            print('Please enter Yes or No')

def computer_choice(board):
    print ("...")
    position = random.randint(1,10)
    if space_check(board, position):
        return position
    else:
        position = computer_choice(board)
        return position

def player_choice(board,player):
    position = ""
    while position not in ['1','2','3','3','5','6','7','8','9',1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = (input('{p} Choose your position: (1-9)\t'.format(p=player)))
        if position.isdigit():
            position = int(position)
            if position not in ['1','2','3','3','5','6','7','8','9',1,2,3,4,5,6,7,8,9] or not space_check(board, position):

                print('Enter valid position from 1 to 9')
                check_posi()
        else:
            print('Enter valid position from 1 to 9')
            check_posi()

    return position

def replay():
    return input('Do you want to play again? Enter Yes or No:\t').lower()[0]=='y'

clear()
print('WELCOME TO TIC TAC TOE!')

while True:

    theBoard = [' '] * 10
    PLAY_GAME = "not started"
    GAME_ON = None

    while GAME_ON != type(True):

        PLAY_GAME = input('Are you ready to play? Enter Yes or No\t')
        if PLAY_GAME.lower()[0] == 'y':
            GAME_ON = True
            player1_marker, player2_marker = player_input()
            clear()
            (turn,player)= players()
            clear()
            print(turn + ' will go first.')
            break
        elif PLAY_GAME.lower()[0] == 'n':
            GAME_ON = False
            break
        else:
            print('Please enter Yes or No')

    while GAME_ON:
        if turn == 'Player 1':
            # Player1's turn.
            display_board(theBoard)
            position = player_choice(theBoard,turn)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                clear()
                display_board(theBoard)
                print('Congratulations Player 1! You have won the game!')
                GAME_ON = False
            else:
                if full_board_check(theBoard):
                    clear()
                    display_board(theBoard)
                    print('Its a Tie!')
                    break
                else:
                    if player == 'Player':
                        turn = 'Player 2'

                    else:
                        turn = 'Computer'
                        clear()


        elif turn == 'Player 2':
            # Player2's turn.
            display_board(theBoard)
            position = player_choice(theBoard,turn)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                clear()
                display_board(theBoard)
                print('Congratulations Player 2! You win!')
                GAME_ON = False
            else:
                if full_board_check(theBoard):
                    clear()
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'
                    clear()

        else:
            # computer's turn.
            display_board(theBoard)
            print('Computer is making a choice ')
            position = computer_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                clear()
                display_board(theBoard)
                print('OOPS! Computer won the game')
                GAME_ON = False

            else:
                if full_board_check(theBoard):
                    clear()
                    display_board(theBoard)
                    print('The game is a draw!')
                    break

                else:
                    turn = 'Player 1'
                    sleep(3)
                    clear()

    if not replay():
        clear()
        print('Well Played! See you Soon😊')
        break