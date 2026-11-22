"""Exact combinatorial checks for the two twenty-line dual-graph candidates.

Requires only Python 3 standard library. All counts are exhaustive, not samples.
"""
from itertools import permutations, product
from collections import Counter

N = 4
SYMS = tuple(range(N))
PERMS = tuple(permutations(SYMS))


def latin(s):
    return lambda r, c: (r+c) % N if s == 'cyclic' else r ^ c


def graph(s):
    L = latin(s)
    A = [[0] * 20 for _ in range(20)]
    for u in range(20):
        for v in range(u):
            adjacent = (u < 16 and v < 16 and
                        (u//4 == v//4 or u%4 == v%4))
            if u >= 16 and v < 16:
                adjacent = (L(v//4, v%4) == u - 16)
            A[u][v] = A[v][u] = int(adjacent)
    return A


def mul(X, Y):
    n = len(X)
    return [[sum(X[i][k] * Y[k][j] for k in range(n))
             for j in range(n)] for i in range(n)]


def charpoly(A):
    """Return exact descending monic coefficients via Newton identities."""
    n = len(A)
    T = [[int(i == j) for j in range(n)] for i in range(n)]
    p = [0]
    for k in range(1, n + 1):
        T = mul(T, A)
        p.append(sum(T[i][i] for i in range(n)))
    c = [1]
    for k in range(1, n + 1):
        numerator = -sum(c[k-j] * p[j] for j in range(1, k+1))
        assert numerator % k == 0
        c.append(numerator // k)
    return c


def pmul(P, Q):
    out = [0] * (len(P) + len(Q) - 1)
    for i, p in enumerate(P):
        for j, q in enumerate(Q):
            out[i+j] += p*q
    return out


def poly_product(factors):
    P = [1]
    for f, power in factors:
        for _ in range(power):
            P = pmul(P, f)
    return P


def direct_colorings(A):
    """Independently count all proper four-colorings by 20-vertex DFS."""
    edges_before = [[j for j in range(i) if A[i][j]] for i in range(20)]
    color = [-1] * 20
    total = 0

    def walk(i):
        nonlocal total
        if i == 20:
            total += 1
            return
        forbidden = {color[j] for j in edges_before[i]}
        for c in SYMS:
            if c not in forbidden:
                color[i] = c
                walk(i+1)
        color[i] = -1

    walk(0)
    return total


def latin_histogram(s):
    """Enumerate every 4-row tuple of permutations, checking all columns."""
    L = latin(s)
    h = Counter()
    n_squares = total = 0
    for rows in product(PERMS, repeat=4):
        if not all({rows[r][c] for r in SYMS} == set(SYMS)
                   for c in SYMS):
            continue
        n_squares += 1
        sizes = [len({rows[r][c] for r in SYMS for c in SYMS
                      if L(r, c) == symbol}) for symbol in SYMS]
        h[tuple(sorted(sizes))] += 1
        choices = 1
        for m in sizes:
            choices *= 4 - m
        total += choices
    return n_squares, h, total


def main():
    expected_adj = poly_product([([-2, 1], 6), ([2, 1], 6),
                                 ([-4, -6, 1], 1), ([-4, 2, 1], 3)])
    expected_gram = poly_product([([0, 1], 9), ([4, 1], 6),
                                  ([5, 1], 3), ([-8, -3, 1], 1)])
    expected_hist = {
        'cyclic': {(1,1,1,1):24, (1,1,2,2):48, (1,2,3,3):192,
                   (2,2,2,2):24, (2,2,4,4):96, (3,3,3,3):192},
        'klein': {(1,1,1,1):24, (1,1,2,2):144, (2,2,2,2):72,
                  (3,3,3,3):288, (4,4,4,4):48},
    }
    for kind, n_expected in [('cyclic', 5400), ('klein', 8568)]:
        A = graph(kind)
        degree = [sum(row) for row in A]
        assert degree == [7]*16+[4]*4
        assert sum(degree)//2 == 64
        assert charpoly(A) == list(reversed(expected_adj))
        Q = [[A[i][j] - (2 if i < 16 else 1)*int(i == j)
              for j in range(20)] for i in range(20)]
        assert charpoly(Q) == list(reversed(expected_gram))
        count, hist, total = latin_histogram(kind)
        assert count == 576
        assert dict(hist) == expected_hist[kind]
        assert total == n_expected
        assert direct_colorings(A) == n_expected
        assert n_expected % 24 == 0
        print(kind, 'edges', 64, 'colorings', total,
              'unlabeled partitions', total//24, 'exact spectrum OK')
    print('ALL EXACT CHECKS PASSED')

if __name__ == '__main__':
    main()
