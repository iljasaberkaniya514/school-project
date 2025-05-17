def add_numbers(a: int, b: int) -> int:
    """
    Add two numbers.
    >>> add_numbers(10, 5)
    15
    """
    return a + b

def square_number(x: int) -> int:
    """
    Square the given number.
    >>> square_number(4)
    16
    """
    return x * x

def main():
    print("This is a simple school project.")
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = add_numbers(num1, num2)

    if isinstance(result, bool):
        print("The operation was unsuccessful. Please try again.")
    else:
        print(f"The sum of {num1} and {num2} is {result}.")
        
if __name__ == "__main__":
    main()
