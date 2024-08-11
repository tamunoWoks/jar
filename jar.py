class Jar:
    def __init__(self, capacity=12):
        """
        Initializes a new Jar instance with a given capacity and size.

        :param capacity: Maximum number of cookies the jar can hold (default is 12).
        :raises ValueError: If capacity is not a non-negative integer.
        """

        if not isinstance(capacity, int) or capacity <= 0:
            raise ValueError("Invalid number")
        self._capacity = capacity  # Set the jar's capacity.
        self._size = 0  # Initialize the jar's size to 0.

    
    def __str__(self):
        """
        Returns a string representation of the jar, displaying cookies as "🍪".

        :return: A string with the current number of cookies.
        """
        return "🍪" * self._size

    
    def deposit(self, n):
        """
        Adds cookies to the jar.

        :param n: Number of cookies to add.
        :raises ValueError: If n is not a positive integer or if adding n cookies would exceed the jar's capacity.
        """
        if not isinstance(n, int) or n < 0 or self._size + n > self._capacity:
            raise ValueError("Deposit error")
        self._size += n  # Increase the size by n cookies.

    def withdraw(self, n):
        """
        Removes cookies from the jar.

        :param n: Number of cookies to remove.
        :raises ValueError: If n is greater than the current size of the jar.
        """
        if n > self._size:
            raise ValueError("Withdraw Error")
        self._size -= n  # Decrease the size by n cookies.

    @property
    def capacity(self):
        """
        Gets the current capacity of the jar.

        :return: The jar's capacity.
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        """
        Sets a new capacity for the jar.

        :param capacity: New maximum number of cookies the jar can hold.
        :raises ValueError: If capacity is not an integer, less than 1, or less than the current size.
        """
        if not isinstance(capacity, int) or capacity < 1:
            raise ValueError("@capacity.setter error")
        if capacity < self._size:
            raise ValueError("New capacity must be at least the current size")     
        self._capacity = capacity  # Update the jar's capacity.   

    @property
    def size(self):
        """
        Gets the current size of the jar.

        :return: The number of cookies currently in the jar.
        """
        return self._size
    
    @size.setter
    def size(self, size):
        """
        Sets the current size of the jar.

        :param size: New number of cookies in the jar.
        :raises ValueError: If size is not a non-negative integer or exceeds the jar's capacity.
        """
        if not isinstance(size, int) or size < 0:
            raise ValueError("@size.setter error")
        if size > self._capacity:
            raise ValueError("@size.setter error")
        self._size = size  # Update the jar's size.

def main():
    """
    Demonstrates the usage of the Jar class by creating an instance and performing deposit operations.
    """