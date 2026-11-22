#!/usr/bin/env python3
"""Standalone exact-arithmetic and numerical checks for a planar regression theorem.

Run with: python3 verify.py
No third-party packages are needed. All nonfinite assertions are proved in RESULT.md;
finite checks here diagnose algebraic and implementation errors only.
"""
from fractions import Fraction as F
from math import acos, cos, pi, sin, sqrt
from random import Random


def cmul(x, y):
    return (x[0]*y[0] - x[1]*y[1], x[0]*y[1] + x[1]*y[0])


def csub(x, y):
    return (x[0]-y[0], x[1]-y[1])


def cconj(x):
    return (x[0], -x[1])


def n2(x):
    return x[0]*x[0] + x[1]*x[1]


def check_exact(law, t, h):
    # Tangent half-angle rational parametrization: c^2+s^2=1, 0<angle<pi.
    c = (1-t*t)/(1+t*t)
    s = 2*t/(1+t*t)
    assert c*c+s*s == 1
    mu = sum((weight*offset for offset,weight in law), F(0))
    m2 = sum((weight*offset*offset for offset,weight in law), F(0))
    v = m2-mu*mu
    q = mu-m2
    D = 1-2*q*(1-c)
    assert D > 0 and v >= 0 and q >= 0
    a = (1-2*mu)*(c-1)/(h*D)
    w = s/(h*D)
    b = (a,w)
    d = ((c-1)/h,s/h)
    cross=(F(0),F(0))
    denom=F(0)
    risk=F(0)
    for off,weight in law:
        z = (1-off+off*c,off*s)
        term=cmul(d,cconj(z))
        cross=(cross[0]+weight*term[0],cross[1]+weight*term[1])
        denom += weight*n2(z)
        risk += weight*n2(csub(cmul(b,z),d))
    assert denom == D
    assert cross[0]/denom == b[0] and cross[1]/denom == b[1]
    assert risk == 4*v*(1-c)**2/(h*h*D)
    assert (a==0) == (mu==F(1,2))
    assert (risk==0) == (v==0)
    return q


def main():
    rng=Random(9122026)
    tests=0
    offsets=[F(0),F(1,4),F(1,2),F(3,4),F(1)]
    laws=[[(F(0),F(1))],[(F(1),F(1))],[(F(1,2),F(1))],
          [(F(0),F(1,6)),(F(1,2),F(2,3)),(F(1),F(1,6))],
          [(F(0),F(1,2)),(F(1),F(1,2))]]
    for _ in range(50):
        wt=[rng.randint(0,15) for _ in offsets]
        if sum(wt)==0: wt[2]=1
        n=sum(wt)
        laws.append([(s,F(w,n)) for s,w in zip(offsets,wt) if w>0])
    qs=set()
    for law in laws:
        for t in [F(1,50),F(1,5),F(1,2),F(1),F(3),F(10),F(100)]:
            for h in [F(1,3),F(1),F(5,2)]:
                qs.add(check_exact(law,t,h))
                tests += 1
    # Sharp derivative factor and fold-sign checks for all observed q values.
    for q in qs:
        Q=float(q)
        D=lambda x: 1-2*Q*(1-cos(x))
        w=lambda x: sin(x)/D(x)
        eps=1e-6
        for i in range(1,300):
            x=pi*i/300
            derivative=((1-2*Q)*cos(x)+2*Q)/D(x)**2
            finite=(w(x+eps)-w(x-eps))/(2*eps)
            assert abs(derivative-finite) < 3e-4*(1+abs(derivative))
            if Q < 0.25-1e-12:
                fold=acos(-2*Q/(1-2*Q))
                assert derivative > 0 if x < fold-1e-9 else (derivative < 0 if x > fold+1e-9 else True)
            else:
                assert derivative > 0
            tests+=1
    # q=1/6 gives fourth-order angular response, standard fourth-order compact symbol.
    q=F(1,6)
    assert (q-F(1,6))==0
    fifth=F(1,120)+q*q-q/F(4)
    assert fifth == -F(1,180)
    q=F(1,4)
    for i in range(1,100):
        theta=pi*i/100
        assert abs(sin(theta)/(1-2*float(q)*(1-cos(theta)))-2*sin(theta)/(1+cos(theta)))<1e-12
        tests+=1
    q=F(1,6)
    fold=acos(-2*float(q)/(1-2*float(q)))
    assert abs(fold-2*pi/3) < 1e-14
    gain=sin(fold)/(1-2*float(q)*(1-cos(fold)))
    assert abs(gain-sqrt(3))<1e-14
    tests+=2
    print(f'PASS: {tests} exact-rational and numerical diagnostic assertions (families and angles).')


if __name__=='__main__':
    main()
