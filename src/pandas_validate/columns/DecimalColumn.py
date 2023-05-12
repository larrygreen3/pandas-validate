import typing

from decimal import Decimal, InvalidOperation
from .Column import Column


class DecimalColumn(Column):
	"""
	A class that represents a decimal column in a DataFrame.

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
		min_value: typing.Union[Decimal, int, float] = None,
		max_value: typing.Union[Decimal, int, float] = None,
		fn: typing.Callable = None,
		*args,
		**kwargs,
	):
		super().__init__(type="Decimal", fn=fn if callable(fn) else self.defaultFn)
		self.min_value = Decimal(min_value) if min_value is not None else None
		self.max_value = Decimal(max_value) if max_value is not None else None

	def defaultFn(self, x: typing.Any) -> typing.Optional[Decimal]:
		"""
		The default validation function for a DecimalColumn object.

		Args:
			x: The value to validate.

		Returns:
			The validated value, or None if the value is invalid.
		"""

		try:
			d = Decimal(x)
		except (TypeError, InvalidOperation):
			raise ValueError(f'Could not convert "{x}" to a decimal')

		if isinstance(self.min_value, Decimal) and d < self.min_value:
			raise ValueError(f'The value {x} < {self.min_value}')

		if isinstance(self.max_value, Decimal) and d > self.max_value:
			raise ValueError(f'The value {x} < {self.max_value}')

		return d
