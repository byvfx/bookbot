
import os
import sys
import pytest

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from stats import get_num_words, get_char_count, sort_chars


def test_get_num_words():
    assert get_num_words("Hello world") == 2
    assert get_num_words("One, two, three.") == 3


def test_get_char_count():
    text = "Aa Bb!"
    expected = {'a': 2, ' ': 1, 'b': 2, '!': 1}
    assert get_char_count(text) == expected


def test_sort_chars():
    text = "Banana!"
    char_dict = get_char_count(text)
    result = sort_chars(char_dict)
    assert result == [('a', 3), ('n', 2), ('b', 1)]
