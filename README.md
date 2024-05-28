# AzNum2Words

- - -
![Continuous Integration](https://github.com/zmmmdf/aznum2words/actions/workflows/ci.yml/badge.svg?branch=master)
[![GitHub Stars](https://img.shields.io/github/stars/zmmmdf/aznum2words.svg?style=social&label=Stars&style=plastic)](https://github.com/zmmmdf/aznum2words/stargazers)
[![License](https://img.shields.io/badge/license-MIT-green)](./LICENSE)

[![Switch to Azerbaijani](https://img.shields.io/badge/lang-az-brightgreen)](./README.az.md)

## Purpose

AzNum2Words serves the purpose of transforming numerical data into written Azerbaijani text, addressing various needs across financial transactions, legal documentation, and statistical analyses.

## Installation

You can install AzNum2Words via pip:

```bash
pip install aznum2words
```

## Usage

```python
from aznum2words import AzerbaijaniNumberConverter

converter = AzerbaijaniNumberConverter()
print(converter.convert(123456789))  # outputs: bir yüz iyirmi üç milyon dörd yüz əlli altı min yeddi yüz səkkiz doqquz
```

## Testing

AzNum2Words includes comprehensive test coverage to ensure reliability and accuracy. To run the tests, you can use pytest:

```bash
pip install pytest
pytest
```

## Contribution Guidelines

Contributions to AzNum2Words are welcome and encouraged! To contribute, please follow these guidelines:

1. Fork the repository.
2. Create a new branch for your feature (`git checkout -b feature/my-feature`).
3. Commit your changes (`git commit -am 'Added some feature'`).
4. Push your changes to your branch (`git push origin feature/my-feature`).
5. Submit a pull request with a clear description of your changes.

## Contributors

This project is made possible by the contributions of dedicated individuals:

<!-- Contributors list -->
<a href="https://github.com/zmmmdf/aznum2words/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=zmmmdf/aznum2words" />
</a>

<!--Made with [contrib.rocks](https://contrib.rocks). -->
<!-- Contributors list -->
