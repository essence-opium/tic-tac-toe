import random
from random import randrange


def board_set():
    _board = []
    _counter = 1
    for row in range(3):
        _row = []
        for column in range(3):
            _column = _counter
            _counter = _counter + 1
            _row.append(_column)
        _board.append(_row)
    return _board


def board_display():
    print("\nBoard status: ")
    for row in board:
        print(row)


def board_check():
    _counterX = 0
    _counterY = 0

    for row in board:
        for column in row:
            if (column == "X"):
                a = 0


def player_pick():
    _row = input("Row ")
    _column = input("Column ")
    board[int(_row)][int(_column)] = player


def npc_pick():
    # NPC first turn
    _counter = 0
    npc_row = randrange(3)
    npc_column = randrange(3)
    if _counter == 0 and npc == "X":
        board[npc_row][npc_column] = "X"
        print("NPC goes: ", npc_row, npc_column)
        return

    # for row in board:
    #     for column in row:
    #
    # print("NPC goes: ", npc_row, npc_column)


# --------------------------------------------------------


print("\nTic-tac-toe TIME!")
print("Pick a side (1) or random assignment (2) ?")
side_or_random = input()
player = ""
npc = ""

if (side_or_random == "1"):
    player = input("Which symbol? (X or O)? ").upper()
    if (player == "X"):
        npc = "O"
    if (player == "O"):
        npc = "X"

if (side_or_random == "2"):
    choices = "XO"
    player = random.choice(choices)
    npc = choices.replace(player, "")

print("\nAssigning roles...")
print("Player:", player)
print("NPC: ", npc)

board = board_set()
board_display()
finish = False

while not finish:

    if (player == "X"):
        player_pick()
        board_display()
        npc_pick()
        board_display()
    else:
        npc_pick()
        board_display()
        player_pick()
        board_display()

    # board_check()

    finish = True
