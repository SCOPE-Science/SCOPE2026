"""Exact rational verification for the dyadic reset-return laws.

Run with: python3 checker.py
This finite audit checks independent algebraic identities; the manuscript's proof
establishes the claims for arbitrary countable reset distributions.
"""
from fractions import Fraction as F
from itertools import product


def tail(weights, j):
    return sum((p if b >= j else p * F(1, 2 ** (j-b)) for b, p in weights.items()), F(0))


def check(weights):
    assert all(isinstance(b, int) and b >= 1 and p > 0 for b, p in weights.items())
    assert sum(weights.values()) == 1
    B = max(weights)
    m = sum(b*p for b, p in weights.items()) + 2
    c = sum(p*2**b for b, p in weights.items())
    h = lambda j: (2 if j == 0 else 2**(j+1)*tail(weights, j))
    assert h(0) == h(1)/2
    for j in range(1, 48):
        right = sum((p * 2**b for b, p in weights.items() if b <= j), F(0))
        assert h(j) == h(j+1)/2 + right, (weights,j)
    # Every dyadic shell's tower mass is the return-time survival probability.
    shell_mass = lambda j: F(h(j), 2**(j+1))
    for j in range(1, 48):
        assert shell_mass(j) == tail(weights, j)
    # Sum the infinite geometric tail rather than truncate the mass.
    sum_shells = sum((tail(weights, j) for j in range(1, B)), F(0)) + c*F(1,2**(B-1))
    assert 1 + sum_shells == m
    # Return-time pgf coefficient f_n from beta+1+geometric leading zeros.
    first = [F(0)] * 45
    for b,p in weights.items():
        for n in range(b+1, len(first)):
            first[n] += p * F(1, 2**(n-b))
    assert all(first[n] == tail(weights, n-1)-tail(weights,n) for n in range(1, len(first)))
    # Renewal probabilities from convolution and algebraic identity U=1/(1-F).
    u = [F(1)] + [F(0)]*44
    for n in range(1, len(u)):
        u[n] = sum((first[t]*u[n-t] for t in range(1,n+1)), F(0))
    zpoly = [F(0)] * 45
    for b,p in weights.items():
        zpoly[b] += p
    # (2-z-zP(z))U(z)=(2-z)
    for n in range(45):
        lhs = 2*u[n] - (u[n-1] if n >= 1 else 0)
        for b,p in weights.items():
            if n>=b+1:
                lhs -= p*u[n-b-1]
        rhs = 2 if n==0 else (-1 if n==1 else 0)
        assert lhs == rhs, (weights,n,lhs,rhs)
    return len(u)


def check_pair_digits(g,h):
    # For the uniform initial y=2x-1 in (0,1), first gap g means
    # y in (2^{-g-1},2^{-g}]. Return x' = 2^g y.
    low = F(1, 2**(g+1)); high = F(1, 2**g)
    # Gap h at the next Y entrance means y'=2x'-1 lies in the h-th dyadic shell.
    yl = (1 + F(1,2**(h+1)))/2**(g+1)
    yh = (1 + F(1,2**h))/2**(g+1)
    overlap = max(F(0), min(yh,high)-max(yl,low))
    assert overlap == F(1,2**(g+h+2)), (g,h,overlap)


if __name__ == '__main__':
    cases = [
        {1:F(1)}, {2:F(1)}, {5:F(1)},
        {1:F(2,5),3:F(3,5)},
        {1:F(1,3),4:F(1,3),7:F(1,3)},
        {2:F(1,7),3:F(2,7),8:F(4,7)},
    ]
    for w in cases:
        check(w)
    for g,h in product(range(10),repeat=2):
        check_pair_digits(g,h)
    # Deterministic beta=1: exact all-lag correlation closed form.
    u=[F(1),F(0)]
    for n in range(2, 50):
        u.append((u[-1]+u[-2])/2)
    for n in range(50):
        assert u[n] == F(1,3)+F(2,3)*F(-1,2)**n
        assert F(1,3)*(u[n]-F(1,3)) == F(2,9)*F(-1,2)**n
    print('PASS: 6 exact-rational parameter laws, 282 transfer identities, 270 renewal identities,')
    print('      100 exact two-gap intersections, and 50 closed-form covariance checks.')
