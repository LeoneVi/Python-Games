import random

MSG_WELCOME = "Let's play a number guessing game!\nGuess a number between 1 and {number}"
MSG_NOT_INT = "Please enter an integer."
MSG_CORRECT = "Your guess is correct, you had {guesses_left} guesses left."
MSG_INCORRECT = "Incorrect! You have {guesses_left} guesses left."
MSG_WARMER = "Warmer! You have {guesses_left} guesses left."
MSG_COLDER = "Colder! You have {guesses_left} guesses left."
MSG_OVER = "Incorrect! You have 0 guesses left. Game over."
MSG_QUIT = "Exiting Number Guesser..."

class NumberGuesser():
    def __init__(self):
        self.max_guesses = 15
        self.max_number = 100
        self.number = random.randrange(1, self.max_number)
        self.guessArr = []

    def is_correct_guess(self, x):
        return self.number == x

    def is_game_over(self):
        return (len(self.guessArr) >= self.max_guesses)

    # Ex. number = 10. prev guess was 5, and user guesses 8.
    # prev - num = 5, cur - num = 3
    def is_warmer(self, prev, cur):
        return abs(prev - self.number) > abs(cur - self.number)

    def guess(self, x):
        guess_count = len(self.guessArr)
        self.guessArr.append(x)
        guesses_left = self.max_guesses - len(self.guessArr)
        prev = self.guessArr[-1]

        if self.number != x:
            if guess_count == 0:
                return MSG_INCORRECT.format(guesses_left=guesses_left)

            if guesses_left == 0:
                return MSG_OVER

            if self.is_warmer(prev, x):
                return MSG_WARMER.format(guesses_left=guesses_left)
            else:
                return MSG_COLDER.format(guesses_left=guesses_left)
        else:
            return MSG_CORRECT.format(guesses_left=guesses_left)

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