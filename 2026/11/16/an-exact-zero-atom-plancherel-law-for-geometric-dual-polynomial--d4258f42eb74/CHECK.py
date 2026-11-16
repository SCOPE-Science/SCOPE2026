#!/usr/bin/env python3
"""Exact finite consistency checks for a zero-atom orthogonal-polynomial formula."""
from fractions import Fraction as F
from math import prod

CASES = [(F(1, 5), F(1, 5)), (F(1, 5), F(3, 10)),
         (F(1, 6), F(1, 5)), (F(1, 10), F(1, 4))]
checks = 0
for q, t in CASES:
    assert 2*q**3+4*q*q <= t
    assert t < (1-q*q)/(2-q*q)
    checks += 2
    def c(n):
        return t if n == 1 else (1-q**n if n % 2 == 0 else q**n)
    def s(n):
        return t if n == 1 else q**n
    assert s(2) < 1-s(1)/(1-s(1))
    checks += 1
    for n in range(3, 35):
        assert s(n) <= s(n-2)/2-2*s(n-1)
        checks += 1
    p = [F(1), F(0)]
    h = F(1)
    rho = t*(1-q)/(q*(1-t))
    for n in range(1, 15):
        a_prev = F(1) if n == 1 else 1-c(n-1)
        h *= a_prev/c(n)
        p.append(-c(n)*p[n-1]/(1-c(n)))
        assert p[n+1] == (-c(n)*p[n-1]/(1-c(n)))
        checks += 1
        if n%2 == 0:
            m=n//2
            den = prod((1-q**k for k in range(1, 2*m+1)), start=F(1))
            assert h*p[n]*p[n] == rho*q**(2*m*m-m)/den
            checks += 1
        else:
            assert p[n] == 0
            checks += 1
    qf=float(q); tf=float(t)
    odd_prod = prod(1-qf**(2*j+1) for j in range(45))
    even_sum = 1.0
    den = 1.0
    for m in range(1, 25):
        den *= (1-qf**(2*m-1))*(1-qf**(2*m))
        even_sum += qf**(2*m*m-m)/den
    assert abs(even_sum*odd_prod-1) < 3e-13
    checks += 1
    mass = 1/(1+float(rho)*(even_sum-1))
    target = 1/(1+float(rho)*(1/odd_prod-1))
    assert abs(mass-target) < 3e-13
    checks += 1
print(f"PASS: {checks} finite exact and numerical checks")
