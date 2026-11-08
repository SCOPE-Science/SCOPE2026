#!/usr/bin/env python3
"""Reproducible finite-field Heisenberg walk checks (science only)."""
from collections import defaultdict
from fractions import Fraction
from math import comb

def field(q):
    if q==4:
        add=lambda a,b:a^b
        neg=lambda a:a
        def mul(a,b):
            w=0
            for j in range(2):
                if (b>>j)&1:w^=a<<j
            for j in (2,):
                if (w>>j)&1:w^=0b111<<(j-2)
            return w
    else:
        assert q in (2,3,5,7)
        add=lambda a,b:(a+b)%q
        neg=lambda a:(-a)%q
        mul=lambda a,b:(a*b)%q
    return add,mul,neg

def evolve(q,m,steps):
    from itertools import product
    add,mul,_=field(q); vs=list(product(range(q),repeat=m));zero=(0,)*m
    def vadd(a,b):return tuple(add(x,y) for x,y in zip(a,b))
    def dot(a,b):
        s=0
        for x,y in zip(a,b):s=add(s,mul(x,y))
        return s
    C={(zero,zero,0):1};Q=q**m;G=q*Q**2
    for t in range(1,steps+1):
        N=defaultdict(int)
        for (x,y,z),n in C.items():
            for v in vs:
                N[(vadd(x,v),y,z)]+=n
                N[(x,vadd(y,v),add(z,dot(x,v)))]+=n
        C=N
        total=(2*Q)**t
        assert sum(C.values())==total
        tv=sum(abs(Fraction(k,total)-Fraction(1,G)) for k in C.values())
        tv+=(G-len(C))*Fraction(1,G)
        tv/=2
        chi=sum((Fraction(k*G,total)-1)**2 for k in C.values())
        chi+=(G-len(C))
        chi/=G
        lp=Fraction(2*(Q-1),4**t)
        # exact rational power eigenvalue moments using paired conjugates
        c=Fraction(1,Q)
        # ((1+1/sqrtQ)/2)^(2t)+((1-1/sqrtQ)/2)^(2t)
        moment=Fraction(2,4**t)*sum(comb(2*t,2*j)*c**j for j in range(t+1))
        expected=lp+(q-1)*Q*moment
        assert chi==expected,(q,m,t,chi,expected)
        # all three-run and longer contributions bounded in TV by (1-1/q)/Q
        alpha=Fraction(t,2**(t-1)) if t>=1 else 1
        assert tv<=alpha+Fraction(q-1,q*Q)
        if t>=2:
            # support low-run has at most 2 Q^2 +2Q group elements
            assert tv>=alpha-Fraction(2,q)-Fraction(2,q*Q)
        print(f'q={q} m={m} t={t} states={len(C)}/{G} TV={float(tv):.8f} chi2={float(chi):.8f} upper={float(alpha+Fraction(q-1,q*Q)):.8f}')
for q,m,T in [(2,1,6),(3,1,6),(4,1,6),(5,1,6),(7,1,5),(2,2,5),(3,2,3),(2,3,4)]:
    evolve(q,m,T)
print('HEISENBERG_LAGRANGIAN_WALK_EXACT_CHECKS_PASS')
