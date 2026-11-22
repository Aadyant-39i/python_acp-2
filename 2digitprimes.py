def sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    crossings = 0
    p = 2
    while p * p <= n:
        if is_prime[p]:
            for multiple in range(p * p, n + 1, p):
                is_prime[multiple] = False
                crossings += 1
        p = p + 1

    primes = []
    for k in range(2, n + 1):
        if is_prime[k]:
            primes.append(k)

    return primes, crossings


all_primes, crossings = sieve(99)
codes = []

for prime in all_primes:
    if prime >= 10:
        codes.append(prime)

print("Team codes (two-digit primes):", codes)
print("How many codes:", len(codes))
if len(codes) > 0:
    print("Smallest:", codes[0], " Largest:", codes[-1])
print("Crossings made by the sieve up to 99:", crossings)
print("Time: O( for the sieve. Space: O(n) for the True/False list.")
