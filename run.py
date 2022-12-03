import random


# Create empty lists for ships and hits
Hidden_Pattern = [[' ']*8 for x in range(8)]
Guess_Pattern = [[' ']*8 for x in range(8)]

col_num = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}


def print_board(board):
    # Create board for the game
    print()
    print('   A   B   C   D   E   F   G   H')
    print('  *** *** *** *** *** *** *** ***')
    row_num = 1
    for row in board:
        print("%d| %s |" % (row_num, " | ".join(row)))
        row_num += 1


def create_ships(board):
    # Function to create ships
    row_list = random.sample(range(0, 7), 5)
    col_list = random.sample(range(0, 7), 5)        
    for row, col in zip(row_list, col_list):
        board[row][col] = 'X'


def get_player_guess():
    # Enter the row number between 1 to 8
    print()
    row = input('Please enter a number between 1 and 8: \n')
    while not row or row not in '12345678':
        print("Please enter a valid number ")
        row = input('Please enter a number between 1 and 8: \n')
    # Enter the Ship column from A TO H
    col = input('Please enter a letter between A and H: \n').upper()
    while not col or col not in 'ABCDEFGH':
        print("Please enter a valid letter ")
        col = input('Please enter a letter between A and H: \n').upper()

    print()
    return int(row)-1, col_num[col]


create_ships(Hidden_Pattern)
print(' Welcome to Battleship!')
print()

print_board(Hidden_Pattern)
print_board(Guess_Pattern)
row, col = get_player_guess()
