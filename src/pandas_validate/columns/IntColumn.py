import typing
from .Column import Column


class IntColumn(Column):
	"""
	A class that represents an integer column in a DataFrame.

	Args:
		min_value: The minimum value allowed in the column.
		max_value: The maximum value allowed in the column.
		fn: A custom validation function.
		*args: Additional arguments to pass to the validation function.
		**kwargs: Additional keyword arguments to pass to the validation function.

	Attributes:
		min_value: The minimum value allowed in the column.
		max_value: The maximum value allowed in the column.
		fn: A custom validation function.

	Methods:
		validate: Validates the values in a Series.
	"""

	def __init__(
		self,
		min_value: int = None,
		max_value: int = None,
		fn: typing.Callable = None,
		*args,
		**kwargs,
	):
		super().__init__(type="int", fn=fn if callable(fn) else self.defaultFn)
		self.min_value = min_value
		self.max_value = max_value

	def defaultFn(self, x: typing.Any) -> typing.Optional[int]:
		"""
		The default validation function for an IntColumn object.

		Args:
			x: The value to validate.

		Returns:
			The validated value, or None if the value is invalid.
		"""

		try:
			i = int(float(x))
		except (ValueError, TypeError):
			raise ValueError(f'Could not convert "{x}" to an integer')

		if isinstance(self.min_value, int) and i < self.min_value:
			raise ValueError(f'The value {x} < {self.min_value}')

		if isinstance(self.max_value, int) and i > self.max_value:
			raise ValueError(f'The value {x} < {self.max_value}')

		return i
