import pytest
from jar import Jar


def test_init():
    # Test default initialization
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

    # Test invalid capacity
    with pytest.raises(ValueError):
        Jar(-1)
    with pytest.raises(ValueError):
        Jar(0)
    
    # Test valid initialization
    jar = Jar(12)
    assert jar.capacity == 12
    assert jar.size == 0

def test_str():
    # Test the string representation of the jar
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"
