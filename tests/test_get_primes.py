from num_theory.get_primes import get_primes
import pytest

def test_get_primes_zero():
    """Testing edge case where x = 0"""
    x = 0
    expected = []
    actual = get_primes(x)
    assert expected == actual, "Given 0, should return an empty list"

def test_get_primes_negative():
    """Testing edge case where x is negative"""
    x = -2
    expected = []
    actual = get_primes(x)
    assert expected == actual, "Given a negative number, should return an empty list"

def test_get_primes_small():
    """Testing edge case where x = 1"""
    x = 1
    expected = []
    actual = get_primes(x)
    assert expected == actual, "Given 0, should return an empty list"

def test_get_primes_fraction():
    """Testing edge case where x is a fraction"""
    x = 0.5
    expected = []
    actual = get_primes(x)
    assert expected == actual, "Given 0.5, should return an empty list"

def test_get_primes_over():
    """Testing case where x is just over a prime"""
    x = 14
    expected = [2, 3, 5, 7, 11, 13]
    actual = get_primes(x)
    assert expected == actual, f"Expected {expected}, got {actual}"

def test_get_primes_exact():
    """Testing case where x is a prime"""
    x = 13
    expected = [2, 3, 5, 7, 11, 13]
    actual = get_primes(x)
    assert expected == actual, f"Expected {expected}, got {actual}"

def test_get_primes_list():
    """Testing edge case where x is a list"""
    x = [5]
    with pytest.raises(TypeError):
        get_primes(x)

def test_get_primes_string():
    """Testing edge case where x is a string"""
    x = "String"
    with pytest.raises(TypeError):
        get_primes(x)

# Additional tests for bad inputs
@pytest.mark.parametrize(
    "x",
    [
        [2,4,5],
        {3,4},
        {'key':'val'},
        (1,2),
        None
    ]
)
def test_get_primes_string_bad_inputs(x):
    with pytest.raises(TypeError):
        get_primes(x)
