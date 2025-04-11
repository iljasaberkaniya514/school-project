import numpy as np

def calculate_mean(numbers):
    """
    Calculate the mean of a list of numbers.
    
    Args:
        numbers (list): A list of numbers.
    
    Returns:
        float: The mean of the numbers.
    """
    if len(numbers) == 0:
        return None
    
    mean = sum(numbers) / len(numbers)
    return mean

# Example usage
data_points = [1, 2, 3, 4, 5]
print("Mean:", calculate_mean(data_points))
