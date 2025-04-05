import time
import math
import multiprocessing
import threading
import asyncio

# Efficient prime number generator using the Sieve of Eratosthenes
def sieve_of_eratosthenes(limit, previous_primes=[]):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not prime numbers
    for p in previous_primes:
        if p * p <= limit:  # Only mark multiples of known primes
            for j in range(p * p, limit + 1, p):
                sieve[j] = False
    for i in range(2, int(math.sqrt(limit)) + 1):
        if sieve[i]:
            for j in range(i * i, limit + 1, i):
                sieve[j] = False
    return [x for x in range(2, limit + 1) if sieve[x]], sieve

# Function to find the highest prime number within a time limit (no fixed upper bound)
def find_prime(limit_seconds=180):
    start_time = time.time()
    highest_prime = 0
    current_limit = 10000  # Initial sieve range limit
    previous_primes = []

    print("Starting to find the highest prime number...")
    
    while time.time() - start_time < limit_seconds:
        primes, previous_primes = sieve_of_eratosthenes(current_limit, previous_primes)
        if primes:
            highest_prime = primes[-1]
        current_limit *= 2  # Increase the range for next iteration
    
    return highest_prime

# Fibonacci function using iteration
def calc_fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# Factorial function using math.factorial
def calc_factorial(n):
    return math.factorial(n)

# Async function to calculate Fibonacci and Factorial
async def compute_fib_and_fact(prime):
    print("Async Fibonacci and Factorial calculation starting...")
    fib_future = asyncio.create_task(calc_fibonacci(prime))
    fact_future = asyncio.create_task(calc_factorial(prime))

    fibonacci_result = await fib_future
    factorial_result = await fact_future
    print("Async calculation completed.")

    return fibonacci_result, factorial_result

# Multiprocessing function to calculate Fibonacci and Factorial 
def calc_fib_and_fact_mp(prime):
    with multiprocessing.Pool(2) as pool:
        fib_result, fact_result = pool.starmap(calc_fibonacci, [(prime,), (prime,)])
    
    print(f"Multiprocessing - Fibonacci: {fib_result}, Factorial: {fact_result}")

# Threading function to calculate Fibonacci and Factorial in parallel
def calc_fib_and_fact_thread(prime):
    print("Threaded Fibonacci and Factorial calculation starting...")
    
    fib_result, fact_result = None, None
    
    def compute_fib():
        nonlocal fib_result
        fib_result = calc_fibonacci(prime)
    
    def compute_fact():
        nonlocal fact_result
        fact_result = calc_factorial(prime)

    fib_thread = threading.Thread(target=compute_fib)
    fact_thread = threading.Thread(target=compute_fact)

    fib_thread.start()
    fact_thread.start()
    
    fib_thread.join()
    fact_thread.join()

    print(f"Threading - Fibonacci: {fib_result}, Factorial: {fact_result}")
    print("Threads finished.")

# Main function
def main():
    start_time = time.time()

    # Step 1: Find the highest prime within the time limit (no fixed upper bound)
    highest_prime = find_prime(180)  # Find the highest prime within 3 minutes
    print(f"\n-------------------------------------\nHighest prime number found: {highest_prime}")

    # Step 2: Calculate Fibonacci and Factorial using Threading
    print("\nCalculating Fibonacci and Factorial using Threading...")
    threading_start_time = time.time()
    calc_fib_and_fact_thread(highest_prime)
    threading_end_time = time.time()
    print(f"Threaded execution time: {threading_end_time - threading_start_time:.2f} seconds")

    # Step 3: Calculate Fibonacci and Factorial using Multiprocessing
    print("\nCalculating Fibonacci and Factorial using Multiprocessing...")
    multiprocessing_start_time = time.time()
    calc_fib_and_fact_mp(highest_prime)
    multiprocessing_end_time = time.time()
    print(f"Multiprocessing execution time: {multiprocessing_end_time - multiprocessing_start_time:.2f} seconds")

    # Step 4: Calculate Fibonacci and Factorial using Asyncio
    print("\nCalculating Fibonacci and Factorial using Asyncio...")
    asyncio_start_time = time.time()
    fib_result, fact_result = asyncio.run(compute_fib_and_fact(highest_prime))
    asyncio_end_time = time.time()
    print(f"Async Fibonacci: {fib_result}, Async Factorial: {fact_result}")
    print(f"Asyncio execution time: {asyncio_end_time - asyncio_start_time:.2f} seconds")

    print(f"Total execution time: {time.time() - start_time:.2f} seconds")

if __name__ == "__main__":
    main()