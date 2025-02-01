# num_theory
[![Documentation Status](https://readthedocs.org/projects/num-theory/badge/?version=latest)](https://num-theory.readthedocs.io/en/latest/?badge=latest)
[![codecov](https://codecov.io/gh/UBC-MDS/num_theory/graph/badge.svg?token=D83Q1sJfPf)](https://codecov.io/gh/UBC-MDS/num_theory)
[![ci-cd](https://github.com/UBC-MDS/num_theory/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/UBC-MDS/num_theory/actions/workflows/ci-cd.yml)
![Python Version](https://img.shields.io/badge/python-3.9%20%7C%203.10%20%7C%203.11-blue.svg)
[![Repo Status](https://img.shields.io/badge/repo%20status-Active-brightgreen)](https://github.com/UBC-MDS/num_theory) 
![PyPI](https://img.shields.io/pypi/v/num-theory-euler-problems?color=blue&label=PyPI)


A high-performance Python package for number theory operations, optimized for Project Euler and computational mathematics problems.  From prime factorization to generating arithmetic progressions, the num_theory package is a versatile tool for students, researchers, and enthusiasts alike. It can also serve as a utility for developing solutions to Project Euler problems.

## Features

- Fast prime number generation and primality testing
- Efficient prime factorization
- Arithmetic progression calculations
- Optimized for computational challenges and competitive programming
- Simple, intuitive API design

## Installation

```bash
pip install num_theory_euler_problems
```

## Usage

### Prime Numbers

```python
from num_theory import get_primes, is_prime, prime_factorization

# Generate all primes under 100
primes = get_primes(100)

# Check if a number is prime
is_prime(997)  # Returns True

# Get prime factorization
factors = prime_factorization(84)  # Returns [(2, 2), (3, 1), (7, 1)]
```

### Arithmetic Progressions

Real-Life Application: Saving Money with an Arithmetic Progression
Imagine you want to save money using an increasing savings plan. You start with $50 in the first month, and you decide to increase your savings by $20 each month.

You can use the arithmetic_progression function to calculate:

The amount of money saved each month for 6 months
The total amount saved after 6 months
The exact amount saved in the 6th month

```python
from num_theory import arithmetic_progression

# 1. Get the savings amount for each month
monthly_savings = arithmetic_progression(a=50, d=20, n=6)
print(monthly_savings)
# Output: [50, 70, 90, 110, 130, 150]

# 2. Calculate the total amount saved in 6 months
total_savings = arithmetic_progression(a=50, d=20, n=6, compute_sum=True)
print(total_savings)
# Output: 600.0

# 3. Find the savings amount in the 6th month
sixth_month_savings = arithmetic_progression(a=50, d=20, n=6, nth_term=True)
print(sixth_month_savings)
# Output: 150

```

## Key Functions

| Function | Description | Example |
|----------|-------------|---------|
| `get_prime_list_under_n(n)` | Generates all primes less than n | `get_prime_list_under_n(10)` returns `[2, 3, 5, 7]` |
| `prime_factorization(n)` | Returns prime factors with their powers | `prime_factorization(12)` returns `[(2, 2), (3, 1)]` |
| `arithmetic_progression(a, d, n, ...)` | Handles arithmetic progression operations | See examples above |
| `is_prime(n)` | Tests primality efficiently | `is_prime(17)` returns `True` |

### Relevance in the Python Ecosystem

This package complements existing Python libraries by offering a targeted collection of number theory utilities specifically for solving Project Euler problems.

Related Packages:

- SymPy: This does provide some symbolic mathematics, including some number theory, but isn't optimized for the computational challenges of advanced number theory.
- NumPy: The general-purpose library for numerical computations, but not specialized in number theory.
- primesieve: A highly efficient library for prime generation. This package provides similar functionalities.

## Comparison with Other Libraries

| Feature | num_theory | SymPy | NumPy | primesieve |
|---------|------------|-------|-------|------------|
| Focus | Number Theory | Symbolic Math | Numerical Computing | Prime Generation |
| Optimization | Project Euler | General Math | General Purpose | Prime Numbers |
| Learning Curve | Simple | Steep | Moderate | Simple |
| Speed | Fast | Moderate | Fast | Very Fast |

## Contributing

Interested in contributing? Check out the [contributing guidelines](contributing.md) . Please note that this project is released with a [Code of Conduct](conduct.md). By contributing to this project, you agree to abide by its terms.

## Authors

- Dhruv Garg
- Dominic Lam
- Thamer Aldawood
- Tingting Chen

## License

`num_theory` was created by Dhruv Garg, Dominic Lam, Thamer Aldawood, Tingting Chen. It is licensed under the terms of the MIT license.

## Credits

`num_theory` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).