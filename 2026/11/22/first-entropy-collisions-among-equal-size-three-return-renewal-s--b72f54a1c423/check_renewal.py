#!/usr/bin/env python3
"""Exact complete small-order collision check for three-return edge shifts.
Only Python's standard library is required. Polynomial calculations use Q[X].
"""
from fractions import Fraction as Q
from itertools import combinations
from math import comb

def trim(p):
    while len(p)>1 and p[-1]==0:p.pop()
    return p

def poly(t):
    a,b,c=t; p=[Q(0)]*(c+1);p[c]+=1
    for k in (a,b,c):p[c-k]-=1
    return trim(p)

def divmod_q(a,b):
    a=trim(a[:]); b=trim(b[:]);q=[Q(0)]*max(1,len(a)-len(b)+1)
    while a!=[0] and len(a)>=len(b):
        k=len(a)-len(b);v=a[-1]/b[-1];q[k]=v
        for j,c in enumerate(b):a[k+j]-=v*c
        trim(a)
    return trim(q),a

def monic(p):
    p=trim(p[:]);return [v/p[-1] for v in p]

def gcd_q(p,q):
    while q!=[0]:p,q=q,divmod_q(p,q)[1]
    return monic(p)

def derivative(p):return trim([Q(j)*p[j] for j in range(1,len(p))] or [Q(0)])

def variations(signs):
    signs=[v for v in signs if v];return sum(a*b<0 for a,b in zip(signs,signs[1:]))

def roots_greater_than_one(p):
    if len(p)<=1:return 0
    chain=[p,derivative(p)]
    while chain[-1]!=[0]:
        r=divmod_q(chain[-2],chain[-1])[1]
        if r==[0]:break
        chain.append([-v for v in r])
    at_one=[sum(p) for p in chain]
    at_infinity=[p[-1] for p in chain]
    return variations(at_one)-variations(at_infinity)

def triples(s,allow_loop=True):
    ans=[]
    for a in range(1 if allow_loop else 2,s//3+1):
        for b in range(a,(s-a)//2+1):
            c=s-a-b
            if (a,b)==(1,1):continue # duplicate hub-to-hub edge
            if c>=b:ans.append((a,b,c))
    return ans

def collisions(max_s,allow_loop):
    out=[]; counts=[]; compared=0
    for s in range(3,max_s+1):
        tri=triples(s,allow_loop);counts.append((s,len(tri)))
        for t,u in combinations(tri,2):
            compared+=1;d=gcd_q(poly(t),poly(u))
            if roots_greater_than_one(d):out.append((s,t,u))
    return out,counts,compared

if __name__=='__main__':
    for allow,cut in ((True,11),(False,13)):
        hits,counts,pairs=collisions(cut,allow)
        print(('loops_allowed' if allow else 'loopless'), 'vertex_max',cut-2, 'tested_pairs',pairs,'collisions',hits)
        assert hits == ([(11,(1,4,6),(2,2,7))] if allow else [(13,(2,5,6),(3,3,7))])
        assert all(len(triples(s,allow))==n for s,n in counts)
    # Correct algebraic relations: first X^3-X^2-1, second X^3-X-1.
    for pair,f in [(((1,4,6),(2,2,7)),[-1,0,-1,1]),(((2,5,6),(3,3,7)),[-1,-1,0,1])]:
        for t in pair:assert divmod_q(poly(t),[Q(k) for k in f])[1]==[0],(t,f)
    print('verified exact common cubic divisors and sharp initial collisions')
