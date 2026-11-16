#!/usr/bin/env python3
"""Finite reproducibility tests for Euclidean-distance bidisk kernel polynomials.

The all-integer theorem requires the analytic argument in RESULT.md.
No external packages or network access are required.
"""
from fractions import Fraction
from math import factorial, comb, isclose


def rise(a, k):
    q = 1
    for i in range(k):
        q *= a + i
    return q


def poly_step(a, m):
    b = [Fraction(0)] * (len(a) + 1)
    for j, v in enumerate(a):
        b[j] += Fraction(2*j + m + 5, m+1) * v
        b[j+1] += Fraction(m+3-2*j, m+1) * v
    while b[-1] == 0:
        b.pop()
    return b


def coeff_rational(a, m, N):
    # coefficient of P_m(x)/(1-x)^(m+4)
    return sum((v*comb(N-j+m+3,m+3) for j,v in enumerate(a)
                if N >= j), Fraction(0))


def val(a, x):
    out = 0.0
    for c in reversed(a):
        out = out*x + float(c)
    return out


def bisect(a):
    # Locate the rightmost negative root first; P_m(-1) may have either sign.
    hi = 0.0
    assert val(a,hi) > 0
    for k in range(1,1001):
        lo = -k/1000
        if val(a,lo) < 0:
            break
    else:
        raise AssertionError('No sign-changing root found in (-1,0)')
    for _ in range(65):
        mid = (lo+hi)/2
        if val(a,mid) < 0:
            lo = mid
        else:
            hi = mid
    return (lo+hi)/2


checks = 0
a = [Fraction(1)]
rightmost = None
for m in range(15):
    d = len(a)-1
    assert d == (0 if m == 0 else 1 if m == 1 else (m+3)//2)
    checks += 1
    assert all(c > 0 for c in a)
    checks += 1
    for N in range(31):
        expected = Fraction(comb(N+3,3)*rise(2*N+5,m),factorial(m))
        assert coeff_rational(a,m,N) == expected, (m,N)
        checks += 1
    if m==1:
        assert a == [Fraction(5), Fraction(3)]
        checks += 1
    if m==2:
        assert a == [Fraction(15),Fraction(22),Fraction(3)]
        checks += 1
    if m >= 2:
        r = bisect(a)
        assert -1 < r < 0
        if rightmost is not None:
            assert r > rightmost, (m, r, rightmost)
        rightmost = r
        checks += 2
    a = poly_step(a,m)

# Independent check of K_1(u,v) numerator against the two-index moment series.
# (1-u)^-3(1-v)^-3 coefficient is C(j+2,2) C(k+2,2).
def base(j,k):
    return (comb(j+2,2) * comb(k+2,2)) if j>=0 and k>=0 else 0
for j in range(30):
    for k in range(30):
        coef = 5*base(j,k)-base(j-1,k)-base(j,k-1)-3*base(j-1,k-1)
        assert coef == (j+1)*(k+1)*(2*j+2*k+5), (j,k)
        checks += 1

print('PASS:',checks,'finite exact/numeric checks; analytic proof needed for all m')
