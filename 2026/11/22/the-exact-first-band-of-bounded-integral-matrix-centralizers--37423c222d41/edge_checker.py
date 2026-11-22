#!/usr/bin/env python3
"""Integer-only diagnostics for an exact finite 2x2 commutant counting formula.

No external files, packages, network, or random seeds are required.
"""
from itertools import product
from math import gcd
from fractions import Fraction

def centralizer_formula(H, a, b, c, d):
    if b == c == 0 and a == d:
        return (2*H+1)**4
    g = gcd(gcd(abs(b),abs(c)), abs(a-d))
    N = max(2*abs(b),2*abs(c),abs(a-d))
    S = (2*g*H)//N
    return (2*H+1)*(2*S+1)-(abs(a-d)//g)*S*(S+1)

def centralizer_direct(H, a, b, c, d):
    count = 0
    R = range(-H,H+1)
    for x,y,z,w in product(R, repeat=4):
        if b*z == c*y and (a-d)*y + b*(w-x)==0 and (a-d)*z+c*(w-x)==0:
            count += 1
    return count

def threshold(H, z):
    # ceil(((6-z)*H+3)/2) in exact rational arithmetic
    t = (6-z)*H+3
    return (t.numerator + 2*t.denominator - 1)//(2*t.denominator)

def lower_band_formula(H,z):
    L = threshold(H,z)
    count=0
    for p in range(max(1,L),2*H+1):
        Q = sum(gcd(gcd(b,c),p)==1 for b in range(-H,H+1) for c in range(-H,H+1))
        count += 2*(2*H+1-p)*Q
    return count

def lower_band_fast(H,z):
    L = threshold(H,z)
    mu = [0] * (2*H+1)
    mu[1]=1
    # direct trial factors for small diagnostics
    for r in range(2,2*H+1):
        x=r; p=2; fac=[]; square=False
        while p*p<=x:
            if x%p==0:
                e=0
                while x%p==0:
                    x//=p; e+=1
                if e>=2: square=True
                fac.append(p)
            p+=1
        if x>1: fac.append(x)
        mu[r] = 0 if square else (-1)**len(fac)
    out=0
    for r in range(1,2*H+1):
        if mu[r]==0: continue
        B=2*(H//r)+1
        low=(L+r-1)//r; high=(2*H)//r
        if high<low:continue
        k=high-low+1
        total=2*(k*(2*H+1)-r*(low+high)*k//2)
        out+=mu[r]*B*B*total
    return out

def checks():
    matrix_comparisons=0
    for H in (1,2,3):
        for a,b,c,d in product(range(-H,H+1),repeat=4):
            x=centralizer_formula(H,a,b,c,d)
            y=centralizer_direct(H,a,b,c,d)
            assert x==y,(H,a,b,c,d,x,y)
            matrix_comparisons+=1
    event_comparisons=0
    for H in range(1,8):
        for z in map(Fraction,['2','5/2','3','7/2','4']):
            direct=sum(centralizer_formula(H,*A)*z.denominator <= z.numerator*H
                       for A in product(range(-H,H+1),repeat=4))
            band=lower_band_formula(H,z)
            fast=lower_band_fast(H,z)
            assert direct==band==fast,(H,z,direct,band,fast)
            event_comparisons+=1
    for H in (50,100,200):
        z=Fraction(3)
        total=lower_band_fast(H,z)
        print('ASYMPTOTIC_SAMPLE',H,total, '/', (2*H+1)**4)
    print('CENTRALIZER_EDGE_OK',matrix_comparisons,event_comparisons)
if __name__=='__main__':checks()
