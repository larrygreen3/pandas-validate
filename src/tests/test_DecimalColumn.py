from datetime import datetime
from decimal import Decimal
import pytest

from pandas_validate.columns import DecimalColumn


def test_decimal_column_init():
    """
    Test that the DecimalColumn class can be initialized with the correct arguments.
    """

    column = DecimalColumn(min_value=1.0, max_value=10.0, precision=2)

    assert column.type == "Decimal"
    assert column.min_value == 1.0
    assert column.max_value == 10.0


def test_decimal_column_validate_valid_value():
    """
    Test that the DecimalColumn class can validate a valid decimal value.
    """

    column = DecimalColumn(min_value=1.0, max_value=10.0, precision=2)

    assert column.defaultFn(1) == 1.0
    assert column.defaultFn(5.0) == 5.0
    assert column.defaultFn(10.0) == 10.0


def test_decimal_column_validate_invalid_value():
    """
    Test that the DecimalColumn class can raise an error for an invalid decimal value.
    """

    column = DecimalColumn(min_value=1.0, max_value=10.0, precision=2)

    with pytest.raises(ValueError):
        column.defaultFn(0.0)

    with pytest.raises(ValueError):
        column.defaultFn(11.0)


def test_decimal_column_validate_string_value():
    """
    Test that the DecimalColumn class can raise an error for a string value.
    """

    column = DecimalColumn(min_value=1.0, max_value=10.0)

    with pytest.raises(ValueError):
        column.defaultFn("foo")

    assert column.defaultFn("3") == Decimal("3")
    assert column.defaultFn("5.4") == Decimal("5.4")


def test_decimal_column_validate_int_value():
    """
    Test that the DecimalColumn class can raise an error for an int value.
    """

    column = DecimalColumn(min_value=1.0, max_value=10.0)

    assert column.defaultFn(3) == Decimal(3)
    assert column.defaultFn(5.4) == Decimal(5.4)


def test_decimal_column_validate_datetime_value():
    """
    Test that the DecimalColumn class can raise an error for a datetime value.
    """

    column = DecimalColumn(min_value=1.0, max_value=10.0)

    with pytest.raises(ValueError):
        column.defaultFn(datetime.now())

