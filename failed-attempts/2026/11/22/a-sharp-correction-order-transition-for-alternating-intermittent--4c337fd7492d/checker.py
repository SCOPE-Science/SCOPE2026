#!/usr/bin/env python3
"""Numerical spot checks for alternating inverse branches; not an infinite proof."""
import math

def inverse(y, a):
    lo, hi = 0., y
    A = 2.**a
    for _ in range(44):
        mid = (lo + hi) / 2
        if mid * (1 + A * mid**a) > y: hi = mid
        else: lo = mid
    return (lo + hi) / 2

def verify(alpha, beta, reverse=False, n=30000):
    x = 0.4
    for _ in range(n):
        if reverse:
            x = inverse(inverse(x, beta), alpha)
        else:
            x = inverse(inverse(x, alpha), beta)
    A, B = 2**alpha, 2**beta
    c = alpha*A
    theta = (beta-alpha)/alpha
    deficit = x**(-alpha)-c*n
    if theta < 1:
        K = alpha*B * c**(-theta)/(1-theta)
        comparison = deficit/(K*n**(1-theta))
        assert abs(comparison-1) < 0.12, (alpha,beta,reverse,comparison)
    elif abs(theta-1)<1.e-10:
        K = A*(1-alpha)/2
        comparison = deficit-K*math.log(n)
        assert abs(comparison)<12, (alpha,beta,reverse,comparison)
    else:
        K = -A*(1+alpha)/2
        comparison = deficit-K*math.log(n)
        assert abs(comparison)<12, (alpha,beta,reverse,comparison)
    print(alpha,beta,'reverse=',reverse,'deficit=',round(deficit,5),'comparison=',round(comparison,6))

if __name__ == '__main__':
    for a,b in [(0.5,0.65),(0.5,0.75),(0.5,1.0),(0.5,1.25)]:
        for reverse in (False,True): verify(a,b,reverse)
    print('PASS: 8 independent numeric recurrence comparisons')
