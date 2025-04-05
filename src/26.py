def calculate_average(numbers):
    if not numbers:
        return None
    else:
        return sum(numbers) / len(numbers)

print(calculate_average([10, 20, 30]))  # Output: 20.0
