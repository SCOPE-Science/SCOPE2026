"""Exact finite arithmetic certificate for a unitary/exponential divisor-sum density bound.

Run with Python 3, standard library only. All acceptance comparisons use integers
or exact Fraction arithmetic; floating point is used only for display.
"""
from fractions import Fraction
from math import isqrt

PRIMES = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29)
CAPS = (16, 12, 6, 5, 4, 3, 3, 3, 2, 2)
EXPECTED_N = 22146947537280283084803283684585457657160649113600
EXPECTED_Q = 28535726520270636024768604478765044285962240000000
EXPECTED_VECTORS = 26732160


def divisor_sum_prime_power(p, a):
    if a == 0:
        return 1, 1
    numer = 1 + p ** a
    denom = sum(p ** d for d in range(1, a + 1) if a % d == 0)
    return numer, denom


def count():
    options = []
    q = 1
    for p, limit in zip(PRIMES, CAPS):
        q *= p ** (limit + 1)
        local = []
        for a in range(limit + 1):
            numer, denom = divisor_sum_prime_power(p, a)
            local.append((numer, denom, (p - 1) * p ** (limit - a)))
        options.append(local)

    state = [0, 0, 0]  # N (weakly acceptable), strict numerator, visited vectors

    def visit(index, numer, denom, weight):
        if index == len(options):
            state[2] += 1
            if numer >= denom:
                state[0] += weight
                if numer > denom:
                    state[1] += weight
            return
        for x, y, w in options[index]:
            visit(index + 1, numer * x, denom * y, weight * w)

    visit(0, 1, 1, 1)
    n, strict, vectors = state
    assert vectors == EXPECTED_VECTORS, (vectors, EXPECTED_VECTORS)
    assert n == EXPECTED_N, (n, EXPECTED_N)
    assert q == EXPECTED_Q, (q, EXPECTED_Q)
    assert strict < n
    assert 397 * n > 308 * q
    return n, q, vectors


def tail():
    # Direct trial division, independent of external prime tables.
    def prime(n):
        return n >= 2 and all(n % d for d in range(2, isqrt(n) + 1))

    ps = [p for p in range(31, 998) if prime(p)]
    assert len(ps) == 158
    s = sum((Fraction(1, p * p) for p in ps), Fraction(0))
    assert s + Fraction(1, 2985) < Fraction(3, 400)
    # Explicit 6j ± 1 integral majorant for all primes greater than 997.
    assert Fraction(1, 2985) == Fraction(2, 6 * (6 * 166 - 1))
    return len(ps), s


def main():
    n, q, vectors = count()
    primes, s = tail()
    print('VERIFY_OK', 'vectors=', vectors, 'prime_tail_check=', primes,
          'N=', n, 'Q=', q)
    print('certified_lower=', float(Fraction(397 * n, 400 * q)),
          'finite_prime_sum=', float(s),
          'strictly_greater_than_77_percent=PASS')


if __name__ == '__main__':
    main()
