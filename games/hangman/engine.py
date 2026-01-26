class Engine:
    def __init__(self, word):
        self.word = word
        self.guesses = []
        for i in range(len(self.word)):
            self.guesses.append(" ")

    def make_guess(self, guess):
        for i in range(len(self.word)):
            if self.word[i] == guess:
               self.guesses[i] = guess

    def is_win(self):
       return self.word == ''.join(self.guesses)