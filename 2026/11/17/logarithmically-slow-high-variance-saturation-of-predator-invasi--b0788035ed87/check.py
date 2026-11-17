"""Supplementary numerical checks for the bounded-refuge strong-noise asymptotic.

Requires Python 3 and mpmath; no data files or external services are used.
This finite numerical check is not a proof of the all-parameter theorem.
"""
from fractions import Fraction
import mpmath as mp

mp.mp.dps = 45
p = mp.mpf(1) / 2
eps = mp.mpf(1) / 4
q = 2 * eps / mp.pi

def phi(v):
    return v / (1 + v)

def H(t):
    return (phi(p + q * mp.atan(t)) + phi(p - q * mp.atan(t))) / 2

H_inf = (phi(p + eps) + phi(p - eps)) / 2

def Q(t):
    return H(t) - H_inf

A = q / 2 * ((1 + p - eps) ** (-2) - (1 + p + eps) ** (-2))
assert mp.almosteq(A, mp.mpf(96) / (1225 * mp.pi))
C = mp.sqrt(2 / mp.pi) * A
assert C > 0

# Truncation at 10^6 is adequate for the scaling comparisons below:
# the omitted remainder decays as O(T^-1).
B_T = mp.quad(Q, [0, 1]) + mp.quad(
    lambda t: Q(t) - A / t, [1, 10, 100, 1000, 10000, 100000, 1000000]
)
E = (mp.log(2) - mp.euler) / 2
errors = []
for s in (mp.mpf(100), mp.mpf(1000), mp.mpf(10000)):
    # The nonnegative density is integrated in unscaled t, preserving
    # the t ~ 1 transition responsible for the logarithmic factor.
    points = [0, 1, 10, 100, s, 4 * s, 12 * s]
    points = sorted(set(points))
    D = mp.sqrt(2 / mp.pi) / s * mp.quad(
        lambda t: Q(t) * mp.exp(-t * t / (2 * s * s)), points
    )
    asym = mp.sqrt(2 / mp.pi) / s * (A * mp.log(s) + B_T + A * E)
    scaled_error = abs(s * (D - asym))
    errors.append(scaled_error)
    assert D > 0
    print('s=', int(s), 'exact integral=', mp.nstr(D, 18),
          'two-term prediction=', mp.nstr(asym, 18),
          'scaled error=', mp.nstr(scaled_error, 10))
assert errors[2] < errors[1] < errors[0]
assert errors[2] < mp.mpf('0.000003')
assert mp.almosteq(C, mp.mpf('0.019903311182651863182'), rel_eps=mp.mpf('1e-17'))
print('PASS: rational coefficient and supplemental Gaussian-integral checks')
