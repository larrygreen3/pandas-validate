from datetime import datetime
import numpy as np
import pandas as pd

from pandas_validate import Schema
from pandas_validate.columns import IntColumn, TextColumn


class MySchema(Schema):
	IntField = IntColumn(min_value=3, max_value=124)
	TextField = TextColumn(min_length=3, max_length=5, pattern="^[a-c]+$")


def test_schema_init():
	"""
	Test that the IntColumn class can be initialized with the correct arguments.
	"""

	assert list(MySchema._getColumns().keys()) == ['IntField', 'TextField']


def test_schema_validate_valid_value():
	"""
	Test that the IntColumn class can validate a valid integer value.
	"""

	test = pd.DataFrame({
		'IntField': [3, 6, 9],
		'TextField': ['abc', 'bbca', 'ccabb']
	})
	
	validated_df, exceptions = MySchema.validate(test)

	assert validated_df.equals(test)
	assert exceptions.empty


def test_schema_validate_invalid_value():
	"""
	Test that the IntColumn class can raise an error for an invalid integer value.
	"""

	test = pd.DataFrame({
		'IntField': [1, 6, 500],
		'TextField': ['ab', 'abcd', 'ccbbaa']
	})

	expected = pd.DataFrame({
		'IntField': [None, 6, None],
		'TextField': [None, None, None]
	})

	expected_exceptions = pd.DataFrame([
			{
				'column': 'IntField', 
				'row': 0, 'value': 1, 
				'error': 'Column validation failed', 
				'error_details': 'The value 1 < 3'
			}, {
				'column': 'IntField', 
				'row': 2, 
				'value': 500, 
				'error': 'Column validation failed', 
				'error_details': 'The value 500 < 124'
			}, {
				'column': 'TextField', 
				'row': 0, 
				'value': 'ab', 
				'error': 'Column validation failed', 
				'error_details': 'The value ab is too short'
			}, {
				'column': 'TextField', 
				'row': 1, 
				'value': 
				'abcd', 
				'error': 'Column validation failed', 
				'error_details': 'The value abcd does not match the regular expression.'
			}, {
				'column': 'TextField', 
				'row': 2, 
				'value': 
				'ccbbaa', 
				'error': 'Column validation failed', 
				'error_details': 'The value ccbbaa is too long'
			}
	])
	
	validated_df, exceptions = MySchema.validate(test)

	assert validated_df.equals(expected)
	assert exceptions.equals(expected_exceptions)
