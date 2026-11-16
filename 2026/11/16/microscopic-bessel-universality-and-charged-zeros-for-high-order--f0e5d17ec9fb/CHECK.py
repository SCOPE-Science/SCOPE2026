#!/usr/bin/env python3
"""Finite independent arithmetic checks for the Laguerre-to-Bessel kernel expansion.

No proof of a statement quantified over all indices follows from these tests.
Requires only the Python standard library.
"""
from fractions import Fraction as F
from decimal import Decimal, localcontext
from math import comb, factorial
import cmath

COUNT = 0

def check(pred, note):
    global COUNT
    assert pred, note
    COUNT += 1

def laguerre_scaled(n, t):
    ans = F(0)
    for k in range(n+1):
        ans += F((-1)**k * comb(n,k),factorial(k)) * (t/F(n))**k
    return ans

def bessel_series(t, cutoff=70):
    h = F(0); hp = F(0)
    for k in range(cutoff+1):
        c = F((-1)**k, factorial(k)**2)
        h += c * t**k
        if k: hp += k*c*t**(k-1)
    return h,hp

# Exact finite coefficient algebra / Bonferroni bound checks.
for n in [1,2,3,5,10,15,30]:
    for k in range(0,2*n+3):
        c=F(1)
        if k>n: c=F(0)
        else:
            for j in range(k): c *= (1-F(j,n))
        s=F(k*(k-1),2*n)
        rem=c-1+s
        check(rem >= 0, ('coefficient lower bound',n,k))
        check(rem <= s*s/2, ('coefficient upper bound',n,k))

# ODE for the Bessel series H(t) = sum (-t)^k/(k!)^2:
# tH''+H'+H=0 coefficientwise. Validate the first 15 exact coefficients.
for j in range(15):
    c=lambda k:F((-1)**k, factorial(k)**2)
    check((j+1)**2*c(j+1)+c(j)==0, ('Bessel ODE',j))

# Exact Laguerre series agrees with its falling-factorial representation.
for n in (2,3,5,11,30):
    for t in [F(1,4),F(1),F(9,4),F(4)]:
        s=sum(F((-1)**k, factorial(k)**2)*t**k *
              (F(0) if k>n else F(factorial(n),factorial(n-k)*n**k))
              for k in range(n+1))
        check(s==laguerre_scaled(n,t), ('Laguerre coefficients',n,t))

# Numeric checks at finite n for the second-order remainder.
with localcontext() as ctx:
    ctx.prec=65
    for t in (F(1,4),F(1),F(9,4),F(4)):
        h,hp=bessel_series(t)
        for n in (13,29,61,113):
            tn=Decimal(t.numerator)/Decimal(t.denominator)
            H=Decimal(h.numerator)/Decimal(h.denominator)
            Hp=Decimal(hp.numerator)/Decimal(hp.denominator)
            L=laguerre_scaled(n,t)
            Ld=Decimal(L.numerator)/Decimal(L.denominator)
            actual=(-tn/(2*Decimal(n))).exp()*Ld
            pred=H+(tn/2)*Hp/Decimal(n)
            error=abs(actual-pred)*n*n
            check(error < Decimal(30), ('quadratic remainder',t,n,error))

# Exact one-point positive/negative charge densities after scaling.
for n in range(1,51):
    a=F(n+1,n); b=F(1)
    unsigned=(a*a+b*b)/(a+b)
    expected=(F(n)+F(1,2)+F(1,4*n+2))/n
    check(unsigned==expected, ('unsigned Kac Rice', n))
    check(a-b==F(1,n), ('charge imbalance',n))

print(f'PASS: {COUNT} finite consistency assertions; no infinite assertion is certified by testing.')
