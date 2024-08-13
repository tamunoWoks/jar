import pytest
from jar import Jar


def test_init():
    # Test default initialization
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0