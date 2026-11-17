#!/usr/bin/env python3
"""Exact integer cut enumeration for half-lazy path averaging.

Every nontrivial subset is represented by a distinct integer bit mask;
all pairwise differences are formed after multiplying the output by four.
The unrestricted proof is in RESULT.md; this program proves small cases
exhaustively and independently checks larger instances.
"""
from fractions import Fraction
from math import floor

def one_step_times_four(bits):
    n = len(bits)
    out = [0] * n
    out[0] = 2 * (bits[0] + bits[1])
    out[-1] = 2 * (bits[-2] + bits[-1])
    for j in range(1, n-1):
        out[j] = bits[j - 1] + 2 * bits[j] + bits[j + 1]
    return out

def coefficient(n):
    if n == 2:
        return Fraction(0)
    if n == 3:
        return Fraction(1, 2)
    if n <= 8:
        return Fraction(1) - Fraction(1, 2 * floor(n*n/4))
    return Fraction(1) + Fraction(n - 9, 4*(n-1))

def gini_scaled_output(bits):
    y = one_step_times_four(bits)
    return sum(abs(y[i]-y[j]) for i in range(len(y)) for j in range(i+1,len(y)))

def test_all_cuts(n):
    target = coefficient(n)
    count = 0
    hits = []
    for mask in range(1, (1<<n)-1):
        x = [(mask >> j) & 1 for j in range(n)]
        k = sum(x)
        num = gini_scaled_output(x)
        den = 4*k*(n-k)
        assert Fraction(num, den) <= target, (n, mask, Fraction(num, den), target)
        if Fraction(num, den) == target and len(hits) < 5:
            hits.append(''.join(map(str,x)))
        count += 1
    assert hits, n
    return count, hits

if __name__ == '__main__':
    total = 0
    for n in range(2, 17):
        count, hits = test_all_cuts(n)
        total += count
        print('EXHAUSTIVE',n,str(coefficient(n)),count,','.join(hits))
    assert total == sum((1<<n)-2 for n in range(2,17))
    print('EXHAUSTIVE_ALL_NONTRIVIAL_CUTS_N2_TO_N16_PASSED',total)
    for n in range(9, 401):
        x = [0]*n
        x[1] = 1
        assert Fraction(gini_scaled_output(x), 4*(n-1)) == coefficient(n),n
    print('EXACT_SECOND_VERTEX_WITNESSES_N9_TO_N400_PASSED')
    print('ALL_HALF_LAZY_PATH_GINI_CHECKS_PASSED')
