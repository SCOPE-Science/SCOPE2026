#!/usr/bin/env python3
"""Independent exhaustive check of identifying codes in small two-coronas.

Uses only Python's standard library. A code is tested directly by intersecting
closed neighborhoods, without calling the structural characterization.
"""
from collections import Counter
from itertools import combinations


def connected(m, edges):
    seen = {0}
    while True:
        more = seen | {b for a, b in edges if a in seen} | {a for a, b in edges if b in seen}
        if more == seen:
            break
        seen = more
    return len(seen) == m


def twin_classes(m, edges):
    adj = [1 << j for j in range(m)]
    for a, b in edges:
        adj[a] |= 1 << b
        adj[b] |= 1 << a
    classes = {}
    for v, bits in enumerate(adj):
        classes.setdefault(bits, []).append(v)
    return list(classes.values())


def expected_coeffs(m, classes):
    # Independently multiply the local (1+x)^(t-1)(t+1+x) polynomials.
    p = [1]
    for cl in classes:
        t = len(cl)
        b = [1]
        for _ in range(t - 1):
            c = [0] * (len(b) + 1)
            for j, a in enumerate(b):
                c[j] += a
                c[j + 1] += a
            b = c
        c = [0] * (t + 1)
        for j, a in enumerate(b):
            c[j] += (t + 1) * a
            c[j + 1] += a
        out = [0] * (len(p) + len(c) - 1)
        for j, a in enumerate(p):
            for k, d in enumerate(c):
                out[j + k] += a * d
        p = out
    return {2 * m + j: c for j, c in enumerate(p)}


def verify(m, edges):
    n = 3 * m
    closed = [(1 << j) for j in range(n)]
    def add(a, b):
        closed[a] |= 1 << b
        closed[b] |= 1 << a
    for a, b in edges:
        add(a, b)
    for j in range(m):
        add(j, m + j)
        add(m + j, 2 * m + j)
    classes = twin_classes(m, edges)
    observed = Counter()
    for mask in range(1 << n):
        traces = [b & mask for b in closed]
        actual = (0 not in traces and len(set(traces)) == n)
        predicted = (mask & ((1 << m) - 1)) == (1 << m) - 1
        if predicted:
            for j in range(m):
                if not (mask & (1 << (m + j)) or mask & (1 << (2 * m + j))):
                    predicted = False
                    break
        if predicted:
            for cl in classes:
                w_only = sum(
                    not (mask & (1 << (m + j))) and bool(mask & (1 << (2 * m + j)))
                    for j in cl
                )
                if w_only >= 2:
                    predicted = False
                    break
        assert actual == predicted, (m, edges, mask, actual, predicted)
        if actual:
            observed[mask.bit_count()] += 1
    assert dict(observed) == expected_coeffs(m, classes), (m, edges, observed)
    assert sum(observed.values()) == (2 ** (m - len(classes))) * __import__('math').prod(len(c) + 2 for c in classes)
    assert observed[2 * m] == __import__('math').prod(len(c) + 1 for c in classes)
    return 1 << n, sum(observed.values())


def main():
    examples = []
    for m in range(2, 5):
        pairs = list(combinations(range(m), 2))
        for em in range(1 << len(pairs)):
            edges = [e for i, e in enumerate(pairs) if em >> i & 1]
            if connected(m, edges):
                examples.append((m, edges))
    examples += [
        (5, [(j, j + 1) for j in range(4)]),
        (5, [(j, (j + 1) % 5) for j in range(5)]),
        (5, [(0, j) for j in range(1, 5)]),
        (5, list(combinations(range(5), 2))),
        (5, [(0, 1), (1, 2), (2, 3), (3, 0), (3, 4)]),
        (6, [(j, j + 1) for j in range(5)]),
    ]
    checked = codes = 0
    for m, edges in examples:
        x, y = verify(m, edges)
        checked += x
        codes += y
    print(f'VERIFY_OK base_graphs={len(examples)} direct_subsets={checked} identifying_codes={codes} '
          'characterization=PASS full_polynomial=PASS minimum_multiplicities=PASS')

if __name__ == '__main__':
    main()
