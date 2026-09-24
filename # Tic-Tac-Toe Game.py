# Tic-Tac-Toe Game

import random

board = [" ", " ", " ",
         " ", " ", " ",
         " ", " ", " "]

scores = {
    "X": 0,
    "O": 0,
    "Draws": 0
}

difficulty = ""


def welcome_screen():
    print()
    print("========================")
    print("      TIC-TAC-TOE")
    print("========================")
    print()
    print("Player X = You")
    print("Player O = Computer")
    print()
    print("Choose positions 1-9")
    print("to place your mark.")
    print()
    print("Let's play!")
    print()


def choose_difficulty():
    global difficulty

    while True:
        print()
        print("Choose difficulty:")
        print("1. Easy")
        print("2. Medium")
        print("3. Hard")

        choice = input("Enter 1, 2, or 3: ")

        if choice == "1":
            difficulty = "easy"
            print("Easy mode selected!")
            break

        elif choice == "2":
            difficulty = "medium"
            print("Medium mode selected!")
            break

        elif choice == "3":
            difficulty = "hard"
            print("Hard mode selected! Good luck!")

            break

        else:
            print("Please choose 1, 2, or 3.")


def display_board():
    print()
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print()


def display_position_guide():
    print()
    print("Position Guide:")
    print("1 | 2 | 3")
    print("--+---+--")
    print("4 | 5 | 6")
    print("--+---+--")
    print("7 | 8 | 9")
    print()


def display_score():
    print()
    print("Score")
    print(f"You: {scores['X']}")
    print(f"Computer: {scores['O']}")
    print(f"Draws: {scores['Draws']}")
    print()


def player_move():
    while True:
        position = input("Your turn! Choose a position (1-9): ")

        if position.isdigit() and 1 <= int(position) <= 9:
            position = int(position) - 1

            if board[position] == " ":
                board[position] = "X"
                break
            else:
                print("That position is already taken!")

        else:
            print("Please choose a number from 1 to 9.")


def find_winning_move(player):
    for i in range(9):
        if board[i] == " ":
            board[i] = player

            if check_winner():
                board[i] = " "
                return i

            board[i] = " "

    return None


def evaluate():
    winning_combinations = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    for combination in winning_combinations:
        a, b, c = combination

        if board[a] == board[b] == board[c] == "O":
            return 1

        if board[a] == board[b] == board[c] == "X":
            return -1

    return 0


def minimax(is_maximizing):
    score = evaluate()

    if score != 0 or check_draw():
        return score

    if is_maximizing:
        best_score = -float("inf")

        for i in range(9):
            if board[i] == " ":
                board[i] = "O"

                score = minimax(False)

                board[i] = " "

                best_score = max(best_score, score)

        return best_score

    else:
        best_score = float("inf")

        for i in range(9):
            if board[i] == " ":
                board[i] = "X"

                score = minimax(True)

                board[i] = " "

                best_score = min(best_score, score)

        return best_score


def computer_move():
    if difficulty == "easy":

        empty_positions = []

        for i in range(9):
            if board[i] == " ":
                empty_positions.append(i)

        position = random.choice(empty_positions)

    elif difficulty == "medium":

        winning_move = find_winning_move("O")

        if winning_move is not None:
            position = winning_move

        else:
            blocking_move = find_winning_move("X")

            if blocking_move is not None:
                position = blocking_move

            else:
                empty_positions = []

                for i in range(9):
                    if board[i] == " ":
                        empty_positions.append(i)

                position = random.choice(empty_positions)

    else:

        best_score = -float("inf")
        best_move = None

        for i in range(9):
            if board[i] == " ":
                board[i] = "O"

                score = minimax(False)

                board[i] = " "

                if score > best_score:
                    best_score = score
                    best_move = i

        position = best_move

    board[position] = "O"
    print(f"Computer chose position {position + 1}.")


def check_winner():
    winning_combinations = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    for combination in winning_combinations:
        a, b, c = combination

        if board[a] == board[b] == board[c] != " ":
            return True

    return False


def check_draw():
    return " " not in board


def reset_board():
    for i in range(9):
        board[i] = " "


welcome_screen()
display_position_guide()
choose_difficulty()


while True:
    display_score()
    display_board()

    while True:

        player_move()
        display_board()

        if check_winner():
            print("You win! 🎉")
            scores["X"] += 1
            break

        if check_draw():
            print("It's a draw!")
            scores["Draws"] += 1
            break

        computer_move()
        display_board()

        if check_winner():
            print("Computer wins!")
            scores["O"] += 1
            break

        if check_draw():
            print("It's a draw!")
            scores["Draws"] += 1
            break

    display_score()

    play_again = input("Play again? (y/n): ").lower()

    if play_again == "y":
        reset_board()
        display_position_guide()
        choose_difficulty()

    else:
        print("Thanks for playing!")
        break