"""Independent numerical quadratic-program checks for small Hamming code hulls.

Requires numpy and scipy; the main exact checker has no external dependencies.
"""

import numpy as np
from scipy.optimize import minimize


def syndrome(word, m):
    result = 0
    for pos in range(1, (1 << m)):
        if word & (1 << (pos - 1)):
            result ^= pos
    return result


def experiment(m):
    n = (1 << m) - 1
    words = [w for w in range(1 << n) if syndrome(w, m) == 0]
    vertices = np.asarray([[(w >> j) & 1 for j in range(n)] for w in words], dtype=float)
    assert len(words) <= 16  # Only m=2,3: truly independent small-instance solve.
    target = np.zeros(n)
    target[0] = 1
    weights0 = np.ones(len(words)) / len(words)

    def fun(weights):
        delta = weights @ vertices - target
        return delta @ delta

    def jac(weights):
        return 2 * (vertices @ (weights @ vertices - target))

    fit = minimize(fun, weights0, jac=jac, method='SLSQP',
                   bounds=[(0,1)]*len(words),
                   constraints={'type': 'eq', 'fun':lambda w: sum(w)-1,
                                'jac':lambda w: np.ones(len(words))},
                   options={'ftol':1e-13, 'maxiter':10000})
    assert fit.success, fit.message
    proj = fit.x @ vertices
    predicted = np.array([(n-1)/(n+3)] + [2/(n+3)]*(n-1))
    assert np.max(np.abs(proj - predicted)) < 1e-7
    assert abs(fit.fun - 4/(n+3)) < 1e-8
    return n, len(words), float(fit.fun), float(np.max(np.abs(proj-predicted)))


if __name__ == '__main__':
    results = [experiment(m) for m in (2,3)]
    print('HAMMING_NUMERIC_QP_PASS:', results)
