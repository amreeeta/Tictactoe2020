#!/usr/bin/env python3
"""Play a 1-player or 2-player game of tic tac toe in the terminal"""

import os
import platform
import random

from copy import deepcopy

__author__ = "Amrita Shah, Danesh Ajith, Gunjan Agarwal, Shaun Hin, Yu Qin"
__credits__ = "CC02 Group 6"

INITIAL_TURN = 1


def introduction_message():
    print('░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗  ████████╗░█████╗░')
    print('░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝  ╚══██╔══╝██╔══██╗')
    print('░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░  ░░░██║░░░██║░░██║')
    print('░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░  ░░░██║░░░██║░░██║')
    print('░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗  ░░░██║░░░╚█████╔╝')
    print('░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝  ░░░╚═╝░░░░╚════╝░')
    print('\n')
    print('████████╗██╗░█████╗░░░░░░░████████╗░█████╗░░█████╗░░░░░░░████████╗░█████╗░███████╗')
    print('╚══██╔══╝██║██╔══██╗░░░░░░╚══██╔══╝██╔══██╗██╔══██╗░░░░░░╚══██╔══╝██╔══██╗██╔════╝')
    print('░░░██║░░░██║██║░░╚═╝█████╗░░░██║░░░███████║██║░░╚═╝█████╗░░░██║░░░██║░░██║█████╗░░')
    print('░░░██║░░░██║██║░░██╗╚════╝░░░██║░░░██╔══██║██║░░██╗╚════╝░░░██║░░░██║░░██║██╔══╝░░')
    print('░░░██║░░░██║╚█████╔╝░░░░░░░░░██║░░░██║░░██║╚█████╔╝░░░░░░░░░██║░░░╚█████╔╝███████╗')
    print('░░░╚═╝░░░╚═╝░╚════╝░░░░░░░░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░░░░░░░░░░╚═╝░░░░╚════╝░╚══════╝\n')


def congratulations():
    """Congratulations display"""
    print('░█████╗░░█████╗░███╗░░██╗░██████╗░██████╗░░█████╗░████████╗██╗░░░██╗██╗░░░░░░█████╗░████████╗██╗░█████╗░███╗░░██╗░██████╗')
    print('██╔══██╗██╔══██╗████╗░██║██╔════╝░██╔══██╗██╔══██╗╚══██╔══╝██║░░░██║██║░░░░░██╔══██╗╚══██╔══╝██║██╔══██╗████╗░██║██╔════╝')
    print('██║░░╚═╝██║░░██║██╔██╗██║██║░░██╗░██████╔╝███████║░░░██║░░░██║░░░██║██║░░░░░███████║░░░██║░░░██║██║░░██║██╔██╗██║╚█████╗░')
    print('██║░░██╗██║░░██║██║╚████║██║░░╚██╗██╔══██╗██╔══██║░░░██║░░░██║░░░██║██║░░░░░██╔══██║░░░██║░░░██║██║░░██║██║╚████║░╚═══██╗')
    print('╚█████╔╝╚█████╔╝██║░╚███║╚██████╔╝██║░░██║██║░░██║░░░██║░░░╚██████╔╝███████╗██║░░██║░░░██║░░░██║╚█████╔╝██║░╚███║██████╔╝')
    print('░╚════╝░░╚════╝░╚═╝░░╚══╝░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░░╚═════╝░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝╚═════╝░')


def game_credits():
    """Prints the credits of the game"""
    print(f"Authors: {__author__}")
    print(f"Credits: {__credits__}\n")


def get_no_of_players():

    while True:
        try:
            no_of_players = int(input("Enter 1 if you wish to play against computer and 2 to play with a friend: "))
            if no_of_players == 1 or no_of_players == 2:
                return no_of_players
            else:
                print("Please enter a either '1' or '2' only.")
        except ValueError:
            print("Please enter a either '1' or '2' only.")


def get_board_size():
    """Returns an odd number between 3 to 99 inclusive for the board size in multiplayer mode"""
    while True:
        try:
            board_size = int(input("Enter value of n for nxn size of tic-tac-toe board (ensure that the value is odd):"))
            if board_size % 2 == 1 and 3 <= board_size <= 99:
                return board_size
            else:
                print("Please enter odd number for value of n greater than 1.")
        except ValueError:
            print("Please enter odd number for value of n.")


def get_number_of_rounds():
    while True:
        try:
            r = int(input("How many rounds do you want to play?"))
            if 1 <= r <= 10:
                return r
            else:
                print("Please input an integer between 1 and 10.")
        except ValueError:
            print("Please input an integer between 1 and 10.")


def get_index_no(marker):
    """Returns the sanitised input for an integer index number"""
    while True:
        try:
            index_no = int(input(f"Choose a number to replace with {marker}:\n"))
            return index_no
        except ValueError:
            print("Please enter odd number for value of n.")


def player_names(no_of_players):
    if no_of_players == 2:
        player1 = input('Enter the name of Player 1: ')
        player2 = input('Enter the name of Player 2: ')
        
    else:
        b = random.randint(0, 1)
        if  b== 0:
            player1= 'Computer'
            player2=input('Enter your name: ')
        else:
            player2= 'Computer'
            player1=input('Enter your name: ')
    return player1, player2


def initialise_variables(number_of_boxes):
    """Returns initial variables"""
    boxes = [i for i in range(number_of_boxes)]
    box_numbers = tuple([str(i) for i in range(number_of_boxes)])
    turn = INITIAL_TURN
    filled_boxes = []
    filled_message = False
    error_message = False
    return boxes, box_numbers, turn, filled_boxes, filled_message, error_message


def check_turn(turn, player_1, player_2):
    """Returns the marker and player for the corresponding turn"""
    if turn % 2 == 1:
        marker = "O"
        player = player_1
    else:
        marker = "X"
        player = player_2
    return marker, player


def print_board(boxes, board_size):
    """Prints the elements of boxes on a size x size board"""
    top_row = ["|"]
    rows = [deepcopy(top_row) for i in range(board_size)]
    lines = "  __" + (board_size - 1) * "   __" + "\n"
    row_lower_bound = 0
    row_upper_bound = board_size
    row_strings = []
    for row in rows:
        for value in boxes[row_lower_bound:row_upper_bound]:
            row.append(str(value).rjust(2) + " |")
        row_strings.append(" ".join(row))
        row_lower_bound += board_size
        row_upper_bound += board_size
    for row in row_strings:
        print(lines)
        print(row)
    print(lines)


def check_win(boxes, board_size):
    """Checks for identical markers in a row, column, or diagonal indicating a win,
    and returns True if there is a win."""
    for i in range(board_size):
        if len(set(boxes[i * board_size:(i + 1) * board_size])) == 1 or len(set(boxes[i::board_size])) == 1:
            return True
    if len(set(boxes[0::board_size + 1])) == 1 or len(set(boxes[board_size - 1:(board_size - 1) * board_size + 1:board_size - 1])) == 1:   
        return True
    return False


def check_overall_winner(player_1_win, player_2_win, player_1, player_2):
    if player_1_win > player_2_win:
        message = f"{player_1} is the overall winner!"
    elif player_1_win == player_2_win:
        message = "There is no overall winner!"
    else:
        message = f"{player_2} is the overall winner!"
    return message


def clear_screen():
    """Clears screen for different OS systems"""
    if platform.system().lower() == "windows":
        os.system("cls")
    else:
        os.system("clear")


def declare_winner(turn, boxes, player_1, player_2, board_size):
    """Prints the winner of the game"""
    if turn is not None:
        clear_screen()
        print("TIC TAC TOE")
        print_board(boxes, board_size)
        if turn == len(boxes):
            print("It's a draw!")

        elif turn % 2 == 1:
            congratulations()
            print(f"{player_1} wins!")

        else:
            congratulations()
            print(f"{player_2} wins!")
        input("Press enter to exit.")
            

def two_player_tic_tac_toe(board_size):
    """Returns the message declaring the final overall winner or lack thereof of the game"""
    number_of_boxes = board_size ** 2
    no_of_players = 2
    no_of_rounds = get_number_of_rounds()
    round_no = 0
    player_1_win = 0
    player_2_win = 0
    player_1, player_2 = player_names(no_of_players)
    while round_no < no_of_rounds:
        round_no += 1
        boxes, box_numbers, turn, filled_boxes, filled_message, error_message = initialise_variables(number_of_boxes)
        while True:
            print(f"ROUND NO {round_no}")
            print("TIC TAC TOE")
            marker, player = check_turn(turn, player_1, player_2)
            print_board(boxes, board_size)

            if filled_message: #checks for errors
                print("That box is filled! Please choose another!")
            elif error_message:
                print("Please input a valid number to replace!")

            if turn == len(boxes): #checks if all boxes are filled
                declare_winner(turn, boxes, player_1, player_2, board_size)
                break
            print(f"Player {player}'s turn")
            index_no = get_index_no(marker)

            if index_no in filled_boxes:
                filled_message = True
            elif str(index_no) in box_numbers:
                filled_message = False
                error_message = False
                filled_boxes.append(index_no)
                boxes[index_no] = marker

                if check_win(boxes, board_size):
                    if turn % 2 == 1:
                        player_1_win += 1
                    else:
                        player_2_win += 1
                    declare_winner(turn, boxes, player_1, player_2, board_size)
                    break
                turn += 1
            else:
                error_message = True
            clear_screen()

    message = check_overall_winner(player_1_win, player_2_win, player_1, player_2)
    return message


def vscomputer(board_size):
    number_of_boxes = board_size ** 2
    no_of_players = 1
    player_1, player_2 = player_names(no_of_players)
    boxes, box_numbers, turn, filled_boxes, filled_message, error_message = initialise_variables(number_of_boxes)

       
    while True:
        print("TIC TAC TOE")
        
        marker, player = check_turn(turn, player_1, player_2)
        print_board(boxes, board_size)
        
        if filled_message: #checks if box is filled
            print("That box is filled! Please choose another!")
            
        elif error_message:#checks if input is valid
            print("Please input a valid number to replace!")
            
        if turn == len(boxes): #if total number of turns are completed
            break
        
        if(player!='Computer'):
            #users turn
            print("Your turn")
            index_no = get_index_no(marker)
            
            if index_no in filled_boxes:
                filled_message = True
                
            elif str(index_no) in box_numbers:
                filled_message = False
                error_message = False
                filled_boxes.append(index_no)
                boxes[index_no] = marker#if no error add the marker to the position
                
                if check_win(boxes, board_size): #if winning move
                    break
                turn += 1
                
            else:
                error_message = True
            clear_screen()
    
        else:
            #computers turn
            print("Computer's turn")
            turncomplete=False
            
            #checks for computer's winning move
            for i in range(9):
                
                check=deepcopy(boxes) #creates a copy of boxes to run tests
                if i not in filled_boxes:
                    
                    check[int(i)] = marker
                    
                    if check_win(check, board_size): #checks if the computer would win
                        boxes[int(i)] = marker
                        filled_boxes.append(i)
                        return turn,boxes, player_1, player_2
                    
            #check for opponents winning move
            if marker=='X':
                oppmarker='O'
            else:
                oppmarker='X'
            
            for i in range(9):
                check=deepcopy(boxes) #creates a copy of boxes to run tests
                if i not in filled_boxes:
                    check[int(i)] = oppmarker
                    if check_win(check, board_size): #checks if the opponent would win
                        boxes[int(i)] = marker #blocks winning move
                        filled_boxes.append(i)
                        turn += 1
                        turncomplete=True
                        break
                    
            
            if turncomplete==False:
                #checks for corner box availability
                ls=[0,2,6,8] #list of corner cell numbers
                l=[]
                while l!=ls:
                    x=random.choice(ls) #chooses a random corner box
                    if x not in l: #checks whether the number generated by random has been repeated
                        l.append(x)
                        l.sort()
                    else:
                        continue
                    if x not in filled_boxes:
                        boxes[int(x)] = marker #fills corner box
                        filled_boxes.append(x)
                        turn += 1
                        turncomplete=True
                        break


            if turncomplete==False:
                    #checks for center box availability
                
                if 4 not in filled_boxes:
                    boxes[4] = marker
                    filled_boxes.append(4)
                    turn += 1
                    turncomplete=True
            
            if turncomplete==False:
                #checks for availability in side boxes
                ls=[1,3,5,7] #list of side cell numbers
                l=[]
                while l!=ls:
                    x=random.choice(ls) #chooses a random side box
                    if x not in l: #checks whether the number generated by random has been repeated
                        l.append(x)
                        l.sort()
                    else:
                        continue
                    if x not in filled_boxes:
                        boxes[int(x)] = marker#fills side box
                        filled_boxes.append(x)
                        turn += 1
                        turncomplete=True
                        break
            
                        
        clear_screen()
    return turn, boxes, player_1, player_2


def play_tic_tac_toe(no_of_players):
    """Runs either a single player or a 2-player game of Tic Tac Toe, and returns the winner"""
    turn = 0
    boxes = []
    board_size = 3
    player_1 = "o"
    player_2 = "o"
    if no_of_players == 1:
        turn, boxes, player_1, player_2 = vscomputer(board_size)
    elif no_of_players == 2:
        board_size = get_board_size()
        print(two_player_tic_tac_toe(board_size))
        return None, None, None, None, None
    return turn, boxes, player_1, player_2, board_size


def main():
    introduction_message()
    game_credits()
    no_of_players = get_no_of_players()
    turn, boxes, player_1, player_2, board_size = play_tic_tac_toe(no_of_players)
    declare_winner(turn, boxes, player_1, player_2, board_size)


if __name__ == "__main__":
    main()
