import typing
from .Column import Column


class FloatColumn(Column):
	"""
	A class that represents a float column in a DataFrame.

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
		min_value: float = None,
		max_value: float = None,
		fn: typing.Callable = None,
		*args,
		**kwargs,
	):
		super().__init__(type="float", fn=fn if callable(fn) else self.defaultFn)
		self.min_value = min_value
		self.max_value = max_value

	def defaultFn(self, x: typing.Any) -> typing.Optional[float]:
		"""
		The default validation function for a FloatColumn object.

		Args:
			x: The value to validate.

		Returns:
			The validated value, or None if the value is invalid.
		"""

		try:
			f = float(x)
		except (ValueError, TypeError):
			raise ValueError(f'Could not convert "{x}" to a float')

		if isinstance(self.min_value, float) and f < self.min_value:
			raise ValueError(f'The value {x} < {self.min_value}')

		if isinstance(self.max_value, float) and f > self.max_value:
			raise ValueError(f'The value {x} < {self.max_value}')

		return f
