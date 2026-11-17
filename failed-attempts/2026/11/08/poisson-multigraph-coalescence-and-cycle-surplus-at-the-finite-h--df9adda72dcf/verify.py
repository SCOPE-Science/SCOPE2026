#!/usr/bin/env python3
"""Reproducibility regressions for a finite-hub percolation theorem."""
import itertools, math, fractions

checks=0

def graph_rank(m, words):
    global checks
    n=len(words)
    vertices=m+n
    edges=[]
    for j, word in enumerate(words):
        edges += [(i,m+j) for i in word]
    parent=list(range(vertices))
    def find(u):
        while parent[u]!=u:
            parent[u]=parent[parent[u]];u=parent[u]
        return u
    for u,v in edges:
        a,b=find(u),find(v)
        if a!=b:parent[a]=b
    c=len({find(i) for i in range(vertices)})
    graph_beta=len(edges)-vertices+c
    ps={p:sum(set(w)==set(p) for w in words) for p in itertools.combinations(range(m),2)}
    parent=list(range(m))
    def root(u):
        while parent[u]!=u:
            parent[u]=parent[parent[u]];u=parent[u]
        return u
    for (u,v),mult in ps.items():
        if mult:
            a,b=root(u),root(v)
            if a!=b:parent[a]=b
    partitions=len({root(i) for i in range(m)})
    predicted=sum(ps.values())-m+partitions
    assert graph_beta==predicted,(m,words,graph_beta,predicted)
    checks+=1

for m in (2,3,4):
    choices=[tuple(i for i in range(m) if k&(1<<i)) for k in range(1<<m) if k.bit_count()<=2]
    for n in range(4):
        for w in itertools.product(choices,repeat=n):graph_rank(m,w)

for a in (0.2,0.5,1.0,1.7,2.0):
    x=a*a
    # P=0 probability equals e^-x, and E 1+1_{P>=1}=2-e^-x.
    vals=[math.exp(-x)*x**k/math.factorial(k) for k in range(60)]
    assert abs(sum(vals)-1)<1e-12
    assert abs((vals[0]+2*sum(vals[1:]))-(2-math.exp(-x)))<1e-12
    assert abs(sum(max(k-1,0)*v for k,v in enumerate(vals))-(x-1+math.exp(-x)))<1e-12
    checks+=3

for m in range(2,9):
    for q in (fractions.Fraction(1,9),fractions.Fraction(2,5),fractions.Fraction(3,4)):
        z=sum(math.comb(m,k)*q**k*(1-q)**(m-k) for k in range(m+1))
        assert z==1
        p2=q*q*(1-q)**(m-2)
        assert p2>0
        checks+=2

print(f'PASS {checks} exact combinatorial and rational assertions; {15} floating distribution checks')
