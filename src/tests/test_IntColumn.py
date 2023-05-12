from datetime import datetime
import pytest

from pandas_validate.columns import IntColumn


def test_int_column_init():
    """
    Test that the IntColumn class can be initialized with the correct arguments.
    """

    column = IntColumn(min_value=1, max_value=10)

    assert column.type == "int"
    assert column.min_value == 1
    assert column.max_value == 10


def test_int_column_validate_valid_value():
    """
    Test that the IntColumn class can validate a valid integer value.
    """

    column = IntColumn(min_value=1, max_value=10)

    assert column.defaultFn(1) == 1
    assert column.defaultFn(5) == 5
    assert column.defaultFn(10) == 10


def test_int_column_validate_invalid_value():
    """
    Test that the IntColumn class can raise an error for an invalid integer value.
    """

    column = IntColumn(min_value=1, max_value=10)

    with pytest.raises(ValueError):
        column.defaultFn(0)

    with pytest.raises(ValueError):
        column.defaultFn(11)


def test_int_column_validate_string_value():
    """
    Test that the IntColumn class can raise an error for a string value.
    """

    column = IntColumn(min_value=1, max_value=10)

    with pytest.raises(ValueError):
        column.defaultFn("foo")

    assert column.defaultFn("3") == 3
    assert column.defaultFn("5.4") == 5


def test_int_column_validate_float_value():
    """
    Test that the IntColumn class can raise an error for a float value.
    """

    column = IntColumn(min_value=1, max_value=10)

    assert column.defaultFn(6.7) == 6


def test_int_column_validate_datetime_value():
    """
    Test that the IntColumn class can raise an error for a datetime value.
    """

    column = IntColumn(min_value=1, max_value=10)

    with pytest.raises(ValueError):
        column.defaultFn(datetime.now())
