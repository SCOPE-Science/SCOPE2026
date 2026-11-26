#!/usr/bin/env python3
"""Independent exhaustive forcing simulation versus a bipartite-tree species enumerator."""
from collections import Counter
from functools import lru_cache
from itertools import combinations
from math import comb, factorial

def qcount(size, length, leafweight):
    return sum(comb(size,j) * (leafweight-1)**j * (size-j)**length for j in range(size+1))

def egf_forest_polynomial(m,n,alpha,beta,p,q):
    # Equivalent to m!n![u^m v^n] exp(alpha*u+beta*v+sum weighted connected bipartite trees).
    N=m+n; full=(1<<N)-1
    @lru_cache(None)
    def f(mask):
        if not mask: return {0:1}
        low=mask & -mask
        rest=mask^low
        output=Counter()
        sub=rest
        while True:
            component=sub|low
            a=(component & ((1<<m)-1)).bit_count()
            b=component.bit_count()-a
            if a+b==1:
                weight=alpha if a else beta; degree=0
            elif a and b:
                degree=a+b-1
                weight=qcount(a,b-1,p)*qcount(b,a-1,q)
            else:
                weight=0; degree=0
            if weight:
                for power,v in f(mask^component).items():
                    output[power+degree] += weight*v
            if sub==0: break
            sub=(sub-1)&rest
        return dict(output)
    return f(full)

def accepted_formula(m,n):
    polys=[
        (1,1,1,1,1), # (coefficient, alpha,beta,leaf A,leaf B)
        (-1,1,0,1,0),
        (-1,0,1,0,1),
        (1,0,0,1,0),
        (1,0,0,0,1),
        (-1,0,0,1,1)
    ]
    out=Counter()
    for coefficient,alpha,beta,p,q in polys:
        for k,count in egf_forest_polynomial(m,n,alpha,beta,p,q).items():
            out[k]+=coefficient*count
    return {k:v for k,v in out.items() if v}

def isforest(m,n,white):
    N=m+n; parent=list(range(N))
    def find(i):
        while parent[i]!=i:
            parent[i]=parent[parent[i]]; i=parent[i]
        return i
    for k in white:
        i,j=divmod(k,n); j+=m
        ri,rj=find(i),find(j)
        if ri==rj: return False
        parent[ri]=rj
    return True

def predicted(m,n,white):
    if not isforest(m,n,white): return False
    A=[0]*m;B=[0]*n
    for k in white:
        i,j=divmod(k,n);A[i]+=1;B[j]+=1
    return (0 in A and (0 in B or 1 in B)) or (0 in B and (0 in A or 1 in A))

def forcing(m,n,white):
    N=m*n
    # Use white-bit set. A black edge can force iff exactly one adjacent white rook square.
    w=sum(1<<k for k in white)
    neighbors=[]
    for k in range(N):
        i,j=divmod(k,n)
        neighbors.append(sum(1<<t for t in range(N) if t!=k and (t//n==i or t%n==j)))
    while w:
        neww=w
        for k in range(N):
            if not (w>>k)&1:
                adjacent=w & neighbors[k]
                if adjacent and adjacent&(adjacent-1)==0:
                    neww &= ~adjacent
        if neww==w: return False
        w=neww
    return True

def stirling(n,k):
    if n<0 or k<0:return 0
    s=[[0]*(k+1) for _ in range(n+1)];s[0][0]=1
    for i in range(1,n+1):
        for j in range(1,k+1):s[i][j]=s[i-1][j-1]+j*s[i-1][j]
    return s[n][k]

def min_formula(m,n):
    return (m*(m-1)**(n-1)*(n**(m-2)-factorial(n)*stirling(m-2,n))+
            n*(n-1)**(m-1)*(m**(n-2)-factorial(m)*stirling(n-2,m)))

count=0
for m,n in [(2,2),(2,3),(2,4),(2,5),(3,3),(3,4),(3,5),(4,4)]:
    direct=Counter(); checks=0
    for mask in range(1<<(m*n)):
        white=[k for k in range(m*n) if (mask>>k)&1]
        true=forcing(m,n,white)
        exp=predicted(m,n,white)
        if true!=exp: raise AssertionError((m,n,mask,'criterion',true,exp))
        if true:direct[len(white)]+=1
        checks+=1
    model=accepted_formula(m,n)
    if direct!=model: raise AssertionError((m,n,'polynomial',direct,model))
    largest=max(direct)
    if largest!=m+n-2: raise AssertionError((m,n,'largest',largest))
    if direct[largest]!=min_formula(m,n): raise AssertionError((m,n,'minimum count',direct[largest],min_formula(m,n)))
    count+=checks
    print('CASE_OK',m,n,'checks',checks,'min_zero_forcing',m*n-largest,'min_sets',direct[largest],'poly_white',dict(sorted(direct.items())))
print('VERIFY_OK boards=8 exhaustive_subsets=',count,'six_EGF_terms=passed','minimum_count=passed')
