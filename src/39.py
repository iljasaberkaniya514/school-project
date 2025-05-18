def add_numbers(x, y):
    return x + y

def subtract_numbers(x, y):
    return x - y

def multiply_numbers(x, y):
    return x * y

def divide_numbers(x, y):
    if y != 0:
        return x / y
    else:
        raise ValueError("Cannot divide by zero")

# Example usage:
result = add_numbers(5, 3)
print(f"Result of adding 5 and 3: {result}")
