import random
import os

LENGTH = 3

board_places = None
players = (
    list("X" for x in range(LENGTH)),
    list("O" for x in range(LENGTH))
)


def create_board():
    global board_places
    board_places = list([" " for i in range(LENGTH)] for _ in range(LENGTH))


def show_board():
    os.system("cls")
    for line in board_places:
            print(" - ".join(line))


def initial_board():
    global board_places
    board_places = [[" " for i in range(LENGTH)] for _ in range(LENGTH)]


def check_for_win():
    for player in players:
        winner = player[0]
        for n in range(LENGTH):
            # horizontal CHECK
            if board_places[n].count(player[0]) == LENGTH:
                return winner

            # check vertical and diagonals
            if list(
                board_places[x][n] for x in range(LENGTH)
            ) == player:
                return winner

            # right diagonal
            if list(
               board_places[x][x] for x in range(LENGTH)
            ) == player:
                return winner

        # left diagonal
        length = LENGTH - 1
        left_diag = list()
        for x in range(LENGTH):
            left_diag.append(board_places[x][length])
            length -= 1
        if left_diag == player:
            return winner
    return False


playing = True

def tictactoe():
    global board_places, playing
    winner = False
    os.system("cls")
    print("Wanna play 2 players or a dumb AI? 2P/AI")
    start_option = input(">>")

    create_board()
    initial_board()
    show_board()


    while playing:
        counter = 0
        space_available = 9
        for line in board_places:
            for col in line:
                if col != " ":
                    space_available -= 1
        if space_available == 0:
            print("It's a draw!")
            break

        while True:
            print("player 1 turn")

            opt = input(">>")
            try:
                y_pos = (int(opt[0]) - 1)
                x_pos = (int(opt[1]) - 1)
                if y_pos >= 0 and x_pos >= 0:
                    if board_places[y_pos][x_pos] == " ":
                        board_places[y_pos][x_pos] = "X"
                        break
                    else:
                        print("that space is already occupied")
                else:
                    print("choose a valid place")
            except (ValueError, IndexError):
                print("choose a valid place")

        winner = check_for_win()

        for line in board_places:
            if " " not in line:
                counter += 1

        if start_option.upper() == "2P":
            show_board()
            while True and winner == False:
                print("Player 2 turn")

                opt = input(">>")
                try:
                    y_pos = (int(opt[0]) - 1)
                    x_pos = (int(opt[1]) - 1)
                    if y_pos >= 0 and x_pos >= 0:
                        if board_places[y_pos][x_pos] == " ":
                            board_places[y_pos][x_pos] = "O"
                            break
                        else:
                            print("that space is already occupied")
                    else:
                        print("choose a valid place")
                except (ValueError, IndexError):
                    print("choose a valid place")
        else:
            if counter != 3:
                while True:
                    ai_y= random.randint(0, 2)
                    ai_x = random.randint(0, 2)
                    if board_places[ai_y][ai_x] == " ":
                        board_places[ai_y][ai_x] = "O"
                        break

        winner = check_for_win()

        if winner == False:
            show_board()
        elif winner == "X" or winner == "O":
            show_board()
            print(f"The winner is {winner}")
            print()
            while playing:
                print("want to play again? Y/N")
                end_opt = input(">>")
                if end_opt.upper() == "Y":
                    tictactoe()
                else:
                    os.system("cls")
                    playing = False


tictactoe()