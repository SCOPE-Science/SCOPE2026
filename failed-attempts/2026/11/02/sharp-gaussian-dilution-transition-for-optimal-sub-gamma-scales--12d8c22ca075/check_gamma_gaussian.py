#!/usr/bin/env python3
"""Independent arithmetic and optimization checks for Gaussian-smoothed Gamma jump sums.
Run: python check_gamma_gaussian.py
"""
import math
from fractions import Fraction

def H(alpha, x):
    assert alpha > 0 and 0 <= x < 1
    if x < .025:
        a = 1.; ans = 1.; power = 1.
        for k in range(1, 200):
            a *= (alpha+k+1)/(k+2)
            power *= x
            ans += a*power
            if abs(a*power) < 1.e-16:
                break
        return ans
    return 2*((1-x)**(-alpha)-1-alpha*x)/(alpha*(alpha+1)*x*x)

def psi(alpha, w, x):
    return -math.expm1(-math.log1p(w*(H(alpha,x)-1)))/x

def phase2(w):
    r=math.sqrt(1-w)
    if w<15/16:
        return 3*(1+r)/(2*(1+2*r))
    return 4*w/3

def psi2(w,x):
    return w*(4-3*x)/(3*(1-x)**2+w*x*(4-3*x))

def golden_max(f, a=0.,b=1.,iters=170):
    phi=(math.sqrt(5)-1)/2
    c=b-phi*(b-a);d=a+phi*(b-a)
    fc=f(c);fd=f(d)
    for _ in range(iters):
        if fc>fd:
            b,d,fd=d,c,fc;c=b-phi*(b-a);fc=f(c)
        else:
            a,c,fc=c,d,fd;d=a+phi*(b-a);fd=f(d)
    z=(a+b)/2
    return z,f(z)

checks=0
# Algebraic exact rational matching, independent of float hypergeometric implementation.
for w_num in range(1,64):
    w=Fraction(w_num,64)
    for x_num in range(1,64):
        x=Fraction(x_num,64)
        H2=(3-2*x)/(3*(1-x)**2)
        v=(1-(1-w+w*H2)**-1)/x
        expected=w*(4-3*x)/(3*(1-x)**2+w*x*(4-3*x))
        assert v == expected
        checks+=1
# Closed-form optimizer and its derivative sign checked at many points.
for wi in range(1,1000):
    w=wi/1000
    p=phase2(w)
    assert p>=1-1.e-12
    if w<15/16:
        r=math.sqrt(1-w)
        x=(4*r-1)/(3*r)
        assert 0<x<1
        assert abs(psi2(w,x)-p) <= 2e-12
    else:
        assert abs(psi2(w,1.e-10)-p) <= 2e-9
    for j in range(1,101):
        x=j/101
        assert psi2(w,x) <= p+1e-11
        checks+=1
    checks+=2
# Check original cumulant generating formula, limiting alpha branches, and normalized Gaussian factor.
for alpha in (.3,.7,1.,1.25,1.5,2.,3.,5.):
    for w in (.025,.12,.5,.95,1.):
        for k in range(1,101):
            x=k/102
            z=H(alpha,x)
            assert z>=1
            v=psi(alpha,w,x)
            assert 0<v<1/x
            if alpha<=1:
                assert v<=1+1e-10
            checks+=3
        if alpha>1:
            x=1-1e-9
            assert psi(alpha,w,x)>1
            checks+=1
# Shape-2 small-weight asymptotic: coefficient 1/12.
for w in (.0005,.001,.002,.004,.008):
    assert abs((phase2(w)-1)/(w/12)-1)<.012
    checks+=1
# Shape threshold cases: analytic alpha<=1 and high-tail alpha>1.
for alpha in (.2,.5,.9,1.):
    for w in (.01,.1,.5,1.):
        for x in (.00001,.01,.13,.42,.8,.95,.99,.9999):
            assert psi(alpha,w,x)<=1+1e-9
            checks+=1
print(f'PASS: {checks} assertions, exact fractions and dense independent gamma-mixture checks')
