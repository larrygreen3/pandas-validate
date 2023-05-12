from datetime import datetime
import numpy as np
import pandas as pd

from pandas_validate.columns import Column


def test_column_init():
	"""
	Test that the IntColumn class can be initialized with the correct arguments.
	"""

	column = Column(type='object')

	assert column.type == "object"
	assert callable(column.fn)


def test_column_validate_valid_value():
	"""
	Test that the IntColumn class can validate a valid integer value.
	"""

	column = Column(type='object')
	test = [None, 1, 1.3, 'testing']
	check = [None, 1, 1.3, 'testing']
	
	validated_series, exceptions = column.validate(pd.Series(test))

	assert validated_series == check
	assert len(exceptions) == 0


def test_column_validate_invalid_value():
	"""
	Test that the IntColumn class can raise an error for an invalid integer value.
	"""

	column = Column(type='object', fn=lambda x: int(x))
	test = [None, 1, 1.3, 'testing', datetime.now()]
	check = [None, 1, 1, None, None]

	validated_series, exceptions = column.validate(pd.Series(test))

	assert validated_series == check
	assert len(exceptions) == 3
