from games.number_guesser import ui as number_guesser
from games.hangman import ui as hangman


MSG_WELCOME = "Thanks for playing Tory's games in python! Select which game you would like to play! ☺"
MSG_NOT_INT = "Please input a number to select which game you would like to play!"
MSG_WRONG_SELECTION = "Not an available game. Please select a number for which game you would like to play!"
MSG_QUIT = "Quitting starting menu..."

MSG_GAMES = """
            [1] Number Guessing Game
            [2] Hangman Game
            """

print(MSG_WELCOME)
while True:
    x = input("> ").lower().strip()

    if x in {"quit", "q"}:
        print(MSG_QUIT)
        break

    if not x.isdigit():
        print(MSG_NOT_INT)
        continue

    match int(x):
        case 1:
            number_guesser.run_game()
        case 2:
            hangman.run_game()
        case _:
            print(MSG_WRONG_SELECTION)