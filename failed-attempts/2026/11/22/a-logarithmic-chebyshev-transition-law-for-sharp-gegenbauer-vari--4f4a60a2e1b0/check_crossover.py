"""Supplementary checks of the finite-degree Gegenbauer primitive formulas."""
from math import exp, log, pi
import numpy as np
from scipy.special import roots_gegenbauer, eval_gegenbauer, gammaln

def primitive_peak(n, lam):
    if lam == 0:
        return 1 / n, pi / 2
    assert n >= 2 and lam > -.5 and abs(lam) < .5
    zeros, _ = roots_gegenbauer(n, lam)
    root = float(zeros[-1] if lam < 0 else zeros[n // 2])
    c1 = float(eval_gegenbauer(n, lam, 1))
    deriv = float(2 * lam * eval_gegenbauer(n - 1, lam + 1, root) / c1)
    M = abs(deriv) * (1 - root * root) ** (lam + .5) / (n * (n + 2 * lam))
    h = exp((2 * lam - 1) * log(2) + 2 * gammaln(lam + .5) + gammaln(n + 1) - log(n + lam) - gammaln(n + 2 * lam))
    return M, h

def check():
    checks = 0
    for lam in [-.24, -.13, .12, .38]:
        for n in [3, 4, 5, 8, 11, 16, 25, 40]:
            m, h = primitive_peak(n, lam)
            # Independently integrate via high-order Gauss-Jacobi quadrature.
            nodes, weights = roots_gegenbauer(max(160, n + 6), lam)
            p = eval_gegenbauer(n, lam, nodes) / eval_gegenbauer(n, lam, 1)
            hq = np.dot(weights, p * p)
            assert abs(hq - h) < 1e-9 * max(1., h)
            checks += 1
            assert m > 0
            checks += 1
    for tau in [-1, 1, 2]:
        expected = exp(-2 * tau) if tau < 0 else exp(-tau)
        results = []
        for n in [100, 300, 700]:
            M, h = primitive_peak(n, tau / log(n))
            results.append(n * M)
            checks += 1
        assert abs(results[-1] - expected) < abs(results[0] - expected)
        checks += 1
        print('tau=', tau, 'nM sequence=', results, 'limit=', expected)
    print('Supplementary checks passed:', checks)

if __name__ == '__main__':
    check()
