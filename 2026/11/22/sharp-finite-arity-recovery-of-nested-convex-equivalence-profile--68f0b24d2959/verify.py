#!/usr/bin/env python3
"""Finite checks of labelled extension profiles for nested convex equivalences.

Uses an exhaustive cut-depth word model independent of the factorized
exponential generating function; all counts are exact integers.
"""
from itertools import product, permutations, combinations
from fractions import Fraction
from math import comb, factorial


def m_counts(depth, h):
    return [1 + sum(d >= level for d in depth) for level in range(1, h + 1)]


def direct(n, h, old_depth, r):
    total = 0
    universe = set(range(n+r))
    for old_positions in combinations(range(n+r), n):
        old_positions = list(old_positions)
        # The new points are labelled and their internal order is arbitrary.
        arrangement_count = factorial(r)
        for gap_depth in product(range(h+1), repeat=n+r-1):
            projected = tuple(max(gap_depth[old_positions[i]:old_positions[i+1]])
                              for i in range(n-1))
            if projected == old_depth:
                total += arrangement_count
    return total


def multiply(a, b, R):
    c = [Fraction(0)] * (R+1)
    for i, x in enumerate(a):
        for j, y in enumerate(b[:R+1-i]):
            c[i+j] += x*y
    return c


def linear_power(c, k, R):
    # Series expansion of (1-c*z)^k for any integer exponent k.
    out = [Fraction(1)]
    cur = Fraction(1)
    for r in range(1, R+1):
        cur *= Fraction(k-r+1, r)*(-c)
        out.append(cur)
    return out


def predicted(n, h, old_depth, r):
    m = m_counts(old_depth, h)
    terms = [(1, -n-m[0])]
    terms += [(j-1, m[j-2]+m[j-1]) for j in range(2,h+1)]
    terms += [(j, -m[j-2]-m[j-1]) for j in range(2,h+1)]
    terms += [(h,m[-1]+1), (h+1,-m[-1]-1)]
    coefs = [Fraction(1)] + [Fraction(0)]*r
    for a,k in terms:
        coefs=multiply(coefs,linear_power(a,k,r),r)
    assert coefs[r].denominator == 1
    return factorial(r)*coefs[r].numerator


def determinant(mat):
    a = [[Fraction(v) for v in row] for row in mat]
    n = len(a)
    sign = 1
    det = Fraction(1)
    for i in range(n):
        pivot = next((j for j in range(i,n) if a[j][i]),None)
        if pivot is None: return 0
        if pivot != i:
            a[i],a[pivot]=a[pivot],a[i]
            sign=-sign
        p=a[i][i]
        det*=p
        for j in range(i+1,n):
            q=a[j][i]/p
            for k in range(i+1,n): a[j][k]-=q*a[i][k]
            a[j][i]=0
    assert det.denominator==1
    return sign*int(det)


def main():
    checks=0
    for h in (1,2,3):
        for n in range(1,5):
            for old_depth in product(range(h+1),repeat=n-1):
                for r in range(0,3):
                    if n+r>6: continue
                    d=direct(n,h,old_depth,r)
                    p=predicted(n,h,old_depth,r)
                    assert d==p, (n,h,old_depth,r,d,p)
                    checks+=1
    # Six tuple types for an example of nonisomorphic bases, direct check.
    for r in range(4):
        assert predicted(3,2,(1,0),r)==predicted(3,2,(0,1),r)
    # Enumerate every finite old-base hierarchy and independently compare
    # the predicted number of nonisomorphic bases with each count vector.
    fiber_cases = 0
    for h in range(1, 5):
        for n in range(1, 7):
            fibers = {}
            for old_depth in product(range(h+1), repeat=n-1):
                key = tuple(m_counts(old_depth, h))
                fibers[key] = fibers.get(key, 0) + 1
            for key, count in fibers.items():
                expected = 1
                previous = n
                for m in key:
                    expected *= comb(previous-1, m-1)
                    previous = m
                assert count == expected, (h,n,key,count,expected)
                fiber_cases += 1
    for h in range(1,9):
        mat=[[(j+1)**r-(j-1)**r for j in range(1,h+1)] for r in range(1,h+1)]
        expected=2**h
        for r in range(1,h+1): expected*=factorial(r)
        assert determinant(mat)==expected
    print('FINITE_EXHAUSTIVE_CHECKS_OK',checks)
    print('MOMENT_DETERMINANTS_OK',8)
    print('FINITE_PROFILE_FIBERS_OK',fiber_cases)
    print('FIRST_COLLISION_EXAMPLE_OK')
    print('n=3,h=2,old_depth=(1,0) counts r=0..4:',
          [predicted(3,2,(1,0),r) for r in range(5)])
    print('h=2,n=3,old_depth=(1,0), m=',m_counts((1,0),2))

if __name__=='__main__':
    main()
