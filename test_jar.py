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

def test_deposit():
    # Test depositing cookies
    jar = Jar()
    jar.deposit(1)
    assert jar.size == 1

    # Test exceeding capacity
    with pytest.raises(ValueError):
        jar.deposit(20)

def test_withdraw():
    # Test withdrawing cookies
    jar = Jar()
    jar.deposit(4)
    jar.withdraw(1)
    assert jar.size == 3

    # Test withdrawing more than available
    with pytest.raises(ValueError):
        jar.withdraw(100)

def test_capacity_setter():
    # Test setting a new capacity
    jar = Jar(10)
    jar.deposit(5)
    assert jar.capacity == 10

    # Test setting capacity less than current size
    with pytest.raises(ValueError):
        jar.capacity = 4

def test_size_setter():
    # Test setting size directly
    jar = Jar(10)
    jar.deposit(5)
    jar.size = 3
    assert jar.size == 3


