#!/usr/bin/env python3
"""Direct finite verification for exact closed-rook neighborhood shattering profiles.

All proofs for unbounded rectangular boards are in RESULT.md. This program
independently enumerates center traces and checks the asserted star-forest
support criterion and every polynomial coefficient on small boards.
"""
from itertools import combinations
from math import comb
from collections import Counter


def choose(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def predicted_coeffs(m, n):
    if m == 1 or n == 1:
        return (1, 0, 0, 0, 0)
    a2 = (m * choose(n, 2) if n >= 3 else 0)
    a2 += (n * choose(m, 2) if m >= 3 else 0)
    a2 += (2 * choose(m, 2) * choose(n, 2) if m >= 3 and n >= 3 else 0)
    a3 = (m * (m - 1) * choose(n, 2) * (n - 2)
          if m >= 3 and n >= 4 else 0)
    a3 += (n * (n - 1) * choose(m, 2) * (m - 2)
           if n >= 3 and m >= 4 else 0)
    return (1, m * n, a2, a3, 0)


def shape_classification(m, n, support):
    # No graph isomorphism package; degrees and connected components computed
    # directly from the selected pairs. Thus independent of the trace checker.
    k = len(support)
    if k == 0:
        return True
    if m < 2 or n < 2:
        return False
    rows = {i for i, j in support}
    cols = {j for i, j in support}
    if len(rows) == m or len(cols) == n:
        return False  # empty trace requires one unused row and column
    dr = Counter(i for i, j in support)
    dc = Counter(j for i, j in support)
    if any(dr[i] != 1 and dc[j] != 1 for i,j in support):
        return False
    if k == 1:
        return True
    if k == 2:
        return True  # star or disjoint pair, both 2-color-coverable
    if k == 3:
        # Exactly one repeated row/column of multiplicity 2, remaining edge
        # entirely disjoint from that star.
        if sorted(dr.values()) == [1, 2] and sorted(dc.values()) == [1, 1, 1]:
            return True
        if sorted(dc.values()) == [1, 2] and sorted(dr.values()) == [1, 1, 1]:
            return True
        return False
    return False


def direct_shattered(m,n,support):
    k=len(support)
    traces=set()
    for a in range(m):
        for b in range(n):
            trace=0
            for t,(i,j) in enumerate(support):
                if a == i or b == j:
                    trace |= (1<<t)
            traces.add(trace)
            if len(traces)==(1<<k):return True
    return False


def run():
    tested=0
    nboards=0
    bysize=Counter()
    # Independently enumerate all support sizes <=4 for all rectangular boards
    # through 6x6, including all one-dimensional boundary boards.
    for m in range(1,7):
        for n in range(m,7):
            vertices=list((i,j) for i in range(m) for j in range(n))
            observed=[1,0,0,0,0]
            predicted=predicted_coeffs(m,n)
            nboards+=1
            for k in range(1,5):
                for support in combinations(vertices,k):
                    actual=direct_shattered(m,n,support)
                    shape=shape_classification(m,n,support)
                    assert actual == shape,(m,n,k,support,actual,shape)
                    if actual: observed[k]+=1
                    tested+=1
                    bysize[k]+=1
            assert tuple(observed)==predicted,(m,n,observed,predicted)
            print('board',m,n,'coefficients',observed)
    assert tuple(predicted_coeffs(4,4))==(1,16,120,288,0)
    assert tuple(predicted_coeffs(3,4))==(1,12,66,72,0)
    print('CLOSED_ROOK_ALL_FINITE_TESTS_PASS', 'boards',nboards,
          'individual_support_decisions',tested,
          'size_counts',dict(sorted(bysize.items())))


if __name__=='__main__':
    run()
