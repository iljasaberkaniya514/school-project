def add_numbers(a, b):
    return a + b

def calculate_average(numbers):
    if not numbers:
        raise ValueError("Cannot divide by an empty list")
    total = sum(numbers)
    average = total / len(numbers)
    return average

numbers = [10, 20, 30, 40, 50]
average = calculate_average(numbers)
print(f"The average of the numbers is: {average}")
