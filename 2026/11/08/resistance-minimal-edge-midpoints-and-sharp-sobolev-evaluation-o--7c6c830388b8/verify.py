#!/usr/bin/env python3
"""Exact rational checks of metric-graph evaluation norms.
The direct solver inserts observation vertices and solves the continuum Poisson equation,
not the vertex-transitive closed formula. Requires only Python standard library.
"""
from fractions import Fraction as Q
from math import comb

def solve(a,b):
    n=len(b); a=[[Q(x) for x in row]+[Q(b[i])] for i,row in enumerate(a)]
    for j in range(n):
        pivot=next((i for i in range(j,n) if a[i][j]),None)
        assert pivot is not None,(n,j)
        a[j],a[pivot]=a[pivot],a[j];p=a[j][j]
        for k in range(j,n+1):a[j][k]/=p
        for i in range(n):
            if i==j: continue
            p=a[i][j]
            if p:
                for k in range(j,n+1): a[i][k]-=p*a[j][k]
    return [a[i][-1] for i in range(n)]

def grounded_potential(n,edges,load):
    l=[[Q(0) for j in range(n)] for i in range(n)]
    for u,v,w in edges:
        w=Q(1)/w
        l[u][u]+=w;l[v][v]+=w;l[u][v]-=w;l[v][u]-=w
    assert sum(load)==0
    sol=solve([row[1:] for row in l[1:]],load[1:]);return [Q(0)]+sol

def direct(g,point,t):
    n=1+max(max(u,v) for u,v in g);e=list(g)
    if t == 0: idx=e[point][0]; segs=[(u,v,Q(1)) for u,v in e]
    elif t == 1: idx=e[point][1]; segs=[(u,v,Q(1)) for u,v in e]
    else:
        idx=n;n+=1;segs=[]
        for i,(u,v) in enumerate(e):
            if i == point: segs.extend([(u,idx,Q(t)),(idx,v,1-Q(t))])
            else: segs.append((u,v,Q(1)))
    T=sum((l for _,_,l in segs),Q(0)); b=[Q(0) for _ in range(n)]
    for u,v,l in segs: b[u]-=l/(2*T);b[v]-=l/(2*T)
    b[idx]+=1
    x=grounded_potential(n,segs,b)
    integral=sum((l*(x[u]+x[v])/2-l**3/(12*T) for u,v,l in segs),Q(0))
    val=x[idx]-integral/T
    assert val>0
    return val

def spectral(g):
    n=1+max(max(u,v) for u,v in g);segs=[(u,v,Q(1)) for u,v in g]
    # resistance on each edge, and Kf via all vertex-pair resistances;
    # grounded solves unit dipoles: independent of the continuum solver
    def r(u,v):
        b=[Q(0)]*n;b[u]=1;b[v]=-1
        p=grounded_potential(n,segs,b);return p[u]-p[v]
    kf=sum((r(u,v) for u in range(n) for v in range(u+1,n)),Q(0))
    rs=[r(u,v) for u,v in g]
    m=len(g)
    assert m*2 % n==0
    d=2*m//n
    assert all(sum(1 for e in g if v in e)==d for v in range(n))
    coeffs=[1-Q(1,m)-R for R in rs]
    return Q(kf,n*n)+Q(1,12*m)+max(Q(0),max(coeffs))/4,rs,kf,coeffs

def cycle(n,steps):
    return sorted({tuple(sorted((i,(i+s)%n))) for i in range(n) for s in steps})
def hyper(n):
    return [(i,i^(1<<k)) for i in range(1<<n) for k in range(n) if not (i>>k)&1]
def complete(n):return [(u,v) for u in range(n) for v in range(u+1,n)]
def prism(n):
    edges=set()
    for j in range(2):
        for i in range(n): edges.add(tuple(sorted((j*n+i,j*n+(i+1)%n))))
    for i in range(n): edges.add((i,n+i))
    return sorted(edges)

cases=[('cycle5',cycle(5,[1])),('K5',complete(5)),('cubicalQ3',hyper(3)),('cubicalQ4',hyper(4)),('circulantC7-1-2',cycle(7,[1,2])),('circulantC8-1-2',cycle(8,[1,2])),('triangular_prism',prism(3)),('pentagonal_prism',prism(5))]
checks=0
for name,g in cases:
    K,rs,kf,cs=spectral(g)
    v=direct(g,0,Q(0));m=len(g);n=max(max(u,w) for u,w in g)+1
    assert v==Q(kf,n*n)+Q(1,12*m)
    for i in range(len(g)):
        for t in [Q(0),Q(1,4),Q(1,2),Q(3,4),Q(1)]:
            actual=direct(g,i,t)
            pred=v+cs[i]*t*(1-t)
            assert actual==pred,(name,i,t,actual,pred)
            assert actual<=K
            checks+=1
    assert max(direct(g,i,Q(1,2)) for i in range(len(g)))==K or all(c<=0 for c in cs)
    print(name,'vertices',n,'edges',m,'K',K,'Kf',kf,'adjacent_resistances',sorted(set(rs)))
assert checks>200
print('DIRECT_CONTINUUM_POISSON_VS_SPECTRAL_FORMULA_PASSED',checks)
for n in range(1,14):
    g=hyper(n) if n<=4 else None
    A=sum((Q(comb(n,k),2*k) for k in range(1,n+1)),Q(0))/(1<<n)
    K=A+Q(1,6*n*(1<<n))+(Q(1,4)-Q(1,2*n) if n>=2 else Q(0))
    if n<=4:
        k,_,_,_=spectral(g);assert k==K,(n,k,K)
    if n==4: assert K==Q(19,48)
    if n==3: assert K==Q(113,288)
    if n>=4:
        assert A>Q(1,n)
        A_next=(A+Q(1,n+1)-Q(1,(n+1)*(1<<(n+1))))/2
        Knext=A_next+Q(1,6*(n+1)*(1<<(n+1)))+Q(1,4)-Q(1,2*(n+1))
        assert Knext<K
print('HYPERCUBE_EXACT_MAXIMUM_AND_MONOTONICITY_PASSED')
