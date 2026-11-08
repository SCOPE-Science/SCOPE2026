"""Independent exact-rational checks for stationary lag laws on complete bipartite graphs.

Run: python3 verify.py
Only Python standard-library modules are required.
"""
from fractions import Fraction
from math import gcd, lcm


def correlation_formula(a, b):
    return Fraction(a + 4 * b - 1, 15 * a * b + a + b - 1)


def graph_neighbors(a, b):
    return [list(range(a, a + b)) for _ in range(a)] + [list(range(a)) for _ in range(b)]


def linear_solve(mat, vec):
    n = len(mat)
    a = [row[:] + [val] for row, val in zip(mat, vec)]
    for c in range(n):
        r = next((r for r in range(c, n) if a[r][c]), None)
        assert r is not None, 'singular covariance system'
        a[c], a[r] = a[r], a[c]
        scale = a[c][c]
        for j in range(c, n + 1):
            a[c][j] /= scale
        for r in range(n):
            if r == c or a[r][c] == 0:
                continue
            mul = a[r][c]
            for j in range(c, n + 1):
                a[r][j] -= mul * a[c][j]
    return [row[n] for row in a]


def stationary_pair_covariances(a, b):
    nbr = graph_neighbors(a, b)
    N = a + b
    pairs = [(u, v) for u in range(N) for v in range(u + 1, N)]
    idx = {p: k for k, p in enumerate(pairs)}
    M = len(pairs)
    t = Fraction(1, 4)
    matrix = [[Fraction(int(i == j)) for j in range(M)] for i in range(M)]
    rhs = [Fraction(0) for _ in range(M)]
    for i, (u, v) in enumerate(pairs):
        w = t / (len(nbr[u]) * len(nbr[v]))
        for x in nbr[u]:
            for y in nbr[v]:
                if x == y:
                    rhs[i] += w
                else:
                    matrix[i][idx[min(x, y), max(x, y)]] -= w
    sol = linear_solve(matrix, rhs)
    C = [[Fraction(int(u == v)) for v in range(N)] for u in range(N)]
    for (u, v), value in zip(pairs, sol):
        C[u][v] = C[v][u] = value
    return nbr, C


def lag_correlations(nbr, C, lagmax=10):
    N = len(nbr)
    dist = [Fraction(int(i == 0)) for i in range(N)]
    result = []
    c = Fraction(1, 2)
    for lag in range(lagmax + 1):
        result.append(c ** lag * sum(dist[v] * C[0][v] for v in range(N)))
        new = [Fraction(0) for _ in range(N)]
        for u in range(N):
            for v in nbr[u]:
                new[v] += dist[u] / len(nbr[u])
        dist = new
    return result


def check():
    assertions = 0
    examples = [(4, 4, 5, 2), (6, 6, 11, 2)]
    for a, b, aa, bb in examples:
        orig = []
        for p, q in [(a, b), (aa, bb)]:
            nbr, C = stationary_pair_covariances(p, q)
            values = lag_correlations(nbr, C, 12)
            y = correlation_formula(p, q)
            for d, actual in enumerate(values):
                predicted = (Fraction(1) if d == 0 else Fraction(0) if d % 2 else
                             Fraction(1, 4) ** (d // 2 - 1) * y)
                assert actual == predicted, (p, q, d, actual, predicted)
                assertions += 1
            orig.append(values)
        assert orig[0] == orig[1]
        assertions += 1

    # Exercise simultaneous collisions without relying on matrix inversion.
    for k in range(2, 16):
        L = lcm(*(5*j-4 for j in range(1, k+1)))
        n = 2 * L
        target = Fraction(1, 3*n+1)
        sizes = []
        for j in range(1, k+1):
            m = 1 + j*(n-1)
            assert j*n % (5*j-4) == 0
            b = j*n // (5*j-4)
            assert m >= n and 2 <= b <= n
            assert correlation_formula(m, b) == target
            sizes.append((m, b))
            assertions += 4
        assert len(set(sizes)) == k
        assertions += 1

    # At fixed n, the integer scaling parameter gives the exact common fiber.
    for n in (12, 33, 66, 132):
        for j in range(1, 20):
            if j*n % (5*j-4):
                continue
            m = j*(n-1)+1
            b = j*n//(5*j-4)
            assert correlation_formula(m, b) == Fraction(1, 3*n+1)
            assertions += 1
    print('VERIFY_OK', assertions, 'exact-rational assertions')


if __name__ == '__main__':
    check()
