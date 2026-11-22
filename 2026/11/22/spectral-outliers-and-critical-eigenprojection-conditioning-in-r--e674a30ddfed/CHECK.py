#!/usr/bin/env python3
"""Exact-rational checks of finite recurrences and numerical hypergeometric sums.
The unrestricted operator-spectrum theorem is proved analytically, not by this test.
"""
from fractions import Fraction as F
from math import prod, isclose

checks = 0

def verify(x):
    global checks
    assert x
    checks += 1

def rising(a, k):
    out = F(1)
    for s in range(k): out *= a + s
    return out

def fac(k):
    return prod(range(1, k+1))

for alpha in [F(-1,2), F(0), F(1,2), F(1), F(3,2), F(2), F(5,2), F(3), F(4), F(5)]:
    A = alpha + 2
    a_inf = F(1, 1) / A
    b_inf = 1 - a_inf
    for n in range(18):
        delta = (n + A) / (n + 1)
        aa = delta / A
        bb = 1 - aa
        verify(aa + bb == 1)
        verify(bb == (A-1)*n/(A*(n+1)))
        verify((delta > 2) == (F(n) < alpha))
        verify((bb < b_inf-a_inf) == (F(n) < alpha))
        verify(F(0) <= bb < b_inf)
    for j in range(6):
        if not F(j) < alpha: continue
        lam = (A-1)*j/(A*(j+1))
        rr = F(j+1)/(A-1)
        verify(F(0) < rr < 1)
        # finite right eigenvector normalized at its last nonzero site
        u = [F(0)]*(j+1)
        u[j] = F(1)
        for n in range(j-1, -1, -1):
            u[n] = u[n+1]*(j+1)*(n+A)/((A-1)*(j-n))
        verify(u[0] == rising(A,j)*rr**j/fac(j))
        for n in range(j+1):
            aa = (n+A)/(A*(n+1)); bb = 1-aa
            rhs = bb*u[n]+(aa*u[n+1] if n<j else 0)
            verify(rhs==lam*u[n])
        # Left eigenvector recurrence and rising-factor formula
        q = F(1)
        for k in range(1, 9):
            n=j+k
            aa_prev=(n-1+A)/(A*n)
            bb_n=(A-1)*n/(A*(n+1))
            q=aa_prev*q/(lam-bb_n)
            expected=(-rr)**k*rising(j+A,k)*rising(j+2,k)/(rising(j+1,k)*fac(k))
            verify(q==expected)
        # The summand ratio has a closed-form hypergeometric sum.
        term=1.0; partial=1.0; r=float(rr)
        for k in range(1, 6000):
            term *= r*(j+float(A)+k-1)*(j+k+1)/((j+k)*k)
            partial += term
            if term < 1e-12*partial: break
        closed=2*(1-r)**(-float(A)-j-1)
        verify(isclose(partial,closed,rel_tol=1e-9,abs_tol=1e-8))
        verify(float(rising(A,j)*rr**j/fac(j))*closed > 1)

# Critical powers and constants are checked by converging ratios (not proofs).
for j in range(4):
    A0=j+2
    C=2*float(rising(F(A0),j))/fac(j)*(j+1)**(2*j+3)
    for eps in [0.05,0.01,0.002]:
        alpha=j+eps; A=alpha+2; r=(j+1)/(alpha+1)
        exact=2*prod(A+t for t in range(j))/fac(j)*r**j*(1-r)**(-A-j-1)
        ratio=exact*(eps**(2*j+3))/C
        verify(abs(ratio-1) < 0.85)

print(f"BERGMAN_DIAGONAL_MARKOV_CHECK_OK {checks}")
