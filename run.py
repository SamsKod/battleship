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


print_board(Hidden_Pattern)
