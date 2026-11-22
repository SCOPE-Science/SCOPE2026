#!/usr/bin/env python3
"""Finite enumeration check of fixed-area Young-diagram shattering."""
from itertools import combinations, combinations_with_replacement
from math import comb


def ideals(m):
    out = []
    for rows in combinations_with_replacement(range(m+1), m):
        h = rows[::-1]
        mask = sum(1 << (i*m+j) for i in range(m) for j in range(h[i]))
        out.append((sum(h), mask))
    assert len(out) == comb(2*m, m)
    return out


def supports(m):
    # All antichains in the product order: increasing row, decreasing column.
    yield ()
    for s in range(1, m+1):
        for rows in combinations(range(m), s):
            for cols in combinations(range(m), s):
                yield tuple(zip(rows, cols[::-1]))


def predicted(m, S, k):
    D = sum(any(i<=a and j<=b for (a,b) in S)
            for i in range(m) for j in range(m))
    U = sum(any(i>=a and j>=b for (a,b) in S)
            for i in range(m) for j in range(m))
    return D <= k <= m*m-U


def brute(ideal_masks, m, S):
    bits = [1 << (i*m+j) for (i,j) in S]
    outcomes = set()
    for mask in ideal_masks:
        outcomes.add(sum((1<<r) for r,bit in enumerate(bits) if mask&bit))
        if len(outcomes)==(1<<len(S)):
            return True
    return False


def run():
    cases=0
    for m in range(1,7):
        all_ideals=ideals(m)
        per_k = [[b for rank,b in all_ideals if rank==k] for k in range(m*m+1)]
        central=m*m//2
        maxs=max(s for s in range(m+1) if s <= (m-s)**2)
        centralmax=0; centralcount=0
        for S in supports(m):
            for k in range(m*m+1) if m<=5 else (central,):
                p=predicted(m,S,k)
                q=brute(per_k[k],m,S)
                assert p == q, (m,S,k,p,q)
                cases+=1
                if k==central and p:
                    if len(S)>centralmax:
                        centralmax=len(S); centralcount=0
                    if len(S)==centralmax:
                        centralcount+=1
        assert centralmax==maxs,(m,centralmax,maxs)
        # Inspect the diagonal construction independently.
        S=tuple((i,m-1-i) for i in range(maxs))
        D=sum(any(i<=a and j<=b for a,b in S) for i in range(m) for j in range(m))
        U=sum(any(i>=a and j>=b for a,b in S) for i in range(m) for j in range(m))
        assert D==U==maxs*(2*m-maxs+1)//2
        assert D<=central<=m*m-U
        print(f'm={m} ideals={len(all_ideals)} central_k={central} '
              f'VCdim={centralmax} maximal_supports={centralcount} '
              f'construct_down_up={D} checks={cases}')
    print(f'PASS total_support_rank_comparisons={cases}')

if __name__=='__main__':run()
