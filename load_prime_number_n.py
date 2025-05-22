import functools
import time

def timeit(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Time taken by {func.__name__}: {end - start}")
        return result
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
            if j > sqrtCeil:
                primes.append(i)
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
Time taken by findPrimeByOptimisedPivot: 0.0032072067260742188
Time taken by get_primes_upto_via_prime_division: 0.016224145889282227
Time taken by get_primes_upto: 0.003081083297729492
Time taken by fastestPrimeFinder: 0.0016629695892333984
True
python3 main.py
Time taken by findPrimeByOptimisedPivot: 0.0034978389739990234
Time taken by get_primes_upto_via_prime_division: 0.017655134201049805
Time taken by get_primes_upto: 0.0032188892364501953
Time taken by fastestPrimeFinder: 0.0018360614776611328
True
python3 main.py
Time taken by findPrimeByOptimisedPivot: 0.003381967544555664
Time taken by get_primes_upto_via_prime_division: 0.01706695556640625
Time taken by get_primes_upto: 0.003200054168701172
Time taken by fastestPrimeFinder: 0.002048969268798828
True
python3 main.py
Time taken by findPrimeByOptimisedPivot: 0.003593921661376953
Time taken by get_primes_upto_via_prime_division: 0.017368078231811523
Time taken by get_primes_upto: 0.003204822540283203
Time taken by fastestPrimeFinder: 0.0017490386962890625
True
"""
