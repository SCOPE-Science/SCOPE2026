#!/usr/bin/env python3
"""Independent finite checker for induced pseudoforests on complete multipartite graphs.

Run with: python pseudoforest_verifier.py
Only standard-library modules are needed.
"""
from itertools import product, combinations
from collections import Counter
from math import comb


def polynomial_by_structure(ns):
    n = sum(ns)
    all_sets = Counter({k: comb(n, k) for k in range(min(3, n) + 1)})
    maximal = Counter()
    r = len(ns)
    assert r >= 3 and min(ns) >= 1
    for i, a in enumerate(ns):
        for k in range(4, a + 1):
            all_sets[k] += comb(a, k)
        for j, b in enumerate(ns):
            if i == j:
                continue
            for k in range(3, a + 1):
                all_sets[k + 1] += comb(a, k) * b
            if a >= 3:
                maximal[a + 1] += b
            elif a == 2 and b == 1:
                maximal[3] += 1
    for i, j in combinations(range(r), 2):
        c = comb(ns[i], 2) * comb(ns[j], 2)
        all_sets[4] += c
        maximal[4] += c
    for i, j, k in combinations(range(r), 3):
        maximal[3] += ns[i] * ns[j] * ns[k]
    return (+all_sets, +maximal)


def direct_polynomials(ns):
    groups = [i for i, a in enumerate(ns) for _ in range(a)]
    n = len(groups)
    adj = [sum((1 << j) for j in range(n) if groups[j] != groups[i]) for i in range(n)]
    cache = bytearray(1 << n)
    all_sets = Counter()
    maximal = Counter()
    for mask in range(1 << n):
        seen = 0
        ok = True
        while (mask & ~seen):
            root = (mask & ~seen) & -(mask & ~seen)
            seen |= root
            frontier = root
            vertices = 0
            degrees = 0
            while frontier:
                b = frontier & -frontier
                frontier ^= b
                x = b.bit_length() - 1
                vertices += 1
                nbr = adj[x] & mask
                degrees += nbr.bit_count()
                new = nbr & ~seen
                frontier |= new
                seen |= new
            if degrees // 2 > vertices:
                ok = False
                break
        if ok:
            cache[mask] = 1
            all_sets[mask.bit_count()] += 1
    for mask in range(1 << n):
        if not cache[mask]:
            continue
        outside = ((1 << n) - 1) ^ mask
        is_max = True
        while outside:
            b = outside & -outside
            outside ^= b
            if cache[mask | b]:
                is_max = False
                break
        if is_max:
            maximal[mask.bit_count()] += 1
    return (+all_sets, +maximal), 1 << n


def main():
    tests = []
    for r in (3, 4, 5):
        for ns in product(range(1, 5 if r == 3 else 4), repeat=r):
            if sum(ns) <= 12 and tuple(sorted(ns)) == ns:
                tests.append(ns)
    tested = 0
    for ns in tests:
        expected = polynomial_by_structure(ns)
        actual, count = direct_polynomials(ns)
        assert actual == expected, (ns, expected, actual)
        tested += count
    for m in range(4, 51):
        actual, maximum = polynomial_by_structure((m, m, m))
        assert maximum[3] == m**3
        assert maximum[4] == 3*comb(m, 2)**2
        assert maximum[m+1] == 6*m
        assert set(maximum) == {3, 4, m+1}
    print(f'VERIFY_OK graph_instances={len(tests)} candidate_subsets={tested} balanced_arithmetic_orders=47')


if __name__ == '__main__':
    main()
