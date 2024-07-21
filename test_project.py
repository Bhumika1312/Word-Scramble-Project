import pytest
from project import scramble_word, check_guess, get_random_words, WORDS


def test_scramble_word():
    word = "python"
    scrambled = scramble_word(word)
    assert sorted(scrambled) == sorted(word)
    assert scrambled != word  # Scrambled word should not be the same as the original

def test_check_guess():
    assert check_guess("python", "python")
    assert not check_guess("python", "java")
    assert check_guess("CS50", "CS50")
    assert not check_guess("CS50", "cs50")

def test_get_random_word():
    word = get_random_words()
    assert word in WORDS

if __name__ == "__main__":
    pytest.main()
