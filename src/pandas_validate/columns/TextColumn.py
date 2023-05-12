import typing

from re import match
from .Column import Column


class TextColumn(Column):
	"""
	A class that represents a text column in a DataFrame.

	Args:
		min_length: The minimum length of the text values in the column.
		max_length: The maximum length of the text values in the column.
		pattern: A regular expression that the strings in the column must match.
		fn: A custom validation function.
		*args: Additional arguments to pass to the validation function.
		**kwargs: Additional keyword arguments to pass to the validation function.

	Attributes:
		min_length: The minimum length of the text values in the column.
		max_length: The maximum length of the text values in the column.
		fn: A custom validation function.

	Methods:
		validate: Validates the values in a Series.
	"""

	def __init__(
		self,
		min_length: int = None,
		max_length: int = None,
		pattern: str = None,
		fn: typing.Callable = None,
		*args,
		**kwargs,
	):
		super().__init__(type="str", fn=fn if callable(fn) else self.defaultFn)
		self.min_length = min_length
		self.max_length = max_length
		self.pattern = pattern

	def defaultFn(self, x: typing.Any) -> typing.Optional[str]:
		"""
		The default validation function for a TextColumn object.

		Args:
			x: The value to validate.

		Returns:
			The validated value, or None if the value is invalid.
		"""

		if not isinstance(x, str):
			raise ValueError(f'The value {x} is not a string')

		if self.min_length is not None and len(x) < self.min_length:
			raise ValueError(f'The value {x} is too short')

		if self.max_length is not None and len(x) > self.max_length:
			raise ValueError(f'The value {x} is too long')
		
		if self.pattern is not None and not match(self.pattern, x):
			raise ValueError(f'The value {x} does not match the regular expression.')

		return x
