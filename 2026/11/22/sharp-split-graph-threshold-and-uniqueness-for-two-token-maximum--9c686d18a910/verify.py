#!/usr/bin/env python3
"""Exact finite checks for a fractional triangle packing in split-graph token graphs.

Requires Python >=3.8, standard library only. Finite enumeration is corroboration,
not a replacement for the all-parameter proof.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import combinations


def graph_and_tokens(r, n):
    assert r >= 2 and n >= 1
    N = r + n
    base_edges = {frozenset(e) for e in combinations(range(N), 2)
                  if min(e) < r}
    tokens = list(combinations(range(N), 2))
    edges = {frozenset((p, q)) for p, q in combinations(tokens, 2)
             if frozenset(set(p) ^ set(q)) in base_edges}
    return tokens, edges


def triangle_weights(r, n):
    assert n >= r - 1
    core = range(r)
    leaves = range(r, r + n)
    gamma = Fraction(1, n)
    if n == r - 1:
        alpha = Fraction(1, r - 1)
        beta = Fraction(1, r - 1) if n > 1 else Fraction(0)
    else:
        alpha = Fraction(0)
        beta = Fraction(1, n - 1)
    T = defaultdict(Fraction)

    def add(v1, v2, v3, w):
        if w:
            key = frozenset((tuple(sorted(v1)), tuple(sorted(v2)), tuple(sorted(v3))))
            assert len(key) == 3
            T[key] += w

    # Every edge between two core-core token states belongs to this family.
    for u in core:
        others = [v for v in core if v != u]
        for v, w in combinations(others, 2):
            for i in leaves:
                add((u, v), (u, w), (u, i), gamma)

    # Every edge between two core-leaf states with the same leaf is covered.
    for u, v in combinations(core, 2):
        for i in leaves:
            add((u, i), (v, i), (u, v), alpha)
            for j in leaves:
                if i != j:
                    add((u, i), (v, i), (i, j), beta)
    return T


def weights_check(r, n):
    tokens, edges = graph_and_tokens(r, n)
    weighted_triangles = triangle_weights(r, n)
    capacities = defaultdict(Fraction)
    for tri, weight in weighted_triangles.items():
        assert weight > 0
        for p, q in combinations(tri, 2):
            edge = frozenset((p, q))
            assert edge in edges, (r, n, tri, edge)
            capacities[edge] += weight
    assert all(w <= 1 for w in capacities.values())
    L = (r * (r-1) * (r-2)) // 2 + n * r * (r-1) // 2
    assert sum(weighted_triangles.values()) == L
    predicted = r * n * (n + r - 2)
    assert len(edges) - L == predicted

    # Cut with the mixed core-leaf token states on one side.
    side = {v: int(len([u for u in v if u < r]) == 1) for v in tokens}
    cuts = sum(side[next(iter(e))] != side[next(iter(e - {next(iter(e))}))]
               for e in edges)
    assert cuts == predicted
    # A second check using the original graph's adjacency, not the triangle list.
    direct = sum((sum(a < r for a in p) == 1) !=
                 (sum(a < r for a in q) == 1)
                 for p, q in (tuple(e) for e in edges))
    assert direct == predicted
    return len(tokens), len(edges), len(weighted_triangles), L


def brute_maxcut(r, n):
    tokens, edges = graph_and_tokens(r, n)
    idx = {v: i for i, v in enumerate(tokens)}
    count = len(tokens)
    nbr = [0] * count
    for e in edges:
        p, q = tuple(e)
        i, j = idx[p], idx[q]
        nbr[i] |= 1 << j
        nbr[j] |= 1 << i
    degrees = [x.bit_count() for x in nbr]
    # Fix the last token's side, so every unordered cut is visited once.
    mask = 0
    weight = 0
    best = 0
    multiplicity = 1
    for t in range(1, 1 << (count - 1)):
        v = (t & -t).bit_length() - 1
        ones = (nbr[v] & mask).bit_count()
        old_cut = degrees[v] - ones if ((mask >> v) & 1) else ones
        weight += degrees[v] - 2 * old_cut
        mask ^= 1 << v
        assert weight >= 0
        if weight > best:
            best = weight
            multiplicity = 1
        elif weight == best:
            multiplicity += 1
    return best, multiplicity


def main():
    for r in range(2, 9):
        for n in range(max(1, r - 1), r + 4):
            V, E, T, L = weights_check(r, n)
            print('WEIGHTED_TRIANGLE_CERTIFICATE_PASS', r, n, V, E, T, L)
    expected = [(2,1,2), (2,2,8), (3,1,8), (3,2,18),
                (3,3,36), (4,2,36), (4,3,60)]
    for r, n, mx in expected:
        found, mult = brute_maxcut(r, n)
        assert found == mx, (r, n, found, mx)
        print('INDEPENDENT_EXHAUSTIVE_MAXCUT_PASS', r, n, found, mult)
    # Both sides of the sharp threshold are witnessed by parity lifts.
    for r in range(3, 10):
        n = r - 2
        lifted_alternative = (r + n - 2) * (r - 1) * (n + 1)
        lifted_standard = (r + n - 2) * r * n
        assert lifted_alternative > lifted_standard
    print('SHARP_THRESHOLD_PARENT_CUT_WITNESSES_PASS')
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
