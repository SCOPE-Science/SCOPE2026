#!/usr/bin/env python3
"""Standalone finite cross-check of the extremal VC-shattering theorem for convex noncrossing perfect matchings."""
from functools import lru_cache
from itertools import combinations
from math import comb

@lru_cache(None)
def recursive_matchings(verts):
    verts = tuple(verts)
    if not verts:
        return (frozenset(),)
    first = verts[0]
    result = []
    for j in range(1, len(verts), 2):
        last = verts[j]
        for left in recursive_matchings(verts[1:j]):
            for right in recursive_matchings(verts[j + 1:]):
                result.append(left | right | frozenset({(first, last)}))
    return tuple(result)

def all_pairings(verts):
    if not verts:
        yield ()
        return
    v = verts[0]
    for i in range(1, len(verts)):
        for rest in all_pairings(verts[1:i] + verts[i+1:]):
            yield ((v, verts[i]),) + rest

def crosses(e, f):
    a,b = e
    c,d = f
    return (a<c<b<d or c<a<d<b)

def brute_noncrossing(n):
    return {frozenset(p) for p in all_pairings(tuple(range(n)))
            if all(not crosses(e,f) for e,f in combinations(p,2))}

def boundary(edge, n):
    a,b = edge
    return b-a == 1 or (a == 0 and b == n-1)

def check(m):
    n = 2*m
    ms = set(recursive_matchings(tuple(range(n))))
    independent = brute_noncrossing(n)
    assert ms == independent, 'independent enumeration disagreement'
    assert len(ms) == comb(2*m,m)//(m+1), 'Catalan count disagreement'
    if m == 1:
        assert len(ms)==1
        return 1, 1, 1
    supports = {frozenset(s) for matching in ms
                for s in combinations(sorted(matching),m-1)}
    shattered = set()
    for support in supports:
        observed = {frozenset(matching & support) for matching in ms}
        if len(observed) == (1 << (m-1)):
            shattered.add(support)
    expected = {support for support in supports
                if all(boundary(e,n) for e in support)}
    assert shattered == expected, f'max shattered supports mismatch at m={m}'
    assert len(shattered) == m*m
    # Any size-m shattered support would have to equal a complete matching.
    for M in ms:
        tr={frozenset(mm & M) for mm in ms}
        assert len(tr)<(1<<m)
    return len(ms),len(supports),len(shattered)

if __name__ == '__main__':
    for m in range(1,7):
        catalan, candidates, shattered = check(m)
        print(f'm={m} vertices={2*m} noncrossing_matchings={catalan} '
              f'candidate_top_supports={candidates} shattered_top_supports={shattered}')
    print('NONCROSSING_MATCHING_EXTREMAL_SHATTERING_PASS')
