"""Finite numerical diagnostics for the conditional stiff-return boundary-layer law.

Only illustrative tests. The asymptotic theorem requires the separate analytic proof.
"""
import numpy as np
from math import sqrt, exp
from scipy.integrate import solve_bvp, simpson
from scipy.special import dawsn


def killed_search_alarm_density(x, D, L, r):
    a = sqrt(r / D)
    x = np.asarray(x)
    return r / (2 * sqrt(D * r)) * (np.exp(-a * np.abs(x)) - np.exp(-a * (2 * L - x)))


def ou_return_hit_probability(x, K, L):
    x = np.asarray(x)
    t = sqrt(K / 2)
    answer = np.exp((K / 2) * ((x / L) ** 2 - 1)) * dawsn(t * x / L) / dawsn(t)
    return np.where(x > 0, answer, 0.)


def bvp_laplace(K, s):
    """F'' + (1-z/K)F' = sF, F(0)=1, F(K)=0."""
    z = np.linspace(0, K, 1000)
    a = (1 + sqrt(1 + 4 * s)) / 2
    guess = np.vstack((np.exp(-a * z), -a * np.exp(-a * z)))
    def ode(z, v):
        return np.vstack((v[1], s * v[0] - (1 - z / K) * v[1]))
    def boundary(left, right):
        return np.array((left[0] - 1, right[0]))
    ans = solve_bvp(ode, boundary, z, guess, tol=2e-8, max_nodes=30000)
    assert ans.success, ans.message
    return ans


def run(D, L, r):
    q = exp(-L * sqrt(r / D))
    print(f'Brownian search: D={D}, L={L}, r={r}, q={q:.8g}')
    for K in (12., 24., 48., 96.):
        grid = np.linspace(0, K, 2001)
        x = L * (1 - grid / K)
        h = killed_search_alarm_density(x, D, L, r)
        f0 = ou_return_hit_probability(x, K, L)
        prob = simpson(h * f0, x=grid) * L / K
        assert prob > 0
        ratio = prob * K ** 2 / (r * L ** 2 / D * q)
        print(f'  K={K:g}  P(E) / [r L² q/(D K²)] = {ratio:.8f}')
        for u, s in ((0.25, 0.15), (0, 0.7), (0.5, 1.5)):
            sol = bvp_laplace(K, s)
            f = sol.sol(grid)[0]
            assert min(f) > -1e-7
            joint = simpson(h * f * np.exp(-u * grid), x=grid) * L / K
            observed = joint / prob
            expected = (u + (1 + sqrt(1 + 4 * s)) / 2) ** -2
            print(f'       u={u:g}, s={s:g}: LT {observed:.7f}; limit {expected:.7f}')
            if K >= 48:
                assert abs(observed - expected) < 0.09

if __name__ == '__main__':
    run(1., 1., 1.)
    run(2., 1.5, 0.6)
    print('All finite BVP consistency checks passed.')
