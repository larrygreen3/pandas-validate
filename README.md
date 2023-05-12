# pandas_validate

A python package used for validating pandas dataframes.

## ⚙️ Installation

```sh
python -m pip install pandas_validate
```


## 🚀 Usage

```python
# Imports
import pandas as pd

from pandas_validate import Schema
from pandas_validate.columns import IntColumn, TextColumn


# Define your Schema
class MySchema(Schema):
	IntField = IntColumn(min_value=3, max_value=10)
	TextField = TextColumn(min_length=3, max_length=5, pattern="^[a-c]+$")


# Get your DataFrame
df = pd.DataFrame({
	'IntField': [1, 6, 11, 7],
	'TextField': ['ab', 'abcd', 'ccbbaa', 'ccb'],
	'UnknownField': [1, 2, 3, 4]
})


# Validate your DataFrame
validated_df, exceptions = MySchema.validate(df)
```

Results
```python
>>> print(validated_df)

   IntField TextField
0       NaN      None
1       6.0      None
2       NaN      None
3       7.0       ccb


>>> print(exceptions)

         column  row   value                     error                                      error_details
0      IntField  0.0       1  Column validation failed                                    The value 1 < 3
1      IntField  2.0      11  Column validation failed                                  The value 11 < 10
2     TextField  0.0      ab  Column validation failed                          The value ab is too short
3     TextField  1.0    abcd  Column validation failed  The value abcd does not match the regular expr...
4     TextField  2.0  ccbbaa  Column validation failed                       The value ccbbaa is too long
5  UnknownField  NaN    None            Unknown Column     The column "UnknownField" is not in the Schema

```



## Code Contributors

This project exists thanks to all the people who contribute. [[Contribute](CONTRIBUTING.md)].

[Current Contributors](https://github.com/larrygreen3/pandas-validate/graphs/contributors)


## 🤝 Contributing

Contributions, issues and feature requests are welcome.<br />
Feel free to check [issues page](https://github.com/larrygreen3/pandas-validate/issues) if you want to contribute.<br />
[Check the contributing guide](CONTRIBUTING.md).<br />

## Author

👤 **Larry Green**

- Github: [@larrygreen3](https://github.com/larrygreen3)

## Show your support

Please ⭐️ this repository if this project helped you!


## 📝 License

Copyright © 2023 [Larry Green](https://github.com/larrygreen3).<br />
This project is [MIT](https://github.com/larrygreen3/pandas-validate/blob/master/LICENSE) licensed.

---