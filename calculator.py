"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    # raise ZeroDivisionError if dividing by zero
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b

def log(a, b):
    # raise ValueError if a <= 0, b <= 0, or a == 1
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("Invalid input for logarithm.")
    return math.log(b, a)

def exp(a, b):
    return a ** b

