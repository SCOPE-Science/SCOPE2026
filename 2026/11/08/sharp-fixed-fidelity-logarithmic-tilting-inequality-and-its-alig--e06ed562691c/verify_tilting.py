#!/usr/bin/env python3
"""Finite corroboration of an analytic sharp fixed-fidelity tilting theorem.
Requires NumPy and SciPy; finite numerical checks are not an infinite proof.
"""
import numpy as np
from scipy.integrate import quad
from scipy.linalg import eigh
from scipy.optimize import minimize_scalar

checks = 0
for alpha in (0.6, 0.75, 0.9):
    s = (1 - alpha) / alpha
    for overlap in (0.17, 0.47, 0.83):
        a, b = 1.7, 3.5
        projection = np.diag([1.0, 0.0])
        q = np.array([np.sqrt(overlap), np.sqrt(1 - overlap)])
        other = np.outer(q, q)
        matrix = a**alpha * projection + b**alpha * other
        eigen, basis = eigh(matrix)
        direction = basis.T @ (b**alpha * other) @ basis
        divided = np.empty((2, 2))
        for i in range(2):
            for j in range(2):
                divided[i, j] = (1 / eigen[i] if i == j
                    else (np.log(eigen[i]) - np.log(eigen[j])) / (eigen[i] - eigen[j]))
        derivative = basis @ (divided * direction) @ basis.T
        direct = a * np.trace(projection @ derivative) / (a**alpha * b**(1-alpha) * overlap)
        ratio = (b / a)**alpha
        integrand = lambda z: z*z / (z*z + (1+ratio)*z + ratio*(1-overlap))**2
        integral = ratio**(1-s) * quad(integrand, 0, np.inf, epsabs=2e-12)[0]
        assert abs(direct - integral) < 3e-12
        checks += 1
for s in (0.25, 0.5, 0.8):
    base = s**s * (1-s)**(1-s)
    coefficient = 2*s*(1-s)*base
    for delta in (1e-3, 1e-5):
        def normalized(log_ratio):
            ratio = np.exp(log_ratio)
            integral = quad(lambda z: z*z / (z*z+(1+ratio)*z+ratio*delta)**2,
                            0, np.inf, epsabs=2e-12)[0]
            return -ratio**(1-s)*integral
        res = minimize_scalar(normalized, bounds=(-6, 6), method='bounded')
        assert res.success
        deficit_ratio = (base + res.fun) / (coefficient*delta*np.log(1/delta))
        assert 0.75 < deficit_ratio < 1.1
        checks += 1
print('TILTING_FINITE_CORROBORATION_OK', checks)
