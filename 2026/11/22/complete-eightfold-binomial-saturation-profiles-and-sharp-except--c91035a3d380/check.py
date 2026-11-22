"""Standalone finite checks for an eightfold binomial divisibility spectrum.
Python 3 standard library only. Finite checks are not infinite proofs.
Run: python3 check.py
"""
from math import comb, gcd


def weight(n):
    return n.bit_count()


def oddpart(n):
    assert n >= 1
    return n >> ((n & -n).bit_length() - 1)


def predicted(m):
    assert m >= 1
    o = oddpart(m)
    return 7 - 2 * (weight(3 * o) <= 2) - (weight(o) <= 2)


def explicit_odd(o):
    assert o >= 1 and o % 2 == 1
    if o in (1, 3):
        return 4
    if o > 3 and ((o - 1) & (o - 2)) == 0:
        return 6
    z = 3 * o - 1
    if z > 0 and (z & (z - 1)) == 0 and ((z.bit_length() - 1) % 2 == 1):
        return 5
    return 7


def direct(m):
    return sum(comb(8 * m, j * m) % 8 == 0 for j in range(1, 8))


def count_odd(X):
    if X < 1:
        return 0
    if X < 3:
        return 1
    a = (X - 1).bit_length() - 1
    b = (3 * X - 1).bit_length() - 1
    return a + (b + 1) // 2 - 1


def count_all(X):
    assert X >= 0
    c = 0
    while X:
        c += count_odd(X)
        X //= 2
    return c


def primes_below(N):
    sieve = bytearray(b'\x01') * (N + 1)
    sieve[:2] = b'\x00\x00'
    for p in range(2, int(N ** .5) + 1):
        if sieve[p]:
            sieve[p * p:N + 1:p] = b'\x00' * ((N - p * p) // p + 1)
    return [p for p in range(N + 1) if sieve[p]]


def run():
    n_direct = 0
    for m in range(1, 181):
        d = direct(m)
        assert d == predicted(m) == explicit_odd(oddpart(m)), (m, d, predicted(m))
        n_direct += 1
    n_prime = 0
    for p in primes_below(251):
        if p <= 8:
            continue
        n = 8 * p
        actual = sum(gcd(n, comb(n, j * p)) == 8 for j in range(1, 8))
        assert actual == predicted(p) == explicit_odd(p), (p, actual, predicted(p))
        n_prime += 1
    tests = [0, 1, 2, 3, 5, 7, 11, 17, 43, 257, 683, 1023, 10000, 100000, 1000000]
    for X in tests:
        observed = sum(predicted(m) < 7 for m in range(1, X + 1))
        assert observed == count_all(X), (X, observed, count_all(X))
        observed_odd = sum(predicted(m) < 7 for m in range(1, X + 1, 2))
        assert observed_odd == count_odd(X), (X, observed_odd, count_odd(X))
    for m in range(1, 100001):
        assert predicted(m) == explicit_odd(oddpart(m)), m
    print('PASS complete proportional rows (mod 8):', n_direct)
    print('PASS prime-index exact gcd cases:', n_prime)
    print('PASS odd and unrestricted cutoff counts:', len(tests), 'cutoffs through 1000000')
    print('PASS four-level explicit classification:', 100000, 'multipliers')


if __name__ == '__main__':
    run()
