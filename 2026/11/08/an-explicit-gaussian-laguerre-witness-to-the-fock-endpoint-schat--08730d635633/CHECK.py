#!/usr/bin/env python3
"""Exact rational spot checks for Gaussian-Laguerre radial Toeplitz symbol identities."""
from fractions import Fraction as Q
from math import comb, factorial

checks = 0

def check(condition, message):
    global checks
    assert condition, message
    checks += 1

def moment_from_polynomial(k, m, t):
    # Integrate the Laguerre polynomial term-by-term against Gamma(k+1,t).
    return (-1)**m * t**(k-m) * sum(((-1)**l * Q(comb(m,l)*factorial(k+l), factorial(k)*factorial(l)) for l in range(m+1)), Q(0))

def heat_at_zero_from_polynomial(m,t):
    return 2*(-1)**m*t**(-m) * sum(((-1)**l * Q(comb(m,l), (1+t)**(l+1)) for l in range(m+1)), Q(0))

for N in range(2, 17):
    t=Q(1,N**4)
    for m in range(N):
        for k in range(N+10):
            expected=Q(comb(k,m)*t**(k-m)) if k>=m else Q(0)
            check(moment_from_polynomial(k,m,t)==expected, f'moment N={N},m={m},k={k}')
        check(heat_at_zero_from_polynomial(m,t)==2*(-1)**m/(1+t)**(m+1), f'heat N={N},m={m}')
    for k in range(N):
        lam=sum(((-1)**m*moment_from_polynomial(k,m,t) for m in range(N)), Q(0))
        check(lam==(-1)**k*(1-t)**k, f'diagonal prefix N={N},k={k}')
    heat=sum(((-1)**m*heat_at_zero_from_polynomial(m,t) for m in range(N)), Q(0))
    check(heat==2*(1-(1+t)**(-N))/t, f'block heat N={N}')
    err=sum(((1-t)**(-m-1)-1 for m in range(N)), Q(0))
    check(err<=Q(2,N**2), f'trace error N={N}')
    check(heat>=Q(3,2)*N, f'heat lower N={N}')
print(f'GAUSSIAN_LAGUERRE_MOMENTS_EXACT_OK {checks}')
