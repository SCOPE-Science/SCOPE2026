"""Exact bounded corroboration of the two-prime-support initial-divisor classification.

This verification is finite; the unrestricted theorem follows from the proof.
"""
from math import isqrt


def primes_below(bound):
    sieve = bytearray(b'\x01') * bound
    sieve[:2] = b'\x00\x00'
    for q in range(2, isqrt(bound - 1) + 1):
        if sieve[q]:
            sieve[q*q:bound:q] = b'\x00' * (((bound - 1 - q*q) // q) + 1)
    return [p for p in range(3, bound, 2) if sieve[p]]


def prefix_sums(a, p, b):
    n = (1 << a) * pow(p, b)
    divs = sorted((1 << i) * pow(p, j)
                  for j in range(b + 1) for i in range(a + 1))
    assert divs[-1] == n and len(divs) == len(set(divs))
    total = 0
    sums = {}
    hits = []
    for d in divs[:-1]:
        total += d
        sums[d] = total
        if total == n:
            hits.append(d)
    return n, hits, sums, divs


def claim_condition(a, p, b):
    return b == 1 and ((a == 3 and p == 3) or p == (1 << (a + 1)) - 1)


def test_grid():
    cases = 0
    equalities = 0
    for a in range(1, 21):
        for b in range(1, 11):
            for p in primes_below(181):
                n, hits, sums, divs = prefix_sums(a, p, b)
                expected = claim_condition(a, p, b)
                assert bool(hits) == expected, (a, p, b, hits, expected)
                assert len(hits) <= 1, (a, p, b, hits)
                cases += 1
                equalities += bool(hits)
    return cases, equalities


def test_straddles():
    cases = 0
    for a in range(1, 26):
        for b in range(1, 14):
            n, hits, sums, ds = prefix_sums(a, 3, b)
            if a == 1 and b >= 2:
                lo, hi = n // 3, n // 2
            elif b == 1 and a == 2:
                lo, hi = n // 3, n // 2
            elif b == 1 and a >= 4:
                lo, hi = n // 4, n // 3
            elif b >= 2 and a in (2, 3):
                lo, hi = n // 4, n // 3
            elif b == 2 and a == 4:
                lo, hi = n // 4, n // 3
            elif b >= 2 and a >= 4:
                lo, hi = n // 6, n // 4
            else:
                assert claim_condition(a, 3, b)
                continue
            assert lo in sums and hi in sums
            assert ds.index(hi) == ds.index(lo) + 1, (a, b, lo, hi)
            assert sums[lo] < n < sums[hi], (a, b, n, lo, hi, sums[lo], sums[hi])
            cases += 1
    return cases


def test_closed_form():
    count = 0
    for a in range(2, 30):
        A = 1 << a
        for b in range(2, 14):
            B = pow(3, b - 1)
            n, hits, sums, ds = prefix_sums(a, 3, b)
            assert sums[n // 4] == ((7*A-9)*B-2*A+1)//2
            assert sums[n // 3] == ((9*A-9)*B-2*A+1)//2
            if a >= 3:
                assert 4*sums[n // 6] == (11*A-18)*B-4*A+2
            count += 1
    return count


def main():
    cases, hits = test_grid()
    switches = test_straddles()
    formulas = test_closed_form()
    print('VERIFY_OK')
    print('full_prefix_cases=', cases)
    print('positive_prefix_instances=', hits)
    print('three_adic_straddles=', switches)
    print('three_adic_formula_tests=', formulas)
    print('exact_integer_arithmetic=True')


if __name__ == '__main__':
    main()
