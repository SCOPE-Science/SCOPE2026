#!/usr/bin/env python3
"""Finite exact-arithmetic checks for the standard simplex-sum cyclohedron.

Requires only Python 3.9+ standard library. Running this script checks the
integer facet-incidence ranks and the proposed angle/census identities.
The all-dimensions theorem is proved separately in RESULT.md.
"""
from fractions import Fraction as Q
from itertools import combinations, permutations
from math import comb

P=1_000_000_007

def rank_mod(vectors):
    """Exact rank over a prime field; a full-rank minor is a rational certificate."""
    if not vectors: return -1
    rows=[[(x-y)%P for x,y in zip(row,vectors[0])] for row in vectors[1:]]
    if not rows:return 0
    d=len(vectors[0]); piv=[]
    for row in rows:
        for col,p in piv:
            c=row[col]
            if c: row=[(x-c*y)%P for x,y in zip(row,p)]
        col=next((j for j,x in enumerate(row) if x),None)
        if col is not None:
            inv=pow(row[col],P-2,P)
            row=[(x*inv)%P for x in row]
            # maintain ordered pivots (needed for correct elimination)
            piv.append((col,row))
            piv.sort(key=lambda z:z[0])
    return len(piv)

def tubes(n):
    return [frozenset((i+j)%n for j in range(k))
            for k in range(1,n) for i in range(n)]

def compatible(A,B,n):
    if A<B or B<A:return True
    if A&B:return False
    return all((i-1)%n not in B and (i+1)%n not in B for i in A)

def check(n):
    B=tubes(n)
    assert len(B)==len(set(B))==n*(n-1)
    N=D=0; left={}; right={}
    for A,T in combinations(B,2):
        if not compatible(A,T,n):continue
        a,b=len(A),len(T)
        gram=Q(n*len(A&T)-a*b,1)
        # Correlation sign is the normalized dot product of centered normals.
        if A<T or T<A:
            x,y=sorted((a,b))
            N+=1; left[x,y]=left.get((x,y),0)+1
            assert gram>0 and gram*gram*Q(1,a*(n-a)*b*(n-b))==Q(x*(n-y),y*(n-x))
        else:
            x,y=sorted((a,b))
            D+=1;right[x,y]=right.get((x,y),0)+1
            assert gram<0 and gram*gram*Q(1,a*(n-a)*b*(n-b))==Q(x*y,(n-x)*(n-y))
    assert N==n*(n-1)*(n-2)*(n+3)//6
    assert D==n*(n-1)*(n-2)*(n-3)//12
    for a in range(1,n):
        for b in range(a+1,n):
            assert left.get((a,b),0)==n*(b-a+1)
    for a in range(1,n):
        for b in range(a,n):
            expect=n*(n-a-b-1)//(2 if a==b else 1) if a+b<=n-2 else 0
            assert right.get((a,b),0)==expect,(n,a,b)
    if n<=6:
        all_tubes=B+[frozenset(range(n))]
        vertices=set()
        for perm in permutations(range(n)):
            ranks={v:i for i,v in enumerate(perm)}
            v=[0]*n
            for T in all_tubes:
                v[max(T,key=lambda j:ranks[j])]+=1
            vertices.add(tuple(v))
        assert len(vertices)==comb(2*n-2,n-1)
        V=list(vertices)
        assert rank_mod(V)==n-1
        minima={}; incidence={}
        for T in B:
            values=[sum(v[i] for i in T) for v in V]
            minima[T]=min(values)
            incidence[T]=[j for j,v in enumerate(values) if v==minima[T]]
            assert rank_mod([V[j] for j in incidence[T]])==n-2
        for A,T in combinations(B,2):
            common=set(incidence[A])&set(incidence[T])
            actual=rank_mod([V[j] for j in common])==n-3
            assert actual==compatible(A,T,n)
    return len(B),N,D

for n in range(3,13):
    f,o,a=check(n)
    print('n=%d facets=%d obtuse=%d acute=%d'%(n,f,o,a))

# For each squared acute cosine, the complementary obtuse angle has
# strictly more than twice the multiplicity, including coincident levels.
for n in range(4,26):
    acute={}; obtuse={}
    for a in range(1,n):
        for b in range(a,n):
            if a+b<=n-2:
                weight=n*(n-a-b-1)//(2 if a==b else 1)
                key=Q(a*b,(n-a)*(n-b))
                acute[key]=acute.get(key,0)+weight
        for b in range(a+1,n):
            key=Q(a*(n-b),b*(n-a))
            obtuse[key]=obtuse.get(key,0)+n*(b-a+1)
    assert all(obtuse.get(k,0)>2*v for k,v in acute.items())
print('CYCLO_RIDGE_AND_REFLECTION_PASS')
