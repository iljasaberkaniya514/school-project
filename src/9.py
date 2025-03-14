import random

def get_random_code():
    letters = "abcdefghijklmnopqrstuvwxyz"
    numbers = "1234567890"
    symbols = "!@#$%^&*"

    password = ""
    for i in range(random.randint(8, 16)):
        if i % 2 == 0:
            password += random.choice(letters)
        else:
            password += random.choice(numbers)

    return password