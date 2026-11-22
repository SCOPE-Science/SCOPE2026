"""Exact rational diagnostics for modal structure of a generalized Poisson--Lindley count law.

Run: python VERIFY.py
The infinite assertions are proved analytically in RESULT.md; finite checks are not a proof.
"""
from fractions import Fraction as F
from random import Random


def ratio(j, a, t):
    b = a * (t + 2)
    return (j + a) * (j + b + 1) / ((t + 1) * (j + 1) * (j + b))


def increment_polynomial(j, a, t):
    return (-t * j * j
            + (a - t * (a * (t + 2) + 1)) * j
            + a * (a * (t + 2) - t*t - 3*t - 1))


def curvature_polynomial(j, a, t):
    b = a * (t + 2)
    return (j*j + (2*b - 2*t - 1)*j
            + b*b - a*t*(t+2) - 2*(t+1))


def cubic(t):
    return 9*t**3 + 36*t*t + 40*t - 7


def check():
    tests = 0
    rng = Random(20231118)
    for _ in range(200):
        a = F(rng.randint(1, 40), rng.randint(1, 25))
        t = F(rng.randint(1, 40), rng.randint(1, 25))
        b = a*(t+2)
        for j in range(15):
            n = (j+a)*(j+b+1) - (t+1)*(j+1)*(j+b)
            assert n == increment_polynomial(j, a, t)
            tests += 1
            assert ratio(j,a,t)-1 == n/((t+1)*(j+1)*(j+b))
            tests += 1
            lhs = ratio(j+1,a,t)-ratio(j,a,t)
            den = (t+1)*(j+1)*(j+2)*(j+b)*(j+b+1)
            assert lhs*den == -a*curvature_polynomial(j,a,t)
            tests += 1

    low, high = F(153,1000), F(154,1000)
    assert cubic(low) < 0 < cubic(high)
    tests += 1
    a=F(2,3)
    for t in (low, high):
        assert ratio(0,a,t) < 1 < ratio(1,a,t)
        assert ratio(2,a,t) < 1
        tests += 3
        assert ratio(0,a,t)*ratio(1,a,t)-1 == -cubic(t)/(9*(t+1)**2*(t+2))
        tests += 1
    # Exact certificate: each quadratic controlling the ratios is monotone
    # on t>0. For t in [low,high], the endpoint inequalities fix all signs.
    assert 3*low**2+7*low-1 > 0
    assert 3*high**2+11*high-2 < 0
    assert 9*low**2+46*low-7 > 0
    tests += 3

    # Independent finite shape checks across parameters.
    for _ in range(400):
        a = F(rng.randint(1,40),rng.randint(1,30))
        t = F(rng.randint(1,50),rng.randint(1,50))
        for j in range(12):
            assert (ratio(j+1,a,t)-ratio(j,a,t) > 0) == (curvature_polynomial(j,a,t) < 0)
            tests += 1
        # Global log-concavity criterion, checked on a finite grid only;
        # the rigorous all-index proof is in RESULT.md.
        h0=curvature_polynomial(0,a,t)
        if h0>=0:
            assert all(curvature_polynomial(j,a,t)>=0 for j in range(100))
            tests+=1
        else:
            assert h0<0 and curvature_polynomial(10000,a,t)>0
            tests+=1
    print(f"PASS: {tests} exact rational assertions")

if __name__ == '__main__':
    check()
