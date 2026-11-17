"""Independent finite numerical and exact-rational checks for a Gaussian localization shape theorem.

The infinite-dimensional theorem is proved analytically in RESULT.md. This script
checks its mode coefficients and several finite-section spectral perturbations.
Requires Python 3, NumPy and SciPy. Run: python check_shape_hessian.py
"""
from fractions import Fraction
from math import exp, factorial, pi
import numpy as np
from scipy.special import gammainc, gammaln, gamma

checks = 0

def test(condition, description):
    global checks
    if not condition:
        raise AssertionError(description)
    checks += 1

def h_exact(R, k):
    assert k >= 1 and R > 0
    last = R**k / factorial(k)
    subtotal = sum((R**j / factorial(j) for j in range(1, k + 1)), Fraction())
    return 1 - last / subtotal

for R in (Fraction(1, 4), Fraction(1, 2), Fraction(1), Fraction(2),
          Fraction(5), Fraction(20)):
    test(h_exact(R, 1) == 0, f"translation mode R={R}")
    test(h_exact(R, 2) == Fraction(2, 1) / (R + 2), f"quadrupole R={R}")
    prev = Fraction(-1)
    for n in range(1, 55):
        h = h_exact(R, n)
        test(0 <= h < 1, f"bounds R={R},n={n}")
        test(h > prev, f"strict monotonicity R={R},n={n}")
        if n >= 2:
            test(h >= h_exact(R, 2), f"sharp bound R={R},n={n}")
        prev = h

def top_eigen(R, eps, components, cutoff=28, angles=384):
    """Exact radial integrals plus angular trapezoid integration; a finite section."""
    theta = 2 * pi * np.arange(angles) / angles
    u = np.zeros_like(theta)
    for kind, k, amplitude in components:
        u += amplitude * (np.cos(k * theta) if kind == 'c' else np.sin(k * theta))
    bound = R + eps * u
    assert np.min(bound) > 0
    t = np.arange(cutoff)
    angles_basis = np.exp(1j * np.outer(t, theta))
    logfac = gammaln(t + 1)
    A = np.zeros((cutoff, cutoff), dtype=complex)
    for j in range(cutoff):
        for k in range(j, cutoff):
            power = (j + k) / 2 + 1
            radial = gamma(power) * gammainc(power, bound)
            z = np.mean(radial * angles_basis[k] * np.conj(angles_basis[j]))
            z *= np.exp(-.5 * (logfac[j] + logfac[k]))
            A[j, k] = z
            A[k, j] = np.conj(z)
    vals, vecs = np.linalg.eigh(A)
    v = vecs[:, -1]
    v *= np.exp(-1j * np.angle(v[0]))
    return float(vals[-1]), v

def predicted_coefficient(R, components):
    spectral = {}
    for kind, k, a in components:
        spectral[k] = spectral.get(k, 0.) + a*a / 4
    return exp(-R) * sum(float(h_exact(Fraction(str(R)), k)) * w
                         for k, w in spectral.items())

for R in (0.5, 2.0, 6.0):
    for k in (1, 2, 3, 4, 5):
        components = [('c', k, 1.)]
        target = predicted_coefficient(R, components)
        results = []
        for eps in (0.04, 0.02):
            val, _ = top_eigen(R, eps, components)
            deficit = (1 - exp(-R) - val) / (eps * eps)
            results.append(deficit)
            test(abs(deficit - target) < 2e-4 + target * 0.005,
                 f"mode limit R={R},k={k},eps={eps},got={deficit},want={target}")
        test(abs(results[-1] - target) <= abs(results[0] - target) + 5e-7,
             f"convergence R={R},k={k}")
    components = [('c', 2, .65), ('s', 3, .32), ('c', 4, .2)]
    target = predicted_coefficient(R, components)
    for eps in (0.04, 0.02):
        val, _ = top_eigen(R, eps, components)
        deficit = (1 - exp(-R) - val) / (eps * eps)
        test(abs(deficit - target) < 2e-4 + target * 0.01,
             f"mixed mode R={R},eps={eps},got={deficit},want={target}")

for R in (0.7, 2., 5.):
    eps = 0.012
    _, v = top_eigen(R, eps, [('c', 2, 1.)])
    S2 = R + R**2/2
    derivative = (R / np.sqrt(2)) * (.5 / S2)
    test(abs(v[2].real / eps - derivative) < 0.004,
         f"eigenvector response R={R}")
    test(abs(v[2].imag) < 1e-7, f"eigenvector phase R={R}")

print(f"GAUSSIAN_SHAPE_CHECKS_PASS {checks}")
