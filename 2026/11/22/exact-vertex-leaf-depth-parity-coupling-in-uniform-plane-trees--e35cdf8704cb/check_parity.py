#!/usr/bin/env python3
"""Exact finite checks for signed vertex and leaf depth in ordered rooted trees.

This is a finite consistency check; the generating-function proof covers all sizes.
Run: python3 check_parity.py
"""
from functools import lru_cache
from fractions import Fraction
from math import comb, sqrt

@lru_cache(None)
def trees(n):
    """All ordered rooted trees with n vertices; () denotes the one-vertex tree."""
    if n == 1:
        return ((),)
    def children(partial, left):
        if not left:
            yield partial
        else:
            for size in range(1, left + 1):
                for subtree in trees(size):
                    yield from children(partial + (subtree,), left - size)
    return tuple(children((), n - 1))

def two_signs(t):
    """Both signs are relative to the root of t."""
    if not t:
        return 1, 1
    children_vals = [two_signs(child) for child in t]
    return 1 - sum(x for x, _ in children_vals), -sum(y for _, y in children_vals)

def cat(k):
    return comb(2*k, k) // (k+1)

def predicted(n):
    assert n >= 3
    ex = Fraction(0)
    ey = -Fraction(n, 2*(2*n-3))
    ex2 = Fraction(n*(n-2),2*n-3)
    exy = Fraction(n,2)
    ey2 = (Fraction(5*n,8) + Fraction(n,8*(2*n-3))
           + Fraction(n*(n-1),4*(2*n-3)*(2*n-5)))
    return ex, ey, ex2, exy, ey2

def main():
    assertions = 0
    for n in range(3, 12):
        ts = trees(n)
        assert len(ts) == cat(n-1)
        assertions += 1
        vals = [two_signs(t) for t in ts]
        actual = tuple(Fraction(sum(fn(x,y) for x,y in vals),len(ts))
                       for fn in (lambda x,y:x, lambda x,y:y,
                                  lambda x,y:x*x, lambda x,y:x*y,
                                  lambda x,y:y*y))
        target = predicted(n)
        for a,b in zip(actual,target):
            assert a == b, (n, a, b)
            assertions += 1
        # Independent coefficient equalities for the two-variable generating series.
        c = cat(n-1)
        assert Fraction(comb(2*n-2,n-1),2*c) == target[3]
        assert (Fraction(5*comb(2*n,n),32) + Fraction(5*cat(n-1),16)
                + Fraction(cat(n-2),4) + cat(n-3)) / c == target[4]
        assertions += 2
    # Exact asymptotic leading coefficients and limiting correlation.
    for n in (100,1000,10000):
        ex,ey,ex2,exy,ey2=predicted(n)
        corr=float(exy)/sqrt(float(ex2*(ey2-ey*ey)))
        assert abs(corr-2/sqrt(5)) < 2/n
        assertions += 1
    print(f"PASS: {assertions} exact/envelope assertions; rooted ordered trees n=3..11; largest n=11.")

if __name__ == '__main__':
    main()
