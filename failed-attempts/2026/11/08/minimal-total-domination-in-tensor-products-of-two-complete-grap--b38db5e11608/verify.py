#!/usr/bin/env python3
"""Exhaustively check minimal total domination from graph-neighborhood definitions.

No graph-theory library or precomputed solution families are required.
"""
from collections import Counter
from itertools import combinations
from math import comb


def predicted(m, n):
    """Generate sets via three distinct-coordinate cells or two doubled lines."""
    out = set()
    for rows in combinations(range(m), 3):
        for cols in combinations(range(n), 3):
            from itertools import permutations
            for p in permutations(cols):
                out.add(sum(1 << (rows[k] * n + p[k]) for k in range(3)))
    for r1, r2 in combinations(range(m), 2):
        for cs1 in combinations(range(n), 2):
            for cs2 in combinations(range(n), 2):
                out.add(sum(1 << (r * n + c) for r,cs in ((r1,cs1),(r2,cs2)) for c in cs))
    for c1, c2 in combinations(range(n), 2):
        for rs1 in combinations(range(m), 2):
            for rs2 in combinations(range(m), 2):
                out.add(sum(1 << (r * n + c) for c,rs in ((c1,rs1),(c2,rs2)) for r in rs))
    return out


def direct_check(m, n):
    N = m * n
    neighbors = tuple(sum(1 << (a*n+b) for a in range(m) for b in range(n)
                          if a != i and b != j)
                      for i in range(m) for j in range(n))
    def total(S):
        return all(S & ne for ne in neighbors)
    actual = set()
    for S in range(1, 1 << N):
        if total(S) and all(not total(S & ~(1 << i)) for i in range(N) if S & (1 << i)):
            actual.add(S)
    assert actual == predicted(m,n), (m,n,len(actual),len(predicted(m,n)))
    A = 6*comb(m,3)*comb(n,3) if m>=3 and n>=3 else 0
    B = comb(m,2)*comb(n,2)*(comb(m,2)+comb(n,2)-1)
    counts = Counter(S.bit_count() for S in actual)
    assert counts == Counter({k:v for k,v in ((3,A),(4,B)) if v}), (m,n,counts,A,B)
    return N, len(actual), counts


def main():
    cases = [(2,2),(2,3),(2,4),(2,5),(3,3),(3,4),(3,5),(4,4),(4,5)]
    total_subsets=0; nsets=0
    for m,n in cases:
        V,k,C=direct_check(m,n)
        total_subsets += (1 << V)-1; nsets += k
        print(f'case {m}x{n}: candidate_subsets={(1<<V)-1} minimal={dict(C)}')
    print(f'VERIFY_OK instances={len(cases)} examined_subsets={total_subsets} '
          f'minimal_sets={nsets} exact_families=PASS all_coefficients=PASS')
if __name__ == '__main__':main()
