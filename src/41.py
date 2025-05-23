def calculate_average(numbers):
    """
    Calculate the average of a list of numbers.
    
    Parameters:
    - numbers: A list of numbers.
    
    Returns:
    - The average of the given numbers as an integer.
    """
    if not numbers:
        return 0
    else:
        total = sum(numbers)
        average = total / len(numbers)
        return int(average)

# Example usage
numbers_list = [10, 20, 30, 40, 50]
print("Average:", calculate_average(numbers_list))
