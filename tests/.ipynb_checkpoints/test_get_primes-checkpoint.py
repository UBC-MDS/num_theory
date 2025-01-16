from num_theory.get_primes import get_primes
import pytest

def test_get_primes():
    x = 0
    expected = []
    actual = get_primes(x)
    assert expected == actual

def test2_get_primes():
    x = -2
    expected = []
    actual = get_primes(x)
    assert expected == actual

def test3_get_primes():
    x = 1
    expected = []
    actual = get_primes(x)
    assert expected == actual

def test4_get_primes():
    x = 0.5
    expected = []
    actual = get_primes(x)
    assert expected == actual

def test5_get_primes():
    x = 14
    expected = [2, 3, 5, 7, 11, 13]
    actual = get_primes(x)
    assert expected == actual

def test6_get_primes():
    x = 13
    expected = [2, 3, 5, 7, 11, 13]
    actual = get_primes(x)
    assert expected == actual

def test7_get_primes():
    x = [5]
    with pytest.raises(TypeError):
        get_primes(x)

def test8_get_primes():
    x = "String"
    with pytest.raises(TypeError):
        get_primes(x)
