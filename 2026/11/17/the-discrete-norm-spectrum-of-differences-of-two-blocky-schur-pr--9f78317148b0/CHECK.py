#!/usr/bin/env python3
"""Deterministic supplementary diagnostics for a Schur norm classification."""
import math

def f(m,a):
    x=(m-1)/m
    return x*math.sqrt(a)+math.sqrt(max(0.0,1-(2*m-1)*a/m**2))

def g(m,a):
    return (m-1)*a/m+math.sqrt(max(0.0,1+2*a/m-(4*m-1)*a*a/m**2))

def exact10(m):
    return 1.0 if m==1 else (m/math.sqrt(2*m-1) if m<=3 else 2-2/m)

def exact11(m):
    return ((m-1+2*m*math.sqrt(m+2))/(4*m-1) if m<=4 else 2-2/m)

def arg11(m):
    return m/(4*m-1)*(1+2*(m-1)/math.sqrt(m+2))

assert arg11(4)<1<arg11(5)
assert abs(exact11(2)-9/7)<1e-13
assert abs(exact11(1)-2/math.sqrt(3))<1e-13
assert abs(exact10(3)-3/math.sqrt(5))<1e-13
assert abs(exact11(3)-(2+6*math.sqrt(5))/11)<1e-13
assert abs(exact11(4)-(3+8*math.sqrt(6))/15)<1e-13
assert abs((2-2/1000000)-2)<3e-6
nchecks=6
for m in range(1,41):
    optimum10=exact10(m)
    optimum11=exact11(m)
    assert 0<=optimum10<=2 and 0<=optimum11<=2
    nchecks+=2
    for j in range(2001):
        a=j/2000
        assert f(m,a)<=optimum10+1e-11, (m,j,'f')
        assert g(m,a)<=optimum11+1e-11, (m,j,'g')
        nchecks+=2
print('SIGNED_BLOCKY_DIFFERENCE_CHECKS_OK',nchecks)
