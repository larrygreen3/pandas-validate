from datetime import datetime
import pytest

from pandas_validate.columns import TextColumn


def test_text_column_init():
    """
    Test that the TextColumn class can be initialized with the correct arguments.
    """

    column = TextColumn()

    assert column.type == "str"
    assert column.min_length is None
    assert column.max_length is None


def test_text_column_validate_valid_value():
    """
    Test that the TextColumn class can validate a valid text value.
    """

    column = TextColumn()

    assert column.defaultFn("foo") == "foo"
    assert column.defaultFn("bar") == "bar"
    assert column.defaultFn("baz") == "baz"


def test_text_column_validate_invalid_value():
    """
    Test that the TextColumn class can raise an error for an invalid text value.
    """

    column = TextColumn()

    with pytest.raises(ValueError):
        column.defaultFn(1)

    with pytest.raises(ValueError):
        column.defaultFn(3.14)

    with pytest.raises(ValueError):
        column.defaultFn(datetime.now())


def test_text_column_min_length():
    """
    Test that the TextColumn class can validate a text value with a minimum length.
    """

    column = TextColumn(min_length=3)

    with pytest.raises(ValueError):
        column.defaultFn("a")

    assert column.defaultFn("abc") == "abc"
    assert column.defaultFn("abcd") == "abcd"


def test_text_column_max_length():
    """
    Test that the TextColumn class can validate a text value with a maximum length.
    """

    column = TextColumn(max_length=3)

    with pytest.raises(ValueError):
        column.defaultFn("abcd")

    assert column.defaultFn("abc") == "abc"
    assert column.defaultFn("ab") == "ab"


def test_text_column_pattern():
    """
    Test that the TextColumn class can validate a text value against a regular expression pattern.
    """

    column = TextColumn(pattern="^[a-z]+$")

    with pytest.raises(ValueError):
        column.defaultFn("123")

    assert column.defaultFn("abc") == "abc"
    assert column.defaultFn("xyz") == "xyz"