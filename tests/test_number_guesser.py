import unittest
from games import number_guesser

class TestNumberGuesser(unittest.TestCase):
    def setUp(self):
        self.game = number_guesser.NumberGuesser()
        self.game.number = 50

    def test_is_correct_guess(self):
        self.assertTrue(self.game.is_correct_guess(self.game.number))
        self.assertFalse(self.game.is_correct_guess(10))
    def test_is_warmer(self):
        self.assertTrue(self.game.is_warmer(8,10))
        self.assertTrue(self.game.is_warmer(1, 15))
        self.assertFalse(self.game.is_warmer(49, 30))

    if __name__ == '__main__':
        unittest.main()