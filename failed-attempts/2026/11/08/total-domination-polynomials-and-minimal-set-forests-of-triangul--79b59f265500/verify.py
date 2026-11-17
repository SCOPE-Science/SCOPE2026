#!/usr/bin/env python3
"""Reproduce exact all-set and minimal total-domination counts for L(K_n).

Standard-library-only independent graph-level tests, with a separate
labeled-component recurrence that evaluates the proposed generating functions.
Run: python3 verify.py
"""
from math import comb, factorial
from collections import Counter
from itertools import combinations


def padd(a, b, factor=1):
    out = dict(a)
    for k, v in b.items():
        out[k] = out.get(k, 0) + factor * v
        if out[k] == 0:
            del out[k]
    return out


def pmul(a, b):
    out = Counter()
    for i, u in a.items():
        for j, v in b.items():
            out[i + j] += u * v
    return {k: v for k, v in out.items() if v}


def tree_count(s):
    """Number of admissible connected selected forests on s labeled base vertices."""
    if s < 3:
        return 0
    if s == 3:
        return 3
    if s == 4:
        return 16
    return s * sum(factorial(s - 1) //
                   (factorial(s - 1 - 2 * q) * factorial(q))
                   for q in range((s - 1) // 2 + 1))


def expected_minimal(n):
    # Count sets of components where every component is a permitted tree.
    f = {(0, 0): 1}
    for a in range(1, n):
        for c in range(1, a // 3 + 1):
            f[a, c] = sum(comb(a - 1, s - 1) * tree_count(s) *
                          f.get((a - s, c - 1), 0)
                          for s in range(3, a + 1))
    out = Counter()
    for c in range(1, (n - 1) // 3 + 1):
        out[n - 1 - c] += n * f.get((n - 1, c), 0)
    if n % 3 == 0:
        t = n // 3
        out[2 * t] += factorial(n) // (2 ** t * factorial(t))
    return {k: v for k, v in out.items() if v}


def expected_all(n):
    # Connected-graph species recurrence. The graph of selected base edges
    # may have at most one singleton component and no K_2 component.
    A = [{k: comb(comb(s, 2), k) for k in range(comb(s, 2) + 1)}
         for s in range(n + 1)]
    connected = [{} for _ in range(n + 1)]
    for s in range(1, n + 1):
        v = A[s]
        for t in range(1, s):
            v = padd(v, pmul(connected[t], A[s-t]), -comb(s-1, t-1))
        connected[s] = v
    clean = [{0: 1}] + [{} for _ in range(n)]
    for s in range(1, n + 1):
        v = {}
        for t in range(3, s + 1):
            v = padd(v, pmul(connected[t], clean[s-t]), comb(s-1,t-1))
        clean[s] = v
    return padd(clean[n], clean[n-1], n)


def graph_masks(n):
    edges = list(combinations(range(n), 2))
    adjacency = []
    for i, e in enumerate(edges):
        mask = sum(1 << j for j, f in enumerate(edges)
                   if i != j and (e[0] in f or e[1] in f))
        adjacency.append(mask)
    return edges, adjacency


def dominates(mask, adj):
    return all(mask & neighbor for neighbor in adj)


def minimal(mask, adj):
    return dominates(mask, adj) and all(
        not dominates(mask ^ (1 << i), adj)
        for i in range(len(adj)) if mask & (1 << i))


def graph_test(n, all_subsets):
    edges, adj = graph_masks(n)
    m = len(edges)
    count_all, count_min = Counter(), Counter()
    tests = 0
    if all_subsets:
        iterator = range(1 << m)
    else:
        # By the proved structural bound, every minimal total-dominating
        # set on n>=4 vertices uses at most n-2 selected edges.
        iterator = (sum(1 << i for i in indices)
                    for k in range(2, n - 1)
                    for indices in combinations(range(m), k))
    for mask in iterator:
        tests += 1
        if dominates(mask, adj):
            if all_subsets:
                count_all[mask.bit_count()] += 1
            if minimal(mask, adj):
                count_min[mask.bit_count()] += 1
    assert dict(count_min) == expected_minimal(n), (n, count_min, expected_minimal(n))
    if all_subsets:
        assert dict(count_all) == expected_all(n), (n, count_all, expected_all(n))
    return tests, sum(count_min.values()), sum(count_all.values())


def main():
    tested = minimal_sets = all_sets = 0
    for n in range(3, 9):
        # Exhaustive all subsets through n=7; for n=8 the proven upper
        # bound restricts the minimal-set search to sizes at most n-2.
        full = n <= 7
        q, r, s = graph_test(n, full)
        tested += q
        minimal_sets += r
        all_sets += s
        print(f"n={n} full={full} tested={q} minimal={r} ",
              dict(sorted(expected_minimal(n).items())))
    # Larger orders: exact coefficient arithmetic and attainable spectra.
    for n in range(4, 31):
        coeffs = expected_minimal(n)
        assert set(coeffs) == set(range((2*(n-1)+2)//3, n-1)), (n,coeffs)
        if n >= 7:
            val = sum(
                factorial(n) // (factorial(n-2-2*q) * factorial(q))
                for q in range((n-2)//2 + 1))
            assert coeffs[n-2] == val, n
    print("VERIFY_OK full_graph_orders=3..7 restricted_order=8",
          f"tested_subsets={tested}", f"minimal_sets={minimal_sets}",
          "all_and_minimal_polynomials=PASS", "arithmetic_orders=4..30")

if __name__ == "__main__":
    main()
