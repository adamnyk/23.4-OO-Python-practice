"""Python serial number generator."""


class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    Attributes
    -----------
    start: int
        starting value

    current_val: int (generated)
        starts at starting value -1

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start):
        """Initialize a serial generator with a starting int value of 'start'"""
        self.start = start
        self.current_val = start - 1

    def __repr__(self):
        return f"<SerialGenerator start={self.start} current_val={self.current_val}>"

    def generate(self):
        """
        Increments current_val by 1 and returns current_val
        """
        self.current_val += 1
        return self.current_val
    
    def reset(self):
        '''Resets instance to its initial start values'''
        self.current_val = self.start -1