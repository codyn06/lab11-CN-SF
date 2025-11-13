# https://github.com/codyn06/lab11-CN-SF
# Partner 1: Cody Nguyen
# Partner 2: Sara Fletcher


"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
import math
def add(a, b): 
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    try:
        return b / a
    except:
        raise ZeroDivisionError("Cannot divide by zero.")
    
def logarithm(a, b):
    try:
        return math.log(b, a)
    except:
        raise ValueError("Invalid logarathmic input.")
    
def exp(a, b):
    return a ** b

def square_root(a):
    try:
        return math.sqrt(a)
    except:
        raise ValueError("Cannot take the square root of a negative number.")

def hypotenuse(a, b):
    return math.hypot(a, b)
