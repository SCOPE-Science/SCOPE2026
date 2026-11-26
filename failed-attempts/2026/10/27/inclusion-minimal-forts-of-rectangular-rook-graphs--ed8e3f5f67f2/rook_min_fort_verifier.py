#!/usr/bin/env python3
"""Finite definition-based and independently enumerated checks for rook-graph forts.

Standard-library only. Each board cell is a vertex of the rook graph. The test
constructs all open neighborhoods directly, enumerates all subsets, and compares
minimal forts with a classification and separately counted candidate families.
"""
from collections import Counter
from functools import lru_cache
from itertools import combinations
from math import comb, factorial


def graph_adj(p, q):
    return [sum(1 << (k*q+l) for k in range(p) for l in range(q)
                if (k == i or l == j) and (k, l) != (i, j))
            for i in range(p) for j in range(q)]


def is_fort(mask, adj):
    return mask != 0 and all((mask >> v) & 1 or
                             (mask & adj[v]).bit_count() != 1
                             for v in range(len(adj)))


def classify(mask, p, q):
    edges = [(i, j) for i in range(p) for j in range(q)
             if (mask >> (i*q+j)) & 1]
    rd, cd = [0]*p, [0]*q
    for i, j in edges:
        rd[i] += 1
        cd[j] += 1
    er, ec = rd.count(0), cd.count(0)
    parent = list(range(p+q))
    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a
    cyclic = False
    for i, j in edges:
        a, b = find(i), find(p+j)
        if a == b:
            cyclic = True
        else:
            parent[a] = b
    high_degree_per_component = Counter(find(v) for v, d in
                                         enumerate(rd+cd) if d > 1)
    stars = not cyclic and max(high_degree_per_component.values(), default=0) <= 1
    if er == ec == 0 and stars:
        if (1 in rd or all(d == 2 for d in rd)) and \
           (1 in cd or all(d == 2 for d in cd)):
            return 'spanning_star_forests'
    if er == 0 and ec > 0 and all(d == 2 for d in rd) and not cyclic:
        return 'row_subdivision_forests'
    if er > 0 and ec == 0 and all(d == 2 for d in cd) and not cyclic:
        return 'column_subdivision_forests'
    if (er or ec) and len(edges) >= 4 and all(d in (0, 2) for d in rd+cd):
        if len({find(v) for v, d in enumerate(rd+cd) if d}) == 1:
            return 'alternating_cycles'
    return None


def minimum_forts_by_definition(p, q):
    adj = graph_adj(p, q)
    minimum = []
    for mask in range(1, 1 << (p*q)):
        if is_fort(mask, adj) and not any((mask & f) == f for f in minimum):
            minimum.append(mask)
    # Any proper subset of a positive integer bitmask has smaller integer value.
    return minimum


def spanning_star_forest_coefficients(p, q):
    """Count spanning labeled bipartite star forests by canonical component recursion.

    A component containing the least remaining row is either a row-centered
    star (one row, one or more columns), or a column-centered star (at least
    two rows, one column). Flag whether each bipartition has a degree-one vertex.
    """
    @lru_cache(None)
    def solve(rows, cols):
        if not rows and not cols:
            return Counter({(0, False, False): 1})
        if not rows or not cols:
            return Counter()
        i = rows[0]
        rest = rows[1:]
        result = Counter()
        # Row-centered stars, including the two-vertex component.
        for k in range(1, len(cols)+1):
            for group in combinations(cols, k):
                others = tuple(c for c in cols if c not in group)
                for (weight, rleaf, cleaf), count in solve(rest, others).items():
                    result[(weight+k, rleaf or k == 1, True)] += count
        # First row as a leaf of a nontrivial column-centered star.
        for j in cols:
            others = tuple(c for c in cols if c != j)
            for k in range(1, len(rest)+1):
                for group in combinations(rest, k):
                    remrows = tuple(r for r in rest if r not in group)
                    for (weight, rleaf, cleaf), count in solve(remrows, others).items():
                        result[(weight+k+1, True, cleaf)] += count
        return result
    all_cases = solve(tuple(range(p)), tuple(range(q)))
    result = Counter()
    for (size, has_row_leaf, has_col_leaf), count in all_cases.items():
        if has_row_leaf and has_col_leaf:
            result[size] += count
    if q == 2*p:
        result[2*p] += factorial(q)//(2**p)
    if p == 2*q:
        result[2*q] += factorial(p)//(2**q)
    return result


def forests_with_isolate(vertices, edges):
    if edges < 0 or edges > comb(vertices, 2):
        return 0
    pairs = list(combinations(range(vertices), 2))
    good = 0
    for selected in combinations(pairs, edges):
        parent = list(range(vertices))
        deg = [0]*vertices
        def find(x):
            while parent[x] != x:
                x = parent[x]
            return x
        cyclic = False
        for a, b in selected:
            deg[a] += 1
            deg[b] += 1
            a, b = find(a), find(b)
            if a == b:
                cyclic = True
                break
            parent[a] = b
        if not cyclic and 0 in deg:
            good += 1
    return good


def cycle_count(p, q, k):
    if k < 2 or k > min(p, q) or k == p == q:
        return 0
    return comb(p, k)*comb(q, k)*factorial(k)*factorial(k-1)//2


def coefficients_from_independent_counts(p, q):
    result = spanning_star_forest_coefficients(p, q)
    result[2*p] += factorial(p)*forests_with_isolate(q, p)
    result[2*q] += factorial(q)*forests_with_isolate(p, q)
    for k in range(2, min(p, q)+1):
        result[2*k] += cycle_count(p, q, k)
    return dict(sorted((weight, count) for weight, count in result.items() if count))


def verify(p, q, exhaustive_classification=False):
    minima = minimum_forts_by_definition(p, q)
    family = Counter()
    actual = Counter()
    for mask in minima:
        kind = classify(mask, p, q)
        assert kind is not None, (p, q, mask)
        family[kind] += 1
        actual[mask.bit_count()] += 1
    if exhaustive_classification:
        minset = set(minima)
        for mask in range(1, 1 << (p*q)):
            assert bool(classify(mask, p, q)) == (mask in minset), (p, q, mask)
    expected = coefficients_from_independent_counts(p, q)
    assert dict(sorted(actual.items())) == expected, (p, q, actual, expected)
    return dict(sorted(actual.items())), dict(sorted(family.items()))


if __name__ == '__main__':
    boards = [(2,2),(2,3),(2,4),(2,5),(2,6),(3,3),(3,4),(3,5),(4,4),(4,5)]
    total_subsets = 0
    for p, q in boards:
        polynomial, families = verify(p, q, p*q <= 16)
        total_subsets += (1 << (p*q)) - 1
        print(f'{p}x{q} polynomial={polynomial} families={families}', flush=True)
    print(f'ALL_ASSERTIONS_PASSED full_nonempty_subsets={total_subsets}', flush=True)
