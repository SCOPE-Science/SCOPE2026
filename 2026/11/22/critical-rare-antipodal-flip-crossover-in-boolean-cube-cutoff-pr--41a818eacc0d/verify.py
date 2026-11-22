#!/usr/bin/env python3
"""Standalone, deterministic checks for an antipodal-flip Boolean-cube chain.
Only Python standard-library dependencies. Infinite-limit claims use the proof.
"""
from fractions import Fraction as F
from itertools import product
from math import comb, exp, log, sqrt, cosh, sinh, pi

checks = 0

def check(statement):
    global checks
    assert statement
    checks += 1


def density(signs, b, h):
    w = (1 + h) / 2
    plus = F(1); minus = F(1)
    for s in signs:
        plus *= 1 + b * s
        minus *= 1 - b * s
    return w * plus + (1 - w) * minus


def binomial_tv(n, b, h):
    w = (1 + h) / 2
    return sum(F(comb(n, j), 2**n) * abs(w*(1+b)**j*(1-b)**(n-j)
                  +(1-w)*(1-b)**j*(1+b)**(n-j)-1)
               for j in range(n+1))/2

for n in range(1, 8):
    states = list(product((-1,1), repeat=n))
    for b in [F(0), F(1,5), F(2,5), F(3,5)]:
        for h in [F(0), F(1,3), F(2,3), F(1)]:
            densities = [density(s, b, h) for s in states]
            check(sum(densities) == 2**n)
            check(all(x >= 0 for x in densities))
            chi = sum((x-1)**2 for x in densities)/2**n
            exact = ((1+h*h)*(1+b*b)**n+(1-h*h)*(1-b*b)**n)/2 - 1
            check(chi == exact)
            brute = sum(abs(x-1) for x in densities)/F(2**(n+1))
            check(brute == binomial_tv(n,b,h))
            for mask in range(1<<n):
                walsh = sum(densities[k] * (1 if (sum(i in range(n) and ((mask>>i)&1) and states[k][i]==-1 for i in range(n))%2 == 0) else -1) for k in range(2**n))/2**n
                expected = b**mask.bit_count() * (h if mask.bit_count()%2 else 1)
                check(walsh == expected)

# Deterministic Gaussian quadrature and large-binomial checks at c=0.
def gaussian_tv(a,h):
    # fixed midpoint quadrature on [-11,11] (Gaussian tails negligible)
    steps=20000
    dz=22/steps
    v=0.
    for i in range(steps):
        z=-11+(i+0.5)*dz
        l=exp(-a*a/2)*(cosh(a*z)+h*sinh(a*z))
        v += 0.5*abs(l-1)*exp(-z*z/2)/sqrt(2*pi)*dz
    return v


def float_binomial_tv(n,b,h):
    # derive binomial weights from a stable recurrence starting at the mode
    mid=n//2
    logpm=__import__('math').lgamma(n+1)-__import__('math').lgamma(mid+1)-__import__('math').lgamma(n-mid+1)-n*log(2)
    p=exp(logpm)
    ps=[0.]*(n+1)
    ps[mid]=p
    for j in range(mid,n):
        ps[j+1]=ps[j]*(n-j)/(j+1)
    for j in range(mid,0,-1):
        ps[j-1]=ps[j]*j/(n-j+1)
    w=(1+h)/2
    return sum(pp*abs(w*(1+b)**j*(1-b)**(n-j)+(1-w)*(1-b)**j*(1+b)**(n-j)-1) for j,pp in enumerate(ps))/2

expected=[0.382924922548, 0.273066429944, 0.206743690623]
for h,target in [(1.,expected[0]),(exp(-0.5),expected[1]),(0.,expected[2])]:
    check(abs(gaussian_tv(1.,h)-target)<0.00005)
    for n in [150,500,1500]:
        finite=float_binomial_tv(n,1/sqrt(n),h)
        check(abs(finite-target)<0.045)
    a=1.0
    chisq=cosh(a*a)-1+h*h*sinh(a*a)
    check(chisq>=0)

# Check finite n monotonicity under increasing global-antipodal mixing.
for n in [2,3,5,9,15,51]:
    b=F(2,7)
    vals=[binomial_tv(n,b,F(v,5)) for v in range(6)]
    check(all(x<=y for x,y in zip(vals,vals[1:])))

print('VERIFY_OK',checks,'exact and deterministic finite checks')
