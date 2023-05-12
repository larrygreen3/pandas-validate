import typing
import pandas as pd

from .columns import Column


class Schema:
	"""
    A class that represents a schema for a DataFrame.

    Methods:
        validate: Validates a DataFrame against the schema.
    """
    
	@classmethod
	def _getColumns(self) -> dict:
		"""
        Gets the columns of the schema.

        Returns:
            A dictionary of column names to Column objects.
        """
		return {attribute: value for attribute, value in self.__dict__.items() if isinstance(value, Column)}

	@classmethod
	def validate(cls, df: pd.DataFrame, throw: bool = False, ignore_unknown_columns: bool = False) -> typing.Tuple[pd.DataFrame, pd.DataFrame]:
		"""
        Validates a DataFrame against the schema.

        Args:
            df: The DataFrame to validate.
            throw: Whether to raise an exception if a column is missing or invalid.
            ignore_unknown_columns: Whether to ignore columns which are not in the schema.

        Returns:
            A tuple of the validated DataFrame and a DataFrame of any errors that occurred.
        """
		validated_df = pd.DataFrame()
		exceptions = {}

		# Validate all columns within the Schema
		for column_name, column in cls._getColumns().items():
			try:
				validated_df[column_name], exceptions[column_name] = column.validate(df[column_name], throw=throw)
			except KeyError:
				if column.required:
					error_details = f'The column "{column_name}" is not in the input DataFrame'
					exceptions[column_name] = [dict(row=None, value=None, error="Missing Column", error_details=error_details)]
					if throw:
						raise KeyError(error_details)

		# Find any columns which are in the dataframe, but not in the Schema
		for column_name in df.columns:
			if not ignore_unknown_columns and column_name not in cls._getColumns():
				error_details = f'The column "{column_name}" is not in the Schema'
				exceptions[column_name] = [dict(row=None, value=None, error="Unknown Column", error_details=error_details)]
				if throw:
					raise KeyError(error_details)
		
		# Convert the exceptions dict into a format that can be turned into a DataFrame
		exceptions_arr = [dict(column=c, **e) for c in exceptions for e in exceptions[c]]
				
		return validated_df, pd.DataFrame(exceptions_arr)
