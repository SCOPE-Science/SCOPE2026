#!/usr/bin/env python3
"""Exact polynomial and independent numerical checks for two-frequency exterior leverage."""
from fractions import Fraction as Q
from math import sin, cos

def padd(a,b):
    return [((a[i] if i < len(a) else 0)+(b[i] if i < len(b) else 0)) for i in range(max(len(a),len(b)))]
def pmul(a,b):
    out=[Q(0)]*(len(a)+len(b)-1)
    for i,ai in enumerate(a):
        for j,bj in enumerate(b):out[i+j]+=ai*bj
    return out
def scale(a,k):return [k*t for t in a]
def check_poly():
    # u=1-z/6+z^2/120.  F(u,z)=2+2u-4u^2-uz
    u=[Q(1),-Q(1,6),Q(1,120)]
    f=padd(padd([Q(2)],scale(u,Q(2))),scale(pmul(u,u),Q(-4)))
    f=padd(f,scale(pmul(u,[Q(0),Q(1)]),Q(-1)))
    expected=[Q(0),Q(0),Q(20,3600),Q(10,3600),Q(-1,3600)]
    assert f==expected,(f,expected)
    return 1

def k(y,x):
    s=sin(y)/y
    return (2-2*s*cos(y*x))/(1-s*s)

def g_ratio(eps,x):
    # g(t)=cos(eps*t)+(3*x/eps)*sin(eps*t); cross integral vanishes.
    v=cos(eps*x)+(3*x/eps)*sin(eps*x)
    avcos2=(1+sin(2*eps)/(2*eps))/2
    avsin2=(1-sin(2*eps)/(2*eps))/2
    return v*v/(avcos2+(3*x/eps)**2*avsin2)

def check_numeric():
    count=0
    xs=[1,1.001,1.1,1.5,2,3,4,5,7,10,25,100]
    for j in range(1,4001):
        y=.02+j*.025
        for x in xs:
            val=k(y,x)
            assert val>0
            assert val < 1+3*x*x+1e-9,(y,x,val,1+3*x*x)
            count+=1
    for x in xs:
        e=.001
        val=g_ratio(e,x)
        assert abs(val-(1+3*x*x)) < .015*(1+3*x*x), (x,val)
        count+=1
    return count

if __name__=='__main__':
    n=check_poly()+check_numeric()
    print(f'CHECK_OK assertions={n} exact_polynomial=1 numerical_points={n-1}')
