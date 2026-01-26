import unittest
from games.hangman import engine

class TestHangman(unittest.TestCase):
    def setUp(self):
        self.game = engine.Engine("cat")

    def test_win(self):
        self.game.word = "cat"
        self.game.make_guess("c")
        self.game.make_guess("t")
        self.game.make_guess("a")
        self.assertTrue(self.game.is_win())
