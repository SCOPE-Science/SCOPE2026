"""Exact and independent numerical checks of five-axis icosahedral harmonic sampling."""
from fractions import Fraction
from math import cos, sin, pi, sqrt
import numpy as np
from scipy.special import sph_harm_y, eval_legendre

F = Fraction
q = [F(1), F(1)]
for n in range(1, 19):
    c = F(1, 5) if n % 2 else F(1)
    q.append(((2 * n + 1) * c * q[n] - n * q[n-1]) / (n + 1))
sharp = {2, 4, 8, 14}
for ell, z in enumerate(q):
    if ell % 2:
        eigenvalues = ([F(1)] + [1 + z] * 2 + [1 - z] * 2)
    else:
        eigenvalues = ([1 + 4 * z] + [1 - z] * 4)
    rank = sum(x != 0 for x in eigenvalues)
    assert rank == ({0: 1, 1: 3, 3: 3}.get(ell, 5)), (ell, rank)
    if ell >= 2 and ell != 3:
        low, high = min(eigenvalues), max(eigenvalues)
        assert low >= F(1, 5)
        assert high <= 6 * low
        assert (low == F(1, 5)) == (ell in sharp)
        assert (high == 6 * low) == (ell in sharp)

# For ell >= 19, Bernstein's strict inequality and sqrt(5) < 9/4, pi > 3 give
# |P_ell(1/sqrt(5))|^2 < 1/26 < 1/25.
assert F(9, 4) / (F(3) * F(39, 2)) == F(1, 26)
assert F(1, 26) < F(1, 25)

points = np.array([(2*cos(2*pi*j/5)/sqrt(5),
                    2*sin(2*pi*j/5)/sqrt(5), 1/sqrt(5)) for j in range(5)])
theta = np.arccos(points[:,2]); phi = np.arctan2(points[:,1], points[:,0])
for ell in range(13):
    sample = np.array([[sph_harm_y(ell, m, theta[i], phi[i])
                        for m in range(-ell, ell + 1)] for i in range(5)], dtype=complex)
    G_ylm = (4 * pi / (2 * ell + 1)) * (sample @ sample.conj().T)
    G_leg = eval_legendre(ell, points @ points.T)
    assert np.max(np.abs(G_leg - G_ylm)) < 5e-12, ell
    predicted = sorted([float(1+4*q[ell])] + [float(1-q[ell])]*4) if ell%2==0 else sorted([1.]+[float(1+q[ell])]*2+[float(1-q[ell])]*2)
    assert np.max(np.abs(np.linalg.eigvalsh(G_ylm) - predicted)) < 5e-12, ell
print('PASS: 19 rational spectral checks; 13 independent harmonic addition-theorem Gram checks; strict all-degree tail certificate')
