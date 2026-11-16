#!/usr/bin/env python3
"""Independent exact-cover enumeration and modular rank verification.
Python standard library only; invoke: python verify_exact_cover.py.
"""
from itertools import combinations
from collections import defaultdict

POINTS = range(1,8)
TRIPLES = list(combinations(POINTS,3))
PAIRS = list(combinations(POINTS,2))
PID = {p:i for i,p in enumerate(PAIRS)}
TRIPLE_PAIRS = [sum(1 << PID[p] for p in combinations(t,2)) for t in TRIPLES]
ALL = (1 << len(PAIRS)) - 1

def enumerate_planes():
    result = []
    by_pair = [[] for _ in PAIRS]
    for i,pairmask in enumerate(TRIPLE_PAIRS):
        for k in range(len(PAIRS)):
            if pairmask >> k & 1: by_pair[k].append(i)
    def rec(covered, chosen):
        if covered == ALL:
            assert len(chosen) == 7
            result.append(sum(1 << i for i in chosen));return
        # Choose uncovered pair with fewest compatible completions.
        candidates = []
        for k in range(len(PAIRS)):
            if not (covered >> k & 1):
                available = [i for i in by_pair[k] if not TRIPLE_PAIRS[i] & covered]
                candidates.append((len(available), k, available))
        _,k,opts = min(candidates)
        for i in opts:rec(covered | TRIPLE_PAIRS[i], chosen+[i])
    rec(0,[])
    assert len(result) == 30 and len(set(result)) == 30
    return sorted(result)

def rank_mod(A,prime):
    if not A:return 0
    rows=[row[:] for row in A]
    m,n=len(rows),len(rows[0]);r=0
    for c in range(n):
        k=next((i for i in range(r,m) if rows[i][c] % prime),None)
        if k is None:continue
        rows[r],rows[k]=rows[k],rows[r]
        v=pow(rows[r][c] % prime,-1,prime)
        for j in range(c,n):rows[r][j]=rows[r][j]*v%prime
        for i in range(r+1,m):
            t=rows[i][c]%prime
            if t:
                for j in range(c,n):rows[i][j]=(rows[i][j]-t*rows[r][j])%prime
        r+=1
        if r==m:break
    return r

def run():
    planes=enumerate_planes()
    # Group labels by pairwise intersection=one; yields two disjoint K15.
    group = {planes[0]:1}
    stack=[planes[0]]
    while stack:
        current=stack.pop()
        for other in planes:
            if other != current and (other & current).bit_count()==1 and other not in group:
                group[other]=1;stack.append(other)
    assert len(group)==15
    for p in planes:
        if p not in group:group[p]=-1
    contrast=[group[p] for p in planes]
    assert sum(contrast)==0
    # For each 0,1,2-line monomial, the two classes contribute equally.
    cols=[(1<<35)-1]
    cols.extend(1<<i for i in range(35))
    cols.extend((1<<i)|(1<<j) for i,j in combinations(range(35),2))
    assert all(sum(contrast[r] for r,p in enumerate(planes) if (p & c)==c)==0 for c in cols)
    # Use a 30x30 Gram, so elimination is small and exact.
    Gram=[[sum((p&c)==c and (q&c)==c for c in cols) for q in planes] for p in planes]
    assert all(rank_mod(Gram,p)==29 for p in (1013,1009))
    # Witness cubic monomial repairs the unique missing contrast dimension.
    c=0
    for t in ((1,2,3),(1,4,5),(2,4,6)):
        c |= 1<<TRIPLES.index(t)
    w=[int((p & c)==c) for p in planes]
    assert sum(w)==1 and abs(sum(v*e for v,e in zip(w,contrast)))==1
    extended=[row+[w[i]] for i,row in enumerate(Gram)]
    assert all(rank_mod(extended,p)==30 for p in (1013,1009))
    print('PASS: independent exact-cover enumeration gives all 30 planes')
    print('PASS: component contrast annihilates every degree <=2 monomial')
    print('PASS: degree <=2 rank 29 and degree <=3 rank 30 modulo 1009 and 1013')

if __name__ == '__main__':run()
