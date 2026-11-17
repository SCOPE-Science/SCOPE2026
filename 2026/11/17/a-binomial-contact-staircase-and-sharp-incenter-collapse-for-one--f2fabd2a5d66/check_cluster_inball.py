#!/usr/bin/env python3
"""Exact verification of Euclidean facet distances for a single-cluster ultrametric.

Requires only the Python standard library. The small-parameter vertex census uses
signed spanning trees of the complete weighted constraint graph, independently
of the explicit potential classification and quadratic optimization.
"""
from fractions import Fraction as F
from itertools import combinations, product
from math import comb
from collections import deque
import heapq


def prufer_edges(sequence, n):
    degree = [1] * n
    for x in sequence:
        degree[x] += 1
    leaves = [i for i in range(n) if degree[i] == 1]
    heapq.heapify(leaves)
    edges = []
    for x in sequence:
        leaf = heapq.heappop(leaves)
        edges.append((leaf, x))
        degree[leaf] -= 1
        degree[x] -= 1
        if degree[x] == 1:
            heapq.heappush(leaves, x)
    a, b = sorted(leaves)
    edges.append((a, b))
    return edges


def brute_vertices(m, t):
    n = m + 1
    vertices = set()
    for seq in product(range(n), repeat=n - 2):
        edges = prufer_edges(seq, n)
        for sign in product((-1, 1), repeat=n - 1):
            adjacency = [[] for _ in range(n)]
            for (a, b), s in zip(edges, sign):
                length = F(1) if a == 0 or b == 0 else t
                adjacency[a].append((b, s * length))
                adjacency[b].append((a, -s * length))
            potential = [None] * n
            potential[0] = F(0)
            queue = deque([0])
            while queue:
                a = queue.popleft()
                for b, delta in adjacency[a]:
                    if potential[b] is None:
                        potential[b] = potential[a] + delta
                        queue.append(b)
            if any(abs(x) > 1 for x in potential[1:]):
                continue
            if any(abs(potential[i] - potential[j]) > t
                   for i in range(1, n) for j in range(i + 1, n)):
                continue
            vertices.add(tuple(potential))
    return vertices


def predicted_vertices(m, t):
    vertices = set()
    for sign in (-1, 1):
        for k in range(1, m + 1):
            for subset in combinations(range(m), k):
                chosen = set(subset)
                leaf_values = [sign * (F(1) if i in chosen else 1 - t)
                               for i in range(m)]
                vertices.add((F(0), *leaf_values))
    return vertices


def norm_squared(vertex):
    n = len(vertex)
    return sum(x * x for x in vertex) - sum(vertex) ** 2 / n


def quadratic(m, t, k):
    n = m + 1
    return (m * (1 - t)**2 + k * (2*t - t*t)
            - (m * (1 - t) + k*t)**2 / n)


def matrix_rank_rational(rows):
    a = [list(row) for row in rows]
    if not a:
        return 0
    rank = 0
    for column in range(len(a[0])):
        pivot = next((i for i in range(rank, len(a)) if a[i][column]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        div = a[rank][column]
        a[rank] = [v/div for v in a[rank]]
        for i in range(len(a)):
            if i != rank and a[i][column]:
                mult = a[i][column]
                a[i] = [x - mult*y for x,y in zip(a[i], a[rank])]
        rank += 1
        if rank == len(a):
            break
    return rank


def check_case(m, t, exhaustive):
    classified = predicted_vertices(m, t)
    if exhaustive:
        enumerated = brute_vertices(m, t)
        assert enumerated == classified, (m, t, len(enumerated), len(classified),
                                          enumerated - classified, classified - enumerated)
    assert len(classified) == 2 * (2**m - 1)
    norms = {u: norm_squared(u) for u in classified}
    maximal = max(norms.values())
    values = [quadratic(m, t, k) for k in range(1, m+1)]
    assert maximal == max(values)
    maxima = {k for k in range(1, m+1) if values[k-1] == maximal}
    contacts = [u for u,q in norms.items() if q == maximal]
    assert len(contacts) == 2 * sum(comb(m, k) for k in maxima)
    alpha = F(m-1, 2) + 1/t
    assert maxima == {k for k in range(1, m+1)
                      if abs(F(k)-alpha) == min(abs(F(j)-alpha)
                                               for j in range(1,m+1))}
    rank = matrix_rank_rational([tuple(v[i] - sum(v)/len(v) for i in range(1,len(v)))
                                 for v in contacts])
    expected = 1 if maxima == {m} else m
    assert rank == expected, (m,t,maxima,rank,expected)
    return len(classified), len(contacts), rank


def main():
    count = total = 0
    for m in range(3,6):
        ts = sorted({F(1,5), F(1,3), F(1,2), F(2,3), F(3,4), F(9,10),
                     F(2,m)} | {F(2, 2*k-m+2)
                                 for k in range((m//2)+1,m)
                                 if 2*k-m+2 > 2})
        for t in ts:
            if t <= 0 or t >= 1: continue
            if m == 5 and t not in (F(2,5),F(2,3),F(9,10)): continue
            facets, contacts, rank = check_case(m, t, True)
            count += 1
            total += facets
    print('SIGNED_SPANNING_TREE_COMPLETE_VERTEX_ENUMERATION_PASS',
          'cases=',count, 'total_vertices=',total)
    for m in range(3,9):
        ts = {F(1,100),F(1,4),F(1,2),F(2,3),F(7,8),F(99,100)}
        ts |= {F(2,2*k-m+2) for k in range((m//2)+1,m) if 2*k-m+2>2}
        for t in ts:
            if 0 < t < 1:
                check_case(m,t,False)
    print('PARITY_STAIRCASE_AND_EXACT_CENTER_RANK_PASS')
    print('SINGLE_CLUSTER_ULTRAMETRIC_INBALL_ALL_CHECKS_PASS')

if __name__ == '__main__':
    main()
