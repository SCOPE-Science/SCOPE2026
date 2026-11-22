"""Exhaustive arithmetic verifier for projective-line point-image shattering.

Run: python3 verify_psl.py
Only standard-library modules are required.
"""
import itertools
from math import comb


def transformations(p):
    result = set()
    for a, b, c, d in itertools.product(range(p), repeat=4):
        if (a * d - b * c) % p != 1:
            continue
        perm = []
        for x in range(p):
            den = (c * x + d) % p
            perm.append(((a * x + b) * pow(den, -1, p)) % p if den else p)
        perm.append((a * pow(c, -1, p)) % p if c else p)
        result.add(tuple(perm))
    return sorted(result)


def binary_rank(columns):
    pivots = {}
    for col in columns:
        x = col
        while x:
            h = x.bit_length() - 1
            if h in pivots:
                x ^= pivots[h]
            else:
                pivots[h] = x
                break
    return len(pivots)


def run(p):
    n = p + 1
    perms = transformations(p)
    assert len(perms) == p * (p * p - 1) // 2
    vertex = lambda x, y: n * x + y
    edges = {}
    for x in range(n):
        for y in range(n):
            for u in range(x + 1, n):
                for v in range(n):
                    if y != v:
                        key = (vertex(x, y), vertex(u, v))
                        edges[key] = len(edges)
    assert len(edges) == 2 * comb(n, 2)**2
    triangles = set()
    for perm in perms:
        for rows in itertools.combinations(range(n), 3):
            triangles.add(tuple(vertex(x, perm[x]) for x in rows))
    assert len(triangles) == len(perms) * comb(n, 3)

    # Directly evaluate all Boolean trace patterns, not just positive incidence.
    count_shattered = 0
    for rows in itertools.combinations(range(n), 3):
        for columns in itertools.permutations(range(n), 3):
            support = [(rows[i], columns[i]) for i in range(3)]
            patterns = set()
            for perm in perms:
                pattern = sum((1 << i) for i, (x, y) in enumerate(support)
                              if perm[x] == y)
                patterns.add(pattern)
            top_present = tuple(vertex(x, y) for x, y in support) in triangles
            assert (len(patterns) == 8) == (top_present and p >= 5)
            count_shattered += (len(patterns) == 8)
    assert count_shattered == (3 * comb(n, 3)**2 if p >= 5 else 0)

    if p >= 5:
        columns = []
        for triangle in triangles:
            col = 0
            for a, b in itertools.combinations(triangle, 2):
                col ^= 1 << edges[(a, b)]
            columns.append(col)
        rank = binary_rank(columns)
        beta1 = len(edges) - n*n + 1 - rank
        beta2 = len(triangles) - rank
        print(f"p={p}: group={len(perms)}, f=(1,{n*n},{len(edges)},{count_shattered}), rank_boundary2={rank}, betti1={beta1}, betti2={beta2}")
        assert (rank, beta1, beta2) == {5: (414, 1, 786), 7: (1504, 1, 7904)}[p]
    else:
        print(f"p={p}: group={len(perms)}, f=(1,{n*n},{len(edges)},0)")

if __name__ == '__main__':
    for prime in (3, 5, 7):
        run(prime)
