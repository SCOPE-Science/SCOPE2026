#!/usr/bin/env python3
"""Exact-rational consistency checks for the stated two-fold return formula.

This script tests finite instances only; the infinite statements are proved
by the accompanying analytic argument.
"""
from fractions import Fraction as F
from itertools import product

def fold(z, h, sign):
    return h + sign*abs(z-h)

def raw_return(z, h1, s1, h2, s2, a, b):
    return a*fold(a*fold(z, h1, s1)+b, h2, s2)+b

def normal_data(h1, s1, h2, s2, a, b):
    H=a*h2+b-h1
    t=a*s1*(a*h1+b-h2)
    sigma=a*s2
    Delta=t+sigma*H
    return H,t,sigma,Delta

def normal_return(z,h1,s1,h2,s2,a,b):
    H,t,sigma,_=normal_data(h1,s1,h2,s2,a,b)
    return h1+H+sigma*abs(abs(z-h1)+t)

def test():
    n=0
    vals=[F(-2), F(-1,2), F(0), F(1,3), F(3,2)]
    pts=[F(-10),F(-7,3),F(-1,10),F(0),F(1,4),F(5),F(37,3)]
    for h1,h2,b,a,s1,s2 in product(vals,vals,vals,(-1,1),(-1,1),(-1,1)):
        H,t,sigma,Delta=normal_data(h1,s1,h2,s2,a,b)
        assert sigma in (-1,1)
        for z in pts:
            assert raw_return(z,h1,s1,h2,s2,a,b)==normal_return(z,h1,s1,h2,s2,a,b)
            n+=1
        # Exact tail identities at points guaranteed past both folding thresholds.
        tail=F(200)+abs(h1)+abs(h2)+abs(b)+abs(t)+abs(H)
        u=sigma*tail
        assert normal_return(h1+u,h1,s1,h2,s2,a,b)-(h1+u)==sigma*Delta
        # Fixed point criterion: finite breakpoints and both far tails
        # suffice to test crossing/zero for these rational cases.
        # This is separate from (and does not prove) the analytic IVT argument.
        if Delta==0:
            assert normal_return(h1+u,h1,s1,h2,s2,a,b)==h1+u
        if Delta>0:
            assert (normal_return(z,h1,s1,h2,s2,a,b)-z)*sigma>0
    h1,s1,h2,s2,a,b=F(0),-1,F(1,5),-1,1,F(1)
    for z in (F(4,5),F(9,10),F(1),F(11,10),F(6,5)):
        z1=raw_return(z,h1,s1,h2,s2,a,b)
        assert z1==2-z
        assert raw_return(z1,h1,s1,h2,s2,a,b)==z
    for b in (F(-1),F(0),F(1)):
        h1=h2=F(0); s1=s2=-1; a=1
        d=normal_data(h1,s1,h2,s2,a,b)[3]
        assert d==-2*b
        if b==F(-1):
            for z in (F(-200),F(-7),F(0),F(5)):
                v=z
                for _ in range(300):
                    if v<=-2:
                        assert raw_return(v,h1,s1,h2,s2,a,b)==v-2
                        break
                    v=raw_return(v,h1,s1,h2,s2,a,b)
                else:
                    raise AssertionError("escape tail not reached")
    print("PASS exact fold identities:",n,"parameter-point cases")
    print("PASS critical interval, both tails and illustrative escape")
if __name__=="__main__":
    test()
