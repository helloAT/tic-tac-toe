import random

def check_win(board):
    for row in board:
        if row == [0]*3:
            return 0
        elif row == [1]*3:
            return 1

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != -1:
            return 1

    if board[0][0] == board[1][1] == board[2][2] != -1:
        return 1
    if board[0][2] == board[1][1] == board[2][0] != -1:
        return 1

    for row in board:
        for col in row:
            if col == -1:
                return None
    
    return 0

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

def update_board(board, available, move, turn):
    id = {'Player': 1, 'Computer': 0}
    available.remove(move)
    board[move//3][move%3] = id[turn]
    draw_board(board)
    state = check_win(board)

    if state == 1:
        print(f'{turn} Wins!')
    elif state == 0:
        print('Draw!')
    else:
        return board

def main():
    available = list(range(9))
    board = [[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]]
    draw_board(board)

    while True:
        player_input = int(input('Enter your move: '))
        while True:
            if player_input in available:
                break
            else:
                player_input = int(input('Please enter a valid move: '))
        update = update_board(board, available, player_input, 'Player')
        if update != None:
            board = update
        update = update_board(board, available, random.choice(available), 'Computer')
        if update != None:
            board = update

main()
