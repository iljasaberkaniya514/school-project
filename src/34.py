def print_square(size):
    """
    This function prints a square of given size.
    """
    for _ in range(size):
        print('*' * (size - 1) + '*' + '*')

print_square(5)
