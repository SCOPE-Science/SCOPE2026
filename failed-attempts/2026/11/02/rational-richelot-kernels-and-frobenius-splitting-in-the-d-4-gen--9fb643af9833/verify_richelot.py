#!/usr/bin/env python3
"""Exact finite-field spot checks of D4-family Frobenius matchings, stdlib only."""
from itertools import combinations
from math import gcd

def prime(p):
    return all(p%d for d in range(2,int(p**.5)+1))

def check(p):
    d=next(x for x in range(2,p) if pow(x,(p-1)//2,p)==p-1)
    # Represent GF(p^2) as a+b*z, z^2=d.
    def mul(x,y):
        a,b=x; c,e=y
        return ((a*c+d*b*e)%p,(a*e+b*c)%p)
    def power(x,n):
        z=(1,0)
        while n:
            if n&1:z=mul(z,x)
            x=mul(x,x); n>>=1
        return z
    def add(x,y):return ((x[0]+y[0])%p,(x[1]+y[1])%p)
    def neg(x):return ((-x[0])%p,(-x[1])%p)
    elems=[(a,b) for a in range(p) for b in range(p)]
    one=(1,0)
    all_matchings=[]
    def match(t,partials=()):
        if not t:
            all_matchings.append(frozenset(partials)); return
        i=t[0]
        for j in t[1:]:match(tuple(k for k in t if k not in (i,j)),partials+(frozenset((i,j)),))
    match(tuple(range(6)))
    assert len(all_matchings)==15
    freq={}; count=0
    for s in range(p):
        if s in (2%p,(-2)%p):continue
        s0=(s,0)
        def evaluate(x):
            x2=power(x,2); x4=power(x,4)
            return add(add(x4,mul(s0,x2)),one)
        r1=[x for x in elems if add(power(x,2),one)==(0,0)]
        r2=[x for x in elems if evaluate(x)==(0,0)]
        assert len(r1)==2 and len(r2)==4 and len(set(r1+r2))==6,(p,s,r1,r2)
        roots=r1+r2
        perm=tuple(roots.index(power(x,p)) for x in roots)
        assert sorted(perm)==list(range(6))
        cycles=[]; seen=set()
        for i in range(6):
            if i in seen:continue
            c=[]; j=i
            while j not in seen:
                c.append(j);seen.add(j);j=perm[j]
            cycles.append(len(c))
        cyc=tuple(sorted(cycles))
        def mapped_pair(pair):return frozenset(perm[i] for i in pair)
        rational_match=sum(frozenset(mapped_pair(z) for z in m)==m for m in all_matchings)
        # Even subsets modulo complementation, count fixed 2-torsion.
        invariant=0
        for mask in range(64):
            if mask.bit_count()%2:continue
            im=sum(1<<perm[i] for i in range(6) if mask>>i&1)
            if im in (mask,63^mask):invariant+=1
        torsion=invariant//2
        theory={(1,1,1,1,1,1):(16,15), (1,1,1,1,2):(8,3), (1,1,2,2):(4,3), (2,2,2):(4,7)}
        assert (torsion,rational_match)==theory[cyc],(p,s,cyc,torsion,rational_match)
        assert all(perm[perm[i]]==i for i in range(6))
        freq[cyc]=freq.get(cyc,0)+1;count+=1
    expected_A=(p-1-gcd(p-1,4))//4
    if p%4==1:
        want={(1,1,1,1,1,1):expected_A,(1,1,2,2):p-2-expected_A}
    else:
        want={(1,1,1,1,2):expected_A,(2,2,2):p-2-expected_A}
    want={k:v for k,v in want.items() if v}
    assert count==p-2 and freq==want,(p,freq,want)
    print('PASS',p,'cases',count,'patterns',freq)

if __name__=='__main__':
    for p in [3,5,7,11,13,17,19,23,29,31]:
        assert prime(p); check(p)
    print('D4_RICHELOT_FROBENIUS_FREQUENCIES_PASS')
