#!/usr/bin/env python3
"""Supplementary numerical checks for a two-tone Fourier inequality.

The mathematical proof is analytic; grid tests here do not certify all parameters.
"""
import math

def sinc(x):
    return math.sin(x) / x if x else 1.0

def bisect_root():
    lo, hi = math.pi + 0.001, 1.5 * math.pi - 0.001
    for _ in range(90):
        mid = (lo + hi) / 2
        if math.tan(mid) - mid > 0:
            hi = mid
        else:
            lo = mid
    return (lo + hi) / 2

def sharp(phi, rho):
    return 2 / (1 + min(-rho, math.cos(phi)))

def main():
    d0 = bisect_root()
    rho = 1 / math.sqrt(1 + d0 * d0)
    phi0 = math.acos(-rho)
    assert abs(d0 - 4.493409457909064) < 1e-12
    assert abs(sinc(d0) + rho) < 1e-13
    assert abs(phi0 - 1.7897758492705223) < 1e-12
    for j in range(1, 1800):
        d = j / 100.0
        assert sinc(d) >= -rho - 1e-13
        assert sinc(d) < 1
    for ii in range(0, 31):
        phi = ii * math.pi / 32
        K = sharp(phi, rho)
        for jj in range(1, 130):
            d = jj * 0.069
            for kk in range(0, 15):
                theta = phi * (2 * kk / 14 - 1)
                h = sinc(d) * math.cos(theta)
                assert 2 / (1 + h) <= K + 1e-11
                for u, v in ((1.0,1.0), (0.2,4.0), (3.0,0.25)):
                    Q = (u + v)**2/(u*u+v*v+2*u*v*h)
                    assert Q <= K + 1e-11
    K0 = sharp(0, rho)
    assert abs(K0 - 2.5550407785526074) < 1e-11
    # Exact alignment for equal positive amplitudes at t=2 pi / d0.
    t = 2 * math.pi / d0
    assert t > 1
    peak = abs(1 + complex(math.cos(d0*t), math.sin(d0*t)))**2
    obs = 2*(1+sinc(d0))
    assert abs(peak/obs - K0) < 1e-12
    for phi in (phi0 + 0.01, 2.0, 2.8, 3.0):
        for d in (0.01, 0.001, 0.0001):
            val = 2/(1+sinc(d)*math.cos(phi))
            assert val < sharp(phi,rho)
            assert sharp(phi,rho)-val < 5000*d*d
    print('PHASE_APERTURE_CHECKS_PASSED')

if __name__ == '__main__':
    main()
