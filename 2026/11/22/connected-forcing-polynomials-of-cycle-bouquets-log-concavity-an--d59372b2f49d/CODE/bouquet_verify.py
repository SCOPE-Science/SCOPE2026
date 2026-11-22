#!/usr/bin/env python3
"""Self-contained finite corroboration of the cycle-bouquet connected-forcing theorem."""
from collections import Counter
from itertools import product
from math import comb


def make_bouquet(lengths):
    adj = [set()]
    for length in lengths:
        first = len(adj)
        adj.extend(set() for _ in range(length - 1))
        ids = [0] + list(range(first, first + length - 1))
        for a, b in zip(ids, ids[1:] + ids[:1]):
            adj[a].add(b)
            adj[b].add(a)
    return adj


def connected(adj, selected):
    if not selected:
        return False
    visited = {min(selected)}
    todo = list(visited)
    while todo:
        u = todo.pop()
        for v in adj[u]:
            if v in selected and v not in visited:
                visited.add(v)
                todo.append(v)
    return visited == selected


def forces(adj, selected):
    blue = set(selected)
    while True:
        updates = set()
        for u in blue:
            white = adj[u] - blue
            if len(white) == 1:
                updates.update(white)
        if not updates:
            return len(blue) == len(adj)
        blue.update(updates)


def direct_polynomial(lengths):
    adj = make_bouquet(lengths)
    n = len(adj)
    out = Counter()
    checked = 0
    for bits in range(1 << n):
        S = {i for i in range(n) if bits >> i & 1}
        checked += 1
        if connected(adj, S) and forces(adj, S):
            out[len(S)] += 1
    return out, checked


def multiply(A, B):
    C = Counter()
    for k, a in A.items():
        for h, b in B.items():
            C[k + h] += a * b
    return C


def predicted(lengths):
    out = Counter({1: 1})
    for length in lengths:
        petal = Counter({s: s + 1 for s in range(1, length - 1)})
        petal[length - 1] = 1
        out = multiply(out, petal)
    return out


def is_log_concave(C):
    keys = range(min(C), max(C) + 1)
    a = [C[k] for k in keys]
    return all(x > 0 for x in a) and all(a[j] ** 2 >= a[j - 1] * a[j + 1]
                                              for j in range(1, len(a) - 1))


def main():
    cases = [(3, 3), (3, 4), (4, 4), (3, 5), (5, 5),
             (3, 3, 3), (3, 4, 4), (3, 4, 5),
             (3, 3, 3, 3), (3, 3, 4, 4), (4, 4, 4),
             (3, 5, 5), (3, 3, 6), (5, 6), (3, 7)]
    total = 0
    for lengths in cases:
        computed, tested = direct_polynomial(lengths)
        exact = predicted(lengths)
        assert computed == exact, (lengths, computed, exact)
        assert min(exact) == len(lengths) + 1
        assert exact[min(exact)] == 2 ** len(lengths)
        assert sum(exact.values()) == __import__('math').prod(comb(x, 2) for x in lengths)
        assert is_log_concave(exact)
        print('EXHAUSTIVE', lengths, 'subsets', tested, 'nonzero_terms', len(exact))
        total += tested
    for r in (2, 3, 4, 7):
        for length in range(3, 21):
            coeff = predicted((length,) * r)
            assert is_log_concave(coeff)
            assert coeff[r + 1] == 2 ** r
            assert sum(coeff.values()) == comb(length, 2) ** r
    for length in range(5, 101):
        d = length - 2
        assert 9 * (d - 1) < 16 * d
    assert predicted((3, 4)) == Counter({3: 4, 4: 8, 5: 5, 6: 1})
    print('EXHAUSTIVE_SUBSETS_CHECKED', total)
    print('LOG_CONCAVITY_PRODUCT_AND_NEWTON_CHECKS_OK')
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
