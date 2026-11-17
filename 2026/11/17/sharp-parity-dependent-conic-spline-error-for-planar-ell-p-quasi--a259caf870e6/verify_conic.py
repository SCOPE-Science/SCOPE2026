"""Standalone finite diagnostics for angular conic interpolation of planar quasi-norms.

Run: python verify_conic.py
The limiting theorem is analytic; finite tests are not its proof.
"""
import math
import numpy as np


def profile(theta, p):
    return (np.abs(np.cos(theta))**p + np.abs(np.sin(theta))**p)**(1/p)


def error_grid(N, p, density=500):
    h = math.pi/N
    t = np.arange(density + 1, dtype=float)/density
    j = np.arange(2*N, dtype=float)[:, None]
    theta = (j+t)*h
    val = profile(theta, p)
    left = profile(j*h, p)
    right = profile((j+1)*h, p)
    interp = (np.sin((1-t)*h)*left + np.sin(t*h)*right)/math.sin(h)
    d = val-interp
    ix = np.unravel_index(int(np.argmax(np.abs(d))), d.shape)
    return float(np.max(np.abs(d))/h**p), float(d[ix]), float(theta[ix])


def constants(p):
    return ((1-p)*p**(p/(1-p))/p, 2**(-p)/p)


def run():
    checks = 0
    for p in (0.5, 0.75, 0.95):
        even, odd = constants(p)
        assert 0 < even < odd
        checks += 1
        previous = None
        for N in (24, 48, 96, 192):
            val, signed, theta = error_grid(N, p)
            assert signed > 0
            # The even grid has its largest cusp error on an axis-adjacent cell.
            assert abs(val-even) < 0.08
            if previous is not None:
                assert abs(val-even) < abs(previous-even)+0.005
            previous = val
            checks += 3
        prev = None
        for N in (25, 49, 97, 193):
            val, signed, theta = error_grid(N, p)
            assert signed < 0
            # The odd grid places two coordinate-axis cusps at cell midpoints.
            assert abs(val-odd) < 0.24
            if prev is not None:
                assert abs(val-odd) < abs(prev-odd)+0.005
            prev = val
            checks += 3
    for N in range(2, 40):
        val, signed, _ = error_grid(N, 1.0)
        exact = 0 if N%2 == 0 else math.tan(math.pi/(2*N))
        # Norm was normalized by h**p in error_grid.
        assert abs(val-(exact/(math.pi/N))) < 2e-11
        checks += 1
    for p in (0.2, 0.5, 0.75, 0.9):
        z = p**(1/(1-p))
        assert abs((z**p-z)-((1-p)*p**(p/(1-p)))) < 1e-12
        checks += 1
    print('ANGULAR_CONIC_DIAGNOSTICS_OK', checks)

if __name__ == '__main__':
    run()
