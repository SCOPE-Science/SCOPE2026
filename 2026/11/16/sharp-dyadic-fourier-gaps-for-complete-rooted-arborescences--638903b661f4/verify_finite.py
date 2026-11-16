"""Exact integer checks for signed rooted-arborescence Fourier multipliers.

Usage: python3 verify_finite.py. Requires only Python's standard library.
"""
from itertools import product
import random


def determinant(matrix):
    """Exact Bareiss determinant with row-pivoting."""
    a = [list(r) for r in matrix]
    n = len(a)
    if not n:
        return 1
    sign = 1
    pivot_previous = 1
    for k in range(n - 1):
        if a[k][k] == 0:
            j = next((j for j in range(k + 1, n) if a[j][k]), None)
            if j is None:
                return 0
            a[k], a[j] = a[j], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                numerator = a[i][j] * pivot - a[i][k] * a[k][j]
                assert numerator % pivot_previous == 0
                a[i][j] = numerator // pivot_previous
            a[i][k] = 0
        pivot_previous = pivot
    return sign * a[-1][-1]


def laplacian_from_signs(signs):
    m = len(signs)
    L = [[0] * m for _ in range(m)]
    for i in range(m):
        L[i][i] = sum(signs[i])
        for j in range(m):
            if j != i:
                L[i][j] = -signs[i][j]
    return L


def representative_signs(n, word):
    m = n - 1
    signs = [[1] * n for _ in range(m)]
    for i in range(m):
        for j in range(m):
            if i == j:
                signs[i][j] = 0
            else:
                bit = j if j < i else j - 1
                signs[i][j] = 1 - 2 * ((word >> (i * (m - 1) + bit)) & 1)
    return signs


def tree_parent_lists(n):
    """Unoriented Cayley trees from Prüfer words, then oriented toward root n-1."""
    root = n - 1
    for word in product(range(n), repeat=n - 2):
        degree = [1] * n
        for v in word:
            degree[v] += 1
        edges = []
        for v in word:
            u = next(u for u in range(n) if degree[u] == 1)
            edges.append((u, v))
            degree[u] -= 1
            degree[v] -= 1
        u, v = [u for u in range(n) if degree[u] == 1]
        edges.append((u, v))
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        parent = [-1] * n
        seen = {root}
        queue = [root]
        for v in queue:
            for u in adj[v]:
                if u not in seen:
                    seen.add(u)
                    parent[u] = v
                    queue.append(u)
        assert len(seen) == n
        yield parent[:-1]


def signed_tree_sum(parents, signs):
    return sum(__import__('math').prod(signs[i][j] for i, j in enumerate(p)) for p in parents)


def even_extremizer(n):
    m = n - 1
    r = m // 2
    signs = [[0] * n for _ in range(m)]
    for i in range(m):
        signs[i][-1] = 1
        for j in range(m):
            if i != j:
                signs[i][j] = 1 if (j-i) % m <= r else -1
    return signs


def odd_extremizer(n):
    m = n - 1
    A = [[0, 1], [-1, 0]]
    while len(A) < m:
        old = len(A)
        u = [1] * (old // 2) + [-1] * (old // 2)
        for i in range(old):
            A[i] += [u[i], -u[i]]
        A.append([-x for x in u] + [0, 1])
        A.append(u + [-1, 0])
    assert len(A) == m and all(sum(row) in (-1, 1) for row in A)
    return [A[i] + [-sum(A[i])] for i in range(m)]


def zero_star_signs(n):
    k = (n - 2) // 2
    signs = [[1 if i != j else 0 for j in range(n)] for i in range(n - 1)]
    for i in range(k):
        signs[i][-1] = -1
    return signs


def main():
    hist = {}
    for n in (3, 4, 5):
        parents = list(tree_parent_lists(n))
        assert len(parents) == n ** (n - 2)
        m = n - 1
        levels = {}
        for w in range(1 << (m * (m - 1))):
            signs = representative_signs(n, w)
            value = signed_tree_sum(parents, signs)
            assert determinant(laplacian_from_signs(signs)) == value
            levels[value] = levels.get(value, 0) + 1
        assert min(abs(v) for v in levels if v) == (1 if n & 1 else 2 ** (n - 2))
        assert (0 in levels) == (n % 2 == 0)
        hist[n] = (len(parents), len(levels), levels.get(0, 0))
    rng = random.Random(20261113)
    n = 6
    parents = list(tree_parent_lists(n))
    assert len(parents) == 1296
    for w in [0, 7, 4668] + [rng.randrange(1 << 20) for _ in range(80)]:
        signs = representative_signs(n, w)
        assert signed_tree_sum(parents, signs) == determinant(laplacian_from_signs(signs))
    for n in range(2, 19):
        if n % 2:
            signs = odd_extremizer(n)
            assert determinant(laplacian_from_signs(signs)) == 1
        else:
            signs = even_extremizer(n)
            assert determinant(laplacian_from_signs(signs)) == 2 ** (n - 2)
            if n >= 4:
                assert determinant(laplacian_from_signs(zero_star_signs(n))) == 0
    print('PASS: Prüfer sums = exact determinants for every reduced n=3,4,5 frequency')
    print('Full reduced frequency histogram checks (trees, levels, zeros):', hist)
    print('PASS: 83 independently sampled n=6 characters')
    print('PASS: unit and dyadic extremizers to n=18, and all even zero-stars to n=18')


if __name__ == '__main__':
    main()
