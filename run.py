import random


# Create empty lists for ships and hits
Hidden_Pattern = [[' ']*8 for x in range(8)]


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


create_ships(Hidden_Pattern)
print(' Welcome to Battleship!')
print()

print_board(Hidden_Pattern)
