"""Finite reproducibility checks for the Coulomb edge law.

Requires numpy and scipy; no downloaded data and no proof by sampling.
Run: python check.py
"""
import math
import numpy as np
from scipy.linalg import eigh_tridiagonal


def edge_count(s, eps):
    # The infinite tail starts below 2+eps after n>(s+0.2)/eps.
    # Cutting it introduces at most a finite-rank boundary discrepancy.
    N = max(2800, math.ceil((s + 0.2)/eps) + 100)
    a = ((np.arange(N-1, dtype=float)+2.0)/(np.arange(N-1, dtype=float)+1.0))**(s/2)
    ev = eigh_tridiagonal(
        np.zeros(N), a, select='v',
        select_range=(2.0+eps, 2.0*max(a)+1.0), eigvals_only=True,
        check_finite=False)
    return len(ev), N


def check_constant_blocks():
    for L in (2, 5, 11, 19):
        for b in (1.0, 1.13):
            expected = np.array([2*b*math.cos(math.pi*k/(L+1)) for k in range(1,L+1)])
            actual = eigh_tridiagonal(np.zeros(L), np.full(L-1,b), eigvals_only=True)
            assert np.max(np.abs(np.sort(expected)-actual)) < 2e-12
    return 8


def check_integral():
    from scipy.integrate import quad
    for s in (0.75, 2.0, 3.5):
        # x=s*sin(u)^2 removes endpoint singularity.
        val = quad(lambda u: 2*s*math.cos(u)**2,0,math.pi/2,epsabs=1e-12)[0]
        assert abs(val/math.pi - s/2) < 2e-12
    return 3


def main():
    n = check_constant_blocks() + check_integral()
    for s in (0.75, 2.0, 3.5):
        for eps in (0.02, 0.01, 0.005, 0.002):
            count, trunc = edge_count(s,eps)
            semiclassical = s/(2*math.sqrt(eps))
            # Pre-asymptotic O(1) phase shifts are visible at these thresholds.
            assert 0 < count <= math.ceil(semiclassical + 2)
            assert abs(count-semiclassical) < 3.0
            print('s=%.2f eps=%g trunc=%d count=%d prediction=%.5f scaled=%.5f' %
                  (s,eps,trunc,count,semiclassical,count*math.sqrt(eps)))
            n += 1
    print('PASS', n, 'finite checks (not a proof of the infinite result)')


if __name__ == '__main__':
    main()
