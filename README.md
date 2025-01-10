# num_theory

Implements different number theory functions

## Installation

```bash
$ pip install num_theory
```

## Usage

This package provides a set of basic number theory utilities that ease the solution of Project Euler and other computational problems. It includes prime generation, prime factorization, and arithmetic progression handling. The utilities herein are implemented for efficiency, having ease of use in mind. This makes the package very useful for both mathematicians and competitive programmers.

### The following functions have been implemented in this package.

get_prime_list_under_n(n): Generates all prime numbers less than n using an efficient algorithm. Useful for operations requiring precomputed prime numbers.

generate_prime_fatorization(n): Computes the prime factorization of a number, returning a list of tuples where each tuple contains a prime factor and its power.

arithmetic_progression(a, d, n, compute_sum=False, nth_term=False): Generate terms of an arithmetic progression (AP), compute the nth term, or calculate the sum of the first n terms.

is_prime(n): Checks if a number is prime using a streamlined algorithm optimized for computational challenges.

### Relevance in the Python Ecosystem

This package complements existing Python libraries by offering a targeted collection of number theory utilities specifically for solving Project Euler problems.

Related Packages:

• SymPy: This does provide some symbolic mathematics, including some number theory, but isn't optimized for the computational challenges of advanced number theory.

• NumPy: The general-purpose library for numerical computations, but not specialized in number theory.

• primesieve: A highly efficient library for prime generation. This package provides similar functionalities.

## Contributors

1. Calista Chen
2. Dhruv Garg
3. Dominic Lam
4. Thamer Aldawood

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`num_theory` was created by Calista Chen, Dhruv Garg, Dominic Lam, Thamer Aldawood. It is licensed under the terms of the MIT license.


## Credits

`num_theory` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).

