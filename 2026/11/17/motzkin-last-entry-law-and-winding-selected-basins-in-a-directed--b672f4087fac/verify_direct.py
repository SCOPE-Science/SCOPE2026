#!/usr/bin/env python3
"""Independent vertex-level exhaustive test for a one-neighbour ternary cyclic automaton.
Run: python3 verify_direct.py"""
from itertools import product
from collections import Counter
from math import comb

def step(x):
    n = len(x)
    return tuple((x[i] + (x[(i+1)%n] == (x[i]+1)%3))%3 for i in range(n))

def signed_winding(x):
    d=[(x[(i+1)%len(x)]-x[i])%3 for i in range(len(x))]
    return d.count(1)-d.count(2)

def motzkin(n):
    m=[0]*(max(n,1)+1);m[0]=1
    for i in range(1,n+1):
        m[i]=m[i-1]+sum(m[j]*m[i-2-j] for j in range(i-1))
    return m[n]

def central(n):
    return sum(comb(n,j)*comb(n-j,j) for j in range(n//2+1))

for n in range(2,11):
    hist=Counter(); selected=Counter(); late=[]
    for x in product(range(3),repeat=n):
        wind=signed_winding(x)
        s=x; T=None
        for t in range(n):
            # Detect genuine periodicity by return to THIS state within n steps.
            z=step(s)
            on_cycle=(z==s)
            for p in range(2,n+1):
                if on_cycle: break
                z=step(z)
                if z==s: on_cycle=True
            if on_cycle:
                T=t
                break
            s=step(s)
        assert T is not None and T<n, (n,x)
        hist[T]+=1
        if T==n-1:late.append(x)
        # Compare periodic trajectory with fixed/rotating prediction
        y=x
        for _ in range(n-1):y=step(y)
        if wind>0:
            assert step(y)==y[1:]+y[:1] and step(y)!=y,(n,x,wind,y)
        else:
            assert step(y)==y,(n,x,wind,y)
        selected['rotate' if wind>0 else 'fixed']+=1
    assert len(late)==3*n*motzkin(n-2),(n,len(late))
    assert selected['rotate']==(3**n-3*central(n))//2
    assert selected['fixed']==(3**n+3*central(n))//2
    print(f'n={n} total={3**n} last_entry={len(late)} max_T={max(hist)} rotate={selected["rotate"]} fixed={selected["fixed"]} hist={dict(sorted(hist.items()))}')
print('PASS: independent vertex-orbit enumeration and all exact formulas')
