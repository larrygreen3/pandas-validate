import pandas as pd
import typing


class Column:
	"""
	A class that represents a column in a DataFrame.

	Args:
		type: The type of the column.
		fn: The validation function for the column.

	Attributes:
		type: The type of the column.
		fn: The validation function for the column.

	Methods:
		validate: Validates the values in a Series.
	"""

	def __init__(self, type: str, fn: typing.Callable = lambda x: x, required: bool = False):
		self.type = type
		self.fn = fn
		self.required = required

	def validate(self, series: pd.Series, throw=False, *args, **kwargs) -> typing.Tuple[typing.Iterable, typing.Iterable[typing.Dict[str, typing.Any]]]:
		"""
		Validates the values in a Series.

		Args:
			series: The Series to validate.
			throw: Whether to raise an exception if a value fails validation.
			*args: Additional arguments to pass to the validation function.
			**kwargs: Additional keyword arguments to pass to the validation function.

		Returns:
			A tuple of the validated Series and a DataFrame of any errors that occurred.
		"""

		validated_series = []
		exceptions = []

		# Loop through all values
		# If the value fails the validation function return None in the series and add an Exception
		for index, value in series.items():
			try:
				validated_value = self.fn(value, *args, **kwargs)
				validated_series.append(validated_value)
			except Exception as e:
				validated_series.append(None)
				exceptions.append(dict(row=index, value=value, error="Column validation failed", error_details=str(e)))

				if throw:
					raise e

		return validated_series, exceptions
