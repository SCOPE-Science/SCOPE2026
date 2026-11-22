"""Independent numerical diagnostics for species-labelled first-capture timing.

Requires numpy and scipy. The analytic proof is in RESULT.md; tests do not
certify uncountably many parameters.
"""
import math
import numpy as np
from scipy.optimize import brentq


def probabilities(rates, t):
    total = float(sum(rates))
    alive = math.exp(-total * t)
    caught = -math.expm1(-total * t)
    return np.r_[alive, caught * np.asarray(rates) / total]


def determinant_formula(rates, t):
    total = float(sum(rates))
    k = len(rates)
    caught = -math.expm1(-total * t)
    return (t*t * math.exp(-total*t) * caught**(k-2)
            * total**(2-k) / np.prod(rates))


def root(k):
    assert k >= 3
    def psi(x):
        return 2/x - 1 + (k-2)/math.expm1(x)
    return brentq(psi, 2.0, max(10.0, 3*math.log(k+2)))


def test():
    rng = np.random.default_rng(192821)
    assertions = 0
    for k in range(3, 9):
        opt = root(k)
        assert opt > 2
        assertions += 1
        if k > 3:
            assert opt > root(k-1)
            assertions += 1
        for _ in range(35):
            rates = rng.lognormal(mean=-0.2, sigma=0.9, size=k)
            t = rng.uniform(0.04, 1.6) / sum(rates)
            p = probabilities(rates, t)
            J = np.empty((k+1, k))
            for j in range(k):
                eps = 1.e-5 * rates[j]
                d = np.zeros(k)
                d[j] = eps
                J[:,j] = (probabilities(rates+d,t)-probabilities(rates-d,t)) / (2*eps)
            mat = J.T @ (J/p[:,None])
            numeric = float(np.linalg.det(mat))
            exact = determinant_formula(rates, t)
            assert abs(numeric/exact-1)<5e-5, (k,numeric,exact)
            assertions += 1
            # Same total rate, different composition: the maximizer is unchanged.
            z = np.r_[max(0.1, 0.2*sum(rates)), rates[1:]]
            z *= sum(rates)/sum(z)
            assert abs(root(k) / sum(z) - opt / sum(rates)) < 1e-10
            assertions += 1
            # Check that two deliberately displaced durations lose determinant.
            best = determinant_formula(rates, opt/sum(rates))
            for shift in (0.6, 0.85, 1.15, 1.8):
                assert determinant_formula(rates, shift*opt/sum(rates)) < best
                assertions += 1
    for k in (10, 50, 100, 300, 1000, 10000):
        x = root(k)
        assert abs(x - math.log(k) - 2/math.log(k)) < 2.5/(math.log(k)**2)
        assertions += 1
        q = -math.expm1(-x)
        ratio = x*x*math.exp(-x)/(q*q)
        ratio2 = (x/(2*math.sinh(x/2)))**2
        assert abs(ratio-ratio2)<1e-12
        assertions += 1
    print(f'PASS {assertions} deterministic diagnostics; x3={root(3):.14f}; '
          f'x10={root(10):.14f}; x100={root(100):.14f}')


if __name__ == '__main__':
    test()
