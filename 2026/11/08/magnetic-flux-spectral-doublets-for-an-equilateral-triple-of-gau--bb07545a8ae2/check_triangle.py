"""Independent finite-section quadrature checks for a three-disk Fock concentration law.

Usage: python check_triangle.py
Requires Python 3, NumPy, SciPy.  Numerical checks are not infinite-dimensional proof.
"""
import math
import numpy as np
from scipy.special import roots_legendre, gammaln


def direct_eigenvalues(distance, radius_sq=0.5, n_basis=72,
                       n_radial=20, n_angular=128, return_matrix=False):
    """Compute a quadrature Fock matrix, not the coherent-state effective matrix."""
    centers = [distance / math.sqrt(3) * np.exp(2j * math.pi * j / 3)
               for j in range(3)]
    ns = np.arange(n_basis)
    inv_sqrt_factorial = np.exp(-0.5 * gammaln(ns + 1))
    matrix = np.zeros((n_basis, n_basis), dtype=complex)
    x, weights = roots_legendre(n_radial)
    angles = np.linspace(0, 2 * math.pi, n_angular, endpoint=False)
    radius = math.sqrt(radius_sq)
    for center in centers:
        for rr, ww in zip((x + 1) * radius / 2, weights * radius / 2):
            points = center + rr * np.exp(1j * angles)
            v = (np.exp(-0.5 * abs(points[:, None])**2)
                 * points[:, None]**ns * inv_sqrt_factorial)
            matrix += (ww * rr * 2 / n_angular) * (v.conj().T @ v)
    assert np.linalg.norm(matrix - matrix.conj().T) < 1e-12
    if return_matrix:
        return matrix
    return np.linalg.eigvalsh(matrix)[::-1]


def gram_predictions(distance, radius_sq):
    phase = math.sqrt(3) * distance**2 / 2
    overlap = math.exp(-distance**2 / 2)
    ell = -math.expm1(-radius_sq)
    harmonics = np.array([math.cos((phase + 2 * math.pi * j) / 3)
                          for j in range(3)])
    return np.sort(ell * (1 + 2 * overlap * harmonics))[::-1]


def run():
    tests = 0
    radius_sq = 0.5
    ell0 = -math.expm1(-radius_sq)
    ell1 = 1 - (1 + radius_sq) * math.exp(-radius_sq)
    previous_error = None
    for triangle_area_in_units_pi in [3.0, 3.5, 4.0, 4.5, 5.0]:
        d = math.sqrt(4 * math.pi * triangle_area_in_units_pi / math.sqrt(3))
        exact_finite = direct_eigenvalues(d, radius_sq)
        predicted = gram_predictions(d, radius_sq)
        overlap = math.exp(-d*d/2)
        phase = math.sqrt(3)*d*d/2
        expected_cos = np.sort(np.cos((phase+2*np.pi*np.arange(3))/3))[::-1]
        for j in range(3):
            assert abs((exact_finite[j] - ell0) / (ell0*overlap)
                       - 2*expected_cos[j]) < 0.0025
            tests += 1
        assert exact_finite[3] < ell1 + 0.001
        tests += 1
        err = max(abs((exact_finite[:3] - predicted)/(ell0*overlap)))
        if previous_error is not None:
            assert err < previous_error
            tests += 1
        previous_error = err
        if triangle_area_in_units_pi.is_integer():
            target = 3.0
            assert abs((exact_finite[0]-exact_finite[1])/(ell0*overlap)-target)<.003
            tests += 1
        else:
            assert abs((exact_finite[0]-exact_finite[1])/(ell0*overlap))<.003
            assert abs((exact_finite[1]-exact_finite[2])/(ell0*overlap)-3)<.003
            tests += 2
    # Each eigenmode of rotation has Fock degrees in a fixed residue class mod 3.
    # Top branches in different sectors truly exchange their order across flux cells.
    sectors = []
    for t in [3.4, 3.6, 3.9, 4.1]:
        d = math.sqrt(4 * math.pi * t / math.sqrt(3))
        full = direct_eigenvalues(d, radius_sq, return_matrix=True)
        tops = []
        for q in range(3):
            idx = np.arange(q, len(full), 3)
            tops.append(np.linalg.eigvalsh(full[np.ix_(idx, idx)])[-1])
        sectors.append(tops)
    assert (sectors[0][0]-sectors[0][1]) * (sectors[1][0]-sectors[1][1]) < 0
    tests += 1
    assert (sectors[2][0]-sectors[2][2]) * (sectors[3][0]-sectors[3][2]) < 0
    tests += 1
    assert ell1 < ell0
    tests += 1
    print(f'TRIANGLE_FLUX_CHECKS_PASS {tests}')


if __name__ == '__main__':
    run()
