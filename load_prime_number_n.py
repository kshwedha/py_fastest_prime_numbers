import functools
import time

def timeit(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(f"Time taken by {func.__name__}: {end - start}")
    return wrapper  

@timeit
def get_primes_upto(n):
    primes = []
    for num in range(2, n + 1):
        if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
            primes.append(num)
    return primes

@timeit
def get_primes_upto_via_prime_division(n):
    primes = []
    for num in range(2, n + 1):
        if all(num % primes[i] != 0 for i in range(len(primes)-1)):
            primes.append(num)
    return primes

def condition(pivotIndex, primes, num):
    if all(num % primes[i] != 0 for i in range(pivotIndex)):
        return True
    return False
        

def findPivot(pivotIndex, num, primes):
    if len(primes) == pivotIndex or primes[pivotIndex]**2 > num:
        return pivotIndex
    return pivotIndex+1

@timeit
def findPrimeByOptimisedPivot(n):
    primes = []
    pivotIndex = 0
    for i in range(2, n+1):
        pivotIndex = findPivot(pivotIndex, i, primes)
        if condition(pivotIndex, primes, i):
            primes.append(i)            
    return primes
        
n = 7000
findPrimeByOptimisedPivot(n)
get_primes_upto_via_prime_division(n)
get_primes_upto(n)

"""
Time taken by findPrimeByOptimisedPivot: 0.0031981468200683594
Time taken by get_primes_upto_via_prime_division: 0.017104148864746094
Time taken by get_primes_upto: 0.0032100677490234375
"""
