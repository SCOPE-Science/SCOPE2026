#!/usr/bin/env python3
"""Independent finite checks for the squareful three-prime divisor-sum classification.

This executable tests the finite cases and examples, not the unbounded prime sieve.
The latter is proved algebraically in RESULT.md.
"""
from math import isqrt


def direct_divisors(n):
    result = []
    for d in range(1, isqrt(n) + 1):
        if n % d == 0:
            result.append(d)
            if d*d != n:
                result.append(n//d)
    return sorted(result)


def product_divisors(p, q):
    n = 2*p*p*q
    result = sorted({(2**a)*(p**b)*(q**c)
                     for a in range(2) for b in range(3) for c in range(2)})
    assert len(result) == 12
    assert result[-1] == n
    return result


def is_prime(n):
    if n < 2:
        return False
    return all(n % d for d in range(2, isqrt(n) + 1))


def pairs_for(n, divs):
    proper = divs[:-1]
    delta = sum(divs) - 2*n
    return sorted((a, b) for i,a in enumerate(proper)
                  for b in proper[i+1:] if a+b == delta)


def main():
    expected = {
        (3,5):(90,54,[(9,45)]),
        (3,7):(126,60,[(18,42)]),
        (3,11):(198,72,[(6,66)]),
        (3,13):(234,78,[]),
        (5,7):(350,44,[]),
        (5,11):(550,16,[(5,11)]),
        (5,13):(650,2,[]),
    }
    for (p,q),(n,delta,witnesses) in expected.items():
        assert is_prime(p) and is_prime(q) and p<q
        d = direct_divisors(n)
        assert d == product_divisors(p,q)
        assert 3*(p*p+p+1)*(q+1) - 4*p*p*q == delta
        assert sum(d)-2*n == delta
        assert pairs_for(n,d) == witnesses
    observed = []
    tested = 0
    primes = [p for p in range(3,500) if is_prime(p)]
    for i,p in enumerate(primes):
        for q in primes[i+1:]:
            n=2*p*p*q
            d=product_divisors(p,q)
            # A second algorithm, independent of the product formula.
            assert direct_divisors(n)==d
            if pairs_for(n,d):
                observed.append((p,q))
            tested += 1
    assert observed == [(3,5),(3,7),(3,11),(5,11)],observed
    for p in primes:
        if p >= 7:
            f = -p**3+4*p*p+12*p+9
            assert f<0
    assert 1+2 == 3
    print('VERIFY_OK finite_prime_pairs=',tested,'admissible_pairs=',len(observed),'small_cases=',len(expected))


if __name__ == '__main__':
    main()
