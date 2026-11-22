#!/usr/bin/env python3
"""Exact finite labelled-graph census and independent fan identities.
Scientific checks only; Python 3 standard library suffices.
"""
from itertools import combinations


def convolution(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def sub(a, b):
    return [(a[k] if k < len(a) else 0) - (b[k] if k < len(b) else 0)
            for k in range(max(len(a), len(b)))]


def independent_polynomials(n, edges):
    Z = [0] * (n + 1)
    singles = [[0] * (n + 1) for _ in range(n)]
    doubles = {(i, j): [0] * (n + 1) for i in range(n) for j in range(i + 1, n)}
    for subset in range(1 << n):
        if any((subset >> u & 1) and (subset >> v & 1) for u, v in edges):
            continue
        k = subset.bit_count()
        Z[k] += 1
        occupied = [i for i in range(n) if subset >> i & 1]
        for i in occupied:
            singles[i][k] += 1
        for i, j in combinations(occupied, 2):
            doubles[i, j][k] += 1
    return Z, singles, doubles


def is_fan_endpoint_pair(n, edges, u, v):
    if n != 5:
        return False
    edge_set = set(edges)
    deg = [sum(k in e for e in edge_set) for k in range(n)]
    centers = [i for i in range(n) if deg[i] == 4]
    if len(centers) != 1:
        return False
    rem = [i for i in range(n) if i != centers[0]]
    remaining_edges = [e for e in edge_set if centers[0] not in e]
    if len(remaining_edges) != 3:
        return False
    rem_deg = [sum(i in e for e in remaining_edges) for i in rem]
    if sorted(rem_deg) != [1, 1, 2, 2]:
        return False
    return sorted((u, v)) == sorted(i for i in rem if sum(i in e for e in remaining_edges) == 1)


def trim(v):
    while len(v) > 1 and v[-1] == 0:
        v.pop()
    return v


def path_poly(n):
    if n == 0:
        return [1]
    a, b = [1], [1, 1]
    for _ in range(2, n + 1):
        z_a = [0] + a
        b, a = [(b[k] if k < len(b) else 0) + (z_a[k] if k < len(z_a) else 0) for k in range(max(len(b), len(z_a)))], b
    return trim(b)


def fan_graph(n):
    return n + 1, [(i, i + 1) for i in range(n - 1)] + [(i, n) for i in range(n)]


def run():
    graph_count, pair_count, exceptional_graphs, exceptional_pairs = 0, 0, set(), 0
    for n in range(1, 6):
        potential_edges = list(combinations(range(n), 2))
        for edge_mask in range(1 << len(potential_edges)):
            edges = [edge for j, edge in enumerate(potential_edges) if edge_mask >> j & 1]
            Z, singles, doubles = independent_polynomials(n, edges)
            graph_count += 1
            for i, j in combinations(range(n), 2):
                pair_count += 1
                C = sub(convolution(doubles[i, j], Z), convolution(singles[i], singles[j]))
                mixed = any(x > 0 for x in C) and any(x < 0 for x in C)
                if mixed:
                    assert is_fan_endpoint_pair(n, edges, i, j), (n, edges, i, j, C)
                    assert trim(C) == [0, 0, 0, 1, -1], (n, edges, i, j, C)
                    assert trim(Z[:]) == [1, 5, 3]
                    exceptional_pairs += 1
                    exceptional_graphs.add((n, edge_mask))
                if is_fan_endpoint_pair(n, edges, i, j):
                    assert mixed
    assert graph_count == 1099, graph_count
    assert pair_count == 10650, pair_count
    assert len(exceptional_graphs) == exceptional_pairs == 60, (len(exceptional_graphs), exceptional_pairs)

    # Independent coefficient-polynomial check of the all-n fan formula,
    # supplementary to the exact continuant proof.
    for n in range(4, 12):
        nv, edges = fan_graph(n)
        Z, A, B = independent_polynomials(nv, edges)
        C = trim(sub(convolution(B[0, n - 1], Z), convolution(A[0], A[n - 1])))
        inside = path_poly(n - 4)
        inside = inside[:] + [0] * max(0, n - 2 - len(inside))
        inside[n - 3] += -1 if n % 2 == 0 else 1
        rhs = [0, 0, 0] + inside
        assert C == trim(rhs), (n, C, rhs)
    print('PASS labelled_graphs=1099 vertex_pairs=10650 unique_exceptional_labelled_graphs=60')
    print('PASS fan_cassini_identity n=4..11')


if __name__ == '__main__':
    run()
