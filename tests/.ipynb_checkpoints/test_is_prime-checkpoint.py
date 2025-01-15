import pytest
from num_theory.is_prime import is_prime

def test_prime_numbers():
    """Test edge cases for prime numbers."""
    assert is_prime(2) == True, "2 should be prime"
    assert is_prime(13) == True, "13 should be prime"
    assert is_prime(101) == True, "101 should be prime"

def test_non_prime_numbers():
    """Test edge cases for non-prime numbers."""
    assert is_prime(4) == False, "4 should not be prime"
    assert is_prime(100) == False, "100 should not be prime"
    with pytest.raises(ValueError):
        is_prime(1) 

def test_invalid_inputs():
    """Test invalid inputs."""
    with pytest.raises(ValueError):
        is_prime(-3)
    with pytest.raises(ValueError):
        is_prime(0)
    with pytest.raises(ValueError):
        is_prime(1)
    with pytest.raises(ValueError):
        is_prime(3.5)
    with pytest.raises(ValueError):
        is_prime("ten") 
