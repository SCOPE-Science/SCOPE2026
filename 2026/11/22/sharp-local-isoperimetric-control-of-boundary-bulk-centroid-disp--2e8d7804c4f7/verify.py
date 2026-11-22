"""Numerical checks for the disk-centroid Fourier law.

Only finite numerical comparisons are performed; analytic proofs establish the theorem.
Run using Python 3 and the standard library.
"""
import cmath
import math
import random

TAU = 2.0 * math.pi


def second_order(coeffs):
    """Positive Fourier index -> coefficient of exp(i k theta), real f by conjugation."""
    energy = sum((k*k-1) * abs(a)**2 for k, a in coeffs.items())
    q = sum((k-1)*(k+2) * a * coeffs.get(k+1, 0j).conjugate()
            for k, a in coeffs.items())
    return q, energy


def quadrature(coeffs, eps, n=16384):
    # Riemann/trapezoid evaluation of exact radial and arclength integrals.
    area_integral = 0.0
    length_integral = 0.0
    volume_moment = 0j
    boundary_moment = 0j
    for j in range(n):
        t = TAU * j / n
        f = 0.0
        fp = 0.0
        for k, a in coeffs.items():
            z = a * cmath.exp(1j*k*t)
            f += 2.0*z.real
            fp += 2.0*(1j*k*z).real
        rho = 1.0 + eps*f
        drho = eps*fp
        ds = math.hypot(rho, drho)
        area_integral += rho*rho
        length_integral += ds
        e = cmath.exp(1j*t)
        volume_moment += e*rho**3
        boundary_moment += e*rho*ds
    dt = TAU/n
    area = 0.5*dt*area_integral
    length = dt*length_integral
    volume_centroid = dt*volume_moment/(3.0*area)
    boundary_centroid = dt*boundary_moment/length
    delta = length*length-4.0*math.pi*area
    return boundary_centroid-volume_centroid, delta, length


def check():
    coeffs = {2: 0.5+0j, 3: 0.5+0j}
    q, energy = second_order(coeffs)
    assert abs(q-1) < 1e-14
    assert abs(energy-11/4) < 1e-14
    # The leading coefficients in this example are exactly 1 and 22*pi^2.
    for eps in (0.006, 0.003, 0.0015):
        z, delta, length = quadrature(coeffs, eps)
        assert abs(z/(eps*eps)-q) < 4.0*eps
        assert abs(delta/(eps*eps)-8.0*math.pi**2*energy) < 500.0*eps
        assert abs(length-TAU) < 200.0*eps*eps

    rng = random.Random(271828)
    for _ in range(12):
        c = {k: complex(rng.uniform(-0.5, 0.5),
                         rng.uniform(-0.5, 0.5)) for k in range(2, 9)}
        q, energy = second_order(c)
        assert energy > 0
        assert abs(q) < energy
        eps = 0.00025
        z, delta, length = quadrature(c, eps, 8192)
        assert abs(z/(eps*eps)-q) < 0.025
        assert abs(delta/(eps*eps)-8.0*math.pi**2*energy) < 3.0
    for start, width in ((10, 20), (100, 100), (2000, 1000)):
        coeffs = {k: 1.0/math.sqrt(k*k-1) for k in range(start,start+width+1)}
        q, energy = second_order(coeffs)
        assert 0 < q.real < energy
        if start == 2000:
            assert (q.real/energy) > 0.999
    print('PASS: 3 trigonometric cases; 12 randomized complex-mode cases; 3 sharpness packets.')


if __name__ == '__main__':
    check()
