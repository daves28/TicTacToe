# Beginning: Ask Player 1 if they want to be X or O

print('Welcome to Tic Tac Toe!')

turn = ''

while turn != 'X' and turn != 'O':
    turn = input('Do you want to be X or O?: ').upper().strip()

start = input('Are you ready to play? Enter Yes or No: ')

# Win condition check function
from winCheck import winCheck

# Begin game if they input Yes.
while start.lower().strip() == 'yes' or start.lower().strip() == 'y':

    pos1 = '1'
    pos2 = '2'
    pos3 = '3'
    pos4 = '4'
    pos5 = '5'
    pos6 = '6'
    pos7 = '7'
    pos8 = '8'
    pos9 = '9'
    empty = '   |   |   '

    win = 0
    winner = ''
    count = 0

    # While there is still no winner, continue playing game.
    while win == 0 and count < 9:

        # Clear board away
        print('\n'*100)

        # Print new board
        print(f'{empty}\n '
              f'{pos7} | {pos8} | {pos9} \n'
              f'{empty}\n'
              f'-----------\n'
              f'{empty}\n '
              f'{pos4} | {pos5} | {pos6} \n'
              f'{empty}\n'
              f'-----------\n'
              f'{empty}\n'
              f' {pos1} | {pos2} | {pos3} \n'
              f'{empty}')

        # Ask player to input position
        pos = int(input(f'Player {turn} choose your next position: (1-9) '))

        # Determine player position selection, ensure that positon has not been selected yet
        # modify position variable to the player choice and change turn variable to other turn letter X or O.
        if pos == 1 and pos1 == '1':
            pos1 = turn.upper().strip()
            count += 1

            if turn.upper().strip() == 'X':
                turn = 'O'
            elif turn.upper().strip() == 'O':
                turn = 'X'

        elif pos == 2 and pos2 == '2':
            pos2 = turn.upper().strip()
            count += 1
            if turn.upper().strip() == 'X':
                turn = 'O'
            elif turn.upper().strip() == 'O':
                turn = 'X'

        elif pos == 3 and pos3 == '3':
            pos3 = turn.upper().strip()
            count += 1

            if turn.upper().strip() == 'X':
                turn = 'O'
            elif turn.upper().strip() == 'O':
                turn = 'X'

        elif pos == 4 and pos4 == '4':
            pos4 = turn.upper().strip()
            count += 1

            if turn.upper().strip() == 'X':
                turn = 'O'
            elif turn.upper().strip() == 'O':
                turn = 'X'

        elif pos == 5 and pos5 == '5':
            pos5 = turn.upper().strip()
            count += 1

            if turn.upper().strip() == 'X':
                turn = 'O'
            elif turn.upper().strip() == 'O':
                turn = 'X'

        elif pos == 6 and pos6 == '6':
            pos6 = turn.upper().strip()
            count += 1

            if turn.upper().strip() == 'X':
                turn = 'O'
            elif turn.upper().strip() == 'O':
                turn = 'X'

        elif pos == 7 and pos7 == '7':
            pos7 = turn.upper().strip()
            count += 1

            if turn.upper().strip() == 'X':
                turn = 'O'
            elif turn.upper().strip() == 'O':
                turn = 'X'

        elif pos == 8 and pos8 == '8':
            pos8 = turn.upper().strip()
            count += 1

            if turn.upper().strip() == 'X':
                turn = 'O'
            elif turn.upper().strip() == 'O':
                turn = 'X'

        elif pos == 9 and pos9 == '9':
            pos9 = turn.upper().strip()
            count += 1

            if turn.upper().strip() == 'X':
                turn = 'O'
            elif turn.upper().strip() == 'O':
                turn = 'X'

        elif pos not in range(1-9):
            print('Not a valid position, please select a position 1-9 that is not taken')

        # Check for winner
        win, winner = winCheck(pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8, pos9)

    # If win condition has been met, say so and ask player if they want to play again.
    if win == 1:
        print('\n' * 100)
        print(f'{empty}\n '
              f'{pos7} | {pos8} | {pos9} \n'
              f'{empty}\n'
              f'-----------\n'
              f'{empty}\n '
              f'{pos4} | {pos5} | {pos6} \n'
              f'{empty}\n'
              f'-----------\n'
              f'{empty}\n'
              f' {pos1} | {pos2} | {pos3} \n'
              f'{empty}')
        print(f'Congratulations player {winner}, you have won the game')
        start = input('Do you want to play again? ').lower().strip()
        if start == 'no':
            print('Bye!')

    if win == 0 and count == 9:
        print('\n' * 100)
        print(f'{empty}\n '
              f'{pos7} | {pos8} | {pos9} \n'
              f'{empty}\n'
              f'-----------\n'
              f'{empty}\n '
              f'{pos4} | {pos5} | {pos6} \n'
              f'{empty}\n'
              f'-----------\n'
              f'{empty}\n'
              f' {pos1} | {pos2} | {pos3} \n'
              f'{empty}')
        print(f'Tie!')
        start = input('Do you want to play again? ').lower().strip()
        if start == 'no':
            print('Bye!')
