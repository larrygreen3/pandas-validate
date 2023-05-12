from datetime import datetime
import pytest

from pandas_validate.columns import FloatColumn


def test_float_column_init():
    """
    Test that the FloatColumn class can be initialized with the correct arguments.
    """

    column = FloatColumn(min_value=1.0, max_value=10.0)

    assert column.type == "float"
    assert column.min_value == 1.0
    assert column.max_value == 10.0


def test_float_column_validate_valid_value():
    """
    Test that the FloatColumn class can validate a valid float value.
    """

    column = FloatColumn(min_value=1.0, max_value=10.0)

    assert column.defaultFn(1.0) == 1.0
    assert column.defaultFn(5.0) == 5.0
    assert column.defaultFn(10.0) == 10.0


def test_float_column_validate_invalid_value():
    """
    Test that the FloatColumn class can raise an error for an invalid float value.
    """

    column = FloatColumn(min_value=1.0, max_value=10.0)

    with pytest.raises(ValueError):
        column.defaultFn(0.0)

    with pytest.raises(ValueError):
        column.defaultFn(11.0)


def test_float_column_validate_string_value():
    """
    Test that the FloatColumn class can raise an error for a string value.
    """

    column = FloatColumn(min_value=1.0, max_value=10.0)

    with pytest.raises(ValueError):
        column.defaultFn("foo")

    assert column.defaultFn("3.0") == 3.0
    assert column.defaultFn("5.4") == 5.4


def test_float_column_validate_int_value():
    """
    Test that the FloatColumn class can raise an error for an int value.
    """

    column = FloatColumn(min_value=1.0, max_value=10.0)

    assert column.defaultFn(3) == 3.0
    assert column.defaultFn(5.4) == 5.4


def test_float_column_validate_datetime_value():
    """
    Test that the FloatColumn class can raise an error for a datetime value.
    """

    column = FloatColumn(min_value=1.0, max_value=10.0)

    with pytest.raises(ValueError):
        column.defaultFn(datetime.now())

