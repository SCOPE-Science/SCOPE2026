#!/usr/bin/env python3
"""Brute-force direct multiplication test in the six-dimensional first Takiff algebra, q=3."""
from itertools import product
from collections import Counter
q=3
vectors=list(product(range(q),repeat=3))
lie=[(u,v) for u in vectors for v in vectors]
def sl2(u,v):
    a,b,c=u; d,e,f=v
    return ((2*(c*d-a*f))%q,(2*(b*f-c*e))%q,(a*e-b*d)%q)
def bracket(X,Y):
    a,b=X; c,d=Y
    top=sl2(a,c)
    u=sl2(a,d); v=sl2(b,c)
    return (top,tuple((x+y)%q for x,y in zip(u,v)))
counts=Counter(bracket(X,Y) for X in lie for Y in lie)
assert len(counts)==len(lie)
for (Z,W),n in counts.items():
    expected=(q**4*(q*q-1) if any(Z) else
       q**4*(q*q-1)*(q+1) if any(W) else
       q**4*(q*q-1)*(q*q+q+1)+q**6)
    assert n==expected,(Z,W,n,expected)
assert sum(counts.values())==q**12
print('DIRECT_MULTIPLICATION_COMMUTATOR_FIBERS_PASS',q,'targets',len(counts),'ordered_pairs',sum(counts.values()))
