import pytest
from normalizer import normalize_text

@pytest.mark.parametrize("inp, expected", [
    ("", ""),                    # empty string
    (None, ""),                  # None -> ""
    ("Hello", "hello"),          # simple lowercase
    ("HELLO", "hello"),          # mixed case
    ("HeLLo WoRLD", "hello world"),  # mixed case multiword
])
def test_basic_cases(inp, expected):
    result = normalize_text(inp)
    assert result == expected
    assert isinstance(result, str)


def test_punctuation_collapse():
    assert normalize_text("hello!!!world??") == "hello world"
    assert normalize_text("a---b---c") == "a b c"


def test_numbers_and_letters():
    assert normalize_text("abc123") == "abc123"
    assert normalize_text("Room 101!") == "room 101"
    assert normalize_text("  42 is THE answer!!! ") == "42 is the answer"


def test_whitespace_collapse():
    assert normalize_text("a   b\tc\nd") == "a b c d"


def test_only_symbols_becomes_empty():
    assert normalize_text("!!!@@@###") == ""
