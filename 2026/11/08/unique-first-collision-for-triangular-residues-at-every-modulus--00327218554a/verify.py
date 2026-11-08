#!/usr/bin/env python3
"""Independent finite exact tests of a triangular-residue first-collision theorem."""
from math import isqrt


def predicted(m):
    assert m >= 1
    odd = m
    while odd % 2 == 0:
        odd //= 2
    divisors = []
    for d in range(1, isqrt(odd) + 1):
        if odd % d == 0:
            divisors.append(d)
            if d * d != odd:
                divisors.append(odd // d)
    opt = min(divisors, key=lambda d: d + 2 * m // d)
    opt_value = opt + 2 * m // opt
    assert sum(d + 2 * m // d == opt_value for d in divisors) == 1
    small, large = sorted((opt, 2 * m // opt))
    assert small % 2 != large % 2
    first = (small + large + 1) // 2
    before = (large - small + 1) // 2
    assert 1 <= before < first
    return first, before


def triangular(n):
    return n * (n - 1) // 2


def observed(m):
    seen = {}
    for n in range(1, 2 * m + 2):
        r = triangular(n) % m
        if r in seen:
            matching = [j for j in range(1, n) if triangular(j) % m == r]
            assert matching == [seen[r]], (m, n, matching)
            return n, seen[r]
        seen[r] = n
    raise AssertionError(('missing collision', m))


def main():
    for m in range(1, 10000):
        exp_n, exp_a = predicted(m)
        got_n, got_a = observed(m)
        assert (exp_n, exp_a) == (got_n, got_a), (m, exp_n, exp_a, got_n, got_a)
        assert triangular(got_n) - triangular(got_a) == m
    for exponent in range(0, 16):
        assert predicted(2**exponent)[0] == 2**exponent + 1
    for p in (3, 5, 7, 11, 13, 17):
        for r in range(0, 5):
            assert predicted(p**(2*r))[0] == (3*p**r + 1) // 2
            assert predicted(p**(2*r+1))[0] == ((p+2)*p**r+1)//2
    print('VERIFY_OK moduli=1..9999 uniqueness_and_exact_difference=PASS prime_powers=PASS')


if __name__ == '__main__':
    main()
