#!/usr/bin/env python3
"""Independent finite checks of a pseudo-Frobenius-type census."""
from fractions import Fraction
from math import comb


def n_allowed(r, j):
    if r % j == 0:
        return 0
    a0 = r % j
    n = r - 1
    count = 1
    for a in range(1, j):
        if a != a0:
            count *= 2 + (n - a) // j
    return count


def directly_test(m, r):
    F = m + r
    N = r - 1
    ways = [0] * (r - 1)
    tot_type = 0
    for mask in range(1 << N):
        B = set(j for j in range(1, r) if mask & (1 << (j - 1)))
        present = {0, m} | {m + b for b in B} | set(range(F + 1, F + m + 2))
        assert min(present - {0}) == m
        assert F not in present
        positive_below_F = sorted(v for v in present if 0 < v <= F)
        for a in positive_below_F:
            for b in positive_below_F:
                assert a+b > F or a+b in present
        pf = {j for j in range(1, F+1) if j not in present
              and all(j+s > F or j+s in present for s in positive_below_F)}
        predicted_high = {m+j for j in range(1,r+1) if j not in B}
        predicted_middle = set(range(r+1,m))
        predicted_low = {j for j in B if all(j+b>r or j+b in B for b in B)}
        assert pf == predicted_high | predicted_middle | predicted_low, (m,r,B,pf)
        assert len(pf) == m - 1 - len(B) + len(predicted_low)
        tot_type += len(pf)
        for j in predicted_low:
            ways[j-1] += 1
    assert ways == [n_allowed(r,j) for j in range(1,r)], (r,ways)
    predicted_mean = Fraction(2*m-2-N,2) + Fraction(sum(ways),2**N)
    assert Fraction(tot_type, 1<<N) == predicted_mean, (m,r)
    return 1 << N

if __name__ == '__main__':
    checked=0
    for r in range(1,13):
        for m in sorted({r+1,r+3,2*r+3}):
            checked += directly_test(m,r)
    print('VERIFY_OK', checked, 'semigroups; r=1..12, three m values')
