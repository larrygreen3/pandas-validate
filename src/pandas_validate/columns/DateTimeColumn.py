import dateparser
import typing

from datetime import datetime
from .Column import Column


class DateTimeColumn(Column):
	"""
	A class that represents a datetime column in a DataFrame.

	Args:
		min_date: The minimum date allowed in the column.
		max_date: The maximum date allowed in the column.
		fn: A custom validation function.
		*args: Additional arguments to pass to the validation function.
		**kwargs: Additional keyword arguments to pass to the validation function.

	Attributes:
		min_date: The minimum date allowed in the column.
		max_date: The maximum date allowed in the column.
		fn: A custom validation function.

	Methods:
		validate: Validates the values in a Series.
	"""

	def __init__(
		self,
		min_date: datetime = None,
		max_date: datetime = None,
		fn: typing.Callable = None,
		*args,
		**kwargs,
	):
		super().__init__(type="DateTime", fn=fn if callable(fn) else self.defaultFn)
		self.min_date = min_date
		self.max_date = max_date

	def defaultFn(self, x: typing.Any) -> typing.Optional[datetime]:
		"""
		The default validation function for a DateTimeColumn object.

		Args:
			x: The value to validate.

		Returns:
			The validated value, or None if the value is invalid.
		"""
		if isinstance(x, str):
			try:
				x = dateparser.parse(x)
			except (ValueError, OverflowError):
				raise ValueError(f'The value of {x} is not a valid datetime')

		if not isinstance(x, datetime):
			raise ValueError(f'The value {x} is not a valid datetime.')
		
		if self.min_date is not None and x < self.min_date:
			raise ValueError(f'The value {x} is too early.')

		if self.max_date is not None and x > self.max_date:
			raise ValueError(f'The value {x} is too late.')

		return x
