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
        