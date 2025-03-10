import random

def get_random_number(max_value):
    return random.randint(0, max_value)

def generate_password():
    length = 8
    password = ''
    for i in range(length):
        password += chr(get_random_number(25) + ord('a'))
    return password
