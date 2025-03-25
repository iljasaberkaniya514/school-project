def calculate_average(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return average

if __name__ == "__main__":
    numbers = [10, 20, 30, 40]
    print(calculate_average(numbers))
