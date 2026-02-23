import json

import requests
from .engine import Engine

ALPHABET = "abcdefghijklmnopqrstuvwxyz"
MSG_WELCOME = "Welcome to Hangman! Guess a letter"
MSG_ERR = "Please input a character"
MSG_QUIT = "Quitting Hangman..."
MSG_WIN = "Well done! You correctly guessed the word '{word}'"
MSG_LOSE = "Nice try! The correct word was '{word}'"
MSG_REPEAT = "You've already guessed this letter!"


def get_word():
    url = "https://random-word-api.herokuapp.com/word"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()[0]
    else:
        print(f"Error: {response.status_code}")


def run_game():
    word = get_word()
    print(word)
    game = Engine(word)

    print(MSG_WELCOME)
    game_over = False
    while not game_over:
        game.print_current_guess()
        game.print_hangman()
        game.print_incorrect_guess()
        x = input("> ").lower().strip()

        if x == "quit":
            print(MSG_QUIT)
            break

        if len(x) != 1 or x not in ALPHABET:
            print(MSG_ERR)
            continue

        if game.is_already_guessed(x):
            print(MSG_REPEAT)
        else:
            game.make_guess(x)

        if game.is_win():
            print(MSG_WIN.format(word=word))
            game_over = True

        if game.is_lose():
            game.print_hangman()
            print(MSG_LOSE.format(word=word))
            game_over = True
