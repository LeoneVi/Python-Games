class Engine:
    def __init__(self, word):
        self.word = word
        self.guesses = []
        self.incorrect_guesses = []
        for i in range(len(self.word)):
            self.guesses.append("_")
        self.incorrect_guess_count = 0

    def is_already_guessed(self, guess):
        return guess in self.guesses or guess in self.incorrect_guesses

    def is_win(self):
        return self.word == ''.join(self.guesses)

    def is_lose(self):
        return self.incorrect_guess_count >= 6

    def make_guess(self, guess):
        none_correct = True
        if not self.is_already_guessed(guess):  # ensure user is guessing a new letter
            for i in range(len(self.word)):
                if self.word[i] == guess:
                    self.guesses[i] = guess
                    if none_correct: none_correct = False  # there was a correct letter found somewhere in word
            if none_correct:
                self.incorrect_guess_count += 1
                self.incorrect_guesses.append(guess)

    def get_current_guess(self):
        return ' '.join(self.guesses)

    def get_incorrect_guess_count(self):
        return self.incorrect_guess_count

    def print_current_guess(self):
        print(' '.join(self.guesses))

    def print_incorrect_guess(self):
        print(' '.join(self.incorrect_guesses))

    def print_hangman(self):
        hangman = ["""
□-----□
|     |
|     
|    
|    
□----
""",
                   """
□-----□
|     |
|     O
|    
|    
□----
""",
                   """
□-----□
|     |
|     O
|     |
|     
□----
""",
                   """
□-----□
|     |
|     O
|    /|
|    
□----
""",
                   r"""
□-----□
|     |
|     O
|    /|\
|    
□----
""",
                   r"""
□-----□
|     |
|     O
|    /|\
|    / 
□----
""",
                   r"""
□-----□
|     |
|     O
|    /|\
|    / \
□----
""",
                   ]
        if self.incorrect_guess_count < len(hangman): print(hangman[self.incorrect_guess_count])
