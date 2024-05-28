# cbar-currency-rates

- - -
[![GitHub Stars](https://img.shields.io/github/stars/zmmmdf/cbar-currency-rates.svg?style=social&label=Stars&style=plastic)](https://github.com/zmmmdf/cbar-currency-rates/stargazers)
[![License](https://img.shields.io/badge/license-MIT-green)](./LICENSE)
[![Switch to Azerbaijani](https://img.shields.io/badge/lang-az-brightgreen)](./README.az.md)

## Purpose

cbar-currency-rates serves the purpose of providing easy access to currency exchange rates from the Central Bank of Azerbaijan Republic (CBAR) XML file. It enables developers to integrate up-to-date currency rates into their applications, facilitating financial calculations and analysis.

## Installation

You can install cbar-currency-rates via pip:

```bash
pip install cbar-currency-rates
```

## Usage

```python
from cbar_currency_rates import rates

# Instantiate CBARRates object
cbar = rates.CBARRates()

# Get currency rates
rates = cbar.get_rates()

# Print currency rates
for code, value in rates.items():
    print(code, "-", value)
```

## Testing

cbar-currency-rates includes comprehensive test coverage to ensure reliability and accuracy. To run the tests, you can use pytest:

```bash
pip install pytest
pytest
```

## Contribution Guidelines

Contributions to cbar-currency-rates are welcome and encouraged! To contribute, please follow these guidelines:

1. Fork the repository.
2. Create a new branch for your feature (`git checkout -b feature/my-feature`).
3. Commit your changes (`git commit -am 'Added some feature'`).
4. Push your changes to your branch (`git push origin feature/my-feature`).
5. Submit a pull request with a clear description of your changes.

## Contributors

This project is made possible by the contributions of dedicated individuals:

<!-- Contributors list -->
<a href="https://github.com/zmmmdf/cbar-currency-rates/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=zmmmdf/cbar-currency-rates" />
</a>

<!--Made with [contrib.rocks](https://contrib.rocks). -->
<!-- Contributors list -->


