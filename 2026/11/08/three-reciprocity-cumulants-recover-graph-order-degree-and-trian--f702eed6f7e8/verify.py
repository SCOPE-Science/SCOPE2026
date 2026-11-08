#!/usr/bin/env python3
"""Exact checks for reciprocal-neighbor counts on regular graphs."""
from collections import Counter
from fractions import Fraction
from itertools import product, combinations
from math import comb

checks = 0

def check(ok, why):
    global checks
    assert ok, why
    checks += 1

def add_edge(g, u, v):
    assert u != v
    g[u].add(v)
    g[v].add(u)

def cycle(n):
    g=[set() for _ in range(n)]
    for i in range(n):add_edge(g,i,(i+1)%n)
    return g

def clique(n):
    g=[set() for _ in range(n)]
    for i,j in combinations(range(n),2): add_edge(g,i,j)
    return g

def biclique(a,b):
    g=[set() for _ in range(a+b)]
    for i in range(a):
        for j in range(a,a+b):add_edge(g,i,j)
    return g

def prism():
    g=[set() for _ in range(6)]
    for i in range(3):
        add_edge(g,i,(i+1)%3)
        add_edge(g,i+3,(i+1)%3+3)
        add_edge(g,i,i+3)
    return g

def cube():
    g=[set() for _ in range(8)]
    for i in range(8):
        for j in range(3):add_edge(g,i,i^(1<<j)) if i < (i^(1<<j)) else None
    return g

def petersen():
    g=[set() for _ in range(10)]
    for i in range(5):
        add_edge(g,i,(i+1)%5)
        add_edge(g,i,i+5)
        add_edge(g,i+5,((i+2)%5)+5)
    return g

def disjoint(*graphs):
    N=sum(len(g) for g in graphs)
    r=[set() for _ in range(N)]; offset=0
    for g in graphs:
        for u in range(len(g)):
            for v in g[u]:
                if u<v:add_edge(r,u+offset,v+offset)
        offset+=len(g)
    return r

def invariants(g):
    n=len(g)
    d=len(g[0]); check(d>=1,'no isolates')
    check(all(len(x)==d for x in g),'not regular')
    edges=[(i,j) for i in range(n) for j in g[i] if i<j]
    tri=sum(1 for a,b,c in combinations(range(n),3) if b in g[a] and c in g[a] and c in g[b])
    return n,d,edges,tri

def expected_from_matchings(g):
    n,d,edges,t=invariants(g)
    ps=[Fraction(0) for _ in range(n//2+1)]
    for r in range(n//2+1):
        for seq in combinations(edges,r):
            ends=[v for e in seq for v in e]
            if len(set(ends))==2*r:ps[r]+=1
    # E[z^X]=sum_M ((z-1)/d^2)^|M|, compare coefficients.
    law=[Fraction(0) for _ in ps]
    for r,mr in enumerate(ps):
        for j in range(r+1):law[j]+=Fraction(mr*comb(r,j)*(-1)**(r-j),d**(2*r))
    check(sum(law)==1,'pgf normalization')
    check(all(z>=0 for z in law),'pgf positivity')
    return law,ps

def expected_from_choices(g):
    n,d,edges,t=invariants(g)
    counts=Counter()
    for picks in product(*(tuple(sorted(v)) for v in g)):
        reciprocals=sum(picks[i]==j and picks[j]==i for i,j in edges)
        counts[reciprocals]+=1
    total=d**n
    return [Fraction(counts[i],total) for i in range(n//2+1)]

def cumulants(p):
    mean=sum(i*pi for i,pi in enumerate(p))
    variance=sum((i-mean)**2*pi for i,pi in enumerate(p))
    third=sum((i-mean)**3*pi for i,pi in enumerate(p))
    return mean,variance,third

graphs=[('edge',clique(2)),('triangle',clique(3)),('cycle4',cycle(4)),
 ('cycle5',cycle(5)),('cycle6',cycle(6)),('cycle7',cycle(7)),('cycle8',cycle(8)),
 ('tetrahedron',clique(4)),('biclique3x3',biclique(3,3)),('prism',prism()),
 ('cube',cube()),('petersen',petersen()),('clique5',clique(5)),
 ('clique6',clique(6)),('two_triangles',disjoint(clique(3),clique(3))),
 ('two_tetrahedra',disjoint(clique(4),clique(4)))]
for name,g in graphs:
    n,d,edges,t=invariants(g)
    law,mcounts=expected_from_matchings(g)
    direct=expected_from_choices(g)
    for i,(u,v) in enumerate(zip(law,direct)):
        check(u==v,f'{name}: exact PMF at {i}: {u} vs {v}')
    mu,va,k3=cumulants(law)
    check(mu==Fraction(n,2*d),f'{name}: mean')
    check(va==Fraction(n*(d-1)**2,2*d**3),f'{name}: variance')
    check(k3==Fraction(n*(d-1)**2*(d-2)**2,2*d**5)-Fraction(6*t,d**6),f'{name}: kappa3')
    check(va/mu==Fraction((d-1)**2,d**2),f'{name}: ratio')
    if d==1:check(va==0 and t==0,f'{name}: degree1')
    if d==2:check(k3<=0,f'{name}: degree2')
    if d==3:check(k3>=0,f'{name}: degree3')
    if d>=4:check(k3>0,f'{name}: degree4+')
    # Reconstruction from exact moments, using variance/mean to identify integer d.
    candidate=[j for j in range(1,n+1) if Fraction((j-1)**2,j**2)==va/mu]
    check(candidate==[d],f'{name}: degree inverse')
    nrec=2*d*mu
    trec=Fraction(nrec*d*(d-1)**2*(d-2)**2,12)-Fraction(d**6,6)*k3
    check(nrec==n and trec==t,f'{name}: triangle inverse')
    print(name,'n',n,'d',d,'triangles',t,'mu',mu,'var',va,'k3',k3)
print('VERIFY_OK',checks,'exact rational assertions')
