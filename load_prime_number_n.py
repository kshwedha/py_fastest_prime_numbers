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

def condition(primes, num):
    if all(num % i != 0 for i in primes):
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
        if condition(primes[:pivotIndex+1], i):
            primes.append(i)            
    return primes

@timeit
def fastestPrimeFinder(n):
    primes = []
    for i in range(2, n+1):
        sqrtCeil = int(i**0.5)+1
        for j in primes:
            if j >= sqrtCeil:
                break
            if i % j == 0:
                break
        else:
            primes.append(i)
    return primes
        

n = 7000
a = findPrimeByOptimisedPivot(n)
b = get_primes_upto_via_prime_division(n)
c = get_primes_upto(n)
d = fastestPrimeFinder(n)
print(a == b == c == d)

"""
python3 main.py
Time taken by findPrimeByOptimisedPivot: 0.002351045608520508
Time taken by get_primes_upto_via_prime_division: 0.01871013641357422
Time taken by get_primes_upto: 0.003467082977294922
Time taken by fastestPrimeFinder: 0.00115203857421875
True
python3 main.py
Time taken by findPrimeByOptimisedPivot: 0.0033140182495117188
Time taken by get_primes_upto_via_prime_division: 0.017297029495239258
Time taken by get_primes_upto: 0.0031731128692626953
Time taken by fastestPrimeFinder: 0.0010852813720703125
"""
