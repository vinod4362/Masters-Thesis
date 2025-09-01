import pytest
from experiment_package.task4_unit_tests.normalizer import normalize_text


def test_none_input():
    result = normalize_text(None)
    assert result == ""
    assert isinstance(result, str)

def test_empty_string():
    result = normalize_text("")
    assert result == ""
    assert isinstance(result, str)

def test_only_punctuation():
    assert normalize_text("!!!") == ""
    assert normalize_text("@#$%^&*") == ""

def test_mixed_case():
    assert normalize_text("HeLLo WoRLd") == "hello world"

def test_numbers():
    assert normalize_text("abc123XYZ") == "abc123xyz"
    assert normalize_text("2025 is here!") == "2025 is here"

def test_multiple_spaces_and_punct():
    assert normalize_text("A   B..C!! D") == "a b c d"

def test_leading_trailing_spaces():
    assert normalize_text("   hello world   ") == "hello world"

def test_alphanumeric_and_underscore():
    assert normalize_text("foo_bar-BAZ") == "foo bar baz"

def test_long_string():
    s = "The quick brown fox jumps over 13 lazy dogs!"
    expected = "the quick brown fox jumps over 13 lazy dogs"
    assert normalize_text(s) == expected
# TODO: Add tests for:
# - empty string
# - None -> ""
# - punctuation collapse
# - mixed case
# - numbers and letters
# Use pytest parametrization where appropriate.
def test_placeholder():
    assert True
