#!/usr/bin/env python3
"""Exact finite checks for Shapley-degree rankings of simple graph coverage games.

No external packages are needed. Cost is the sum of first-cover positions
of edges, counted from position 1. Every graph and every permutation is
examined at the stated finite orders.
"""
from functools import lru_cache
from itertools import combinations, permutations


def edge_index(n):
    return tuple(combinations(range(n), 2))


def edges_from_mask(n, mask):
    return tuple(e for j, e in enumerate(edge_index(n)) if mask >> j & 1)


def exact_costs(n, edges):
    """Subset DP for optimum and minimum over degree-nonincreasing orders."""
    deg = tuple(sum(v in e for e in edges) for v in range(n))
    full = (1 << n) - 1
    uncovered = [sum(not (s >> u & 1) and not (s >> v & 1)
                     for u, v in edges) for s in range(1 << n)]

    @lru_cache(None)
    def opt(s):
        if s == full:
            return 0
        return uncovered[s] + min(opt(s | (1 << v)) for v in range(n)
                                   if not (s >> v & 1))

    @lru_cache(None)
    def deg_sorted(s):
        if s == full:
            return 0
        remaining = [v for v in range(n) if not (s >> v & 1)]
        dmax = max(deg[v] for v in remaining)
        return uncovered[s] + min(deg_sorted(s | (1 << v)) for v in remaining
                                   if deg[v] == dmax)

    return opt(0), deg_sorted(0)


def brute_costs(n, edges):
    """Independent exhaustive permutation implementation."""
    deg = tuple(sum(v in e for e in edges) for v in range(n))
    ranked = sorted(deg, reverse=True)
    best = 10**20
    best_shapley = 10**20
    for p in permutations(range(n)):
        loc = [0] * n
        for i, v in enumerate(p):
            loc[v] = i + 1
        cost = sum(min(loc[u], loc[v]) for u, v in edges)
        best = min(best, cost)
        if [deg[v] for v in p] == ranked:
            best_shapley = min(best_shapley, cost)
    return best, best_shapley


def is_triangle_plus_edge(n, edges):
    if n != 5 or len(edges) != 4:
        return False
    deg = [sum(i in e for e in edges) for i in range(n)]
    hi = [i for i in range(n) if deg[i] == 2]
    lo = [i for i in range(n) if deg[i] == 1]
    if len(hi) != 3 or len(lo) != 2:
        return False
    es = set(tuple(sorted(e)) for e in edges)
    return all(tuple(sorted(e)) in es for e in combinations(hi, 2)) and tuple(lo) in es


def family_edges(k, q):
    es = []
    for b in range(k):
        es.extend(combinations(range(3*b, 3*b+3), 2))
    for b in range(q):
        es.append((3*k+2*b, 3*k+2*b+1))
    return 3*k + 2*q, tuple(es)


def formulas(k, q):
    n = 3*k + 2*q
    m = 3*k + q
    optimum_cost = (5*k*k+4*k*q+3*k+q*q+q)//2
    # The integer numerator is even for all integer k,q.
    sh_cost = optimum_cost + k*q
    return optimum_cost, sh_cost, (n+1)*m-optimum_cost


def integer_partitions(n, lower=1):
    if n == 0:
        yield ()
        return
    for first in range(lower, n+1):
        for rest in integer_partitions(n-first, first):
            yield (first,) + rest


def clique_union(sizes):
    edges = []
    offset = 0
    for size in sizes:
        edges.extend((offset+i, offset+j) for i,j in combinations(range(size),2))
        offset += size
    return offset, tuple(edges)


def clique_union_opt_auc(sizes):
    n = sum(sizes)
    marginal = sorted((g for s in sizes for g in range(s)), reverse=True)
    return sum((n-i)*g for i,g in enumerate(marginal))


def run():
    total = 0
    failures_by_n = {}
    for n in range(1, 6):
        bad = []
        for graph_mask in range(1 << len(edge_index(n))):
            edges = edges_from_mask(n, graph_mask)
            dp = exact_costs(n, edges)
            brute = brute_costs(n, edges)
            assert dp == brute, (n, graph_mask, dp, brute)
            if dp[1] != dp[0]:
                assert n == 5
                assert dp[1] - dp[0] == 1
                assert is_triangle_plus_edge(n, edges)
                bad.append(graph_mask)
            total += 1
        failures_by_n[n] = len(bad)
        assert len(bad) == (10 if n == 5 else 0), (n, len(bad))
    assert total == 1+2+8+64+1024
    print('Finite graph classification PASS:', total, 'graphs, all permutations; failures', failures_by_n)

    checked = 0
    for k in range(1, 4):
        for q in range(1, 4):
            n, edges = family_edges(k, q)
            dp_opt, dp_ranked = exact_costs(n, edges)
            expect_opt, expect_ranked, expect_auc = formulas(k, q)
            assert (dp_opt, dp_ranked) == (expect_opt, expect_ranked), (k, q, dp_opt, dp_ranked)
            assert (n+1)*len(edges)-dp_opt == expect_auc
            checked += 1
    print('Infinite-family formula finite spot checks PASS:', checked, 'pairs (k,q), each by exact subset DP')
    clique_types = 0
    for n in range(1,11):
        for sizes in integer_partitions(n):
            size, edges = clique_union(sizes)
            opt, ranked = exact_costs(size, edges)
            auc = (size+1)*len(edges)-opt
            assert auc == clique_union_opt_auc(sizes), sizes
            different = len({s for s in sizes if s >= 2}) > 1
            assert (ranked > opt) == different, sizes
            clique_types += 1
    print('Disjoint-clique criterion PASS:', clique_types, 'unlabeled component-size profiles through n=10')
    assert formulas(1,1) == (7,8,17)
    print('Five-player witness PASS: optimum AUC 17, best Shapley AUC 16')


if __name__ == '__main__':
    run()
