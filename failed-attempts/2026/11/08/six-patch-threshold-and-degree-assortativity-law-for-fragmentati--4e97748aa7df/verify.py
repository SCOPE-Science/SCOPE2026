"""Exact finite checks for cluster-count cumulants under Bernoulli vertex survival.

Python 3.9+; standard library only. Infinite polynomial statements require
(and are supplied with) the separate analytic argument.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import product
from math import comb


def prufer_edges(code, n):
    if n == 1:
        return ()
    degree = [1] * n
    for v in code:
        degree[v] += 1
    edges = []
    for v in code:
        leaf = next(i for i, d in enumerate(degree) if d == 1)
        edges.append(tuple(sorted((leaf, v))))
        degree[leaf] -= 1
        degree[v] -= 1
    last = [i for i, d in enumerate(degree) if d == 1]
    assert len(last) == 2
    edges.append(tuple(last))
    return tuple(sorted(edges))


def degrees(edges, n):
    deg = [0] * n
    for a, b in edges:
        deg[a] += 1
        deg[b] += 1
    return tuple(deg)


def canonical(edges, n):
    nbrs = [set() for _ in range(n)]
    for a, b in edges:
        nbrs[a].add(b)
        nbrs[b].add(a)
    remaining = set(range(n))
    while len(remaining) > 2:
        leaves = {v for v in remaining if len(nbrs[v] & remaining) <= 1}
        remaining.difference_update(leaves)
    def code(root, parent):
        return '(' + ''.join(sorted(code(v, root) for v in nbrs[root] if v != parent)) + ')'
    return min(code(v, -1) for v in remaining)


def parameters(edges, n):
    d = degrees(edges, n)
    H = sum(comb(x, 2) for x in d)
    J = sum(comb(x, 3) for x in d)
    P4 = sum((d[u] - 1) * (d[v] - 1) for u, v in edges)
    return H, J, P4


def moments_by_subsets(edges, n, p):
    q = 1 - p
    counts = Counter()
    raw = [Fraction(0) for _ in range(4)]
    for mask in range(1 << n):
        k = mask.bit_count()
        occupied_edges = sum(bool(mask & (1 << u)) and bool(mask & (1 << v)) for u, v in edges)
        c = k - occupied_edges  # every induced subgraph is a forest
        counts[(k, c)] += 1
        prob = p ** k * q ** (n - k)
        for r in range(4):
            raw[r] += prob * (c ** r)
    assert raw[0] == 1
    mean = raw[1]
    variance = raw[2] - mean * mean
    third_cumulant = raw[3] - 3 * mean * raw[2] + 2 * mean ** 3
    return mean, variance, third_cumulant, counts


def closed_form(edges, n, p):
    m = n - 1
    q = 1 - p
    H, J, P4 = parameters(edges, n)
    mean = n * p - m * p ** 2
    variance = p * q * (n - 3 * m * p + (m + 2 * H) * p ** 2)
    third = (n * p * q * (1 - 2 * p)
             - m * p ** 2 * q * (7 - 17 * p + 10 * p ** 2 - 2 * p ** 3)
             + 12 * H * p ** 3 * q ** 3
             - 6 * J * p ** 4 * q * (1 - 2 * p)
             - 6 * P4 * p ** 4 * q ** 2)
    return mean, variance, third


def main():
    class_counts = {}
    for n in range(2, 7):
        classes = {}
        for code in product(range(n), repeat=n-2):
            edges = prufer_edges(code, n)
            classes[canonical(edges, n)] = edges
        class_counts[n] = len(classes)
        by_moment_signature = defaultdict(list)
        for edges in classes.values():
            H, J, P4 = parameters(edges, n)
            by_moment_signature[H].append((edges, P4))
            for p in (Fraction(1, 4), Fraction(1, 2), Fraction(2, 3), Fraction(3, 4)):
                assert moments_by_subsets(edges, n, p)[:3] == closed_form(edges, n, p)
        if n <= 5:
            assert all(len(group) == 1 for group in by_moment_signature.values())
        else:
            collisions = [group for group in by_moment_signature.values() if len(group) > 1]
            assert len(collisions) == 1 and len(collisions[0]) == 2
            assert sorted(x[1] for x in collisions[0]) == [3, 4]
    assert class_counts == {2:1, 3:1, 4:2, 5:3, 6:6}

    long = ((0,1),(0,2),(0,3),(3,4),(4,5))
    split = ((0,1),(0,2),(0,3),(2,4),(3,5))
    assert parameters(long, 6) == (5,1,3)
    assert parameters(split, 6) == (5,1,4)
    for p in (Fraction(1, 8), Fraction(1, 2), Fraction(2,3), Fraction(5,6)):
        L = moments_by_subsets(long, 6, p)
        S = moments_by_subsets(split, 6, p)
        assert L[:2] == S[:2]
        assert S[2] - L[2] == -6 * p**4 * (1-p)**2
    L = moments_by_subsets(long, 6, Fraction(1,2))[-1]
    S = moments_by_subsets(split, 6, Fraction(1,2))[-1]
    assert {c:S[4,c]-L[4,c] for c in range(1,5)} == {1:1,2:-3,3:3,4:-1}
    assert all(L[k,c] == S[k,c] for k in range(7) if k != 4 for c in range(7))
    print('EXACT_OK; nonisomorphic trees n=2..6:',class_counts)
    print('First equal-mean-variance distinct-shape pair: n=6; P4=3 versus P4=4')
    print('PGF split minus long: -p^4*(1-p)^2*t*(t-1)^3')


if __name__ == '__main__':
    main()
