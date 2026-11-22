#!/usr/bin/env python3
"""Numerical, not infinite, checks of circular von Mises variation coefficients."""
import math
from math import pi

def besseli(n, b):
    # I_n(b) = (b/2)^n/n! sum_{k>=0}(b*b/4)^k/[k!(n+1)...(n+k)]
    term = (b/2)**n / math.factorial(n)
    total = term
    for k in range(1, 250):
        term *= (b*b/4)/(k*(n+k))
        total += term
        if abs(term) < 1e-17 * max(abs(total), 1e-300):
            break
    return total

def sharp(b, r):
    den = besseli(0,b)
    return 4/pi*sum(((-1)**j)/(2*j+1)*(besseli(2*j+1,b)/den)**r for j in range(34))

def simpson(f,a,b,n=8192):
    step=(b-a)/n
    return step/3*(f(a)+f(b)+4*sum(f(a+(2*j-1)*step) for j in range(1,n//2+1))+2*sum(f(a+2*j*step) for j in range(1,n//2)))

for b in (0.1,0.6,1.0,2.0,5.0,10.0):
    s1=sharp(b,1)
    independent=(simpson(lambda t: math.exp(b*math.cos(t)),-pi/2,pi/2)/(pi*besseli(0,b))-1)
    assert abs(s1-independent)<3e-11,(b,s1,independent)
    vals=[sharp(b,r) for r in range(1,7)]
    assert all(0<v<1 for v in vals)
    assert all(vals[i+j+1] < vals[i]*vals[j]+1e-13 for i in range(3) for j in range(3) if i+j+1<len(vals)), (b,vals)
    first=besseli(1,b)/besseli(0,b)
    e=abs(sharp(b,32)/((4/pi)*first**32)-1)
    assert e<0.005,(b,e)
print('VON_MISES_BV_DIRECT_QUADRATURE_AND_ODD_SPECTRAL_SERIES_PASS')
print('VON_MISES_BV_STRICT_SUBMULTIPLICATIVITY_SAMPLED_PASS')
print('VON_MISES_BV_FIRST_MODE_LONG_ITERATION_SAMPLED_PASS')
