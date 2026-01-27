import requests
from .engine import Engine

ALPHABET= "abcdefghijklmnopqrstuvwxyz"
MSG_WELCOME = "Welcome to Hangman! Guess a letter"
MSG_ERR = "Please input a character"
MSG_QUIT = "Quitting Hangman..."

def get_word():
    url = "https://random-word-api.herokuapp.com/word"
    response = requests.get(url)
    if response.status_code == 200:
        print(response.json())
        return response.json()
    else:
        print(f"Error: {response.status_code}")

def run_game():
    game = Engine(get_word())

    print(MSG_WELCOME)
    game_over = False
    while not game_over:
        game.print_current_guess()
        game.print_hangman()
        x = input("> ").lower().strip()

        if x in {"quit", "q"}:
            print(MSG_QUIT)
            break

        if len(x) != 1 or x not in ALPHABET:
            print(MSG_ERR)

        game.make_guess(x)


