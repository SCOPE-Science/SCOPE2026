#!/usr/bin/env python3
"""Independent symbolic identities and finite-sample checks of split-graph jamming laws."""
import math
import numpy as np
import sympy as sp


def verify_symbolic():
    u, c, beta = sp.symbols('u c beta', positive=True, real=True)
    observed = sp.simplify(sp.exp(c) / beta * sp.integrate(u * (u + 2) * sp.exp(-u), (u, 0, c)))
    target = (4 * sp.exp(c) - (c + 2)**2) / beta
    assert sp.simplify(observed - target) == 0
    x, y = sp.symbols('x y', positive=True, real=True)
    F = x / y - sp.log(y)
    direction = sp.simplify(sp.diff(F, x) * (-x * (x + y)) + sp.diff(F, y) * (-x*y))
    assert direction == 0
    print('PASS: fluid invariant and full quadratic-variation integral verified symbolically')


def simulate(a, b, samples, seed):
    gen = np.random.default_rng(seed)
    A = np.full(samples, a, dtype=np.int32)
    B = np.full(samples, b, dtype=np.int32)
    while np.any(A):
        denom = A - 1 + 2*B
        live = A > 0
        good = live & (denom > 0)
        p = np.zeros(samples)
        p[good] = 2 * B[good] / denom[good]
        cross = good & (gen.random(samples) < p)
        internal = good & ~cross
        A[cross] -= 1
        B[cross] -= 1
        A[internal] -= 2
        A[live & ~good] = 0
    return B.astype(float)


def main():
    verify_symbolic()
    R = 400
    for j, (alpha, beta) in enumerate(((1, 1), (2, 1), (1, 2))):
        vals = simulate(alpha*R, beta*R, 30000, 98761+j)
        c = alpha / beta
        mean_limit = beta * math.exp(-c)
        variance_limit = beta * (4*math.exp(-c) - (c+2)**2*math.exp(-2*c))
        empirical_mean = vals.mean() / R
        empirical_variance = vals.var() / R
        assert abs(empirical_mean - mean_limit) < 0.018, (alpha, beta, empirical_mean)
        assert abs(empirical_variance - variance_limit) < 0.030, (alpha, beta, empirical_variance)
        print('alpha,beta:',alpha,beta,'vacancy mean / scale:',round(empirical_mean,6),
              'target:',round(mean_limit,6),'vacancy variance / scale:',
              round(empirical_variance,6),'target:',round(variance_limit,6))
    print('PASS: three seeded large-finite simulation comparisons; these are not proofs of limits')


if __name__ == '__main__':
    main()
