#!/usr/bin/env python3
"""Exact certificate for a small two-neighbor complete-cascade reversal.

No external libraries.  All computations use integer bitmasks and counts.
Run: python3 verify.py
"""
from collections import Counter, defaultdict
from itertools import combinations, permutations

THETA = ((0, 1), (0, 4), (0, 5), (1, 2), (2, 3), (3, 4), (3, 5))
BARBELL = ((0, 1), (0, 2), (0, 3), (1, 2), (3, 4), (3, 5), (4, 5))
N = 6
EXPECTED_THETA = (0, 0, 0, 10, 14, 6, 1)
EXPECTED_BARBELL = (0, 0, 0, 12, 13, 6, 1)
EXPECTED_CONNECTED = (1, 1, 4, 38, 728, 26704)


def adjacency(n, edges):
    adj = [0] * n
    for u, v in edges:
        assert 0 <= u < v < n
        adj[u] |= 1 << v
        adj[v] |= 1 << u
    return tuple(adj)


def connected(adj):
    n = len(adj)
    if n == 0:
        return False
    reached = 1
    while True:
        more = reached
        for v in range(n):
            if reached & (1 << v):
                more |= adj[v]
        if more == reached:
            return reached == (1 << n) - 1
        reached = more


def closed_seed_set(adj, seed):
    """Synchronous monotone threshold-two closure; at most n strict rounds."""
    n = len(adj)
    while True:
        added = 0
        for v in range(n):
            if not seed & (1 << v) and (seed & adj[v]).bit_count() >= 2:
                added |= 1 << v
        if not added:
            return seed
        seed |= added


def profile(adj):
    n = len(adj)
    answer = [0] * (n + 1)
    for seed in range(1 << n):
        if closed_seed_set(adj, seed) == (1 << n) - 1:
            answer[seed.bit_count()] += 1
    return tuple(answer)


def degree_sequence(adj):
    return tuple(sorted(bits.bit_count() for bits in adj))


def is_fort(adj, subset):
    """Every vertex in the inactive subset has fewer than 2 external neighbors."""
    n = len(adj)
    outer = ((1 << n) - 1) ^ subset
    return bool(subset) and all(
        (adj[v] & outer).bit_count() < 2
        for v in range(n) if subset & (1 << v)
    )


def fort_profile(adj):
    """Independent static obstruction computation, without time evolution."""
    n = len(adj)
    forts = [u for u in range(1, 1 << n) if is_fort(adj, u)]
    answer = [0] * (n + 1)
    full = (1 << n) - 1
    for seed in range(1 << n):
        complement = full ^ seed
        if all((u & complement) != u for u in forts):
            answer[seed.bit_count()] += 1
    return tuple(answer)


def has_strict_ranking_reversal(a, b):
    d = [x - y for x, y in zip(a, b)]
    return min(d) < 0 < max(d)


def automorphisms(adj):
    n = len(adj)
    edges = {(u, v) for u in range(n) for v in range(u + 1, n) if adj[u] >> v & 1}
    total = 0
    for p in permutations(range(n)):
        moved = {tuple(sorted((p[u], p[v]))) for u, v in edges}
        total += moved == edges
    return total


def verify_all_graphs():
    n_connected = []
    crossing_by_order = []
    witness_profile_counts = Counter()
    for n in range(1, 7):
        all_edges = tuple(combinations(range(n), 2))
        classes = defaultdict(set)
        conn = 0
        for mask in range(1 << len(all_edges)):
            edges = (e for i, e in enumerate(all_edges) if mask & (1 << i))
            adj = adjacency(n, edges)
            if not connected(adj):
                continue
            conn += 1
            degrees = degree_sequence(adj)
            counts = profile(adj)
            classes[degrees].add(counts)
            if n == N and degrees == (2, 2, 2, 2, 3, 3):
                witness_profile_counts[counts] += 1
        reversals = []
        for degrees, distinct_profiles in classes.items():
            for a, b in combinations(sorted(distinct_profiles), 2):
                if has_strict_ranking_reversal(a, b):
                    reversals.append((degrees, a, b))
        n_connected.append(conn)
        crossing_by_order.append(reversals)
        print(f"n={n}, connected_labeled={conn}, degree_classes={len(classes)}, "
              f"reversing_profile_pairs={len(reversals)}")
    assert tuple(n_connected) == EXPECTED_CONNECTED
    assert all(not r for r in crossing_by_order[:5])
    assert crossing_by_order[5] == [
        ((2, 2, 2, 2, 3, 3), EXPECTED_THETA, EXPECTED_BARBELL)
    ]
    assert witness_profile_counts[EXPECTED_THETA] == 180
    assert witness_profile_counts[EXPECTED_BARBELL] == 90
    # Orbit-stabilizer proves each reversing profile is a single isomorphism class.
    theta_aut = automorphisms(adjacency(N, THETA))
    barbell_aut = automorphisms(adjacency(N, BARBELL))
    assert (theta_aut, barbell_aut) == (4, 8)
    assert 720 // theta_aut == witness_profile_counts[EXPECTED_THETA]
    assert 720 // barbell_aut == witness_profile_counts[EXPECTED_BARBELL]
    print('unique_reversing_unlabeled_pair=theta(2,2,3)/two_triangles_one_bridge')


def verify_witness():
    theta = adjacency(N, THETA)
    barbell = adjacency(N, BARBELL)
    assert degree_sequence(theta) == degree_sequence(barbell) == (2, 2, 2, 2, 3, 3)
    for adj, expected in ((theta, EXPECTED_THETA), (barbell, EXPECTED_BARBELL)):
        assert profile(adj) == expected
        assert fort_profile(adj) == expected
        # Every set of size <= 2 fails, as the 7 edges cannot support
        # the necessary 2*(6-2)=8 distinct predecessor edges.
        assert all(expected[k] == 0 for k in range(3))
    assert EXPECTED_BARBELL[3] - EXPECTED_THETA[3] == 2
    assert EXPECTED_THETA[4] - EXPECTED_BARBELL[4] == 1
    assert all(EXPECTED_THETA[k] == EXPECTED_BARBELL[k]
               for k in (0, 1, 2, 5, 6))
    # Under independent Bernoulli seeding of probability p, the difference
    # in full-cascade reliabilities is exactly p^3*(1-p)^2*(3*p-2).
    # Equivalently, -2 p^3(1-p)^3 + p^4(1-p)^2.
    for num in range(11):
        den = 10
        poly = sum((a - b) * num**k * (den - num)**(6 - k)
                   for k, (a, b) in enumerate(zip(EXPECTED_THETA, EXPECTED_BARBELL)))
        factor = num**3 * (den - num)**2 * (3 * num - 2 * den)
        assert poly == factor
    print('witness_profiles_and_fort_method=PASS; Bernoulli_reliability_factor=PASS')


if __name__ == '__main__':
    verify_witness()
    verify_all_graphs()
    print('ALL_CHECKS_PASSED')
