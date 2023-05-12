from datetime import datetime
import pytest

from pandas_validate.columns import DateTimeColumn


def test_datetime_column_init():
	"""
	Test that the DateTimeColumn class can be initialized with the correct arguments.
	"""

	column = DateTimeColumn()

	assert column.type == "DateTime"
	assert column.min_date is None
	assert column.max_date is None


def test_datetime_column_validate_valid_value():
	"""
	Test that the DateTimeColumn class can validate a valid datetime value.
	"""

	column = DateTimeColumn()

	now = datetime.now()

	assert column.defaultFn(now) == now


def test_datetime_column_validate_invalid_value():
	"""
	Test that the DateTimeColumn class can raise an error for an invalid datetime value.
	"""

	column = DateTimeColumn()

	with pytest.raises(ValueError):
		column.defaultFn("foo")

	with pytest.raises(ValueError):
		column.defaultFn(1)

	with pytest.raises(ValueError):
		column.defaultFn(3.14)

def test_datetime_column_min_date():
	"""
	Test that the DateTimeColumn class can validate a datetime value with a minimum date.
	"""

	column = DateTimeColumn(min_date=datetime(2023, 5, 10))

	with pytest.raises(ValueError):
		column.defaultFn(datetime(2023, 5, 9))

	assert column.defaultFn(datetime(2023, 5, 10)) == datetime(2023, 5, 10)


def test_datetime_column_max_date():
	"""
	Test that the DateTimeColumn class can validate a datetime value with a maximum date.
	"""

	column = DateTimeColumn(max_date=datetime(2023, 5, 10))

	with pytest.raises(ValueError):
		column.defaultFn(datetime(2023, 5, 11))

	assert column.defaultFn(datetime(2023, 5, 10)) == datetime(2023, 5, 10)

def test_datetime_column_valid_string_date():
    """
    Test that the DateTimeColumn class can validate a valid datetime value represented as a string.
    """

    column = DateTimeColumn()

    assert column.defaultFn("2023-05-10") == datetime(2023, 5, 10)


def test_datetime_column_invalid_string_date():
    """
    Test that the DateTimeColumn class can raise an error for an invalid datetime value represented as a string.
    """

    column = DateTimeColumn()

    with pytest.raises(ValueError):
        column.defaultFn("foo")

    with pytest.raises(ValueError):
        column.defaultFn("2023-05-32")