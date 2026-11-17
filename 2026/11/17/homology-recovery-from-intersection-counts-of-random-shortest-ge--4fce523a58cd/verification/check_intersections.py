#!/usr/bin/env python3
"""Finite, exact-rational checks and direct simulations for a fixed-geodesic intersection-count law."""
from fractions import Fraction as F
from math import floor, isqrt
import random

def integral_poly(lo, hi, x0, x1, y0, y1):
    if hi <= lo:
        return F(0)
    return x0*y0*(hi-lo) + (x0*y1+x1*y0)*(hi*hi-lo*lo)/2 + x1*y1*(hi**3-lo**3)/3

def exact_law(p,q):
    a,b=sorted((abs(p),abs(q)),reverse=True)
    assert a>=1
    regions=[]
    if b==0:
        regions=[(F(0),F(a,2),F(2,a),F(0))] # density of abs(W)
    else:
        v=F(a-b,2); t=F(a+b,2)
        if v>0: regions.append((F(0),v,F(2,a),F(0)))
        regions.append((v,t,F(a+b,a*b),F(-2,a*b)))
    cap=(a+b+1)//2
    probabilities=[]
    for k in range(cap+1):
        hats=[(F(0),F(1),F(1),F(-1))] if k==0 else [(F(k-1),F(k),F(1-k),F(1)), (F(k),F(k+1),F(k+1),F(-1))]
        pr=F(0)
        for l,u,c0,c1 in regions:
            for h0,h1,d0,d1 in hats:
                pr+=integral_poly(max(l,h0),min(u,h1),c0,c1,d0,d1)
        probabilities.append(pr)
    return probabilities

def exact_moments(p,q):
    n=exact_law(p,q)
    return sum((i*x for i,x in enumerate(n)),F(0)),sum((i*i*x for i,x in enumerate(n)),F(0))

def formula(p,q):
    a,b=sorted((abs(p),abs(q)),reverse=True)
    return F(3*a*a+b*b,12*a),F(a*a+b*b+2,12)

def invert(mu,nu):
    S=12*nu-2
    d=9*mu*mu-S/2
    assert d>=0
    root=F(isqrt(d.numerator), isqrt(d.denominator))
    assert root*root==d
    a=3*mu+root
    b2=S-a*a
    assert b2>=0
    b=F(isqrt(b2.numerator),isqrt(b2.denominator))
    assert b*b==b2
    return a,b

def run():
    for p in range(0,13):
        for q in range(0,13):
            if p==q==0:continue
            law=exact_law(p,q)
            assert sum(law)==1,(p,q,law,sum(law))
            assert all(x>=0 for x in law)
            m=exact_moments(p,q)
            assert m==formula(p,q),(p,q,m,formula(p,q))
            a,b=invert(*m)
            assert a==max(p,q) and b==min(p,q),(p,q,a,b)
    assert exact_law(1,0)==[F(3,4),F(1,4)]
    assert exact_law(1,1)==[F(2,3),F(1,3)]
    assert exact_law(2,1)==[F(23,48),F(24,48),F(1,48)]
    rng=random.Random(20261112)
    for p,q,L,H in [(1,0,1.,1.),(1,1,4.,.3),(2,1,.2,7.),(3,2,3.,5.),(5,3,1.,100.)]:
        # Simulate two Haar endpoints A,B, choose geodesic by shortest coordinate representatives,
        # and count torus intersections via its linear phase. Do not use exact-law sampler.
        n=240000
        s1=s2=0
        for _ in range(n):
            x0=rng.random();y0=rng.random();x1=rng.random();y1=rng.random()
            dx=(x1-x0+.5)%1-.5; dy=(y1-y0+.5)%1-.5
            phase=(q*x0-p*y0)%1
            count=abs(floor(phase+q*dx-p*dy))
            s1+=count; s2+=count*count
        mu,nu=formula(p,q)
        assert abs(s1/n-float(mu))<.016,(p,q,s1/n,mu)
        assert abs(s2/n-float(nu))<.09,(p,q,s2/n,nu)
        print(f'homology=({p},{q}) aspect={L/H:g} exact={mu},{nu} observed={s1/n:.6f},{s2/n:.6f} law={exact_law(p,q)}')
    # Independent geometric test: solve all intersections of the lifted open segment
    # with integer translates of one fundamental primitive closed-geodesic arc.
    for p,q in [(1,0),(1,1),(2,1),(3,2),(5,3),(-3,2)]:
        m=max(abs(p),abs(q))
        for _ in range(200):
            x0,y0,x1,y1=[rng.random() for j in range(4)]
            dx=(x1-x0+.5)%1-.5;dy=(y1-y0+.5)%1-.5
            W=q*dx-p*dy
            if abs(W)<1e-8: continue
            predicted=abs(floor((q*x0-p*y0)%1+W))
            observed=0
            for i in range(-m-2,m+3):
                for j in range(-m-2,m+3):
                    s=(q*(i-x0)-p*(j-y0))/W
                    t=(dy*(i-x0)-dx*(j-y0))/W
                    if 1e-10<s<1-1e-10 and 1e-10<=t<1-1e-10:
                        observed+=1
            assert observed==predicted,(p,q,observed,predicted)
    print('FIXED_GEODESIC_HOMOLOGY_CHECKS_OK')

if __name__=='__main__': run()
