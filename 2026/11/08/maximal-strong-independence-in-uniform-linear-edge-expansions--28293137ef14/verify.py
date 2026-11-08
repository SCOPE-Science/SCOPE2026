"""Independent brute-force checks of maximal strong independence in linear uniform edge expansions.

Run: python3 verify.py
"""
import itertools
from collections import Counter


def brute(n, edges, r):
    m = len(edges)
    t = r - 2
    blocks = []
    for e, (u, v) in enumerate(edges):
        b = (1 << u) | (1 << v)
        for j in range(t):
            b |= 1 << (n + e*t + j)
        blocks.append(b)
    total = n + m*t
    c = Counter()
    maximal_sets = []
    for mask in range(1 << total):
        if any((mask & block).bit_count() > 1 for block in blocks):
            continue
        maximal = True
        for v in range(total):
            if mask >> v & 1:
                continue
            bigger = mask | (1 << v)
            if all((bigger & block).bit_count() <= 1 for block in blocks):
                maximal = False
                break
        if maximal:
            c[mask.bit_count()] += 1
            maximal_sets.append(mask)
    return c, set(maximal_sets), 1 << total


def predict(n, edges, r):
    t = r - 2
    m = len(edges)
    family = set()
    for X in range(1 << n):
        if any((X >> u & 1) and (X >> v & 1) for u, v in edges):
            continue
        if any(not(X >> v & 1) and all(v not in e for e in edges) for v in range(n)):
            continue
        free = [i for i, (u, v) in enumerate(edges) if not(X >> u & 1) and not(X >> v & 1)]
        for choice in itertools.product(range(t), repeat=len(free)):
            mask = X
            for i, j in zip(free, choice):
                mask |= 1 << (n + i*t + j)
            family.add(mask)
    return Counter(v.bit_count() for v in family), family


def graphs(n):
    pairs = list(itertools.combinations(range(n), 2))
    for mask in range(1 << len(pairs)):
        yield tuple(e for i, e in enumerate(pairs) if mask >> i & 1)


def check():
    cases = subsets = solutions = 0
    for n in range(1, 5):
        for edges in graphs(n):
            for r in (3, 4):
                # all simple graphs on up to four vertices, including isolates
                c, family, sub = brute(n, edges, r)
                d, predicted = predict(n, edges, r)
                assert c == d and family == predicted, (n, edges, r, c, d)
                cases += 1
                subsets += sub
                solutions += len(family)
    for n in range(4, 7):
        # additional nontrivial loose cycles, where the expansion has n edges
        edges = tuple((i, (i + 1) % n) for i in range(n))
        for r in (3, 4):
            c, family, sub = brute(n, edges, r)
            d, predicted = predict(n, edges, r)
            assert c == d and family == predicted
            # cyclic-independent-set coefficient check
            from math import comb
            expected = Counter()
            t = r - 2
            for k in range(n//2 + 1):
                coeff = n * comb(n-k, k) // (n-k)
                expected[n-k] += coeff * t**(n-2*k)
            assert c == expected, (n, r, c, expected)
            cases += 1
            subsets += sub
            solutions += len(family)
    print(f'VERIFY_OK instances={cases} vertex_subsets={subsets} maximal_sets={solutions} full_families=PASS loose_cycle_coefficients=PASS')


if __name__ == '__main__':
    check()
