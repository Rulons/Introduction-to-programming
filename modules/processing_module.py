# processing_module.py

def add(a, b):
    """Function to add two numbers."""
    return a + b

def subtract(a, b):
    """Function to subtract the second number from the first."""
    return a - b

def multiply(a, b):
    """Function to multiply two numbers."""
    return a * b

def divide(a, b):
    """Function to divide the first number by the second."""
    if b != 0:
        return a / b
    else:
        print("Error: Division by zero is not allowed.")
        return None
