"""Independent numerical checks for the acute-triangle anisotropy theorem.

Requires numpy and scipy. The mathematical proof is independent of this script.
"""
from __future__ import annotations

import math
import numpy as np
from scipy.special import roots_legendre


def acute_quad(ratio: float, n: int = 1600) -> float:
    assert ratio >= 1.0
    nodes, weights = roots_legendre(n)
    theta = math.pi * (nodes + 1.0) / 4.0
    u = 1.0 + (ratio - 1.0) * np.cos(theta) ** 2
    val = np.sum((weights / 2.0) * u / np.sqrt((1.0 + 3.0*u)*(ratio + 3.0*u)))
    return 9.0 * float(val) - 2.0


def acute_sym(ratio: float, n: int = 160) -> float:
    nodes, weights = roots_legendre(n)
    theta = math.pi * (nodes + 1.0) / 4.0
    u = 1.0 + (ratio - 1.0) * np.cos(theta) ** 2
    a = u[:, None]
    b = u[None, :]
    kernel = (a-b)**2/(3.0*a*a+10.0*a*b+3.0*b*b)
    return 0.25 - 2.25 * float(np.sum((weights[:, None]*weights[None, :]/4.0)*kernel))


def acute_sim(ratio: float, n: int, seed: int) -> float:
    rng = np.random.default_rng(seed)
    x = rng.standard_normal((n, 3, 2))
    x[:, :, 0] *= math.sqrt(ratio)
    a = x[:, 1, :] - x[:, 0, :]
    b = x[:, 2, :] - x[:, 0, :]
    c = x[:, 2, :] - x[:, 1, :]
    p1 = np.sum(a*b,axis=1) > 0
    p2 = np.sum((-a)*c,axis=1) > 0
    p3 = np.sum((-b)*(-c),axis=1) > 0
    return float(np.mean(p1 & p2 & p3))


def verify() -> None:
    assert abs(acute_quad(1.0) - 0.25) < 5e-13
    ratios = (1.0, 1.5, 2.0, 4.0, 16.0, 100.0)
    qs = [acute_quad(r) for r in ratios]
    assert all(qs[i] > qs[i+1] for i in range(5))
    for r, val in zip(ratios, qs):
        assert abs(val-acute_sym(r)) < 1e-10, (r,val,acute_sym(r))
        sim=acute_sim(r,200000,20261102+int(r*100))
        assert abs(val-sim) < 0.006, (r,val,sim)
    for delta in (0.02, 0.01, 0.005):
        approx=(.25-acute_quad(1.0+delta))/(delta*delta)
        assert abs(approx - 9/256) < 0.003
    tail = []
    for r in (1e4, 1e6, 1e8):
        val=acute_quad(r, 5000)
        coeff=val*r/math.log(r)
        tail.append(coeff)
        assert abs(coeff-math.sqrt(3)/math.pi) < 0.02, (r,coeff)
    assert tail[0] > tail[-1] > math.sqrt(3)/math.pi
    print('VERIFY_OK', 'exact_isotropic=1/4',
          'quadrature_symmetry_cases=6', 'direct_triangle_simulations=1200000',
          'local_quadratic_cases=3', 'large_anisotropy_cases=3',
          'tail_coefficients='+','.join(f'{v:.9f}' for v in tail))


if __name__ == '__main__':
    verify()
