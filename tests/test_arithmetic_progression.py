import pytest
from num_theory.arithmetic_progression import arithmetic_progression

def test_check_ap_sum():
    expected = 40
    actual = arithmetic_progression(a=2, d=3, n=5, compute_sum=True)
    assert actual == expected