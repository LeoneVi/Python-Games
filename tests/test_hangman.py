import pytest
from games.hangman import engine

class TestHangman():

    def test_win(self):
        game = engine.Engine("cat")
        game.make_guess("c")
        game.make_guess("t")
        game.make_guess("a")
        assert game.is_win()

    def test_get_current_guess(self):
        game = engine.Engine("cat")
        assert game.get_current_guess() == "_ _ _"
        assert game.get_current_guess() != "_ _ _ _"

    def test_incorrect_guess_count(self):
        game = engine.Engine("cat")
        game.make_guess("d")
        assert game.get_incorrect_guess_count() == 1
        game.make_guess("o")
        assert game.get_incorrect_guess_count() == 2
        game.make_guess("g")
        assert game.get_incorrect_guess_count() == 3

    def test_already_guessed(self):
        game = engine.Engine("cat")
        game.make_guess("c")
        game.is_already_guessed("c")
        game.make_guess("d")
        game.is_already_guessed("d")
