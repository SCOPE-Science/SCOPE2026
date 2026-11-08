#!/usr/bin/env python3
"""Independent finite replay of exact two-total-bondage cut classifications."""
from itertools import combinations
from math import comb, factorial


def stirling(n,k):
    if k<0 or k>n: return 0
    s=[0]*(k+1);s[0]=1
    for _ in range(n):
        t=[0]*(k+1)
        for j in range(1,k+1): t[j]=j*s[j]+s[j-1]
        s=t
    return s[k]


def formula(a,b):
    if a==2: return b,factorial(a)*stirling(b,a)
    q=min(b,2*a)
    low=factorial(a)*stirling(b,a) if b<=2*a else 0
    high=comb(b,3)*factorial(3)*stirling(a,3) if b>=2*a else 0
    return q,low+high


def full_td_size_at_most_three(a,b,deleted):
    # Independent adjacency-based implementation: directly check all 2/3 subsets.
    d=set(deleted)
    n=a+b
    neighbors=[0]*n
    for i in range(a):
        for j in range(b):
            if (i,j) not in d:
                neighbors[i]|=1<<(a+j)
                neighbors[a+j]|=1<<i
    if any(x==0 for x in neighbors): return None  # forbidden isolated vertex
    for k in (2,3):
        for xs in combinations(range(n),k):
            mask=0
            for v in xs: mask|=neighbors[v]
            if mask==(1<<n)-1:return k
    return 4


def exhaustive(a,b):
    m=a*b
    target,expected=formula(a,b)
    good=0
    fewer=0
    edges=[(i,j) for i in range(a) for j in range(b)]
    for k in range(target+1):
        for ix in combinations(range(m),k):
            deletions=[edges[u] for u in ix]
            outcome=full_td_size_at_most_three(a,b,deletions)
            if outcome==4:
                if k<target:fewer+=1
                else:good+=1
    assert fewer==0,(a,b,'fewer',fewer)
    assert good==expected,(a,b,'count',good,expected)
    print('EXHAUSTIVE_OK',a,b,'min_deletions',target,'optimal_cuts',good)


def explicit(a,b):
    # Low-regime surjection: one missing edge per B, all A hit.
    low={(j%a,j) for j in range(b)}
    assert len(low)==b
    assert full_td_size_at_most_three(a,b,low)==4
    if a>=3 and b>=2*a:
        # Three-column triangle cut; all A miss two edges.
        # Rows 0,1,2 assigned missing pairs (0,1),(0,2),(1,2).
        # Further rows assigned pair (0,1).
        pairs=[(0,1),(0,2),(1,2)]+[(0,1)]*(a-3)
        high={(i,j) for i,(x,y) in enumerate(pairs) for j in (x,y)}
        assert len(high)==2*a
        assert full_td_size_at_most_three(a,b,high)==4


def check_incidence_lemma(a):
    # Independently exhaust every family of proper subsets with cost < 2a,
    # and verify it cannot cover all unordered pairs of a labels.
    universe=frozenset((i,j) for i in range(a) for j in range(i+1,a))
    proper=[frozenset(c) for k in range(1,a) for c in combinations(range(a),k)]
    states={frozenset():0}
    for subset in proper:
        cost=len(subset)
        cover=frozenset((i,j) for i,j in universe if i in subset and j in subset)
        for seen,spent in list(states.items()):
            if spent+cost>=2*a:continue
            key=seen|cover
            new=spent+cost
            if new<states.get(key,10**8):states[key]=new
    assert universe not in states, (a,'lemma failed')
    print('PAIR_COVER_LOWER_BOUND_OK',a)


def main():
    for a in range(3,6):check_incidence_lemma(a)
    for a,b in [(2,2),(2,3),(2,4),(2,5),(2,6),
                (3,3),(3,4),(3,5),(3,6),(3,7),(3,8),
                (4,4),(4,5),(4,6)]:
        exhaustive(a,b)
    for a in range(2,12):
        for b in range(a,3*a+7): explicit(a,b)
    print('EXPLICIT_FAMILIES_OK',sum(2*a+7 for a in range(2,12)))
    print('VERIFY_OK')

if __name__=='__main__':main()
