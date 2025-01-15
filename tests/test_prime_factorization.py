from num_theory.prime_factorization import prime_factorization
import pytest

def test_simple_cases():
    """Test prime factorization of simple numbers."""
    assert prime_factorization(2) == [(2, 1)]  # Smallest prime
    assert prime_factorization(3) == [(3, 1)]  # Another prime
    assert prime_factorization(4) == [(2, 2)]  # 4 = 2^2
    assert prime_factorization(5) == [(5, 1)]  # Another prime


def test_composite_numbers():
    """Test prime factorization of composite numbers."""
    assert prime_factorization(28) == [(2, 2), (7, 1)]  # 28 = 2^2 * 7
    assert prime_factorization(100) == [(2, 2), (5, 2)]  # 100 = 2^2 * 5^2
    assert prime_factorization(84) == [(2, 2), (3, 1), (7, 1)]  # 84 = 2^2 * 3 * 7


def test_large_numbers():
    """Test prime factorization of large numbers."""
    assert prime_factorization(2 ** 10) == [(2, 10)]  # Power of a single prime
    assert prime_factorization(3 ** 5) == [(3, 5)]  # Power of another prime
    assert prime_factorization(2 ** 3 * 3 ** 2 * 5) == [(2, 3), (3, 2), (5, 1)]  # Mixed primes


def test_edge_cases():
    """Test edge cases for input validation."""
    with pytest.raises(ValueError, match="Input must be a positive integer greater than 1."):
        prime_factorization(1)  # n must be > 1
    with pytest.raises(ValueError, match="Input must be a positive integer greater than 1."):
        prime_factorization(-10)  # Negative numbers are invalid
    with pytest.raises(ValueError, match="Input must be a positive integer greater than 1."):
        prime_factorization(0)  # Zero is not valid
    with pytest.raises(ValueError, match="Input must be an integer."):
        prime_factorization(2.5)  # Non-integers are invalid


def test_performance():
    """Test performance for a very large number."""
    result = prime_factorization(2 ** 20 * 3 ** 15)  # Large composite number
    assert result == [(2, 20), (3, 15)]  # Expect accurate results even for large inputs