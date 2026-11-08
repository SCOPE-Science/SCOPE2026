#!/usr/bin/env python3
"""Finite checks for a critical percolated cycle-square theorem.

Exact combinatorics only. These checks are not proofs of distributional limits.
Run: python3 verify.py
"""
from itertools import combinations
from fractions import Fraction
from math import comb

COUNT = 0

def check(condition, message):
    global COUNT
    COUNT += 1
    if not condition:
        raise AssertionError(message)


def geometry(n):
    edges = [(i, (i + d) % n) for i in range(n) for d in (1, 2)]
    indexed = {frozenset(edge): j for j, edge in enumerate(edges)}
    walls = [tuple(sorted(indexed[frozenset(edge)] for edge in
            [(i, (i + 1) % n), ((i - 1) % n, (i + 1) % n), (i, (i + 2) % n)]))
            for i in range(n)]
    windows = []
    for i in range(n):
        vset = {(i + j) % n for j in range(5)}
        windows.append(tuple(j for j, (a, b) in enumerate(edges) if a in vset and b in vset))
    return edges, walls, windows


def component_labels(n, edges, absent_mask):
    parent = list(range(n))
    def root(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for j, (a, b) in enumerate(edges):
        if not ((absent_mask >> j) & 1):
            parent[root(a)] = root(b)
    return [root(i) for i in range(n)]


def verify(n):
    edges, walls, windows = geometry(n)
    check(len(edges) == 2*n, 'edge count')
    check(len(set(map(frozenset, edges))) == len(edges), 'edge distinct')
    for wall in walls:
        check(len(wall) == 3, 'wall size')
    for window in windows:
        check(len(window) == 7, 'window edge size')
    for a, b in combinations(range(n), 2):
        intersection = set(walls[a]).intersection(walls[b])
        d = min((a-b) % n, (b-a) % n)
        check(len(intersection) == (1 if d == 1 else 0), 'wall intersections')
    tested = 0
    for missing in range(1 << (2*n)):
        # Exact search over every labelled subgraph for n=7,8.
        is_good = True
        for window in windows:
            if sum((missing >> e) & 1 for e in window) >= 4:
                is_good = False
                break
        if not is_good:
            continue
        labels = component_labels(n, edges, missing)
        k = len(set(labels))
        wall_count = sum(all((missing >> e) & 1 for e in wall) for wall in walls)
        check(k == max(1, wall_count), 'component/wall equality')
        if k > 1:
            check(wall_count >= 2, 'at least two walls')
            # Component segments do not overlap and each is connected.
            cuts = [i for i, wall in enumerate(walls) if all((missing >> e) & 1 for e in wall)]
            for idx, a in enumerate(cuts):
                b = cuts[(idx + 1) % len(cuts)]
                vertices = []
                v = (a + 1) % n
                while True:
                    vertices.append(v)
                    if v == b:
                        break
                    v = (v + 1) % n
                check(len(vertices) >= 2, 'each segment at least 2 vertices')
                check(len({labels[v] for v in vertices}) == 1, 'each segment connected')
        tested += 1
    return tested


def check_moments():
    # Exact pair moments for walls and exact covariance of the wall count.
    for n in (7, 8, 10, 14):
        _, walls, _ = geometry(n)
        for q in (Fraction(1, 7), Fraction(2, 5)):
            moment1 = n*q**3
            moment2 = sum(q**len(set(walls[i]) | set(walls[j]))
                          for i in range(n) for j in range(n) if i != j)
            check(moment2 == n*(n-3)*q**6 + 2*n*q**5, 'wall second factorial moment')
            var = moment2 + moment1 - moment1**2
            check(var == n*q**3*(1-q**3) + 2*n*(q**5-q**6), 'wall variance')
            check(var >= 0, 'nonnegative variance')


def main():
    count7=verify(7)
    count8=verify(8)
    check_moments()
    print(f'VERIFICATION_OK total_checks={COUNT} valid_configuration_checks_n7={count7} valid_configuration_checks_n8={count8}')
    print('LIMIT: exhaustive only for n=7,8; asymptotic claims require analytic proofs.')

if __name__ == '__main__':
    main()
