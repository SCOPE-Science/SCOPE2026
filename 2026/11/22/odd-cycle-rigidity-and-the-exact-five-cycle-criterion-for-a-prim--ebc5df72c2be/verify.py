"""Finite regression for arithmetic cycles of a prime-shift map.

This checks a theorem by two independent representations: the predicted
largest-factor/power-of-two test, and direct five-fold map iteration.
Finite checks are not substitutes for the infinite proof.
"""


def greatest_prime_factor_sieve(limit):
    lpf = [0] * (limit + 1)
    for prime in range(2, limit + 1):
        if lpf[prime] == 0:
            for multiple in range(prime, limit + 1, prime):
                lpf[multiple] = prime
    return lpf


def main():
    bound = 200001
    factors = greatest_prime_factor_sieve(2 * bound + 10)

    def isprime(x):
        return x >= 2 and factors[x] == x

    def step(x, k):
        if isprime(x):
            return x + k
        return factors[x]

    predicted = []
    observed = []
    count = 0
    for k in range(1, bound + 1, 2):
        q = factors[k + 1]
        condition = isprime(k + 2) and q > 2 and (k + q) & (k + q - 1) == 0
        if condition:
            predicted.append(k)
        orbit = [2]
        for _ in range(5):
            orbit.append(step(orbit[-1], k))
        actual = orbit[-1] == 2 and len(set(orbit[:5])) == 5
        if actual:
            observed.append(k)
            assert orbit == [2, 2 + k, 2 + 2*k, q, q+k, 2], (k, orbit)
        assert actual == condition, (k, condition, orbit)
        count += 1

    assert predicted == observed
    assert observed == [5, 21, 51, 59, 1365, 16271, 87381]
    print('odd shifts checked:', count)
    print('five-cycle parameters <= 200001:', observed)
    for k in observed:
        q = factors[k+1]
        print('k=',k,'q=',q,'states=',[2, k+2, 2*k+2, q, q+k])
    print('all direct-iteration and arithmetic-criterion comparisons passed')


if __name__ == '__main__':
    main()
