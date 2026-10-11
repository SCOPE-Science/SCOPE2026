#!/usr/bin/env python3
"""Finite regression checks for the mod-p transvection-orbit lemma."""
from collections import deque

def pairing(x,v,p):
    g=len(x)//2
    return sum(x[i]*v[g+i]-x[g+i]*v[i] for i in range(g))%p

def vectors(g,p):
    n=2*g
    for m in range(1,p**n):
        z=m; c=[]
        for _ in range(n):
            c.append(z%p); z//=p
        yield tuple(c)

def orbit_size(g,p):
    V=list(vectors(g,p))
    start=(1,)+(0,)*(2*g-1)
    seen={start}; q=deque([start])
    # Squared twists give transvection coefficients 2k. For odd p these run
    # through every nonzero field coefficient as k runs through 1,...,p-1.
    coeffs=[(2*k)%p for k in range(1,p)]
    while q and len(seen)<len(V):
        x=q.popleft()
        for v in V:
            s=pairing(x,v,p)
            if not s:
                continue
            for c in coeffs:
                a=c*s%p
                y=tuple((x[i]+a*v[i])%p for i in range(2*g))
                if y not in seen:
                    seen.add(y); q.append(y)
    return len(seen),len(V)

rows=[]
for g,p in ((2,3),(2,5),(3,3)):
    got,want=orbit_size(g,p)
    assert got==want==p**(2*g)-1
    assert want%2==0
    rows.append((g,p,got,want//2))
print('VERIFY_OK '+' '.join(
    f'g{g}_p{p}={got}/{p**(2*g)-1},pairs={pairs}'
    for g,p,got,pairs in rows
))
