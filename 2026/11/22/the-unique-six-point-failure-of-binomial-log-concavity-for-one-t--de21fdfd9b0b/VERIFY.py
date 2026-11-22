#!/usr/bin/env python3
"""Standalone exhaustive six-vertex certificate and independent direct wheel count."""
from itertools import combinations
from math import comb


def census(n):
    pairs = tuple(combinations(range(n), 2))
    edge_bit = {ab: 1 << j for j, ab in enumerate(pairs)}
    tri_data = []
    for t in combinations(range(n), 3):
        em = sum(edge_bit[ab] for ab in combinations(t, 2))
        vm = sum(1 << a for a in t)
        tri_data.append((em, vm))
    k4_edges = [sum(edge_bit[ab] for ab in combinations(s, 2)) for s in combinations(range(n), 4)]
    subset_buckets = [[s for s in range(1 << n) if s.bit_count() == k] for k in range(n+1)]
    count_k4free = 0
    bad_count = 0
    bad_signatures = {}
    violating_indices = {}
    for e in range(1 << len(pairs)):
        if any(e & c == c for c in k4_edges):
            continue
        count_k4free += 1
        triangles = [vm for em, vm in tri_data if e & em == em]
        f = [sum(all(s & t != t for t in triangles) for s in bucket)
             for bucket in subset_buckets]
        bad = [k for k in range(1, n) if
               f[k]**2 * comb(n, k-1) * comb(n, k+1) <
               f[k-1] * f[k+1] * comb(n, k)**2]
        if bad:
            bad_count += 1
            degrees = tuple(sorted(sum(bool(e & edge_bit[(min(i,j), max(i,j))])
                                       for j in range(n) if j != i) for i in range(n)))
            sig = (degrees, tuple(f))
            bad_signatures[sig] = bad_signatures.get(sig, 0) + 1
            for k in bad:
                violating_indices[k] = violating_indices.get(k, 0) + 1
    return count_k4free, bad_count, bad_signatures, violating_indices


def direct_wheel():
    n = 6
    edges = {(0, i) for i in range(1, 6)}
    edges.update({tuple(sorted((i, i % 5 + 1))) for i in range(1, 6)})
    out = [0] * (n+1)
    for s in range(1 << n):
        vertices = [i for i in range(n) if (s >> i) & 1]
        triangles = [tr for tr in combinations(vertices, 3)
                     if all(tuple(sorted(ab)) in edges for ab in combinations(tr, 2))]
        if not triangles:
            out[len(vertices)] += 1
    assert out == [1, 6, 15, 15, 5, 1, 0], out
    # normalized k=3,4,5 inequality and its exact positive reversal gap
    # Use exact rational arithmetic for the normalized inequality.
    from fractions import Fraction
    b3 = Fraction(out[3], comb(n,3))
    b4 = Fraction(out[4], comb(n,4))
    b5 = Fraction(out[5], comb(n,5))
    assert b3 == Fraction(3,4) and b4 == Fraction(1,3) and b5 == Fraction(1,6)
    assert b3 * b5 - b4 * b4 == Fraction(1,72)
    return out


def main():
    for n in range(0, 7):
        admissible, bad, signatures, indices = census(n)
        print(f'n={n} K4free_labelled={admissible} bad_labelled={bad} indices={indices}')
        if n <= 5:
            assert bad == 0
        else:
            assert bad == 72, (bad,signatures)
            expected_sig = ((3,3,3,3,3,5), (1,6,15,15,5,1,0))
            assert signatures == {expected_sig:72}, signatures
            assert indices == {4:72}, indices
            # A six-vertex graph with one universal vertex, each other
            # vertex degree 3 has a 2-regular five-vertex induced graph.
            # The only such simple graph is C5, so all are wheels.
    print('W6:', direct_wheel())
    print('EXHAUSTIVE_K4_FREE_BINOMIAL_THRESHOLD_OK')

if __name__ == '__main__':
    main()
