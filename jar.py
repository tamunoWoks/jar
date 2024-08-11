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