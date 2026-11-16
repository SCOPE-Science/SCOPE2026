#!/usr/bin/env python3
"""Reproducibility checks for fixed-three cyclic hard-core Fourier frames.

Only Python 3's standard library is used. Finite tests support the separate
all-dimensional proof; these checks do not establish an infinite theorem.
"""
from fractions import Fraction
from itertools import combinations
from math import cos, pi, isclose


def count(n):
    return n * (n - 4) * (n - 5) // 6


def independent_triples(n):
    return [a for a in combinations(range(n), 3)
            if all((a[(i + 1) % 3] - a[i]) % n > 1 for i in range(3))]


def covariance_row_formula(n):
    T = count(n)
    p = Fraction(3, n)
    return [p-p*p if r == 0 else
            -p*p if r in (1, n-1) else
            Fraction(n-5 if r in (2, n-2) else n-6, T)-p*p
            for r in range(n)]


def covariance_row_enum(n):
    sets = independent_triples(n)
    T = len(sets)
    means = Fraction(sum(0 in z for z in sets), T)
    return [Fraction(sum(0 in z and r in z for z in sets), T)-means*means
            for r in range(n)]


def eig_formula(n, k):
    t = 2*pi*k/n
    T = count(n)
    return 3/n - ((n-6)*(1+2*cos(t))-2*cos(2*t))/T


def eig_fourier(row, k):
    n = len(row)
    return sum(float(q)*cos(2*pi*k*j/n) for j, q in enumerate(row))


def sign(x):
    return (x > 0) - (x < 0)


def check_cubic_brackets():
    f7 = lambda t: 8*t*t*t+4*t*t-4*t-1
    f9 = lambda t: 8*t*t*t-6*t+1
    for poly, intervals in [(f7, [(Fraction(3,5),Fraction(2,3)),
                                    (Fraction(-1,4),Fraction(-1,5)),
                                    (Fraction(-1,1),Fraction(-4,5))]),
                            (f9, [(Fraction(3,4),Fraction(4,5)),
                                    (Fraction(1,6),Fraction(1,5)),
                                    (Fraction(-1,1),Fraction(-9,10))])]:
        assert len(intervals) == 3
        for a, b in intervals:
            assert sign(poly(a)) * sign(poly(b)) == -1
        assert len(set(intervals)) == 3
    print('EXACT_RATIONAL_CUBIC_BRACKETS_PASS n=7,9')


def main():
    assert len(independent_triples(6)) == 2
    assert covariance_row_enum(6) == [Fraction(1,4) * (-1)**j for j in range(6)]
    assert isclose(eig_fourier(covariance_row_enum(6),3), Fraction(3,2))
    for n in range(7, 27):
        assert len(independent_triples(n)) == count(n), n
        assert covariance_row_enum(n) == covariance_row_formula(n), n
        row = covariance_row_enum(n)
        assert sum(row) == 0, n
        for k in range(n):
            found = eig_fourier(row,k)
            predicted = 0 if k == 0 else eig_formula(n,k)
            assert isclose(found,predicted,rel_tol=1e-9,abs_tol=3e-12), (n,k,found,predicted)
    print('EXHAUSTIVE_TRIPLE_COUNTS_AND_EXACT_COVARIANCE_PASS n=7..26')
    check_cubic_brackets()
    for n in range(7,1001):
        eigs=[eig_formula(n,k) for k in range(1,n//2+1)]
        assert all(a>0 for a in eigs),(n,min(eigs))
        assert eigs[0] == min(eigs),n
        assert eigs[-1] == max(eigs),n
    print('NUMERICAL_MODE_ORDERING_PASS n=7..1000')
    for n in (1000,10000,100000):
        # For these large n, the first mode is minimal, the Nyquist mode maximal.
        rat=eig_formula(n,n//2)/eig_formula(n,1)
        assert abs((rat-1)*n-8)<0.5, (n,rat)
    print('ASYMPTOTIC_CONSTANT_SPOT_CHECK_PASS')
    print('THREE_HARD_CORE_FOURIER_FRAME_CHECKS_PASS')

if __name__ == '__main__': main()
