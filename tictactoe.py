"""
1. Generate a tic-tac-toe board and display it on screen.
2. a. The player will be the 'X' marker and AI will be the 'O' marker.
   b. The player with the 'X' marker will make the first move. 
      Request an input using `x, y` coordinates or integer values [0, 8], inclusive, and mark the spot with 'X'.
   c. The AI will then select a random available position as its move.
3. Declare a winner when 3 of the same symbol are in the same row, column or diagonal.
4. Declare a tie game if all squares are filled and no set of 3 symbols exist in the same row, column or diagonal.
"""
import random

def check_win(board):
    player = 1
    ai = 0

    for row in board:
        if row == [0]*3:
            return 0
        elif row == [1]*3:
            return 1
    
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == 0:
            return 0
        elif board[0][col] == board[1][col] == board[2][col] == 1:
            return 1
    
    if board[0][0] == board[1][1] == board[2][2] == 0:
        return 0
    elif board[0][0] == board[1][1] == board[2][2] == 1:
        return 1
    
    if board[0][2] == board[1][1] == board[2][0] == 0:
        return 0
    elif board[0][2] == board[1][1] == board[2][0] == 1:
        return 1

    for row in board:
        for col in row:
            if col == -1:
                return None
    
    return -1

def draw_board(board):
    for r,row in enumerate(board):
        for c,col in enumerate(row):
            if c == 2:
                e = ''
            else:
                e = '|'
            if col == -1:
                print(c+r*3, end=e)
            elif col == 0:
                print('X', end=e)
            elif col == 1:
                print('O', end=e)
        if r != 2:
            print('\n-----')
        else:
            print('\n')

def main():
    vboard = list(range(9))
    board = [[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]]

    while True:
        while True:
            player_input = int(input())
            if player_input in vboard:
                break

        vboard.remove(player_input)
        board[player_input//3][player_input%3] = 1

        draw_board(board)

        if check_win(board) == 1:
            print('You Win!')
            break
        elif check_win(board) == 0:
            print('Computer Wins!')
            break
        elif check_win(board) == -1:
            print('Draw')
            break
        
        computer_input = random.choice(vboard)
        vboard.remove(computer_input)
        board[computer_input//3][computer_input%3] = 0

        draw_board(board)

        if check_win(board) == 1:
            print('You Win!')
            break
        elif check_win(board) == 0:
            print('Computer Wins!')
            break
        elif check_win(board) == -1:
            print('Draw')
            break

main()
