#!/usr/bin/env python3
"""Independent finite tests for vertex traces of minimum independent dominating path sets.
Python 3 standard library only. Mathematical proof is in RESULT.md.
"""
from itertools import combinations
from math import comb, log2
from functools import lru_cache

def all_i_sets(n):
    r=(n+2)//3
    found=[]
    def extend(seq):
        if len(seq)==r:
            if n-seq[-1]<=1:
                found.append(sum(1<<(v-1) for v in seq))
            return
        for nxt in (seq[-1]+2, seq[-1]+3):
            if nxt<=n:
                extend(seq+[nxt])
    for first in (1,2):
        if first<=n:extend([first])
    return sorted(set(found))

def brute_i_sets(n):
    ans=[]
    for mask in range(1<<n):
        if mask.bit_count()!=(n+2)//3:continue
        if mask&(mask<<1):continue
        closed=mask | (mask<<1) | (mask>>1)
        if closed&((1<<n)-1) == (1<<n)-1:ans.append(mask)
    return sorted(ans)

def trace_counts(n,sets,depth):
    counts=[1]
    for d in range(1,depth+1):
        acc=0
        for indices in combinations(range(n),d):
            traces={sum(((v>>i)&1)<<j for j,i in enumerate(indices)) for v in sets}
            acc+=(len(traces)==1<<d)
        counts.append(acc)
    return counts

def expected(n):
    k,rem=divmod(n,3)
    if rem==0:return [1,0,0,0]
    if rem==2:return [1,2*k+2,0,0]
    if k==0:return [1,0,0,0]
    if k==1:return [1,4,0,0]
    return [1,3*k+1,2*k*k+k-2,0]

def ldim(sols,n):
    masks=[sum(1<<j for j,s in enumerate(sols) if s>>i&1) for i in range(n)]
    @lru_cache(None)
    def f(S):
        best=0
        if S.bit_count()<2:return 0
        for M in masks:
            L=S&M;R=S^L
            if not L or not R:continue
            if min(L.bit_count(),R.bit_count())<=best:continue
            best=max(best,1+min(f(L),f(R)))
            if (1<<(best+1))>S.bit_count():break
        return best
    return f((1<<len(sols))-1)

# Brute search is genuinely independent of the gap-generation model.
for n in range(1,17):
    assert all_i_sets(n)==brute_i_sets(n),('brute',n)

# Full singleton/pair/triple support enumeration through n=43.
for n in range(1,44):
    sols=all_i_sets(n)
    assert len(sols) == (1 if n%3==0 else ((n//3+2)*(n//3+1)//2 if n%3==1 else n//3+2)),('count',n)
    result=trace_counts(n,sols,3)
    assert result==expected(n),('traces',n,result,expected(n))

# Direct dynamic-programming recomputation of the online depth for the linear threshold subfamily.
for k in range(0,11):
    n=3*k+2
    sols=all_i_sets(n)
    expected_depth=(k+2).bit_length()-1
    assert ldim(sols,n)==expected_depth,('online',n)

# Support classification tests, including every attainable pair of states and time indices.
for r in range(3,16):
    sets_by_gap={}
    for p,q in combinations(range(1,r+2),2):
        states=tuple(int(p<=j)+int(q<=j) for j in range(1,r+1))
        sets_by_gap[(p,q)]=states
    for j,h in combinations(range(1,r+1),2):
        for a in range(3):
            for b in range(3):
                traces={(int(st[j-1]==a),int(st[h-1]==b)) for st in sets_by_gap.values()}
                shattered=len(traces)==4
                expected_pair=((a,b)==(1,1) or ((a,b)==(0,1) and (j,h)!=(r-1,r))
                               or ((a,b)==(1,2) and (j,h)!=(1,2))
                               or ((a,b)==(0,2) and h-j>=2))
                assert shattered==expected_pair,('pair',r,j,h,a,b,traces)
print('MIN_I_PATH_SHATTERING_AND_ONLINE_PASS n=1..43; brute n=1..16; online k=0..10; gap pair types r=3..15')
