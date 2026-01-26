from .engine import Engine

MSG_WELCOME = "Let's play a number guessing game!\nGuess a number between 1 and {number}"
MSG_NOT_INT = "Please enter an integer."
MSG_CORRECT = "Your guess is correct, you had {guesses_left} guesses left."
MSG_INCORRECT = "Incorrect! You have {guesses_left} guesses left."
MSG_WARMER = "Warmer! You have {guesses_left} guesses left."
MSG_COLDER = "Colder! You have {guesses_left} guesses left."
MSG_OVER = "Incorrect! You have 0 guesses left. Game over."
MSG_REPEAT = "You've already guessed that number!"
MSG_QUIT = "Exiting Number Guesser..."


def run_game():
    game = Engine()
    print(MSG_WELCOME.format(number=game.get_max_number()))
    game_over = False
    while not game_over:
        x = input("> ").lower().strip()

        if x in {"quit", "q"}:
            print(MSG_QUIT)
            break

        if not x.isdigit():
            print(MSG_NOT_INT)
            continue

        result = game.make_guess(int(x))
        match result:
            case "correct":
                print(MSG_CORRECT.format(guesses_left=game.get_guesses_left()))
                game_over = True
            case "over":
                print(MSG_OVER.format(guesses_left=game.get_guesses_left()))
                game_over = True
            case "incorrect":
                print(MSG_INCORRECT.format(guesses_left=game.get_guesses_left()))
            case "warmer":
                print(MSG_WARMER.format(guesses_left=game.get_guesses_left()))
            case "colder":
                print(MSG_COLDER.format(guesses_left=game.get_guesses_left()))
            case "repeat":
                print(MSG_REPEAT.format(guesses_left=game.get_guesses_left()))