import random

def get_random_code():
    """
    Generates a random 8-digit code
    """
    return str(random.randint(10000000, 99999999)).zfill(8)