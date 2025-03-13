import random

def get_random_python_code():
    """Returns a random Python code snippet"""
    # Generate a random integer between 1 and 10
    x = random.randint(1, 10)
    # Use the integer to generate a random operation (+, -, *, /)
    op = "+" if x % 2 == 0 else "-"
    # Generate two more random integers between 1 and 10
    y = random.randint(1, 10)
    z = random.randint(1, 10)
    # Use the operation to perform a calculation on the integers
    result = eval(f"{x}{op}{y} {op} {z}")
    # Return the code snippet as a string
    return f"{x}{op}{y} {op} {z} = {result}"