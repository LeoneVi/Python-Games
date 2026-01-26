import unittest
from games.number_guesser import engine

class TestNumberGuesser(unittest.TestCase):
    def setUp(self):
        self.game = engine.Engine()
        self.game.number = 50
        self.game.max_number = 3

    def test_is_warmer(self):
        self.assertTrue(self.game.is_warmer(8,10))
        self.assertTrue(self.game.is_warmer(1, 15))
        self.assertFalse(self.game.is_warmer(49, 30))

    def test_correct(self):
        self.assertEqual(self.game.make_guess(self.game.number), "correct")
        self.assertNotEqual(self.game.make_guess(self.game.number - 1), "correct")

    def test_incorrect(self):
        # If the user has not previously made a guess, and they guess incorrectly, they should receive "incorrect" message
        self.assertEqual(self.game.make_guess(self.game.number - 1), "incorrect")
        self.assertNotEqual(self.game.make_guess(self.game.number - 2), "incorrect")

    def test_warmer(self):
        self.game.make_guess(self.game.number - 5)
        self.assertEqual(self.game.make_guess(self.game.number - 4), "warmer")
        self.assertEqual(self.game.make_guess(self.game.number - 3), "warmer")
        self.assertNotEqual(self.game.make_guess(self.game.number - 2), "colder")

    def test_colder(self):
        self.game.make_guess(self.game.number - 5)
        self.assertEqual(self.game.make_guess(self.game.number - 6), "colder")
        self.assertEqual(self.game.make_guess(self.game.number - 7), "colder")
        self.assertNotEqual(self.game.make_guess(self.game.number - 8), "warmer")

    def test_repeat(self):
        self.game.make_guess(self.game.number - 5)
        self.assertEqual(self.game.make_guess(self.game.number - 5), "repeat")

    if __name__ == '__main__':
        unittest.main()