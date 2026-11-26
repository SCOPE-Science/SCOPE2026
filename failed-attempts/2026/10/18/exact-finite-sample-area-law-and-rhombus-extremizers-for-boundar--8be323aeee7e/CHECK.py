#!/usr/bin/env python3
"""Self-contained numerical and exact checks for a boundary-sampled parallelogram area formula."""
import math
import random
from fractions import Fraction as F
from math import comb

def theoretical(a,b,n):
    a,b=F(a),F(b)
    L=2*(a+b)
    k=n+2
    deficit = F(2*L*L, a*b*(n+1)*k) * (
        1-((L-a)/L)**k-((L-b)/L)**k+(a/L)**k+(b/L)**k)
    return 1-deficit

def direct(t,a,b):
    h=a+b
    L=2*h
    t=t%L
    if t<a:return (t,0.)
    if t<h:return (a,t-a)
    if t<2*a+b:return (2*a+b-t,b)
    return (0.,L-t)

def shoelace(ts,a,b):
    points=[direct(t,a,b) for t in sorted(ts)]
    area=sum(points[i][0]*points[(i+1)%len(points)][1]-points[(i+1)%len(points)][0]*points[i][1] for i in range(len(points)))/2
    return area/(a*b)

def circular_cross(s,a,b):
    # direct expression C(s) = int_0^L det(P(t),P(t+s)) dt
    L=2*(a+b)
    return 2*a*b*s-F(2,3)*s**3+F(2,3)*(max(s-a,0)**3+max(s-b,0)**3-max(s-(L-a),0)**3-max(s-(L-b),0)**3)

def calc_cross(s,a,b,steps=20000):
    L=2*(a+b);delta=L/steps
    z=0.
    for i in range(steps):
        t=(i+.5)*delta
        x,y=direct(t,a,b);xx,yy=direct(t+s,a,b)
        z+=x*yy-y*xx
    return z*delta

def run():
    for a,b in [(1,1),(1,3),(2,5),(5,13)]:
        L=2*(a+b)
        for j in range(1,10):
            s=L*j/11
            want=float(circular_cross(s,F(a),F(b)))
            got=calc_cross(s,a,b,5000)
            assert abs(want-got)<2e-5*L*L,('cross',a,b,j,want,got)
        for n in [3,4,5,7,10,16]:
            exact=theoretical(a,b,n)
            assert 0<exact<1,(a,b,n,exact)
            rng=random.Random(2026+100*a+10*b+n)
            total=0.
            trials=6000
            for _ in range(trials):
                ts=[rng.random()*L for _ in range(n)]
                total+=shoelace(ts,a,b)
            empirical=total/trials
            assert abs(empirical-float(exact))<.008,(a,b,n,float(exact),empirical)
    for n in range(3,65):
        # Exact endpoint and strict positive coefficients of the sharp shape-order polynomial.
        k=n+2
        cs=[F(2*comb(k,2*j)*(3**(k-2*j)-1),4**k) for j in range(1,k//2+1)]
        assert cs[0]>0
        assert cs[1]>0
        assert sum(cs)==1-F(2*(3**k-1),4**k)
        for z in [F(0),F(1,4),F(1,2),F(3,4),F(1)]:
            numer=1-F((3+z)**k+(3-z)**k-(1+z)**k-(1-z)**k,4**k)
            assert numer==sum(c*(1-z**(2*j)) for j,c in enumerate(cs,1))
        if n==3:
            assert theoretical(1,1,n)==F(5,32)
            assert theoretical(1,2,n)==F(11,72)
    print('PASS: 36 deterministic cross-correlation quadratures; 24 direct Monte Carlo area tests; 62 exact polynomial positivity and identity checks; exact three-point anchors.')
if __name__=='__main__':run()
