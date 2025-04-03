import time
import math
import multiprocessing
import threading
import asyncio

# Prime number function
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Find the highest prime nnumber in 3 minutes
def find_prime(limit_sec = 180):
    start_time = time.time()
    current_number = 0
    highest_prime = 0

    while time.time() - start_time < limit_sec:
        if is_prime(current_number):
            highest_prime = current_number
        current_number += 1

    return highest_prime

# Fibonacci function using iteration
def calc_fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for _ in range(n, n + 1):
        a, b = b, a + b
    return b

# Factorial function using math.factorial
def calc_factorial(n):
    return math.factorial(n)

# Async function to calculate Fibonacci and Factorial