def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b

def divide(a, b):
    if a == 0 or b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
