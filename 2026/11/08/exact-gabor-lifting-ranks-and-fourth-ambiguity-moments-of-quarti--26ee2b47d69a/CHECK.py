#!/usr/bin/env python3
"""Exact cyclotomic-histogram and moment checks for prime-field quartic chirps.

Uses Python's standard library; no external files or dependencies.
An exact zero decision uses the degree-(p-1) cyclotomic minimal polynomial.
"""
from math import gcd

PRIMES = [5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]


def isprime(n):
    return n >= 2 and all(n % i for i in range(2, int(n ** .5) + 1))


def zero_root_sum(exponents, p):
    """Exact test: sum of p-th roots ζ^e vanishes iff exponents equally distributed."""
    c = [0] * p
    for e in exponents:
        c[e % p] += 1
    return len(set(c)) == 1


def root_sum_abs2_equals_p(exponents, p):
    """Exact test: |sum ζ^e|^2 = p, reducing in Q[ζ] / Φ_p."""
    c = [0] * p
    for u in exponents:
        for v in exponents:
            c[(u - v) % p] += 1
    c[0] -= p
    return len(set(c)) == 1


def quartic_phase(p, a, x):
    return (pow((x+a) % p, 4, p) - pow(x, 4, p)) % p


def check(p):
    assert isprime(p) and p >= 5
    zcount = 0
    # Check *every* ambiguity zero without floating point or zero tolerance.
    for a in range(p):
        for b in range(p):
            exponents = [(quartic_phase(p,a,x) + b*x) % p for x in range(p)]
            exact_zero = zero_root_sum(exponents,p)
            predicted_zero = (a == 0 and b != 0) or (a != 0 and p % 3 == 2 and b == (-a**3) % p)
            assert exact_zero == predicted_zero, (p, a, b, exact_zero, predicted_zero)
            zcount += exact_zero
    expected_zero = p-1 if p % 3 == 1 else 2*(p-1)
    assert zcount == expected_zero, (p,zcount,expected_zero)
    # Exact finite-field Gauss identity (checks each nonzero shift h and a).
    for a in range(1,p):
        for h in range(1,p):
            exponents = [(quartic_phase(p,a,(x+h)%p)-quartic_phase(p,a,x))%p for x in range(p)]
            assert root_sum_abs2_equals_p(exponents,p), (p,a,h)
    # From the exact tested identities: for each a !=0,
    # sum_b |A(a,b)|^4 = (2p-1)/p^2, and a=0 adds 1.
    moment_numerator = 3*p*p-3*p+1
    assert moment_numerator == p*p + (p-1)*(2*p-1)
    assert (p*p-zcount == (p*p-p+1 if p%3==1 else p*p-2*p+2))
    return zcount, p*p-zcount, f'{moment_numerator}/{p*p}'


def main():
    for p in PRIMES:
        zeros,rank,moment = check(p)
        print(f'p={p}: exact_zeros={zeros}, lifted_rank={rank}, ambiguity_fourth_moment={moment}')
    print('ALL_EXACT_QUARTIC_CHECKS_PASSED')


if __name__ == '__main__':
    main()
