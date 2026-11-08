#!/usr/bin/env python3
"""Finite, reproducible checks for maximal threshold induced subsets of L(K_n).
Uses the forbidden-induced-subgraph criterion; does not rely on the counting proof.
Python 3 standard library. Run: python verify.py
"""
from collections import Counter
from itertools import combinations
from math import comb, factorial


def formula(n):
    m = n - 3
    out = Counter()
    for r in range(m // 2 + 1):
        x = factorial(m) // (factorial(m - 2*r) * 2**r * factorial(r))
        out[n-r] += 3 * comb(n, 3) * x
    if m % 2 == 0:
        x = factorial(m) // (2**(m//2) * factorial(m//2))
        out[n-m//2] -= 2 * comb(n,3) * x
    return {k:v for k,v in out.items() if v}


def brute(n):
    base_edges = list(combinations(range(n), 2))
    sz = len(base_edges)
    neighbors = [sum(1<<j for j,f in enumerate(base_edges)
                     if i != j and (set(e) & set(f)))
                 for i,e in enumerate(base_edges)]
    forbidden_by_vertex = [[] for _ in range(sz)]
    num_bad = 0
    for Q in combinations(range(sz), 4):
        degrees = sorted(sum(bool(neighbors[i] & (1<<j)) for j in Q) for i in Q)
        if degrees in ([1,1,1,1], [1,1,2,2], [2,2,2,2]):
            num_bad += 1
            for v in Q:
                forbidden_by_vertex[v].append(sum(1<<w for w in Q if w!=v))

    def can_add(S,v):
        return all((S&Q) != Q for Q in forbidden_by_vertex[v])

    counts = Counter()
    visited_good = 0
    def visit(v,S):
        nonlocal visited_good
        if v == sz:
            visited_good += 1
            if not any(can_add(S,w) for w in range(sz) if not (S>>w&1)):
                counts[S.bit_count()] += 1
            return
        visit(v+1,S)
        if can_add(S,v):
            visit(v+1,S|(1<<v))
    visit(0,0)
    return dict(counts), visited_good, num_bad


def main():
    total_good=0
    total_maximal=0
    for n in range(3,9):
        observed,good,bad = brute(n)
        predicted=formula(n)
        assert observed==predicted,(n,observed,predicted)
        assert sum(observed.values())==sum(predicted.values())
        total_good+=good; total_maximal+=sum(observed.values())
        print('n',n,'eligible',good,'maximal',sum(observed.values()),
              'size_counts',sorted(observed.items()),'forbidden_foursets',bad)
    print('VERIFY_OK n=3..8 eligible_sets=%d maximal_sets=%d formula_equality=true' %
          (total_good,total_maximal))

if __name__=='__main__':main()
