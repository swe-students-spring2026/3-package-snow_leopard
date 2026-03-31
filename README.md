# pyquote

[![CI / CD](https://github.com/swe-students-spring2026/3-package-snow_leopard/actions/workflows/build.yaml/badge.svg?branch=main)](https://github.com/swe-students-spring2026/3-package-snow_leopard/actions/workflows/build.yaml)

## Overview
**pyquote** is a Python package that provides quotes, compliments, and fortunes for developers.

---

## Installation

### From PyPI
https://pypi.org/project/

```bash
pip install pyquote
```

---

## Usage

### Import
```python
from your_package import (
    get_quote_by_type,
    get_random_quote,
    get_compliment,
    get_fortune,
    get_quotes_by_author_name
)
```

### Examples
```python
print(get_random_quote(1))
print(get_quote_by_type("motivation", 2))
print(get_compliment(personality=True))
print(get_fortune("tech"))
print(get_quotes_by_author_name("Mahatma Gandhi"))
```

---

## API

### get_quote_by_type(quote_type, num_of_quotes=1)
Return one or more quotes filtered by type.

### get_random_quote(num_of_quotes)
Return a list of random quotes.

### get_compliment(appearance=False, personality=False, corny=False)
Return a compliment filtered by tags.

### get_fortune(topic)
Return a fortune for a topic: general, tech, career, love.

---

## Development

### Setup
```bash
git clone https://github.com/swe-students-spring2026/3-package-snow_leopard
cd 3-package-snow_leopard

pip install pipenv
pipenv install --dev
pipenv shell
```

### Test
```bash
pytest
```

### Contribute
```bash
git checkout -b feature/your-feature
git commit -m "Add feature"
git push origin feature/your-feature
```

---

## Contributors
- https://github.com/mikhailbond1
- https://github.com/ClaireBocz
- https://github.com/ermuun0930
- https://github.com/lucasbazoberry
- https://github.com/ChrisC0205