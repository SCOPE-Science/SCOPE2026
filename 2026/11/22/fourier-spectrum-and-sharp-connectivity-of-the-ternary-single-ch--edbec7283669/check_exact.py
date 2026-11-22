"""Reproducible exact checks for ternary single-parity polytope edge and spectrum formulas.
Run: python check_exact.py
Uses only Python standard library; no external inputs.
"""
from itertools import product, combinations
from collections import Counter
from math import comb, factorial

def words(n):
    return [x+((-sum(x))%3,) for x in product(range(3),repeat=n-1)]

def support_zero_subset(d):
    inds=[i for i,x in enumerate(d) if x]
    for r in range(1,len(inds)):
        for sub in combinations(inds,r):
            if sum(d[i] for i in sub)%3==0:return True
    return False

def direct_edge(x,y):
    d=tuple((b-a)%3 for a,b in zip(x,y))
    return not support_zero_subset(d)

def claimed_edge(x,y):
    d=tuple((b-a)%3 for a,b in zip(x,y)); vals=[t for t in d if t]
    return len(vals)==2 and sum(vals)%3==0 or len(vals)==3 and len(set(vals))==1

def spec_lap(n):
    result=Counter()
    for a in product(range(3),repeat=n-1):
        cc=Counter(a+(0,))
        F=sum(cc[i]*cc[j]*(cc[i]+cc[j]) for i in range(3) for j in range(i+1,3))
        result[3*F//2]+=1
        assert (3*F)%2==0
    return result

def direct_cayley_spectrum(n):
    # Number of distinct roots of unity requires no floating point: 1, omega, omega^2.
    # Pair +/- generator contributions equal 2 if phase 0, and -1 otherwise.
    gen=[]
    for i,j in combinations(range(n),2):
        for sign in (1,2):
            g=[0]*n;g[i]=sign;g[j]=(-sign)%3;gen.append(tuple(g))
    for ijk in combinations(range(n),3):
        for sign in (1,2):
            g=[0]*n
            for i in ijk:g[i]=sign
            gen.append(tuple(g))
    degree=len(gen)
    assert len(set(gen))==degree
    tally=Counter()
    for a in product(range(3),repeat=n-1):
        a=a+(0,)
        nonzero=sum(1 for g in gen if sum(x*y for x,y in zip(a,g))%3)
        # Real adjacency eigenvalue as integer: sum of all omega^(a.g),
        # nonzero phases occur in opposite pairs, yielding -1 per pair.
        assert nonzero%2==0
        lam=degree-3*nonzero//2
        tally[degree-lam]+=1
    return tally

for n in range(2,7):
    w=words(n); assert len(w)==3**(n-1)
    bydist=Counter()
    for i,x in enumerate(w):
        for y in w[i+1:]:
            actual=direct_edge(x,y);predicted=claimed_edge(x,y)
            assert actual==predicted,(n,x,y)
            if actual: bydist[sum(a!=b for a,b in zip(x,y))]+=1
    assert bydist==Counter({2:3**(n-1)*comb(n,2),3:3**(n-1)*comb(n,3)}) if n>=3 else bydist==Counter({2:3})
    s1=spec_lap(n);s2=direct_cayley_spectrum(n)
    assert s1==s2,(n,s1,s2)
    gap=min(k for k in s1 if k>0)
    assert gap==3*n*(n-1)//2
    expected_gap_mult=2 if n==2 else (8 if n==3 else 2*n)
    assert s1[gap]==expected_gap_mult,(n,s1[gap],expected_gap_mult)
    print('n=',n,'vertices=',len(w),'edges_by_hamming=',dict(bydist),'algebraic_connectivity=',gap,'multiplicity=',s1[gap], 'eigenvalue_count=',len(s1))
print('TERNARY_SPC_EDGE_SPECTRUM_EXACT_PASS')
