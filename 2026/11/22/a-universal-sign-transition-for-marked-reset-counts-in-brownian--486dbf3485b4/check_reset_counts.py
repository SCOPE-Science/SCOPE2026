"""Independent exact-rational checks of marked pre-absorption reset moments.

A killed excursion from state s succeeds with rational probability g[s]; if it
fails, its reset label j is sampled with probability p[j]. We solve the finite
Markov-reward equations directly and compare against the closed formulas.
"""
from fractions import Fraction as F
from random import Random
from math import exp, sqrt


def solve(A, b):
    """Gauss--Jordan elimination entirely over rationals."""
    n = len(b)
    X = [[F(A[i][j]) for j in range(n)] + [F(b[i])] for i in range(n)]
    for col in range(n):
        piv = next(k for k in range(col, n) if X[k][col])
        X[col], X[piv] = X[piv], X[col]
        z = X[col][col]
        X[col] = [q / z for q in X[col]]
        for row in range(n):
            if row != col:
                z = X[row][col]
                if z:
                    X[row] = [v - z * w for v, w in zip(X[row], X[col])]
    return [X[i][-1] for i in range(n)]


def one_case(p, g, g0):
    n = len(p)
    assert n >= 2 and sum(p) == 1 and 0 < g0 < 1
    assert all(0 < x < 1 for x in g) and all(x > 0 for x in p)
    G = sum(p[i] * g[i] for i in range(n))
    Q = [[(1 - g[s]) * p[j] for j in range(n)] for s in range(n)]
    A = [[F(s == j) - Q[s][j] for j in range(n)] for s in range(n)]
    # Reward equations for each count and their pairwise products, not PGF differentiation.
    means = []
    checked = 0
    for i in range(n):
        v = solve(A, [(1 - g[s]) * p[i] for s in range(n)])
        mi = (1 - g0) * (p[i] + sum(p[s] * v[s] for s in range(n)))
        assert mi == (1 - g0) * p[i] / G
        means.append((v, mi))
        checked += 1
    for i in range(n):
        for j in range(i + 1, n):
            vi, mi = means[i]
            vj, mj = means[j]
            rhs = [(1 - g[s]) * (p[i] * vj[i] + p[j] * vi[j]) for s in range(n)]
            v_ij = solve(A, rhs)
            mixed = (1 - g0) * (
                p[i] * vj[i] + p[j] * vi[j] + sum(p[s] * v_ij[s] for s in range(n)))
            assert mixed == (1 - g0) * p[i] * p[j] * (2 - g[i] - g[j]) / G ** 2
            cov = mixed - mi * mj
            expected = (1 - g0) * p[i] * p[j] * (1 + g0 - g[i] - g[j]) / G ** 2
            assert cov == expected
            assert (cov > 0) == (1 + g0 - g[i] - g[j] > 0)
            checked += 3
    return checked


def root_for(x0, a, b):
    assert x0 > a + b > 0
    def c(k):
        return 1 + exp(-k * x0) - exp(-k * a) - exp(-k * b)
    lo, hi = 1e-9, 1.0
    while c(hi) <= 0:
        hi *= 2
    for _ in range(110):
        mid = (lo + hi) / 2
        if c(mid) > 0:
            hi = mid
        else:
            lo = mid
    k = (lo + hi) / 2
    assert abs(c(k)) < 2e-13
    for z in (k / 5, k / 2):
        assert c(z) < 0
    for z in (2 * k, 5 * k):
        assert c(z) > 0
    return k


def main():
    rng = Random(20261121)
    checks = 0
    cases = 0
    for n in (2, 3, 4, 5):
        for rep in range(40):
            weights = [rng.randrange(1, 12) for _ in range(n)]
            p = [F(w, sum(weights)) for w in weights]
            g = [F(rng.randrange(1, 15), 16) for _ in range(n)]
            g0 = F(rng.randrange(1, 15), 16)
            checks += one_case(p, g, g0)
            cases += 1
    # Brownian probabilities chosen exactly: D=1, r=(ln 2)^2 and integer distances.
    # Then g(x)=exp(-sqrt(r/D)*x)=2^{-x} is rational.
    for n in (2, 3, 4):
        for x0 in range(1, 9):
            ds = list(range(1, n + 1))
            p = [F(i + 1, n * (n + 1) // 2) for i in range(n)]
            checks += one_case(p, [F(1, 2 ** x) for x in ds], F(1, 2 ** x0))
            cases += 1
    k = root_for(4.0, 1.0, 2.0)
    assert abs(k - 0.2811995743228) < 1e-10
    assert abs(k * k - 0.0790732005994) < 1e-10
    for a, b, x0 in ((1, 2, 2), (1, 2, 3), (1, 2, 4), (.4, 2, 5), (1.1, 2.6, 5.2)):
        for k0 in (.001, .1, .5, 1, 3):
            c = 1 + exp(-k0*x0)-exp(-k0*a)-exp(-k0*b)
            if x0 <= a+b:
                assert c > 0
        checks += 5
    print('PASS', cases, 'exact-rational finite-state cases;', checks,
          'exact moment/covariance and sign assertions; example k*=', format(k,'.14f'),
          'r*/D=', format(k*k,'.14f'))

if __name__ == '__main__':
    main()
