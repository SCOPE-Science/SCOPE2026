#!/usr/bin/env python3
"""Exact checks of stochastic-order crossing for random vertex-greedy independent sets."""
from fractions import Fraction
from functools import lru_cache
from itertools import permutations

@lru_cache(None)
def law(n, edges, mask):
    if mask == 0:
        return (Fraction(1),)
    nn = mask.bit_count()
    p = [Fraction(0)] * (n + 1)
    for v in range(n):
        if not mask & (1 << v):
            continue
        keep = mask & ~(1 << v)
        for a,b in edges:
            if a == v: keep &= ~(1 << b)
            if b == v: keep &= ~(1 << a)
        for k,pr in enumerate(law(n, edges, keep)):
            p[k+1] += pr / nn
    while len(p)>1 and p[-1]==0: p.pop()
    return tuple(p)

def p(n,edges):
    return law(n,tuple(sorted(tuple(sorted(e)) for e in edges)),(1<<n)-1)

def tail(p,k):return sum(p[k:],Fraction(0))
def graph_edges(n,mask):
    poss=[(i,j) for i in range(n) for j in range(i+1,n)]
    return [e for i,e in enumerate(poss) if mask & (1<<i)]
def connected(n,edges):
    if n==1:return True
    seen={0}
    changed=True
    while changed:
        changed=False
        for a,b in edges:
            if a in seen and b not in seen:seen.add(b);changed=True
            if b in seen and a not in seen:seen.add(a);changed=True
    return len(seen)==n

def main():
    checks=0
    for n in range(1,4):
        for mask in range(1 << (n*(n-1)//2)):
            e=graph_edges(n,mask)
            if not connected(n,e):continue
            old=p(n,e)
            for root in range(n):
                new=p(n+1,e+[(root,n)])
                for k in range(n+2):
                    assert tail(new,k) >= tail(old,k), ('minimality',n,e,root,k,old,new)
                    checks+=1
    for m in range(3,9):
        edges=[(0,i) for i in range(1,m+1)]
        old=p(m+1,edges)
        new=p(m+2,edges+[(1,m+1)])
        expected_old={1:Fraction(1,m+1),m:Fraction(m,m+1)}
        expected_new={2:Fraction(m+1,m*(m+2)),m:1-Fraction(m+1,m*(m+2))}
        for j in range(m+2):
            assert (old[j] if j<len(old) else 0)==expected_old.get(j,0)
            assert (new[j] if j<len(new) else 0)==expected_new.get(j,0)
            checks+=2
        assert tail(new,2)>tail(old,2)
        assert tail(new,m)<tail(old,m)
        assert sum(j*x for j,x in enumerate(new))-sum(j*x for j,x in enumerate(old))==Fraction(m*m+m+2,m*(m+1)*(m+2))
        checks+=3
    print('VERIFY_OK',checks,'exact assertions')
if __name__=='__main__': main()
