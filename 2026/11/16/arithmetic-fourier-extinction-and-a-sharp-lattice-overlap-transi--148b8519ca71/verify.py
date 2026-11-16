#!/usr/bin/env python3
"""Numerical and exact-arithmetic corroboration of the clipped-square Fourier/coverage identities.

The infinite-dimensional results require the analytical proof; these finite checks are not substitutes.
"""
from fractions import Fraction
from math import cos, sin, pi, gcd, isclose


def fourier(a, m, n):
    if m == n == 0:
        return 4 - 2*a*a
    if m*m != n*n:
        return (cos(2*pi*a*m) - cos(2*pi*a*n)) / (pi*pi*(m*m-n*n))
    return -a*sin(2*pi*a*m)/(pi*m)


def is_zero_arithmetic(m, n, q):
    if m == n == 0:
        return False
    if m*m != n*n:
        return (m-n) % q == 0 or (m+n) % q == 0
    return (2*m) % q == 0


def zero_count(M, q):
    nr = [sum(k % q == r for k in range(-M, M+1)) for r in range(q)]
    g = gcd(2, q)
    union = sum(c*c for c in nr)
    union += sum(nr[r] * nr[(-r)%q] for r in range(q))
    union -= sum(nr[r]**2 for r in range(q) if (2*r)%q == 0)
    return union - 1 - 4*(M - M//(q//g))


def coverage(a, x, y):
    lost = (x+y < a) + (x+y > 2-a) + (y-x > 1-a) + (x-y > 1-a)
    return 4 - lost


def coverage_law(a):
    z = max(a - .5, 0.)
    return (4*z*z, 2*a*a - 8*z*z, 1 - 2*a*a + 4*z*z)


def check():
    # Exact residue computations, including the exceptional diagonal case and origin.
    total = 0
    for q in range(2, 16):
        for M in range(0, 18):
            expected = zero_count(M, q)
            got = sum(is_zero_arithmetic(m, n, q)
                      for m in range(-M, M+1) for n in range(-M, M+1))
            assert expected == got, (q, M, expected, got)
            total += 1
    print('OCTAGON_EXACT_ZERO_COUNTS_PASS', 'cases='+str(total))

    # Compare the exact rational phase criterion to the derived Fourier coefficient.
    trials = 0
    for q in range(2, 16):
        for p in range(1, q):
            if gcd(p, q) != 1:
                continue
            a = p/q
            for m in range(-8, 9):
                for n in range(-8, 9):
                    expected = is_zero_arithmetic(m, n, q)
                    actual = abs(fourier(a, m, n)) < 1e-10
                    assert expected == actual, (p, q, m, n, fourier(a,m,n))
                    trials += 1
    print('OCTAGON_RATIONAL_FOURIER_ZEROS_PASS', 'frequency_tests='+str(trials))

    # A separately discretized triangular integral vs. the closed formula.
    for a in (0.27, 0.73):
        for m, n in ((0,1), (1,0), (1,1), (2,-2), (2,3), (3,-1)):
            count = 5000
            h = a/count
            acc = 0.0
            for j in range(count):
                u = (j+.5)*h
                inner = (a-u) if n == 0 else sin(2*pi*n*(a-u))/(2*pi*n)
                acc += cos(2*pi*m*u)*inner
            observed = -4*h*acc
            assert abs(observed - fourier(a,m,n)) < 2e-7, (a,m,n,observed,fourier(a,m,n))
    print('OCTAGON_TRIANGLE_INTEGRAL_PASS', 'cases=12')

    # Midpoint coverage area approximation is deliberately not an exact proof.
    steps = 500
    for a in (0.2, .5, .65, .9):
        counts = {2:0, 3:0, 4:0}
        for j in range(steps):
            x = (j+.5)/steps
            for k in range(steps):
                y = (k+.5)/steps
                counts[coverage(a,x,y)] += 1
        pred = coverage_law(a)
        for w in (2,3,4):
            observed = counts[w]/(steps*steps)
            assert abs(observed - pred[w-2]) < .003, (a,w,observed,pred)
    print('OCTAGON_COVERAGE_AREA_PASS', 'apertures=4')

    # Fourier Parseval sums converge to the exactly computed coverage variance.
    for a in (0.27, 0.73):
        target = 2*a*a - 4*a**4 + 8*max(a-.5,0)**2
        acc = 0.
        for m in range(-115, 116):
            for n in range(-115, 116):
                if m == n == 0:
                    continue
                acc += fourier(a,m,n)**2
        assert 0 <= target-acc < .008, (a,target,acc,target-acc)
    print('OCTAGON_PARSED_PARSEVAL_PASS', 'apertures=2, cutoff=115')

if __name__ == '__main__':
    check()
