#!/usr/bin/env python3
"""Independent exact checks for the multipartite leaf-inclusion theorem.

Enumerates ordinary edge subsets (not the product-count proof), checks joint
inclusion probabilities, and tests the log-submodular lattice inequalities.
No floating-point arithmetic is used.
"""
from fractions import Fraction
from itertools import combinations
from math import comb, prod


def partitions(n, lo=1):
    if n == 0:
        yield ()
        return
    for x in range(lo, n + 1):
        for t in partitions(n - x, x):
            yield (x,) + t


def graph(parts):
    types = tuple(i for i, size in enumerate(parts) for _ in range(size))
    edges = tuple((i, j) for i in range(len(types)) for j in range(i + 1, len(types))
                  if types[i] != types[j])
    return types, edges


def inclusion(parts, mask):
    N, k = sum(parts), len(parts)
    types, _ = graph(parts)
    s = [sum(bool(mask & (1 << i)) for i, t in enumerate(types) if t == j)
         for j in range(k)]
    m = N - sum(s)
    denominator = N ** (k-2) * prod((N-v) ** (v-1) for v in parts)
    numerator = m ** (k-2) * prod((m - parts[j] + s[j]) ** (parts[j]-1)
                                    for j in range(k))
    return Fraction(numerator, denominator)


def enumerated_inclusion(parts, max_candidates=400000):
    types, edges = graph(parts)
    N, E = len(types), len(edges)
    if comb(E, N-1) > max_candidates:
        return None
    counts = [0] * (1 << N)
    total = 0
    for chosen in combinations(edges, N-1):
        parent = list(range(N))
        rank = [0] * N
        degrees = [0] * N
        def root(a):
            while parent[a] != a:
                parent[a] = parent[parent[a]]
                a = parent[a]
            return a
        good = True
        for a, b in chosen:
            aa, bb = root(a), root(b)
            if aa == bb:
                good = False
                break
            if rank[aa] < rank[bb]:
                aa, bb = bb, aa
            parent[bb] = aa
            if rank[aa] == rank[bb]:
                rank[aa] += 1
            degrees[a] += 1
            degrees[b] += 1
        if not good:
            continue
        total += 1
        leaves = [i for i, d in enumerate(degrees) if d == 1]
        for r in range(len(leaves)+1):
            for chosen_leaves in combinations(leaves, r):
                mask = sum(1 << i for i in chosen_leaves)
                counts[mask] += 1
    return [Fraction(x, total) for x in counts]


def main():
    checks = 0
    exhaustively_enumerated = 0
    tested_shapes = 0
    for N in range(3, 11):
        for sizes in partitions(N):
            if len(sizes) < 2:
                continue
            tested_shapes += 1
            P = [inclusion(sizes, S) for S in range(1 << N)]
            # Every submodularity inequality, including zero-probability boundaries.
            for S in range(1 << N):
                for u, v in combinations([i for i in range(N) if not (S & (1 << i))], 2):
                    left = P[S] * P[S | (1 << u) | (1 << v)]
                    right = P[S | (1 << u)] * P[S | (1 << v)]
                    assert left <= right, (sizes, S, u, v, left, right)
                    if len(sizes) >= 3 and right > 0:
                        assert left < right, (sizes, S, u, v)
                    checks += 1
            enumerated = enumerated_inclusion(sizes, max_candidates=120000)
            if enumerated is not None:
                exhaustively_enumerated += 1
                for i, (a,b) in enumerate(zip(P,enumerated)):
                    assert a == b, (sizes, i, a, b)
                    checks += 1
    print('PASS: %d exact checks; %d multipartite shapes; %d independent exhaustive tree enumerations'
          % (checks, tested_shapes, exhaustively_enumerated))


if __name__ == '__main__':
    main()
