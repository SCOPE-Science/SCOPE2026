"""Exact small-case checks for wheel spanning-tree polytope Euclidean widths.

Run using Python 3.9 or later, no third-party packages. These finite checks
support, but do not replace, the all-rim-length proof in RESULT.md.
"""
from fractions import Fraction
from itertools import product
from math import isqrt


def wheel_edges(m):
    assert m >= 3
    return [(0, j) for j in range(1, m + 1)] + [
        (j, j % m + 1) for j in range(1, m + 1)
    ]


def graph_rank(m, mask, edges):
    parent = list(range(m + 1))

    def root(x):
        while parent[x] != x:
            x = parent[x]
        return x

    for j, (a, b) in enumerate(edges):
        if mask & (1 << j):
            aa, bb = root(a), root(b)
            if aa != bb:
                parent[aa] = bb
    return m + 1 - len({root(j) for j in range(m + 1)})


def connectivity(m, mask, edges):
    complete = (1 << (2 * m)) - 1
    return graph_rank(m, mask, edges) + graph_rank(m, complete ^ mask, edges) - m


def squared_cut_width(m, mask, edges):
    k = mask.bit_count()
    return Fraction(2 * m * connectivity(m, mask, edges) ** 2, k * (2 * m - k))


def proposed_cut(m):
    a = (m + 1) // 2
    mask = sum(1 << j for j in range(a))
    mask |= sum(1 << (m + j) for j in range(a - 1))
    if m % 2 == 0:
        mask |= 1 << (m + a - 1)
    return mask


def test_exhaustive():
    for m in range(3, 10):
        edges = wheel_edges(m)
        n = 2 * m
        squared_min = None
        types = {}
        achievers = 0
        for mask in range(1, (1 << n) - 1):
            k = mask.bit_count()
            lam = connectivity(m, mask, edges)
            assert lam >= (1 if min(k, n - k) == 1 else 2), (m, mask, lam)
            sq = Fraction(n * lam * lam, k * (n - k))
            if squared_min is None or sq < squared_min:
                squared_min = sq
                achievers = 1
                types = {(k, lam): 1}
            elif sq == squared_min:
                achievers += 1
                types[(k, lam)] = types.get((k, lam), 0) + 1
        expected = min(Fraction(n, n - 1), Fraction(8, m))
        assert squared_min == expected, (m, squared_min, expected)
        if m <= 7:
            assert types == {(1, 1): n, (n - 1, 1): n}, (m, types)
        else:
            assert types == {(m, 2): 2 * m}, (m, types)
        print('m=', m, 'width^2=', str(squared_min),
              'number of oriented minimizing subsets=', achievers,
              'types=', types)


def test_support_identity():
    # Optimizations across actual spanning-tree incidence vectors, not
    # approximations by a sampled convex hull.
    for m in [3, 4]:
        edges = wheel_edges(m)
        n = 2 * m
        trees = [mask for mask in range(1 << n)
                 if mask.bit_count() == m and graph_rank(m, mask, edges) == m]
        for u in product((-1, 0, 1), repeat=n):
            if max(u) == min(u):
                continue
            scores = [sum(u[j] for j in range(n) if mask >> j & 1) for mask in trees]
            direct = max(scores) - min(scores)
            order = sorted(range(n), key=lambda i: -u[i])
            identity = 0
            for j in range(n - 1):
                delta = u[order[j]] - u[order[j + 1]]
                if not delta:
                    continue
                prefix = sum(1 << i for i in order[:j + 1])
                identity += delta * connectivity(m, prefix, edges)
            assert direct == identity, (m, u, direct, identity)
        print('m=', m, 'support-order exhaustive identity PASS; trees=', len(trees))


def test_cut_construction():
    for m in range(3, 65):
        edges = wheel_edges(m)
        mask = proposed_cut(m)
        assert mask.bit_count() == m
        assert connectivity(m, mask, edges) == 2, (m, mask)
    print('balanced-cut construction PASS, m=3..64')


if __name__ == '__main__':
    test_exhaustive()
    test_support_identity()
    test_cut_construction()
    print('WHEEL_SPANNING_TREE_WIDTH_EXACT_PASS')
