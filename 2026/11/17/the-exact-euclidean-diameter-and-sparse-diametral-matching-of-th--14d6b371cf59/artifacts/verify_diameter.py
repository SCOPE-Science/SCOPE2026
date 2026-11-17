#!/usr/bin/env python3
"""Finite, exact-integer cross-check of the harmonic-polytope diameter theorem.

The mathematical proof is independent of enumeration. Requires Python's standard library only.
"""
from itertools import permutations
from math import factorial
from random import Random

def vertices(n):
    ranks = list(permutations(range(1, n+1)))
    vertices = set()
    for p in ranks:
        for q in ranks:
            for k in range(n):
                if all(not(p[j] > p[k] and q[j] > q[k]) for j in range(n)):
                    vertices.add(tuple(p[t]+(t==k) for t in range(n)) + tuple(q[t]+(t==k) for t in range(n)))
    return sorted(vertices)

def sqdist(v,w):
    return sum((a-b)**2 for a,b in zip(v,w))

def formula(n):
    return 2*n*(n*n-1)//3 + 8*n-4

def witness(n):
    p=tuple(range(n,0,-1))
    q=p
    rev=tuple(n+1-x for x in p)
    a=tuple(p[t]+(t==0) for t in range(n))*2
    b=tuple(rev[t]+(t==n-1) for t in range(n))*2
    return a,b

def main():
    totals=[]
    for n in range(2,5):
        vs=vertices(n)
        target=formula(n)
        mx=-1
        ties=0
        endpoints=set()
        for i,v in enumerate(vs):
            for j in range(i+1,len(vs)):
                d=sqdist(v,vs[j])
                if d>mx:
                    mx=d
                    ties=0
                    endpoints.clear()
                if d==mx:
                    ties+=1
                    endpoints.update((i,j))
        expected=n*(n-1)*factorial(n-2)**2//2
        endpoint_expected=2*expected
        harmonic_count=factorial(n)**2*sum(1/k for k in range(1,n+1))
        assert len(vs)==round(harmonic_count),(n,len(vs))
        assert mx==target and ties==expected,(n,mx,target,ties,expected)
        assert len(endpoints)==endpoint_expected,(n,len(endpoints),endpoint_expected)
        totals.append((n,len(vs),ties,target))
    for n in range(2,101):
        a,b=witness(n)
        assert sqdist(a,b)==formula(n),(n,'witness mismatch')
    rng=Random(20191114)
    vs=vertices(5)
    assert len(vs)==32880
    limit=formula(5)
    for _ in range(120000):
        v=vs[rng.randrange(len(vs))]
        w=vs[rng.randrange(len(vs))]
        assert sqdist(v,w)<=limit
    print('HARMONIC_DIAMETER_PASS exhaustive='+str(totals)+' witnesses_n=2..100 random_pairs_n5=120000')
if __name__=='__main__':main()
