import random

score = {
    "player": 0,
    "computer": 0,
    "draw": 0
}

board = [" " for _ in range(9)]


def show_board():
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()


def show_score():
    print("\n=== СЧЁТ ===")
    print(f"Ты:         {score['player']}")
    print(f"Компьютер:  {score['computer']}")
    print(f"Ничьи:      {score['draw']}")


def check_winner():
    combinations = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in combinations:
        if board[a] != " " and board[a] == board[b] == board[c]:
            return board[a]

    if " " not in board:
        return "draw"

    return None


def player_move():
    while True:
        try:
            position = int(input("Выбери клетку (1-9): "))

            if not 1 <= position <= 9:
                print("Введи число от 1 до 9.")
                continue

            position -= 1

            if board[position] != " ":
                print("Эта клетка уже занята!")
                continue

            board[position] = "X"
            break

        except ValueError:
            print("Нужно ввести число.")


def computer_move():
    free_cells = [i for i in range(9) if board[i] == " "]

    if free_cells:
        position = random.choice(free_cells)
        board[position] = "O"
        print(f"Компьютер выбрал клетку {position + 1}")


def game():
    global board

    board = [" " for _ in range(9)]

    print("\n=== НОВАЯ ИГРА ===")
    print("Ты — X, компьютер — O.")

    while True:
        show_board()

        player_move()

        result = check_winner()

        if result:
            show_board()

            if result == "X":
                print("Ты победил! 🎉")
                score["player"] += 1

            elif result == "draw":
                print("Ничья!")
                score["draw"] += 1

            break

        computer_move()

        result = check_winner()

        if result:
            show_board()

            if result == "O":
                print("Компьютер победил!")
                score["computer"] += 1

            elif result == "draw":
                print("Ничья!")
                score["draw"] += 1

            break


def main():
    while True:
        print("\n=== КРЕСТИКИ-НОЛИКИ ===")
        print("1. Начать игру")
        print("2. Показать счёт")
        print("3. Выйти")

        choice = input("Выбери действие: ")

        if choice == "1":
            game()

        elif choice == "2":
            show_score()

        elif choice == "3":
            print("До встречи!")
            break

        else:
            print("Неверный выбор.")


main()
