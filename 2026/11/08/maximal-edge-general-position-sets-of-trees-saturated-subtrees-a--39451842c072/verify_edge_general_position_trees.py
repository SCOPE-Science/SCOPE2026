#!/usr/bin/env python3
"""Independent finite checks for edge-general-position counts on trees.

Only the Python standard library is required. Each edge subset is tested
against the unique simple paths between every pair of vertices. The two
polynomial recurrences are evaluated separately and compared coefficientwise.
"""
from collections import Counter
from itertools import product
from heapq import heapify, heappop, heappush
from math import comb, prod
import random


def add(*polynomials):
    result = Counter()
    for poly in polynomials:
        for degree, coefficient in poly.items():
            result[degree] += coefficient
    return +result


def mul(left, right):
    result = Counter()
    for i, a in left.items():
        for j, b in right.items():
            result[i + j] += a * b
    return +result


def rooted_recursions(n, edges):
    neighbors = [[] for _ in range(n)]
    for a, b in edges:
        neighbors[a].append(b)
        neighbors[b].append(a)
    parent = [-1] * n
    parent[0] = 0
    order = [0]
    for v in order:
        for w in neighbors[v]:
            if parent[w] == -1:
                parent[w] = v
                order.append(w)
    children = [[u for u in neighbors[v] if u != parent[v]] for v in range(n)]

    # A_v weights descendant leaves, where the parent edge is included.
    A, B, sums = {}, {}, {}
    for v in reversed(order):
        q, s = {0: 1}, {}
        for u in children[v]:
            q = mul(q, add({0: 1}, A[u]))
            s = add(s, A[u])
        B[v], sums[v] = q, s
        A[v] = add({1: 1}, q, {0: -1})

    leaf_census = Counter()
    for v in order:
        s = sums[v]
        leaf_census = add(leaf_census,
                          {degree + 1: count for degree, count in s.items()},
                          B[v], {0: -1},
                          {degree: -count for degree, count in s.items()})
    all_poly = add({0: 1, 1: n - 1, 2: -(n - 1)}, leaf_census)

    # C_v weights permitted full-or-terminal descendant subtrees.
    C = {}
    for v in reversed(order):
        ch = children[v]
        if not ch:
            C[v] = {1: 1}
        else:
            p = {0: 1}
            for u in ch:
                p = mul(p, C[u])
            C[v] = add({1: 1}, p)

    saturated = Counter()
    for v in order:
        row = Counter()
        for u in children[v]:
            for degree, count in C[u].items():
                row[degree + 1] += count
        if v == 0 and len(children[v]) >= 2:
            p = {0: 1}
            for u in children[v]:
                p = mul(p, C[u])
            row = add(row, p)
        saturated = add(saturated, row)
    maximal_poly = add(saturated, {2: -(n - 1)})
    return all_poly, maximal_poly


def brute_polynomials(n, edges):
    neighbors = [[] for _ in range(n)]
    for eid, (a, b) in enumerate(edges):
        neighbors[a].append((b, eid))
        neighbors[b].append((a, eid))
    geodesics = []
    for start in range(n):
        queue = [(start, -1, 0)]
        for v, predecessor, bits in queue:
            if v > start:
                geodesics.append(bits)
            for w, eid in neighbors[v]:
                if w != predecessor:
                    queue.append((w, v, bits | (1 << eid)))
    m = len(edges)
    valid = [all((mask & path).bit_count() <= 2 for path in geodesics)
             for mask in range(1 << m)]
    all_counts, maximal_counts = Counter(), Counter()
    for mask, is_valid in enumerate(valid):
        if not is_valid:
            continue
        size = mask.bit_count()
        all_counts[size] += 1
        if all(not valid[mask | (1 << eid)]
               for eid in range(m) if not mask & (1 << eid)):
            maximal_counts[size] += 1
    return +all_counts, +maximal_counts, sum(valid)


def prufer_tree(seq):
    n = len(seq) + 2
    degree = [1] * n
    for v in seq:
        degree[v] += 1
    available = [v for v in range(n) if degree[v] == 1]
    heapify(available)
    edges = []
    for v in seq:
        leaf = heappop(available)
        edges.append((leaf, v))
        degree[leaf] -= 1
        degree[v] -= 1
        if degree[v] == 1:
            heappush(available, v)
    a, b = available
    edges.append((a, b))
    return edges


def branch_arm_product(n, edges):
    neighbors = [[] for _ in range(n)]
    for a, b in edges:
        neighbors[a].append(b)
        neighbors[b].append(a)
    branching = [v for v in range(n) if len(neighbors[v]) >= 3]
    if not branching:
        return comb(n - 1, 2)
    lengths = []
    for v in branching:
        for u in neighbors[v]:
            last, curr, length = v, u, 1
            while len(neighbors[curr]) == 2:
                nxt = next(w for w in neighbors[curr] if w != last)
                last, curr = curr, nxt
                length += 1
            if len(neighbors[curr]) == 1:
                lengths.append(length)
    return prod(lengths)


def two_edge_maximal_count(n, edges):
    neighbors = [[] for _ in range(n)]
    for a, b in edges:
        neighbors[a].append(b)
        neighbors[b].append(a)
    total = 0
    for v in range(n):
        if len(neighbors[v]) == 2:
            continue
        for w in neighbors[v]:
            if len(neighbors[w]) != 2 and v > w:
                continue
            last, curr, length = v, w, 1
            while len(neighbors[curr]) == 2:
                nxt = next(u for u in neighbors[curr] if u != last)
                last, curr = curr, nxt
                length += 1
            if len(neighbors[curr]) != 2 and v > curr:
                continue
            total += comb(length, 2)
    return total


def check(n, edges):
    all_expected, maximal_expected = rooted_recursions(n, edges)
    all_direct, maximal_direct, valid_count = brute_polynomials(n, edges)
    assert all_expected == all_direct, (n, edges, all_expected, all_direct)
    assert maximal_expected == maximal_direct, (n, edges, maximal_expected, maximal_direct)
    degrees = Counter(x for edge in edges for x in edge)
    nonleaf_min = min(degrees[v] for v in range(n) if degrees[v] >= 2)
    assert min(maximal_expected) == nonleaf_min, (n, edges, maximal_expected)
    leaf_count = sum(degrees[v] == 1 for v in range(n))
    assert max(maximal_expected) == leaf_count
    assert maximal_expected[leaf_count] == branch_arm_product(n, edges)
    assert maximal_expected.get(2, 0) == two_edge_maximal_count(n, edges)
    return valid_count, sum(maximal_direct.values())


def main():
    cases = valid_total = maximal_total = 0
    for n in range(3, 8):
        for code in product(range(n), repeat=n - 2):
            v, m = check(n, prufer_tree(code))
            cases += 1
            valid_total += v
            maximal_total += m
    random.seed(20261103)
    random_cases = 0
    for n in range(8, 11):
        for _ in range(150):
            code = [random.randrange(n) for _ in range(n - 2)]
            v, m = check(n, prufer_tree(code))
            cases += 1
            random_cases += 1
            valid_total += v
            maximal_total += m
    print(f"VERIFY_OK labeled_trees_n3_to7=18247 "
          f"additional_trees_n8_to10={random_cases} "
          f"instances={cases} valid_edge_sets={valid_total} "
          f"maximal_edge_sets={maximal_total} "
          f"both_polynomials=PASS lower_number=PASS "
          f"upper_number=PASS extremal_counts=PASS")


if __name__ == '__main__':
    main()
