class NegativeNumberException(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"Cannot take square root of negative number: {self.value}"
