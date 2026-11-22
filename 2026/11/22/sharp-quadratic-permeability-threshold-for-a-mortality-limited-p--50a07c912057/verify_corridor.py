"""Exact-arithmetic checks for a mortal random walk on a direct edge plus a detour.

Requires only Python 3 standard library. Proofs of universal statements are in RESULT.md;
these finite tests are supplementary and are not completeness certificates.
"""
from fractions import Fraction as F
from itertools import product
from math import acosh, cosh


def solve(mat, vec):
    n = len(vec)
    a = [[F(x) for x in row] + [F(vec[i])] for i, row in enumerate(mat)]
    for j in range(n):
        p = next(i for i in range(j, n) if a[i][j])
        a[j], a[p] = a[p], a[j]
        z = a[j][j]
        a[j] = [x / z for x in a[j]]
        for i in range(n):
            if i != j:
                z = a[i][j]
                a[i] = [x - z * y for x, y in zip(a[i], a[j])]
    return [row[-1] for row in a]


def hit_probability(n, d, k, alpha, g):
    # Non-target indices 0=s, 1..n=v_i, absorbing target t=n+1.
    size = n + 1
    a = [[F(k if i == j else 0) for j in range(size)] for i in range(size)]
    b = [F(0) for _ in range(size)]
    edges = [(0, n + 1, d), (0, 1, alpha)] + [
        (j, j + 1, g) for j in range(1, n + 1)
    ]
    for u, v, r in edges:
        for x, y in [(u, v), (v, u)]:
            if x < size:
                a[x][x] += r
                if y < size:
                    a[x][y] -= r
                else:
                    b[x] += r
    return solve(a, b)[0]


def isolated_path(n, k, g):
    # Non-target indices 0..n-1; target t is n.
    a = [[F(k if i == j else 0) for j in range(n)] for i in range(n)]
    b = [F(0) for _ in range(n)]
    for j in range(n):
        for nbr in [j - 1, j + 1]:
            if nbr < 0:
                continue
            a[j][j] += g
            if nbr == n:
                b[j] += g
            else:
                a[j][nbr] -= g
    z = solve(a, b)[0]
    R = solve(a, [F(int(i == 0)) for i in range(n)])[0]
    return z, R


def continuous_path(n, k, g):
    th = acosh(1.0 + float(k) / (2.0 * float(g)))
    return cosh(th / 2) / cosh((n + 0.5) * th)


def critical(n, d, k):
    p0 = float(d / (d + k))
    lo, hi = 0.01, max(2.0, float(d))
    while continuous_path(n, k, hi) <= p0:
        hi *= 2
    for _ in range(90):
        mid = (lo + hi) / 2
        if continuous_path(n, k, mid) < p0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def main():
    assert hit_probability(2, F(1), F(1), F(1), F(1)) == F(3, 7)
    assert hit_probability(1, F(1), F(1), F(1), F(1)) == F(1, 2)
    assert isolated_path(2, F(1), F(1))[0] == F(1, 5)

    checks = 0
    for n, d, k, alpha, g in product(range(1, 6), [F(1, 2), F(1), F(3)], [F(1, 3), F(1), F(2)], [F(1, 4), F(2)], [F(1, 2), F(1), F(4)]):
        z, R = isolated_path(n, k, g)
        beta = alpha / (1 + alpha * R)
        p = hit_probability(n, d, k, alpha, g)
        p0 = d / (d + k)
        assert p == (d + beta * z) / (d + k + beta)
        assert p - p0 == beta * (z - p0) / (d + k + beta)
        assert ((p > p0) == (z > p0))
        assert ((p < p0) == (z < p0))
        assert d + 1 / (1 / alpha + n / g) > d
        checks += 1

    for n in range(1, 11):
        for k, g in product([F(1, 3), F(1), F(3)], [F(1, 2), F(1), F(5)]):
            z, _ = isolated_path(n, k, g)
            assert abs(float(z) - continuous_path(n, k, g)) < 1e-10
            checks += 1

    last = 0
    for n in range(1, 21):
        gc = critical(n, F(1), F(1))
        assert gc > last
        last = gc
        checks += 1
    # This is a finite sanity check only, not a proof of asymptotics.
    limit = 1 / (acosh(2) ** 2)
    assert abs(critical(400, F(1), F(1)) / 400**2 - limit) < 0.003
    print('PASS', checks, 'exact and numerical checks; g_c(2)=', critical(2, F(1), F(1)))

if __name__ == '__main__':
    main()
