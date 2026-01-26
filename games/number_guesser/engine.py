import random

CORRECT = "correct"
INCORRECT = "incorrect" # when a user guesses incorrect but has not previously made a guess
WARMER = "warmer"
COLDER = "colder"
OVER = "over" # when user runs out of guesses
REPEAT = "repeat" # number has already been guessed

class Engine():
    def __init__(self):
        self.max_guesses = 15
        self.max_number = 100
        self.number = random.randrange(1, self.max_number)
        self.guesses = []

    def get_max_number(self):
        return self.max_number

    def get_guesses_left(self):
        return self.max_guesses - len(self.guesses)

    def is_game_over(self):
        return len(self.guesses) >= self.max_guesses

    # Ex. number = 10. prev guess was 5, and user guesses 8.
    # prev - num = 5, cur - num = 3
    def is_warmer(self, prev, cur):
        return abs(prev - self.number) > abs(cur - self.number)

    def make_guess(self, guess):
        if guess in self.guesses:
            return REPEAT

        if len(self.guesses) > 0:
            prev = self.guesses[-1]
        else:
            prev = None

        guess_count = len(self.guesses)
        self.guesses.append(guess)

        if self.number == guess:
            return CORRECT

        # if the first guess is incorrect
        if guess_count == 0:
            return INCORRECT

        # if user has run out of guesses
        if self.get_guesses_left() == 0:
            return OVER

        if self.is_warmer(prev, guess):
            return WARMER
        else:
            return COLDER

