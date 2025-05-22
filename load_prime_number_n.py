def get_primes_upto(n):
    primes = []
    for num in range(2, n + 1):
        if all(num % primes[i] != 0 for i in range(len(primes)-1)):
            primes.append(num)
    return primes
