def winCheck(pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8, pos9):

    win = 0
    winner = 0

    if pos1 == pos2 == pos3 != ' ':
        winner = pos1
        win = 1

    elif pos4 == pos5 == pos6 != ' ':
        winner = pos4
        win = 1

    elif pos7 == pos8 == pos9 != ' ':
        winner = pos7
        win = 1

    elif pos1 == pos4 == pos7 != ' ':
        winner = pos1
        win = 1

    elif pos2 == pos5 == pos8 != ' ':
        winner = pos2
        win = 1

    elif pos3 == pos6 == pos9 != ' ':
        winner = pos3
        win = 1

    elif pos1 == pos5 == pos9 != ' ':
        winner = pos1
        win = 1

    elif pos3 == pos5 == pos7 != ' ':
        winner = pos3
        win = 1

    return win, winner
