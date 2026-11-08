"""Solve (I + A) x = 1 over GF(2) by elimination, independently of the parity-partition derivation."""
from collections import Counter
from itertools import combinations
from math import comb

def solve(n):
    edges=list(combinations(range(n),2)); E=len(edges)
    rows=[]
    for i,(u,v) in enumerate(edges):
        mask=0
        for j,(s,t) in enumerate(edges):
            if {u,v}&{s,t}: mask|=1<<j
        rows.append(mask | (1<<E))
    rank=0;pivots=[]
    for col in range(E):
        pivot=next((r for r in range(rank,E) if rows[r]>>col&1),None)
        if pivot is None:continue
        rows[rank],rows[pivot]=rows[pivot],rows[rank]
        for r in range(E):
            if r!=rank and rows[r]>>col&1:rows[r]^=rows[rank]
        pivots.append(col);rank+=1
    assert all((r&((1<<E)-1)) or not(r>>E&1) for r in rows)
    free=[i for i in range(E) if i not in pivots]
    W=Counter(); WC=Counter(); edgeadj=[]
    for i,(u,v) in enumerate(edges):
        edgeadj.append(sum(1<<j for j,(a,b) in enumerate(edges) if i!=j and ({u,v}&{a,b})))
    for z in range(1<<len(free)):
        x=sum(((z>>i)&1)<<c for i,c in enumerate(free))
        for r in range(rank-1,-1,-1):
            c=pivots[r];x=(x&~(1<<c))|(((rows[r]>>E&1)^((rows[r]&((1<<E)-1)&~(1<<c)&x).bit_count()%2))<<c)
        assert all(((r&((1<<E)-1)&x).bit_count()%2)==(r>>E&1) for r in rows)
        weight=x.bit_count();W[weight]+=1
        reach=x&-x;seen=0
        while reach:
            seen|=reach
            nxt=0
            for j in range(E):
                if reach>>j&1:nxt|=edgeadj[j]
            reach=nxt&x&~seen
        if seen==x: WC[weight]+=1
    return rank,W,WC
for n in range(3,10):
    rank,w,wc=solve(n)
    expect=Counter();expect_c=Counter();E=comb(n,2)
    if n%2==0:expect[E]=1;expect_c[E]=1
    else:
        for a in range(0,n+1,2):
            weight=comb(a,2)+comb(n-a,2)
            expect[weight]+=comb(n,a)
            if a in (0,n-1):expect_c[weight]+=comb(n,a)
    assert w==expect,(n,w,expect)
    assert wc==expect_c,(n,wc,expect_c)
    expected_rank=E-(n-1 if n%2 else 0)
    assert rank==expected_rank,(n,rank,expected_rank)
    print(f'n={n} rank={rank} nullity={E-rank} total={sum(w.values())} connected={sum(wc.values())} weight_profile={sorted(w.items())} connected_profile={sorted(wc.items())} CHECKED')
print('GAUSSIAN_SOLVER_PASS')
