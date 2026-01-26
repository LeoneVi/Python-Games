MSG_WELCOME = "Let's play a number guessing game!\nGuess a number between 1 and {number}"
MSG_NOT_INT = "Please enter an integer."
MSG_CORRECT = "Your guess is correct, you had {guesses_left} guesses left."
MSG_INCORRECT = "Incorrect! You have {guesses_left} guesses left."
MSG_WARMER = "Warmer! You have {guesses_left} guesses left."
MSG_COLDER = "Colder! You have {guesses_left} guesses left."
MSG_OVER = "Incorrect! You have 0 guesses left. Game over."
MSG_QUIT = "Exiting Number Guesser..."

"""
def game(self):
    print(MSG_WELCOME.format(number=self.max_number))
    while not self.is_game_over():
        x = input().strip().lower()
        if x == "quit" or x == "q":
            print(MSG_QUIT)
            break
        elif not x.isdigit():
            print(MSG_NOT_INT)

        else:
            result = self.guess(int(x))
            print(result)
            if self.is_correct_guess(int(x)):
                break
"""