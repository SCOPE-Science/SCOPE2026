#!/usr/bin/env python3
"""Finite numerical checks for radial zeros of a Gaussian analytic trinomial.
These assertions do not replace the proof of the global peak classification.
"""
import math

def solve_u(m):
    assert isinstance(m, int) and m >= 2
    def f(u): return 4*m*m*(u-1)**3-4*u**3+1
    lo, hi = 1.0, 2.0
    while f(hi) <= 0: hi *= 2
    for _ in range(100):
        mid = (lo+hi)/2
        if f(mid) > 0: hi = mid
        else: lo = mid
    return (hi+lo)/2

def acrit(m): return 4*solve_u(m)**1.5

def h(x,a):
    c = math.cosh(x)
    return math.sinh(x)*(a/(a*c+2)-4/(a+2*c))

def hp(x,a):
    c=math.cosh(x)
    return a*(a+2*c)/(a*c+2)**2 - 4*(a*c+2)/(a+2*c)**2

def expected_density(r,m,a):
    s=r**(2*m)
    return m*m/math.pi *r**(2*m-2)*(a+4*s+a*s*s)/(1+a*s+s*s)**2

def other_density(r,m,a):
    x=2*m*math.log(r)
    c=math.cosh(x)
    return 2*m*m/(math.pi*r*r)*(a*c+2)/(a+2*c)**2

def extrema_count(m,a):
    # Numerically detect sign crossings of the exact log-density derivative.
    # The critical shoulder is excluded from this checker.
    xs=[-12+i*24/20000 for i in range(20001)]
    values=[h(x,a)-1/m for x in xs]
    changes=[]
    for i in range(len(values)-1):
        if values[i]*values[i+1]<0:
            changes.append((xs[i]+xs[i+1])/2)
    return changes

def run():
    k=0
    for m in (2,3,4,6,10,40,100):
        u=solve_u(m); a=4*u**1.5
        t=math.sqrt(u)
        c=(2*t**4-1)/(t*(2*t*t-1))
        x=math.acosh(c)
        assert abs(h(x,a)-1/m)<1e-10; k+=1
        assert abs(hp(x,a))<1e-10; k+=1
        assert abs(4*m*m*(u-1)**3-(4*u**3-1))<1e-7; k+=1
        for factor,expected in ((0.7,1),(1.3,3)):
            roots=extrema_count(m,a*factor)
            assert len(roots)==expected,(m,factor,roots); k+=1
        for factor in (0.7,1.3):
            for r in (.7,.9,1.02,1.2):
                p=expected_density(r,m,a*factor)
                q=other_density(r,m,a*factor)
                assert math.isclose(p,q,rel_tol=2e-9), (m,r,p,q); k+=1
    for a in (0.1,0.7,1.4,2.0,4.0,4.1,6.0,10.0,100.0):
        for x in (-3,-1.1,0,.2,1.5,3):
            deriv=(h(x+1e-5,a)-h(x-1e-5,a))/2e-5
            assert math.isclose(deriv,hp(x,a),rel_tol=1e-7,abs_tol=1e-8);k+=1
    for m in (300,1000,3000,10000):
        a=acrit(m)
        coeff=6*(3/4)**(1/3)
        ratio=(a-4)*m**(2/3)/coeff
        assert abs(ratio-1)<.2; k+=1
    print(f'PASS {k} finite numerical assertions; the theorem relies on analytic proofs.')
if __name__=='__main__': run()
