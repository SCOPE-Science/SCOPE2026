#!/usr/bin/env python3
"""Supplementary scalar and finite-matrix checks for the tapered Hilbert law."""
import math
from fractions import Fraction


def simpson(fun, a, b, n=12000):
    assert n % 2 == 0
    h = (b-a)/n
    total = fun(a)+fun(b)
    for j in range(1,n):
        total += (4 if j&1 else 2)*fun(a+j*h)
    return total*h/3


def arcosh_exp(t):
    # stable near zero
    return math.acosh(math.exp(t))


def profile(L):
    return simpson(arcosh_exp, 0.0, L)/math.pi**2


def kernel_symbol(xi):
    z=math.pi*xi
    if abs(z)>50:
        return 2*math.pi*math.exp(-abs(z))/(1+math.exp(-2*abs(z)))
    return math.pi/math.cosh(z)


def check():
    count=0
    for power, target in [(1, .5), (2, 1.), (3, math.pi**2/4)]:
        kappa=simpson(lambda x: kernel_symbol(x)**power, -20., 20., 12000)/(2*math.pi)
        assert abs(kappa-target) < 1e-7, (power,kappa,target)
        count+=1
    for L in [.02, .15, .7, 1.7]:
        h=1e-5
        deriv=(profile(L+h)-profile(L-h))/(2*h)
        assert abs(deriv-arcosh_exp(L)/math.pi**2) < 2e-5
        count+=1
    for L in [1e-3, 3e-3]:
        edge=(2*math.sqrt(2)/(3*math.pi**2))*L**1.5
        assert abs(profile(L)/edge-1)<1e-2
        count+=1
    for L in [15., 20.]:
        asym=L*L/(2*math.pi**2)+math.log(2)*L/math.pi**2
        # bounded correction, not a claim of equality
        assert abs(profile(L)-asym)<1
        count+=1
    # Rational finite compressions at epsilon=2. Check principal minors by LDL.
    for n in range(1,9):
        h=[[Fraction(1,i*j*(i+j)) for j in range(1,n+1)] for i in range(1,n+1)]
        for k in range(n):
            pivot=h[k][k]
            assert pivot>0
            for i in range(k+1,n):
                for j in range(k+1,n):
                    h[i][j]-=h[i][k]*h[k][j]/pivot
            for i in range(k+1,n):
                h[i][k]=Fraction(0)
        count+=n
    print('TAPERED_HILBERT_SUPPLEMENT_OK',count)

if __name__=='__main__':
    check()
