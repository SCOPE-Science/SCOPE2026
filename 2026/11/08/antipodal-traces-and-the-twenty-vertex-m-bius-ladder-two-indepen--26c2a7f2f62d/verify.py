#!/usr/bin/env python3
"""Finite certificate for the P3-free complex on the 20-vertex Mobius ladder.

Run with Python 3.9 or later; no third-party packages are needed.
"""
from collections import Counter, deque
from itertools import combinations

N = 20
HALF = N // 2
ORDER = (19, 7, 3, 15, 17, 9, 11, 6, 10, 18, 12, 14, 16, 1, 2, 4, 0, 8, 5, 13)


def graph():
    edges = set()
    for i in range(N):
        edges.add(tuple(sorted((i, (i + 1) % N))))
        edges.add((i, i + HALF) if i < HALF else (i - HALF, i))
    assert len(edges) == 30
    adj = [0] * N
    for u, v in sorted(edges):
        adj[u] |= 1 << v
        adj[v] |= 1 << u
    assert all(a.bit_count() == 3 for a in adj)
    return adj, edges


def two_enumerations(adj):
    # First construction: direct induced-degree test (equivalent to components <=2).
    direct = []
    for mask in range(1, 1 << N):
        if all(not(mask & (1 << v)) or (mask & adj[v]).bit_count() <= 1
               for v in range(N)):
            direct.append(mask)
    # Second construction: list all forbidden triples as independent 3-element masks.
    forbidden = set()
    for v in range(N):
        neighbors = [u for u in range(N) if adj[v] & (1 << u)]
        for u, w in combinations(neighbors, 2):
            forbidden.add((1 << u) | (1 << v) | (1 << w))
    by_triples = [mask for mask in range(1, 1 << N)
                  if not any(mask & tri == tri for tri in forbidden)]
    assert direct == by_triples
    return sorted(direct, key=lambda f: (f.bit_count(), f)), len(forbidden)


def matching(faces):
    # Deterministic iterated element matching, with no use of the empty simplex.
    remaining = set(faces)
    pairs = {}
    for v in ORDER:
        bit = 1 << v
        for lower in faces:
            if lower in remaining and not (lower & bit):
                upper = lower | bit
                if upper in remaining:
                    pairs[lower] = upper
                    remaining.remove(lower)
                    remaining.remove(upper)
    assert len(set(pairs).intersection(set(pairs.values()))) == 0
    assert 2 * len(pairs) + len(remaining) == len(faces)
    return pairs, remaining


def check_acyclicity(faces, pairs):
    # Cover relations point from the higher to the lower face, except reversed
    # on the matching. Empty face is omitted from the face poset.
    idx = {f: i for i, f in enumerate(faces)}
    successors = [[] for _ in faces]
    indegree = [0] * len(faces)
    edges = 0
    matched_edges = 0
    for upper in faces:
        subset = upper
        while subset:
            bit = subset & -subset
            lower = upper ^ bit
            subset -= bit
            if not lower:
                continue
            if pairs.get(lower) == upper:
                source, target = idx[lower], idx[upper]
                matched_edges += 1
            else:
                source, target = idx[upper], idx[lower]
            successors[source].append(target)
            indegree[target] += 1
            edges += 1
    queue = deque(i for i, d in enumerate(indegree) if d == 0)
    visited = 0
    while queue:
        v = queue.popleft()
        visited += 1
        for w in successors[v]:
            indegree[w] -= 1
            if indegree[w] == 0:
                queue.append(w)
    assert visited == len(faces), 'Matching directed graph contains a cycle'
    assert matched_edges == len(pairs)
    return edges, visited


def halfturn(mask):
    lo = mask & ((1 << HALF) - 1)
    hi = mask >> HALF
    return (lo << HALF) | hi


def cycle_independence_value(n):
    # f_m=I(P_m;-1), f_0=1, f_1=0, f_m=f_{m-1}-f_{m-2}.
    f = [1, 0]
    for m in range(2, n):
        f.append(f[m-1] - f[m-2])
    return f[n-1] - f[n-3]


def halfturn_trace(faces):
    # Reduced alternating simplicial-chain trace includes -1 from C_{-1}.
    trace = -1
    counts = Counter()
    for face in faces:
        if halfturn(face) != face:
            continue
        k = face.bit_count() // 2
        counts[k] += 1
        trace += (-1) ** ((face.bit_count() - 1) + k)
    return trace, dict(sorted(counts.items()))


def main():
    adj, edges = graph()
    faces, forbidden_triples = two_enumerations(adj)
    dims = dict(sorted(Counter(f.bit_count() - 1 for f in faces).items()))
    assert len(faces) == 53670
    assert dims == {0:20,1:190,2:1080,3:3975,4:9624,5:15050,
                    6:14340,7:7505,8:1760,9:126}
    reduced_chi = sum((-1) ** d * count for d, count in dims.items()) - 1
    assert reduced_chi == -23
    pairs, critical = matching(faces)
    critical_dims = dict(sorted(Counter(f.bit_count() - 1 for f in critical).items()))
    assert len(pairs) == 26823
    assert critical_dims == {0:1,7:23}
    cover_edges, visited = check_acyclicity(faces, pairs)
    trace, fixed_counts = halfturn_trace(faces)
    assert trace == 1
    assert cycle_independence_value(10) == -1
    assert trace == -cycle_independence_value(10)
    # In reduced homology only H_7 is nonzero. Therefore trace(H_7)=-trace.
    h7_trace = -trace
    assert h7_trace == -1
    plus = (23 + h7_trace) // 2
    minus = (23 - h7_trace) // 2
    assert (plus, minus) == (11,12)
    assert [cycle_independence_value(i) for i in range(3, 9)] == [-2,-1,1,2,1,-1]
    print('GRAPH vertices=20 edges=30 forbidden_triples=%d' % forbidden_triples)
    print('FACES nonempty=%d f_vector=%s' % (len(faces), dims))
    print('REDUCED_EULER_CHARACTERISTIC', reduced_chi)
    print('MORSE matched_pairs=%d critical=%s' % (len(pairs), critical_dims))
    print('ACYCLIC covering_relations=%d visited=%d' % (cover_edges, visited))
    print('HALFTURN fixed_simplex_orbits_by_pairs=%s' % fixed_counts)
    print('HALFTURN reduced_lefschetz=%d cycle_polynomial_at_minus_one=%d' %
          (trace, cycle_independence_value(10)))
    print('H7 rank=23 involution_trace=%d rational_plus=%d rational_minus=%d' %
          (h7_trace, plus, minus))
    print('ALL_MOBIUS_DISSOCIATION_CHECKS_PASS')


if __name__ == '__main__':
    main()
