"""Finite numerical cross-checks of the pointwise localized transport formula.

The universal separation theorem is proved analytically; these finite linear
programs test its concrete cost matrices and boundary examples.
Requires numpy and scipy.
"""
import itertools
import random
import numpy as np
from scipy.optimize import linprog


def pointwise(d, r, mu, nu):
    n = len(mu)
    result = 0.0
    costs = []
    for m in range(n):
        k = np.maximum(0.0, r - d[m])
        ball = np.flatnonzero(k > 1e-10)
        diameter = max((d[x, y] for x in ball for y in ball), default=0.0)
        c = np.minimum(k[:, None], k[None, :]) * d + diameter * np.abs(k[:, None] - k[None, :])
        costs.append(c)
        S = max(k @ mu, k @ nu)
        if S <= 0:
            raise ValueError('Measures must be strictly positive')
        A = np.zeros((2*n, n*n))
        for x in range(n):
            for y in range(n):
                A[x, x*n+y] = 1
                A[n+y, x*n+y] = 1
        b = np.r_[mu, nu]
        # Drop one redundant constraint.
        sol = linprog(c.ravel(), A_eq=A[:-1], b_eq=b[:-1], bounds=(0, None), method='highs')
        if not sol.success:
            raise RuntimeError(sol.message)
        result = max(result, float(sol.fun)/S)
    return result, costs


def l1(v):
    return float(sum(abs(x) for x in v))


def verify(d, r, mu, nu):
    active = [x for x in range(len(mu)) if any(d[x, y] < r-1e-10 for y in range(len(mu)) if y != x)]
    delta, costs = pointwise(d, r, mu, nu)
    lower = max((min(costs[x][x, y] for y in range(len(mu)) if y != x) / r * abs(mu[x]-nu[x]) for x in active), default=0.0)
    assert delta + 1e-8 >= lower, (d, r, mu, nu, delta, lower)
    if all(abs(mu[x]-nu[x]) < 1e-10 for x in active):
        assert delta < 1e-8, (d, r, active, delta)
    if any(abs(mu[x]-nu[x]) >= 1e-7 for x in active):
        assert delta > 1e-8
    return active, delta, lower


def main():
    # Paper Appendix A, Example A.1, including its non-triangle behavior.
    x = np.array([0., 1., 3.])
    d = abs(x[:, None]-x[None, :])
    mu = np.array([1, 6, 1])/8
    nu = np.array([3, 2, 3])/8
    lam = np.array([2, 5, 1])/8
    vals = [pointwise(d, 2, a, b)[0] for a, b in [(mu, nu),(mu, lam),(lam, nu)]]
    assert np.allclose(vals, [3/4, 2/9, 1/2], atol=2e-9), vals
    # Two isolated sites have exactly zero transport separation.
    z = np.array([0., 1., 5., 10.])
    d = abs(z[:, None]-z[None, :])
    mu = np.array([.2,.3,.2,.3])
    nu = np.array([.2,.3,.3,.2])
    active, delta, _ = verify(d, 2., mu, nu)
    assert active == [0, 1] and delta < 1e-9
    # One isolated site: changing its mass forces change on an active site.
    z = np.array([0., 1., 5.])
    d = abs(z[:, None]-z[None, :])
    active, delta, lower = verify(d, 2., np.array([.2,.3,.5]), np.array([.3,.3,.4]))
    assert active == [0, 1] and delta >= lower > 0
    rng = random.Random(451)
    checks = 0
    for n in range(3, 7):
        for case in range(17):
            # Exact graph-shortest-path integer metric; path with random extra edges.
            d = np.array([[abs(i-j)*2 for j in range(n)] for i in range(n)], dtype=float)
            for i in range(n):
                for j in range(i+1, n):
                    if rng.random() < .35:
                        d[i,j] = d[j,i] = rng.randint(1,5)
            for k in range(n):
                for i in range(n):
                    for j in range(n):
                        d[i,j] = min(d[i,j],d[i,k]+d[k,j])
            for r in sorted(set(float(t) for t in d.ravel() if t > 0)):
                a = np.array([rng.randint(1,10) for _ in range(n)], dtype=float)
                b = np.array([rng.randint(1,10) for _ in range(n)], dtype=float)
                a /= a.sum(); b /= b.sum()
                verify(d, r, a, b)
                checks += 1
    print('Appendix A rational example: PASS; zero-class examples: PASS; random metric/radius pairs:', checks, 'PASS')


if __name__ == '__main__':
    main()
