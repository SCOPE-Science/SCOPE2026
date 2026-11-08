#!/usr/bin/env python3
"""Finite exhaustive checks for the stated composition-window deletion law."""
from itertools import product, combinations
from collections import Counter
from math import comb
from fractions import Fraction

def B(x, q, ell):
    n=len(x)
    win=[tuple(sum(x[t]==a for t in range(i,i+ell)) for a in range(q)) for i in range(n-ell+1)]
    desc={tuple(win[:i]+win[i+1:]) for i in range(len(win))}
    return len(desc)

def forest(n,es):
    parent=list(range(n))
    def root(v):
        while parent[v]!=v: v=parent[v]
        return v
    for u,v in es:
        a,b=root(u),root(v)
        if a==b: return False
        parent[a]=b
    return True

def check():
    samples=0
    for q in (2,3,4):
        for n in range(1,9):
            if q**n>10000: break
            words=list(product(range(q),repeat=n))
            moments=[Counter() for _ in range(n)]
            vals=[]
            for x in words:
                b=tuple(B(x,q,ell) for ell in range(1,n+1))
                vals.append(b)
                for ell,v in enumerate(b): moments[ell][v]+=1
            N=len(words)
            for e in range(n):
                t=n-(e+1)
                for j in range(t+1):
                    target=comb(t,j)*(q-1)**j*q**(n-t)
                    assert moments[e][1+j]==target,(q,n,e,j,moments[e],target)
            for e in range(n):
                for k in range(e+1,n):
                    a=sum(v[e] for v in vals)
                    b=sum(v[k] for v in vals)
                    cross=sum(v[e]*v[k] for v in vals)
                    assert N*cross==a*b,(q,n,e,k)
            samples+=N
    # Every simple edge subset on four vertices, test the cycle-vs-forest criterion.
    n=4
    pairs=list(combinations(range(n),2))
    for q in (2,3):
        words=list(product(range(q),repeat=n))
        for mask in range(1<<len(pairs)):
            E=[pairs[i] for i in range(len(pairs)) if mask>>i&1]
            count=sum(all(x[u]==x[v] for u,v in E) for x in words)
            # If edge equality indicators were independent, all-equal joint event has prob q^-|E|.
            exactly_product=(count*q**len(E)==q**n)
            assert exactly_product==forest(n,E),(q,E)
    # Two read lengths are uncorrelated, not independent.
    x=list(product((0,1),repeat=3))
    assert sum(B(s,2,1)==2 for s in x)==4
    assert sum(B(s,2,2)==2 for s in x)==4
    assert sum(B(s,2,1)==2 and B(s,2,2)==2 for s in x)==4
    print('PASS exhaustive random-input laws, pairwise covariance, forest criterion; input samples',samples)
if __name__=='__main__':check()
