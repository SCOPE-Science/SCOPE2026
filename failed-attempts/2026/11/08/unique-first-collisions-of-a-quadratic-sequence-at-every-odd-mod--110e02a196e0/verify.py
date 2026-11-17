#!/usr/bin/env python3
"""Independent exact tests of a quadratic sequence's first collision."""
from math import isqrt

def divisors(n):
    small = [d for d in range(1, isqrt(n) + 1) if n % d == 0]
    return small + [n // d for d in small if d*d != n]

def exact_from_divisors(m):
    assert m >= 3 and m % 2 == 1
    terms = sorted((d + 2 * (m // d), d) for d in divisors(m))
    if len(terms) > 1:
        assert terms[0][0] != terms[1][0]
    s, d = terms[0]
    return (s + 1) // 2, (abs(d - 2*(m//d)) + 1)//2, d

def direct_first(m, horizon):
    earlier = {}
    for k in range(1, horizon + 1):
        val = (2*k*(k-1)) % m
        if val in earlier:
            # Test that exactly one earlier index has the same residue.
            partners = [j for j in range(1, k) if 2*j*(j-1) % m == val]
            assert partners == [earlier[val]]
            return k, earlier[val]
        earlier[val] = k
    raise AssertionError("No collision within test horizon")

def is_prime(p):
    return p >= 2 and all(p % d for d in range(2, isqrt(p)+1))

def main():
    tests = 0
    for m in range(3, 5002, 2):
        k, i, d = exact_from_divisors(m)
        assert direct_first(m, k) == (k, i), (m, k, i)
        assert (2*k*(k-1) - 2*i*(i-1)) % m == 0
        tests += 1
    prime_tests = 0
    for p in range(3, 98, 2):
        if not is_prime(p):
            continue
        for a in range(1, 8):
            m = p ** a
            if m > 10000000:
                continue
            k, i, d = exact_from_divisors(m)
            if a % 2 == 0:
                t = a//2
                assert (k, i, d) == ((3*p**t+1)//2, (p**t+1)//2, p**t)
            else:
                t = (a-1)//2
                assert (k, i, d) == (((p+2)*p**t+1)//2, ((p-2)*p**t+1)//2, p**(t+1))
            prime_tests += 1
    print(f"VERIFY_OK odd_moduli={tests} prime_powers={prime_tests} unique_first_partner=PASS")
if __name__ == "__main__":
    main()
