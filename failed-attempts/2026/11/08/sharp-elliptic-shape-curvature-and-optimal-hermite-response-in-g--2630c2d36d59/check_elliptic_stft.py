"""Independent numerical quadrature for a Gaussian localization ellipse.

Run: python check_elliptic_stft.py
Requires numpy and scipy. This is a finite numerical corroboration, not a proof.
"""
import math
import numpy as np
from scipy.special import roots_legendre


def gram(area, log_axis, levels=14, radial_nodes=120, angular_nodes=192):
    nodes, weights = roots_legendre(radial_nodes)
    v = (nodes + 1) * (area / 2)
    weights = weights * area / 2
    angle = np.arange(angular_nodes) * (2 * np.pi / angular_nodes)
    z = np.sqrt(v[:, None] / np.pi) * (
        np.exp(log_axis) * np.cos(angle)[None, :]
        + 1j * np.exp(-log_axis) * np.sin(angle)[None, :]
    )
    measure = np.exp(-np.pi * abs(z) ** 2) * np.broadcast_to(
        weights[:, None] / angular_nodes, z.shape
    )
    fock = np.stack([
        (np.pi ** (k / 2)) * z**k / math.sqrt(math.factorial(k))
        for k in range(levels)
    ])
    return np.einsum('iab,jab,ab->ij', fock.conj(), fock, measure,
                     optimize=True)


def verify():
    assertions = 0
    def close(a, b, tol):
        nonlocal assertions
        assert np.max(abs(np.asarray(a)-np.asarray(b))) < tol, (a, b, tol)
        assertions += 1

    for area in (0.4, 1.0, 3.0, 5.0):
        diag = np.array([1 - math.exp(-area) * sum(
            area**j/math.factorial(j) for j in range(k+1))
            for k in range(14)])
        center = gram(area, 0)
        close(center, np.diag(diag), 2e-11)
        close(np.trace(center).real, sum(diag), 2e-11)
        # Finite difference estimates, independently computed from 2D quadrature.
        h = 0.001
        pos = gram(area, h)
        neg = gram(area, -h)
        d1 = (pos - neg)/(2*h)
        d2 = (pos + neg - 2*center)/(h*h)
        close(d1[2, 0], area**2*math.exp(-area)/math.sqrt(2), 2e-6)
        close(d2[0, 0], -2*area**2*math.exp(-area), 5e-6)
        close(d1[0, 0], 0, 1e-9)
        for k in list(range(1, 14)):
            if k != 2:
                close(d1[k, 0], 0, 4e-6)
        delta0 = 1-math.exp(-area)
        c = 2*area**2*math.exp(-area)/(area+2)
        mode = math.sqrt(2)*area/(area+2)
        for t in (0.02, 0.01, 0.005):
            plus = gram(area, t)
            minus = gram(area, -t)
            eigs, vecs = np.linalg.eigh(plus)
            eigm = np.linalg.eigvalsh(minus)
            # This is a truncated matrix, not an infinite-dimensional proof.
            close(eigs[-1], eigm[-1], 2e-11)
            measured = (delta0-eigs[-1])/t**2
            close(measured, c, max(2e-4, 0.004*c))
            vec = vecs[:, -1] / vecs[0, -1]
            close((vec[2]/t).real, mode, 0.0025)
            close((vec[2]/t).imag, 0, 1e-7)
            close(vec[1], 0, 1e-7)
            close(vec[3], 0, 1e-7)
        # Independent perturbation identity: second eigenvalue derivative.
        gap = diag[0] - diag[2]
        close(-d2[0, 0] / 2 - abs(d1[2,0])**2/gap, c, 2e-5)
        close(d1[2,0]/gap, mode, 2e-5)
    print(f"ELLIPSE_STFT_CURVATURE_CHECKS_PASS {assertions}")

if __name__ == '__main__':
    verify()
