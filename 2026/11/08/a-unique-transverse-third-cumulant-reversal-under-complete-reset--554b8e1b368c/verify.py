#!/usr/bin/env python3
"""Independent exact-rational moment checks for the stationary resetting active swimmer.
Run with: python3 verify.py. Only Python's standard library is required.
"""
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
from math import sqrt

ZERO=(F(0),F(0))
def add(*zs):return (sum((z[0] for z in zs),F(0)),sum((z[1] for z in zs),F(0)))
def scale(z,k):return (z[0]*k,z[1]*k)
def div_i(z):return (z[1],-z[0])

def moments(d,r,h):
    @lru_cache(None)
    def m(p,q,n):
        if p+q==0:
            return (F(1),F(0)) if n==0 else (r/(r+d*n*n),F(0))
        terms=[]
        if p:
            terms.append(scale(add(m(p-1,q,n+1),m(p-1,q,n-1)),F(p,2)))
        if q:
            terms.append(scale(div_i(add(m(p,q-1,n+1),scale(m(p,q-1,n-1),-1))),F(q,2)))
        if p>=2:terms.append(scale(m(p-2,q,n),h*p*(p-1)))
        if q>=2:terms.append(scale(m(p,q-2,n),h*q*(q-1)))
        return scale(add(*terms),F(1)/(r+p+q+d*n*n))
    mean=m(1,0,0)[0]
    y2=m(0,2,0)[0]
    xy2=m(1,2,0)[0]
    assert m(0,1,0)==ZERO and m(1,1,0)==ZERO
    return mean,y2,xy2,xy2-mean*y2

def Q(d,r):
    return 3*r**4+(15*d+9)*r**3+(12*d*d+20*d+6)*r*r-(58*d*d+34*d)*r-(36*d**3+147*d*d+30*d)
def S(d,r):return (r*r+2*r-d)*(4*d+r)*(9*d+r)*(d+r+1)*(4*d+r+1)
def P(d,r,h):return 2*d*Q(d,r)+h*S(d,r)
def denom(d,r):return (d+r)*(4*d+r)*(9*d+r)*(r+1)*(r+2)*(r+3)*(d+r+1)*(d+r+2)*(4*d+r+1)
def theory(d,r,h):
    mean=r/((d+r)*(r+1))
    y2=4*d/((4*d+r)*(r+2)*(d+r+1))+2*h/(r+2)
    xy2=(4*d*r*(9*d+4*r+3)/((d+r)*(9*d+r)*(r+1)*(r+3)*(d+r+2)*(4*d+r+1))
          +2*r*h*(d+2*r+3)/((d+r)*(r+1)*(r+3)*(d+r+2)))
    return mean,y2,xy2,2*r*P(d,r,h)/denom(d,r)

def polynomial_coefficients(d,h):
    return [
        -6*d*d*(h*(24*d**3+30*d*d+6*d)+(12*d*d+49*d+10)),
        d*d*(h*(56*d*d+223*d+59)-(116*d+68)),
        d*(h*(144*d**3+539*d*d+279*d+25)+(24*d*d+40*d+12)),
        h*(232*d**3+329*d*d+73*d+2)+30*d*d+18*d,
        h*(105*d*d+66*d+5)+6*d,
        2*h*(9*d+2),
        h]
def find_root(d,h):
    lo=0.0;hi=1.0
    while float(P(d,hi,h))<=0:hi*=2
    for _ in range(100):
        mid=(lo+hi)/2
        if float(P(d,mid,h))>0:hi=mid
        else:lo=mid
    return (lo+hi)/2

def run():
    checks=0
    D=[F(1,20),F(1,3),F(1),F(2),F(5)]
    R=[F(1,7),F(1,2),F(1),F(3),F(8)]
    H=[F(0),F(1,10),F(1),F(5)]
    for d,r,h in product(D,R,H):
        got=moments(d,r,h);expect=theory(d,r,h)
        for name,a,b in zip(['EX','EY2','EXY2','C'],got,expect):
            assert a==b,(name,d,r,h,a,b)
            checks+=1
        coefficients=polynomial_coefficients(d,h)
        assert sum(coefficients[i]*r**i for i in range(7))==P(d,r,h)
        assert coefficients[0]<0 and all(t>0 for t in coefficients[2:5])
        assert coefficients[5]>=0 and coefficients[6]>=0
        checks+=3
    # The identity at r_T: d = t(t+2), independent of h.
    for t in [F(1,11),F(1,3),F(2),F(9)]:
        d=t*(t+2)
        assert Q(d,t)==-t*(t+2)*(24*t**4+163*t**3+384*t*t+325*t+30)
        checks+=1
    # Strict ordering and thermal monotonicity of the unique positive zero.
    for d in [0.01,0.1,0.5,1,2,10,100]:
        roots=[find_root(d,h) for h in [0,0.01,0.1,1,10,100]]
        lower=sqrt(1+d)-1
        assert all(lower<rr for rr in roots) and all(roots[i]>roots[i+1] for i in range(5))
        checks+=1
    # Athermal square-root singular asymptotics (finite-parameter probes, not proof).
    assert abs(find_root(1e-7,0)/sqrt(5e-7)-1)<0.01
    assert abs(find_root(1e7,0)/sqrt(3e7)-1)<0.01
    checks+=2
    print('PASS:',checks,'exact-rational assertions and independent limiting checks')
    print('d=1: athermal critical reset=',find_root(1,0))
    print('d=1: h=1 critical reset=',find_root(1,1))
    print('d=1: thermal floor=',sqrt(2)-1)
if __name__=='__main__':run()
