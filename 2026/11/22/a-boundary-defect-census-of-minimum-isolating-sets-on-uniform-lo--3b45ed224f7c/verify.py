#!/usr/bin/env python3
"""Independent literal-hyperedge checks and interval-cover recurrence for the mathematical result."""
from itertools import combinations
from collections import defaultdict
from math import comb

def predicted(m,r):
    assert m>=1 and r>=3
    q=(m+3)//4; a=r-1; t=4*q-m
    return (1,
            1+q*a,
            1+2*q*a+comb(q,2)*a*a,
            1+(3*q-2)*a+3*comb(q,2)*a*a+comb(q,3)*a**3)[t]

def literal_edges(m,r):
    # An explicit labeled hypergraph, independently of the interval proof.
    blocks=[]; next_label=m-1
    for i in range(m):
        b=[]
        if i: b.append(i-1)
        if i<m-1: b.append(i)
        while len(b)<r:
            b.append(next_label); next_label+=1
        blocks.append(frozenset(b))
    return blocks,next_label

def literal_count(m,r):
    E,n=literal_edges(m,r)
    influence=[]
    for v in range(n):
        closed={v}
        for e in E:
            if v in e: closed.update(e)
        mask=sum(1<<j for j,e in enumerate(E) if closed.intersection(e))
        influence.append(mask)
    q=(m+3)//4; target=(1<<m)-1
    ct=0
    for ds in combinations(range(n),q):
        mask=0
        for v in ds:
            mask|=influence[v]
        ct += mask==target
    return ct

def recurrence(m,r):
    # Independent weighted-interval cover DP: no use of the claimed polynomial.
    q=(m+3)//4
    if m==1:return r
    cand=[]
    for i in range(1,m+1):
        cand.append((max(1,i-1),min(m,i+1),r-1 if i in (1,m) else r-2))
    for i in range(1,m):
        cand.append((max(1,i-1),min(m,i+2),1))
    cand.sort(key=lambda x:(x[1],x[0]))
    dp=defaultdict(int);dp[(0,0)]=1
    for l,h,w in cand:
        for (k,end),ways in list(dp.items()):
            if k<q and l<=end+1 and h>end:
                dp[(k+1,h)]+=ways*w
    return dp[q,m]

def run():
    checks=0
    for m in range(1,14):
        for r in (3,4,5):
            got=literal_count(m,r)
            want=predicted(m,r)
            assert got==want,(m,r,got,want)
            checks+=1
    print('INDEPENDENT_LITERAL_HYPEREDGE_MINIMUM_SET_COUNTS_PASS',checks)
    checks=0
    for m in range(1,81):
        for r in range(3,11):
            got=recurrence(m,r)
            want=predicted(m,r)
            assert got==want,(m,r,got,want)
            checks+=1
    print('INDEPENDENT_INTERVAL_DP_ALL_RESIDUES_PASS',checks)
    for q in range(1,25):
        assert predicted(4*q,3)==1
        assert predicted(4*q-1,5)==1+4*q
    print('RIGIDITY_AND_BOUNDARY_POLYNOMIAL_CHECKS_PASS')
    print('VERIFY_OK')
if __name__=='__main__':run()
