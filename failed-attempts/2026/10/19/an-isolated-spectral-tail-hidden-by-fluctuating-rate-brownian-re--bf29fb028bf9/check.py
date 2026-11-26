"""Numerical cross-checks for the exact spectral mixture of refreshed-rate resetting.

Run: python check.py
Requires NumPy 2.x and SciPy 1.x. The analytical proof is in RESULT.md.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.linalg import eigh
from scipy.optimize import brentq
from scipy.special import exp1, expi, roots_laguerre

GAMMA = 0.5772156649015329
TESTS = 0


def verify(predicate, label):
    global TESTS
    TESTS += 1
    if not predicate:
        raise AssertionError(label)


def B(s, mean):
    return math.exp(s / mean) * float(exp1(s / mean)) / mean


def spectral_parameters(refresh, mean):
    root = brentq(lambda s: refresh * B(s, mean) - 1.0,
                  1e-270, refresh, xtol=1e-270, rtol=2e-13)
    rate = refresh - root
    atom = mean * root / (refresh * rate)
    return root, rate, atom


def density(rate_variable, refresh, mean):
    z = rate_variable / mean
    factor = math.exp(-z)
    real = 1.0 + refresh / mean * factor * float(expi(z))
    imag = math.pi * refresh / mean * factor
    return factor / (mean * (real * real + imag * imag))


SPLITS = [-35., -22., -17., -12., -8., -4., -1., 0., 1., 3., 5.]


def spectral_integral(refresh, mean, h):
    def integrand(t):
        lam = math.exp(t)
        return lam * density(lam, refresh, mean) * h(lam)
    return sum(quad(integrand, a, b, epsabs=2e-12,
                    epsrel=2e-11, limit=150)[0]
               for a, b in zip(SPLITS[:-1], SPLITS[1:]))


for refresh in (0.05, 0.2, 0.5, 1.0, 2.0):
    mean = 1.0
    root, rate, atom = spectral_parameters(refresh, mean)
    verify(0.0 < root < refresh and 0.0 < rate < refresh, "root location")
    verify(0.0 < atom < 1.0, "atom probability")
    verify(abs(refresh * B(root, mean) - 1.0) < 2e-11, "pole equation")

    mass = spectral_integral(refresh, mean, lambda z: 1.0)
    verify(abs(atom + mass - 1.0) < 1e-8, "normalization")
    for q in (0.0, 0.25, 1.0, 3.0):
        transform = B(refresh + q, mean) / (1.0 - refresh * B(refresh + q, mean))
        spectral = atom / (q + rate) + spectral_integral(
            refresh, mean, lambda z: 1.0 / (q + refresh + z))
        verify(abs(transform - spectral) < 1e-8, "Stieltjes transform")

    width2 = 2.0 * B(refresh, mean) / (1.0 - refresh * B(refresh, mean))
    from_transform = 2.0 * (atom / rate + spectral_integral(
        refresh, mean, lambda z: 1.0 / (refresh + z)))
    verify(abs(width2 - from_transform) < 2e-8, "second moment")

for refresh in (0.04, 0.05):
    root, rate, atom = spectral_parameters(refresh, 1.0)
    tiny = math.exp(-GAMMA - 1.0 / refresh)
    verify(abs(root / tiny - 1.0) < 2e-5, "exponentially small pole")
    verify(abs(atom / (tiny / (refresh * refresh)) - 1.0) < 2e-5,
           "exponentially small residue")

# Matrix discretization of the self-adjoint refreshed-rate generator,
# independent of the analytic Stieltjes boundary-value calculation.
for refresh in (0.5, 1.0):
    exact_rate = spectral_parameters(refresh, 1.0)[1]
    rates, weights = roots_laguerre(128)
    w = np.sqrt(weights)
    generator = -np.diag(rates + refresh) + refresh * np.outer(w, w)
    top = eigh(generator, subset_by_index=(127, 127), check_finite=True)[0][0]
    verify(abs(-top - exact_rate) < 2e-6, "finite quadrature spectral edge")

# The positive, isolated pole eventually dominates the continuum at long range.
refresh, mean, diffusion = 0.5, 1.0, 1.0
_, rate, atom = spectral_parameters(refresh, mean)
for x, tolerance in ((300., 0.008), (900., 0.0002)):
    excess = spectral_integral(refresh, mean,
       lambda z: math.sqrt((refresh + z) / rate)
       * math.exp(-x * (math.sqrt(refresh + z) - math.sqrt(rate)))) / atom
    verify(0.0 <= excess < tolerance, "spatial far-field pole dominance")

print("PASS: %d numerical spectral, normalization, asymptotic and matrix checks" % TESTS)
