import pytest
from num_theory.arithmetic_progression import arithmetic_progression

def test_check_ap_sum_1():
    """Test the compute_sum=True"""
    result = arithmetic_progression(a=2, d=3, n=5, compute_sum=True)
    assert result == 40, f"Expected 25.0, got {result}"

def test_generate_terms():
    """Test generating terms of an arithmetic progression."""
    result = arithmetic_progression(a=1, d=2, n=5)
    assert result == [1, 3, 5, 7, 9], f"Expected [1, 3, 5, 7, 9], got {result}"

def test_nth_term():
    """Test the nth_term= True"""
    result = arithmetic_progression(a=1, d=2, n=5, nth_term=True)
    assert result == 9, f"Expected 9, got {result}"

def test_both_compute_sum_and_nth_term():
    """Test when both compute_sum=True and nth_term=True."""
    result = arithmetic_progression(a=1, d=2, n=5, compute_sum=True, nth_term=True)
    assert result == 9, f"Expected 9, got {result}"

def test_zero_terms():
    """Test when n is zero, which should raise a ValueError."""
    try:
        arithmetic_progression(a=1, d=2, n=0)
        assert False, "Expected ValueError, but no exception was raised"
    except ValueError as e:
        assert str(e) == "The number of terms 'n' must be a positive integer."

def test_negative_terms():
    """Test when n is negative, which should raise a ValueError."""
    try:
        arithmetic_progression(a=1, d=2, n=-5)
        assert False, "Expected ValueError, but no exception was raised"
    except ValueError as e:
        assert str(e) == "The number of terms 'n' must be a positive integer."

def test_no_flags():
    """Test the else branch when no flags are set."""
    result = arithmetic_progression(a=3, d=3, n=4)
    assert result == [3, 6, 9, 12], f"Expected [3, 6, 9, 12], got {result}"

def test_edge_case_first_term():
    """Test the nth_term=True for the first term."""
    result = arithmetic_progression(a=10, d=5, n=1, nth_term=True)
    assert result == 10, f"Expected 10, got {result}"

def test_large_progression():
    """Test generating a large progression."""
    result = arithmetic_progression(a=1, d=1, n=1000)
    assert result[0] == 1, f"Expected first term 1, got {result[0]}"
    assert result[-1] == 1000, f"Expected last term 1000, got {result[-1]}"

def test_large_sum():
    """Test the sum of a large progression."""
    result = arithmetic_progression(a=1, d=1, n=1000, compute_sum=True)
    assert result == 500500.0, f"Expected 500500.0, got {result}"

def test_large_nth_term():
    """Test computing the nth term for a large n."""
    result = arithmetic_progression(a=2, d=5, n=1000, nth_term=True)
    assert result == 4997, f"Expected 4997, got {result}"
