#!/usr/bin/env python3
"""Reproducible supplementary checks for odd finite exponential Gabor cutoffs.
Requires Python 3 standard library only. Numerical sampling is not a proof of the global theorem.
"""
from math import acos, cos, exp, log, pi, sin, sqrt, cosh


def cheb(n, x):
    return cos(n * acos(max(-1.0, min(1.0, x))))


def cheb_prime(n, x):
    # U_{n-1}(x) polynomial recurrence, valid at x = +/-1.
    u0 = 1.0
    u1 = 2.0 * x
    for j in range(2, n):
        u0, u1 = u1, 2.0 * x * u1 - u0
    return n * u1


def E(n, r, x):
    d = 1 + r*r - 2*r*x
    nn = 1 + r**(2*n) - 2*r**n*cheb(n, x)
    return nn - r**(n-1)*d*cheb_prime(n, x)


def root_bisect(f, a, b):
    assert f(a)*f(b) <= 0.0
    for _ in range(85):
        mid = (a+b)*0.5
        if f(mid) * f(a) <= 0:
            b=mid
        else:
            a=mid
    return (a+b)*0.5


def threshold(n):
    m=(n-1)//2
    return root_bisect(lambda r:1+r**n-n*r**m*(1+r),1e-8,1-1e-12)


def predicted(n, r):
    left, right = -1.0, -cos(pi/n)
    if E(n,r,left)>=0: return left
    return root_bisect(lambda x:E(n,r,x),left,right)


def F(n, r, x):
    return (1+r**(2*n)-2*r**n*cheb(n,x))/(1+r*r-2*r*x)


def direct_modulus_sq(n, r, theta):
    z = r*complex(cos(theta),sin(theta))
    power=1+0j
    total=0+0j
    for _ in range(n):
        total += power
        power *= z
    return total.real**2 + total.imag**2


def golden_min(f, left, right):
    frac=(sqrt(5)-1)/2
    c=right-frac*(right-left)
    d=left+frac*(right-left)
    fc,fd=f(c),f(d)
    for _ in range(90):
        if fc<fd:
            right,d,fd=d,c,fc
            c=right-frac*(right-left);fc=f(c)
        else:
            left,c,fc=c,d,fd
            d=left+frac*(right-left);fd=f(d)
    return min(f((left+right)/2),f(left),f(right))


def main():
    checks=0
    for n in [3,5,7,9,11,15,21,41,81]:
        q=threshold(n)
        assert 0<q<1
        lam=-log(q)
        assert abs(cosh(n*lam/2)-n*cosh(lam/2)) < 2e-7
        checks+=2
        for r in [0.04,.18,.3,.5,.8,.95,.99,max(.001,q-1e-4),min(.99999,q+1e-4)]:
            x=predicted(n,r)
            value=F(n,r,x)
            assert -1-1e-12<=x<=-cos(pi/n)+1e-12
            assert value > 0
            # Independent direct geometric series, not the rational formula.
            theta=acos(x)
            assert abs(value-direct_modulus_sq(n,r,theta)) < 5e-7
            # Independent bounded minimization on leftmost angular arc.
            opt=golden_min(lambda t:direct_modulus_sq(n,r,t),pi-pi/n,pi)
            assert value <=opt+2e-7
            assert abs(value-opt)<2e-7
            # Full frequency-grid challenge; never interpreted as exhaustive proof.
            gridmin=min(direct_modulus_sq(n,r,2*pi*k/1401) for k in range(1401))
            assert value<=gridmin+2e-7
            checks+=6
    q=threshold(5)
    assert abs(q-(3-sqrt(5))/2)<1e-13
    m=2
    etaprime=5*(m*q**(m-1)*(1+q)+q**m)-5*q**4
    c=12*(1+q**5)*etaprime/(q**4*(1+q)**2*25*24)
    assert abs(c-(5+3*sqrt(5))/4)<1e-10
    for dr in [1e-3,1e-4,1e-5]:
        v=pi-acos(predicted(5,q+dr))
        assert abs(v/sqrt(dr)-sqrt(c))<.005
        checks+=1
    checks+=2
    print('PASS:',checks,'supplementary comparisons')

if __name__=='__main__': main()
