#!/usr/bin/env python3
"""Independent exact finite checks of a split-graph spanning-tree defect law."""
from itertools import combinations
from collections import Counter
from math import comb, factorial, prod, isclose
from fractions import Fraction
import sympy as sp

def analyze(a,b):
    n=a+b
    edges=[(i,j) for i in range(a) for j in range(i+1,a)] + [(i,j) for i in range(a) for j in range(a,n)]
    hist=Counter(); good=0; count=0
    for subset in combinations(edges,n-1):
        par=list(range(n))
        def root(x):
            while par[x]!=x: x=par[x]
            return x
        degrees=[0]*n; k=0; okay=True
        for idx in subset:
            u,v=idx
            ru,rv=root(u),root(v)
            if ru==rv:
                okay=False;break
            par[ru]=rv
            degrees[u]+=1;degrees[v]+=1
            if u<a and v<a:k+=1
        if not okay:continue
        count+=1
        sur=tuple(d-1 for d in degrees[a:])
        hist[(k,)+sur]+=1
        if k==0 and all(d<=2 for d in degrees[a:]):good+=1
    exact=a**(b-1)*(a+b)**(a-1)
    assert count==exact,(a,b,count,exact)
    for key,freq in hist.items():
        k=key[0];s=key[1:]
        assert k+sum(s)==a-1
        target=Fraction(factorial(a-1),factorial(k)*prod(factorial(x) for x in s))*a**k*a**(b-1)
        assert freq==target,(a,b,key,freq,target)
    for k in range(a):
        for s in __import__('itertools').product(range(a),repeat=b):
            if k+sum(s)!=a-1:continue
            target=Fraction(factorial(a-1),factorial(k)*prod(factorial(x) for x in s))*a**k*a**(b-1)
            assert hist[(k,)+s]==target,(a,b,k,s)
    falling=prod(b-i for i in range(a-1)) if b>=a-1 else 0
    assert good==a**(b-1)*falling,(a,b,good,falling)
    return count, good,len(hist)

def determinant(a,b):
    t=sp.Symbol('t'); ys=sp.symbols(f'y0:{b}')
    n=a+b
    mat=sp.zeros(n,n)
    for i in range(a):
        for j in range(i+1,a):
            mat[i,i]+=t;mat[j,j]+=t;mat[i,j]-=t;mat[j,i]-=t
    for i in range(a):
        for j in range(b):
            w=ys[j];v=a+j
            mat[i,i]+=w;mat[v,v]+=w;mat[i,v]-=w;mat[v,i]-=w
    co=mat[1:,1:].det(method='berkowitz')
    want=a**(b-1)*sp.prod(ys)*(a*t+sum(ys))**(a-1)
    assert sp.expand(co-want)==0,(a,b,co,want)



def cayley_pair_distance(a):
    # Direct enumeration over Prüfer sequences, independent of forest formula.
    from itertools import product
    from collections import Counter
    from heapq import heapify, heappop, heappush
    hist=Counter()
    for code in product(range(a),repeat=a-2):
        degree=[1]*a
        for u in code:degree[u]+=1
        leaves=[u for u in range(a) if degree[u]==1]
        heapify(leaves)
        adj=[[] for _ in range(a)]
        for u in code:
            v=heappop(leaves)
            adj[u].append(v);adj[v].append(u)
            degree[v]-=1;degree[u]-=1
            if degree[u]==1:heappush(leaves,u)
        u,v=leaves
        adj[u].append(v);adj[v].append(u)
        seen={0}; layer=[0];dist=0
        while 1 not in seen:
            layer=[w for z in layer for w in adj[z] if w not in seen]
            seen.update(layer);dist+=1
        hist[dist]+=1
    for dist in range(1,a):
        predicted=(dist+1)*prod(range(a-dist,a-1))*a**(a-dist-2)
        assert hist[dist]==predicted,(a,dist,hist[dist],predicted)
    assert sum(hist.values())==a**(a-2)
    return len(hist)

if __name__=='__main__':
    cases=[]
    for a in range(2,5):
      for b in range(1,4):
        cases.append((a,b,*analyze(a,b)))
        determinant(a,b)
    for a in range(2,8):
        cayley_pair_distance(a)
    print('VERIFY_OK exact tree enumeration, multivariate determinants, and pair-distance laws:')
    for a,b,total,good,patterns in cases:
        print(f'  a={a} b={b} spanning_trees={total} favorable={good} multinomial_patterns={patterns}')
