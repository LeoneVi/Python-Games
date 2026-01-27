from mimetypes import guess_type


class Engine:
    def __init__(self, word):
        self.word = word
        self.guesses = []
        for i in range(len(self.word)):
            self.guesses.append("_")
        self.guess_count = 0

    def make_guess(self, guess):
        for i in range(len(self.word)):
            if self.word[i] == guess:
               self.guesses[i] = guess
        self.guess_count += 1

    def is_win(self):
       return self.word == ''.join(self.guesses)


    def print_current_guess(self):
        print(self.guesses)

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
           """
            □-----□
            |     |
            |     O
            |    /|\
            |    
            □----
           """,
           """
            □-----□
            |     |
            |     O
            |    /|\
            |    / 
            □----
           """,
           """
            □-----□
            |     |
            |     O
            |    /|\
            |    / \
            □----
           """,
        ]
        print(hangman[self.guess_count])