#!/usr/bin/env python3
"""Standalone finite check of reflected-generator fibers.

Requires Python 3 standard library only; bounded enumeration is a test, not a proof.
"""
from collections import defaultdict
from math import gcd, ceil


def semigroup(gens, cutoff=320):
    v=[False]*(cutoff+1)
    v[0]=True
    for n in range(1,cutoff+1):
        v[n]=any(n>=g and v[n-g] for g in gens)
    return v


def minimal_gens(v):
    return tuple(i for i in range(1,len(v)) if v[i] and not any(v[a] and v[i-a] for a in range(1,i)))


def fiber_data(v, m):
    if not v[m]:
        return None
    P={s for s in range(1,m) if v[m-s] and v[m+s]}
    A=set(minimal_gens(v))
    R={abs(m-a) for a in A if a!=m}
    if not R.issubset(P):
        return None
    return P, R


def check():
    total=0
    for m in range(1,13):
        fibers=defaultdict(list)
        for mask in range(1<<(m-1)):
            S={m}|{i+1 for i in range(m-1) if mask>>i&1}
            g=0
            for i in S:g=gcd(g,i)
            if g!=1:continue
            v=semigroup([m]+[m-s for s in S]+[m+s for s in S])
            signature=minimal_gens(v)
            fibers[signature].append(S)
        for gens,all_S in fibers.items():
            v=semigroup(gens)
            data=fiber_data(v,m)
            assert data is not None,(m,gens)
            P,R=data
            predicted=[{m}|R|{s for idx,s in enumerate(sorted(P-R)) if bit>>idx&1}
                       for bit in range(1<<len(P-R))]
            assert {frozenset(s) for s in predicted}=={frozenset(s) for s in all_S},(m,gens)
            total+=1
        print('m',m,'distinct semigroup targets',len(fibers),'primitive sets',sum(map(len,fibers.values())))
    for c in range(1,14):
        H=[False]+[n>=c for n in range(1,321)]
        for m in range(1,30):
            data=fiber_data(H,m)
            cutoff=(3*c-1+1)//2
            predicted=(0 if m<cutoff else (1 if m<=2*c else (1<<(m-2*c))))
            actual=(0 if data is None else 1<<len(data[0]-data[1]))
            assert actual==predicted,(c,m,actual,predicted)
    print('FIXED_MAX_JUMP_FIBERS_OK',total,'distinct observed target pairs; ordinary c=1..13,m=1..29')

if __name__=='__main__':check()
