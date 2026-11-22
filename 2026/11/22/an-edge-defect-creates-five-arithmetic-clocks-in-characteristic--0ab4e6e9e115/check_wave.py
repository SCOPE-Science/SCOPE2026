"""Independent finite checks for reversible waves on one-edge-deleted bicliques.

Run: python3 check_wave.py
Uses only the Python standard library. Finite checks supplement, not replace, the proof.
"""
from collections import Counter
from itertools import product


def matmul(a, b):
    n = len(a)
    c = [[0] * n for _ in range(n)]
    for i in range(n):
        for h in range(n):
            z = a[i][h]
            if z:
                for j in range(n):
                    c[i][j] = (c[i][j] + z * b[h][j]) % 3
    return c


def eye(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def power(a, k):
    n = len(a)
    v = eye(n)
    while k:
        if k & 1:
            v = matmul(v, a)
        a = matmul(a, a)
        k >>= 1
    return v


def rank(a):
    a = [row[:] for row in a]
    n = len(a[0])
    r = 0
    for j in range(n):
        pivot = next((i for i in range(r, len(a)) if a[i][j] % 3), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        c = a[r][j] % 3
        inv = 1 if c == 1 else 2
        a[r] = [(v * inv) % 3 for v in a[r]]
        for i in range(len(a)):
            if i != r and a[i][j]:
                coeff = a[i][j]
                a[i] = [(u - coeff * v) % 3 for u, v in zip(a[i], a[r])]
        r += 1
        if r == len(a):
            break
    return r


def graph(a, b):
    n = a + b
    adj = [[0] * n for _ in range(n)]
    for i in range(a):
        for j in range(b):
            if i == 0 and j == 0:
                continue
            adj[i][a + j] = adj[a + j][i] = 1
    return adj


def time_matrix(a, b):
    adj = graph(a, b)
    n = a + b
    t = [[0] * (2 * n) for _ in range(2 * n)]
    for i in range(n):
        for j in range(n):
            t[i][j] = adj[i][j]
        t[i][n + i] = 2
        t[n + i][i] = 1
    return t


def predicted(a, b):
    if a == b == 2:
        return 10
    i, j = sorted((a % 3, b % 3))
    return {(0, 0): 36, (0, 1): 24, (0, 2): 20,
            (1, 1): 12, (1, 2): 12, (2, 2): 20}[(i, j)]


def prime_factors(n):
    ans = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            ans.append(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        ans.append(n)
    return ans


def test_global_orders():
    checked = 0
    for a in range(2, 9):
        for b in range(2, 9):
            t = time_matrix(a, b)
            order = predicted(a, b)
            one = eye(len(t))
            assert power(t, order) == one, (a, b, 'upper bound')
            for prime in prime_factors(order):
                assert power(t, order // prime) != one, (a, b, prime)
            checked += 1
    return checked


def test_fixed_counts():
    checked = 0
    for a, b in product((2, 5, 8), repeat=2):
        t = time_matrix(a, b)
        n = len(t)
        one = eye(n)
        for k in range(1, 41):
            mk = power(t, k)
            nullity = n - rank([[(mk[i][j] - one[i][j]) % 3
                                  for j in range(n)] for i in range(n)])
            formula = 4 * (k % 5 == 0) + 4 * (k % 10 == 0) + \
                2 * (a + b - 4) * (k % 4 == 0)
            assert nullity == formula, (a, b, k, nullity, formula)
            checked += 1
    return checked


def exhaustive_path4():
    t = time_matrix(2, 2)
    counts = Counter()
    for state in product(range(3), repeat=8):
        y = tuple(state)
        for k in range(1, 11):
            y = tuple(sum(t[i][j] * y[j] for j in range(8)) % 3
                      for i in range(8))
            if y == state:
                counts[k] += 1
                break
        else:
            raise AssertionError('unexpected orbit')
    assert counts == {1: 1, 5: 80, 10: 6480}, counts
    return dict(sorted(counts.items()))


if __name__ == '__main__':
    print('Direct exact global-period matrix checks:', test_global_orders())
    print('Exact rank/formula comparisons:', test_fixed_counts())
    print('Exhaustive 3^8 period census for P4:', exhaustive_path4())
    print('ALL CHECKS PASSED')
