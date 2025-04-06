import numpy as np

def calculate_mean(data):
    """
    Calculate the mean of a dataset.
    
    Parameters:
    data (list or numpy.ndarray): The input list or numpy array containing numerical values.
    
    Returns:
    float: The mean value of the input dataset.
    """
    if isinstance(data, (list, np.array)):
        return np.mean(data)
    else:
        raise ValueError("Input must be a list or numpy array.")

# Example usage
if __name__ == "__main__":
    data = [10, 20, 30, 40, 50]
    print(f"The mean of the dataset is: {calculate_mean(data)}")
