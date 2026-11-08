#!/usr/bin/env python3
"""Exact rational consistency checks for a two-row Monge-polytope centroid formula.

Run: python3 verify_centroid.py.  Only the Python standard library is required.
Finite checks supplement, but do not replace, the analytic proof.
"""
from fractions import Fraction
from math import comb


def half_beta(a, b):
    """Integral_0^{1/2} u^(a-1) (1-u)^b du (integer a>=1,b>=0)."""
    assert a >= 1 and b >= 0
    return sum((Fraction((-1)**k * comb(b, k), a + k) * Fraction(1, 2**(a+k))
                for k in range(b + 1)), Fraction())


def r_direct(q, j):
    assert 1 <= j <= q
    return sum((comb(q, k) * half_beta(q-k, k) for k in range(j)), Fraction())


def r_recurrence(q):
    """Alternative from adjacent order-statistic gaps."""
    arr = [Fraction(1, q * (2**q))]
    for j in range(1, q):
        arr.append(arr[-1] + comb(q, j) * half_beta(q-j, j))
    return arr


def harmonic_endpoint(q):
    return sum((Fraction(1, r) - Fraction(1, r * 2**r) for r in range(1, q+1)), Fraction())


def verify():
    tests = 0
    for q in range(1, 37):
        direct = [r_direct(q, j) for j in range(1, q+1)]
        recur = r_recurrence(q)
        assert direct == recur; tests += q
        assert direct[0] == Fraction(1, q*2**q); tests += 1
        assert direct[-1] == harmonic_endpoint(q); tests += 1
        top = [(Fraction(1,2) + a)/(2*q) for a in direct]
        bottom = top[::-1]
        assert sum(top) == Fraction(1,2); tests += 1
        assert sum(bottom) == Fraction(1,2); tests += 1
        assert sum(top + bottom) == 1; tests += 1
        assert all(top[j] < top[j+1] for j in range(q-1)); tests += max(q-1,0)
        assert all(bottom[j] > bottom[j+1] for j in range(q-1)); tests += max(q-1,0)
        cols = [top[j]+bottom[j] for j in range(q)]
        assert cols == cols[::-1]; tests += q
        assert all(cols[j+2] - 2*cols[j+1] + cols[j] > 0 for j in range(q-2))
        tests += max(q-2,0)
        assert all(all(c >= 0 for c in pair) for pair in zip(top,bottom)); tests += q
        if q == 2:
            # Independent 2x2 Dirichlet/Beta calculation:
            # s=c11+c22 ~ Beta(2,2); conditioned on s<=1/2,
            # E[s]=5/16.  By symmetry E[c11]=E[c22]=5/32.
            assert top == [Fraction(5,32), Fraction(11,32)]; tests += 1
            assert bottom == [Fraction(11,32), Fraction(5,32)]; tests += 1
        if q == 3:
            assert top == [Fraction(13,144), Fraction(19,144), Fraction(5,18)]
            tests += 1
    print(f"PASS: {tests} exact rational assertions; q=1..36")

if __name__ == '__main__':
    verify()
