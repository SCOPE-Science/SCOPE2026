#!/usr/bin/env python3
"""Exact combinatorial and graph-level check of cycle-power induced-matching formulas.

Only the Python standard library is required. Finite tests supplement, and do not
replace, the proof for unrestricted parameters.
"""
from collections import Counter
from itertools import combinations
from math import ceil


def predicted(n, r, maximal):
    assert 1 <= r and n >= 2*r+1
    block = Counter()
    for length in range(1, r+1):
        endpoint = min(n-length, 2*r+2) if maximal else n-length
        for gap in range(r+1, endpoint+1):
            block[length+gap] += 1
    answer = Counter()
    preceding = {0: 1}
    for k in range(1, n//(r+2)+1):
        following = Counter()
        for length, c in preceding.items():
            for size, d in block.items():
                if length+size <= n:
                    following[length+size] += c*d
        preceding = following
        coefficient = n*preceding.get(n, 0)
        assert coefficient % k == 0, (n,r,k,coefficient)
        if coefficient:
            answer[k] = coefficient//k
    return answer


def independently_enumerated(n, r):
    edges = [(a,b) for a in range(n) for b in range(a+1,n)
             if min(b-a, n-(b-a)) <= r]
    def far(a,b):
        delta = abs(a-b)
        return min(delta, n-delta) > r
    compatibility = [0]*len(edges)
    for i,(a,b) in enumerate(edges):
        for j,(c,d) in enumerate(edges):
            if i != j and len({a,b,c,d})==4 and all(
                far(x,y) for x in (a,b) for y in (c,d)):
                compatibility[i] |= 1 << j
    all_counts = Counter()
    maximal_counts = Counter()
    candidate_subsets = 0
    for k in range(1,n//(r+2)+1):
        for combo in combinations(range(len(edges)),k):
            candidate_subsets += 1
            if any(not (compatibility[i] & (1 << j)) for i,j in combinations(combo,2)):
                continue
            all_counts[k] += 1
            candidate_additions = (1 << len(edges))-1
            for i in combo:
                candidate_additions &= compatibility[i]
            if candidate_additions == 0:
                maximal_counts[k] += 1
    return all_counts, maximal_counts, candidate_subsets


def run():
    instances = candidates = induced = maximal = 0
    for r in range(1,5):
        for n in range(2*r+1,17):
            all_actual, maximal_actual, examined = independently_enumerated(n,r)
            all_expected = predicted(n,r,False)
            maximal_expected = predicted(n,r,True)
            assert all_actual == all_expected, (n,r,'all',all_actual,all_expected)
            assert maximal_actual == maximal_expected, (n,r,'maximal',maximal_actual,maximal_expected)
            instances += 1
            candidates += examined
            induced += sum(all_actual.values())
            maximal += sum(maximal_actual.values())
    arithmetic_pairs = 0
    for r in range(1,9):
        for n in range(2*r+1,121):
            a = predicted(n,r,False)
            m = predicted(n,r,True)
            lo = (n+3*r+1)//(3*r+2)
            hi = n//(r+2)
            assert set(m)==set(range(lo,hi+1)), (n,r,m)
            assert set(a)==set(range(1,hi+1)), (n,r,a)
            if n % (r+2) == 0:
                assert m[hi] == r+2, (n,r,'max',m)
            if n % (3*r+2) == 0:
                assert m[lo] == 3*r+2, (n,r,'min',m)
            arithmetic_pairs += 1
    print('VERIFY_OK graph_instances=%d edge_subset_candidates=%d induced_matchings=%d maximal_induced_matchings=%d arithmetic_parameter_pairs=%d' %
          (instances,candidates,induced,maximal,arithmetic_pairs))

if __name__ == '__main__':
    run()
