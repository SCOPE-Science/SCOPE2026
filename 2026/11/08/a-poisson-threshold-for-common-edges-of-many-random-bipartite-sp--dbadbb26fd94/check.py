#!/usr/bin/env python3
"""Standalone exact checks for common-edge intersections in complete bipartite USTs."""
from fractions import Fraction
from math import comb, factorial
from itertools import combinations

tests = 0

def eq(actual, expected, note):
    global tests
    tests += 1
    if actual != expected:
        raise AssertionError((note, actual, expected))

def falling(n, r):
    if r > n: return 0
    v = 1
    for t in range(r): v *= n-t
    return v

def k_entry(a,b,e,f):
    i,j=e; x,y=f
    return (Fraction(int(i==x),b) + Fraction(int(j==y),a)
            - Fraction(1,a*b))

def det(M):
    if not M: return Fraction(1)
    n=len(M)
    B=[[Fraction(x) for x in row] for row in M]
    result=Fraction(1)
    for c in range(n):
        pivot=next((r for r in range(c,n) if B[r][c]),None)
        if pivot is None: return Fraction(0)
        if pivot != c:
            B[c],B[pivot]=B[pivot],B[c]
            result=-result
        v=B[c][c]; result*=v
        for r in range(c+1,n):
            q=B[r][c]/v
            for s in range(c+1,n): B[r][s]-=q*B[c][s]
            B[r][c]=0
    return result

def tree_edges(a,b):
    edges=[(i,j) for i in range(a) for j in range(b)]
    trees=[]
    for indices in combinations(range(len(edges)), a+b-1):
        parent=list(range(a+b))
        def root(x):
            while parent[x] != x: x=parent[x]
            return x
        good=True
        for idx in indices:
            i,j=edges[idx]; u=root(i); v=root(a+j)
            if u==v:
                good=False; break
            parent[u]=v
        if good and len({root(x) for x in range(a+b)})==1:
            trees.append(frozenset(indices))
    return edges,trees

def second(a,b,k):
    p=Fraction(a+b-1,a*b)
    qA=Fraction(a-1,a*b)
    qB=Fraction(b-1,a*b)
    q0=Fraction(-1,a*b)
    mean=a*b*p**k
    fm2=(a*b*((b-1)*(p*p-qA*qA)**k
                 +(a-1)*(p*p-qB*qB)**k
                 +(a-1)*(b-1)*(p*p-q0*q0)**k))
    return mean,fm2

for a,b in [(2,2),(2,3),(3,2),(2,4),(3,3),(3,4),(4,3)]:
    edges,ts=tree_edges(a,b)
    eq(len(ts),a**(b-1)*b**(a-1),('treecount',a,b))
    p=Fraction(a+b-1,a*b)
    for r in range(1,min(3,len(edges))+1):
        for subset in combinations(range(len(edges)),r):
            observed=Fraction(sum(all(idx in t for idx in subset) for t in ts),len(ts))
            selected=[edges[i] for i in subset]
            predicted=det([[k_entry(a,b,e,f) for f in selected] for e in selected])
            eq(observed,predicted,('forest',a,b,subset))
            eq(predicted <= p**r,True,('Hadamard',a,b,subset))
            if len({x for x,y in selected})==r and len({y for x,y in selected})==r:
                forest_formula=Fraction((a+b)**(r-1)*(a+b-r),(a*b)**r)
                eq(observed,forest_formula,('matching',a,b,subset))
    # Pair factorial moments from explicit pair classifications, independently enumerating forest pairs.
    for k in (2,3,4):
        m2=Fraction(0)
        for ix in range(len(edges)):
            for jx in range(len(edges)):
                if ix!=jx:
                    freq=Fraction(sum(ix in t and jx in t for t in ts),len(ts))
                    m2+=freq**k
        mean,fm2=second(a,b,k)
        eq(mean,a*b*p**k,('mean',a,b,k))
        eq(m2,fm2,('fm2',a,b,k))
        eq(fm2<=mean**2,True,('variance',a,b,k))

# Pure finite exact critical-sequence tests for k=3 and k=4:
for k in (3,4):
    for a in (5,10,25,50):
        b=a**(k-1)
        mean,fm2=second(a,b,k)
        eq(mean > 0,True,('positive',a,b,k))
        eq(fm2 <= mean**2,True,('pair_negative',a,b,k))
        # matchings are a valid positive contribution to factorial moments
        for r in (1,2,3):
            D=Fraction((a+b)**(r-1)*(a+b-r),(a*b)**r)
            lower=falling(a,r)*falling(b,r)*D**k
            upper=falling(a*b,r)*Fraction(a+b-1,a*b)**(k*r)
            eq(0<=lower<=upper, True, ('factorial_sandwich',a,b,k,r))


# Independent full common-intersection enumeration for small multi-tree systems.
for a,b,k in ((2,3,3),(2,3,4),(3,3,3)):
    edges,trees=tree_edges(a,b)
    masks=[sum(1<<i for i in t) for t in trees]
    count_by_overlap={}
    from itertools import product
    total=0
    for ix in product(range(len(masks)), repeat=k):
        common=(1<<len(edges))-1
        for z in ix: common &= masks[z]
        r=common.bit_count()
        count_by_overlap[r]=count_by_overlap.get(r,0)+1
        total+=1
    eq(total,len(trees)**k,('tuple_count',a,b,k))
    mu=sum(r*c for r,c in count_by_overlap.items())
    fm2=sum(r*(r-1)*c for r,c in count_by_overlap.items())
    expected_mu,expected_fm2=second(a,b,k)
    eq(Fraction(mu,total),expected_mu,('fullmean',a,b,k))
    eq(Fraction(fm2,total),expected_fm2,('fullfm2',a,b,k))
    eq(sum(count_by_overlap.values()),total,('fullmass',a,b,k))

print('VERIFY_OK', tests, 'exact assertions')
