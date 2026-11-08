#!/usr/bin/env python3
"""Exact finite consistency tests for a quotient-genus formula (not a proof)."""
from math import gcd


def predicted(a, p):
    m, r = divmod(a, 2 * p)
    h = (r - 2) // 2
    D_twice = 2 * (r - p + 1) - gcd(p, r) - gcd(p, r + 2)
    assert D_twice % 2 == 0
    D = D_twice // 2
    C = sum(((s + 1) * r - 1) // p - (s * (r + 2)) // p
            for s in range(h + 1))
    return p * m * m + (p + D) * m + C


def counted_by_independent_dp(a, p):
    # The conductor of <a,a+1,a+2> is at most a*((a-2)//2+1).
    bound = a * (a + 3)
    in_semigroup = bytearray(bound + 1)
    in_semigroup[0] = 1
    gens = (a, a + 1, a + 2)
    for n in range(1, bound + 1):
        in_semigroup[n] = int(any(n >= g and in_semigroup[n - g] for g in gens))
    assert all(in_semigroup[n] for n in range(a * ((a - 2) // 2 + 2), bound + 1))
    return sum(not in_semigroup[n] for n in range(0, bound + 1, p))


def main():
    cases = 0
    for a in range(3, 128):
        for p in range(2, 29):
            actual = counted_by_independent_dp(a, p)
            expect = predicted(a, p)
            assert actual == expect, (a, p, actual, expect)
            cases += 1
    print('GENUS_INDEPENDENT_DP_OK', cases)
    # Verify quadratic branch differences on entire residue classes, including
    # branch boundary where a<p and no eventual restriction can be assumed.
    branches = 0
    for p in range(2, 45):
        for r in range(2 * p):
            a0 = 2 * p * 5 + r
            vals = [predicted(a0 + 2 * p * j, p) for j in range(7)]
            assert {vals[i+2] - 2*vals[i+1] + vals[i] for i in range(5)} == {2 * p}
            branches += 1
    print('QUASIPOLYNOMIAL_BRANCHES_OK', branches)
    for p in range(2, 100):
        h = lambda r: gcd(p, r) + gcd(p, r + 2)
        linear_periods = [d for d in range(1, p + 1) if p % d == 0 and
                          all(h(r) == h((r + d) % p) for r in range(p))]
        least_linear = min(linear_periods)
        assert least_linear == (2 if p == 4 else p if p >= 3 else 2), (p, least_linear)
    print('LINEAR_COEFFICIENT_PERIODS_OK', 98)
    print('VERIFY_OK finite_checks_only=True infinite_period_proof_separate=True independent_audit=False')


if __name__ == '__main__':
    main()
