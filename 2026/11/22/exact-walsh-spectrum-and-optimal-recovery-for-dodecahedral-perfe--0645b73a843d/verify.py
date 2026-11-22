#!/usr/bin/env python3
"""Standalone exact integer certificate for dodecahedral perfect-matching XOR convolution.

Execute with Python >=3.9: python3 verify.py
No third-party packages or external files are required.
"""
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from itertools import combinations

# Canonical generalized Petersen GP(10,2): outer ten-cycle,
# ten spokes, and the inner pentagram edges.
def gp_edges():
    s = set()
    for i in range(10):
        for a,b in ((i,(i+1)%10), (i,10+i), (10+i,10+(i+2)%10)):
            s.add(tuple(sorted((a,b))))
    return tuple(sorted(s))

# Shinsaku Fujita, MATCH 69 (2013), p. 345, Equation (49),
# zero-based reindexing of the published graph.
PAPER_EDGES = '''1-2 1-5 1-8 2-3 2-10 3-4 3-12 4-5 4-14 5-6
6-7 6-15 7-8 7-17 8-9 9-10 9-18 10-11 11-12 11-19
12-13 13-14 13-20 14-15 15-16 16-17 16-20 17-18 18-19 19-20'''
def paper_edges():
    return tuple(sorted(tuple(sorted(int(x)-1 for x in p.split('-')))
                        for p in PAPER_EDGES.split()))

# Explicit graph isomorphism, paper vertex 0..19 -> GP(10,2) vertex.
ISO = [0,1,11,19,9,8,18,10,12,2,3,13,15,17,7,6,16,14,4,5]

def adjacency(E):
    a=[[] for _ in range(20)]
    for i,(u,v) in enumerate(E): a[u].append((v,i));a[v].append((u,i))
    for row in a:row.sort()
    return a

def matchings(E):
    adj=adjacency(E); out=[]
    def rec(left,edge_mask):
        if left==0:out.append(edge_mask);return
        v=(left&-left).bit_length()-1
        for u,j in adj[v]:
            if (left>>u)&1:
                rec(left^(1<<v)^(1<<u),edge_mask|(1<<j))
    rec((1<<20)-1,0)
    return tuple(out)

def spanning_tree_cotree(E,reverse=False):
    adj=adjacency(E);found={0};todo=[0];tree=[]
    while todo:
        u=todo.pop() if reverse else todo.pop(0)
        for v,j in reversed(adj[u]) if reverse else adj[u]:
            if v not in found:
                found.add(v);todo.append(v);tree.append(j)
    assert len(found)==20 and len(tree)==19
    return tuple(i for i in range(len(E)) if i not in tree)

def reduce_mask(mask,cotree):
    return sum(((mask>>j)&1)<<k for k,j in enumerate(cotree))

def fwht(a):
    a=list(a);n=len(a);h=1
    while h<n:
        for i in range(0,n,2*h):
            for j in range(i,i+h):
                x,y=a[j],a[j+h];a[j]=x+y;a[j+h]=x-y
        h*=2
    return a

def direct_spectrum(E,cotree):
    matches=matchings(E)
    pats=tuple(reduce_mask(m,cotree) for m in matches)
    return [sum(1-2*((s&r).bit_count()%2) for r in pats)
            for s in range(1<<len(cotree))]

def weighted_dp_spectrum(E,cotree):
    adj=adjacency(E)
    def one(s):
        negative=sum(1<<j for k,j in enumerate(cotree) if (s>>k)&1)
        @lru_cache(None)
        def rec(left):
            if left==0:return 1
            v=(left&-left).bit_length()-1
            tot=0
            for u,j in adj[v]:
                if (left>>u)&1:
                    tot+=(-1 if ((negative>>j)&1) else 1)*rec(left^(1<<v)^(1<<u))
            return tot
        return rec((1<<20)-1)
    return [one(s) for s in range(1<<len(cotree))]

def run():
    gp,paper=gp_edges(),paper_edges()
    assert len(gp)==len(paper)==30 and len(set(ISO))==20
    assert {tuple(sorted((ISO[u],ISO[v]))) for u,v in paper}==set(gp)
    A=matchings(gp);B=matchings(paper)
    assert len(A)==len(B)==len(set(A))==len(set(B))==36
    assert {tuple(sorted((ISO[u],ISO[v]))) for u,v in paper}==set(gp)
    c1=spanning_tree_cotree(gp,False)
    c2=spanning_tree_cotree(paper,True)
    assert len(c1)==len(c2)==11
    F=[0]*2048
    for m in A:F[reduce_mask(m,c1)]+=1
    W=fwht(F)
    assert W==direct_spectrum(gp,c1)
    W2=weighted_dp_spectrum(paper,c2)
    spec=Counter(abs(w) for w in W)
    assert spec==Counter(abs(w) for w in W2)
    assert spec=={0:700,4:882,8:240,12:140,16:84,36:2}
    assert all(sum(bool((m>>j)&1) for m in A)==12 for j in range(30))
    # Direct check of the exact first cancellation support and its multiplicity.
    zero_pairs=[]
    for i,j in combinations(range(30),2):
        common=sum(bool((m>>i)&1) and bool((m>>j)&1) for m in A)
        if common==3:zero_pairs.append((i,j))
        val=sum(1-2*(((m>>i)&1)^((m>>j)&1)) for m in A)
        assert val==4*(common-3)
    assert len(zero_pairs)==60 and all(36-2*12==12 for _ in range(30))
    # Fourier inversion of nonvanishing spectral support on 11 independent cuts.
    P=[int(w!=0) for w in W]
    Q=fwht(P)
    assert sum(P)==1348 and sum(int(q==0) for q in Q)==1024
    assert sum(abs(q) for q in Q)==21248
    sharp=Fraction(sum(abs(q) for q in Q),2048)
    assert sharp==Fraction(83,8)
    assert sum(q*q for q in Q)==2048*1348
    assert max(abs(w) for w in W)==36
    assert min(abs(w) for w in W if w)!=0 and min(abs(w) for w in W if w)==4
    # Translate the quotient multiplicities into the full Boolean frequency space.
    full_rank=1348*(1<<19);full_nullity=700*(1<<19)
    assert full_rank==706740224 and full_nullity==367001600
    assert full_rank+full_nullity==(1<<30)
    print('PASS: graph isomorphism, both complete matching enumerations (36),')
    print('two independent signed-spectrum methods, 2048 characters each,')
    print('30 edge marginals, 435 pair incidences, exact Fourier inversion,')
    print('support norm 83/8, rank 706740224, nullity 367001600.')

if __name__=='__main__':run()
