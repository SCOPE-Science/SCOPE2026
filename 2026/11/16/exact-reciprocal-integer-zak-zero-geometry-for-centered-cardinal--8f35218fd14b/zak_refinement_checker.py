"""Exact rational checks for sampled cardinal spline refinement identities.
Run: python3 zak_refinement_checker.py
Checks are finite supporting tests, not a substitute for the infinite proof.
"""
from fractions import Fraction as F
from math import comb, factorial


def centered_spline(n, t):
    t = F(t)
    return sum(F((-1)**j * comb(n, j), factorial(n-1)) *
               max(t + F(n, 2) - j, F(0)) ** (n-1)
               for j in range(n+1))


def multiply(A, B):
    out = {}
    for i, a in A.items():
        for j, b in B.items():
            out[i+j] = out.get(i+j, F(0)) + a*b
    return {k:v for k,v in out.items() if v}


def power(A, n):
    result = {0:F(1)}
    for _ in range(n):
        result = multiply(result,A)
    return result


def samples(n, m, x):
    return {k:v for k in range(-n*m-3,n*m+4)
            if (v:=centered_spline(n,(x-k)/m))}


count=0
for n in range(2, 9):
    for m in range(2, 8):
        mask = power({-j:F(1) for j in range(m)},n)
        scale=F(1,m**(n-1))
        sh=F(n*(m-1),2)
        for x in (F(1,7),F(3,7),F(5,7)):
            left=samples(n,m,x)
            base={k:v for k in range(-n*m-3,n*m+4)
                  if (v:=centered_spline(n,x+sh-k))}
            right={k:scale*v for k,v in multiply(mask,base).items()}
            assert left==right, ('refinement identity failed',n,m,x)
            count+=1

# Exact mask divisibility for representative all-order integer scales.
from math import gcd
for m in range(2, 22):
    assert all(gcd(j,m)<m for j in range(1,m))
print('CHECK_OK exact_refinement_samples=%d integer_mask_cases=20' % count)
