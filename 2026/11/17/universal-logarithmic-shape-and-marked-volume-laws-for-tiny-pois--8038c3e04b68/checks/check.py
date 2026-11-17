"""Standalone numerical checks for Poisson-cuboid rare-volume formulas.

Run: python checks/check.py
Requires: mpmath (see checks/requirements.txt). No external data.
"""
import math
import random
import mpmath as mp

mp.mp.dps = 70

def f_product_d2(k, a):
    z = 2 * mp.sqrt(a)
    if k == 1:
        return 1 - z * mp.besselk(1, z)
    if k == 2:
        return 1 - 2 * a * mp.besselk(2, z) - 2 * a ** mp.mpf('1.5') * mp.besselk(1, z)
    raise ValueError('Only the two cell-selection conventions are checked')

def twoterm(k, d, a):
    l = -mp.log(a)
    return a ** k / (k * math.factorial(d-1)) * (
        l ** (d-1) + (d-1)*(mp.mpf(1)/k-d*mp.euler)*l ** (d-2))

for k in (1, 2):
    errors = []
    for a in (mp.mpf('1e-4'), mp.mpf('1e-6'), mp.mpf('1e-8')):
        exact = f_product_d2(k, a)
        approx = twoterm(k, 2, a)
        rel = float(abs(exact / approx - 1))
        errors.append(rel)
        print('EXACT_2D', k, mp.nstr(a, 4), mp.nstr(exact, 12), 'relative_error', f'{rel:.9g}')
    assert errors[2] < errors[1] < errors[0] < 0.001
print('TWO_TERM_CONSTANTS_OK')

rng = random.Random(20261111)
N = 100000
lam = (0.7, 1.4, 2.1)
for k in (1, 2):
    sums = [0.0, 0.0, 0.0]
    sqs = [0.0, 0.0, 0.0]
    marks = [0.0, 0.0, 0.0]
    for _ in range(N):
        for j, rate in enumerate(lam):
            left = rng.expovariate(rate)
            right = rng.expovariate(rate)
            w = left if k == 1 else left + right
            sums[j] += w
            sqs[j] += w*w
            marks[j] += (left/(left+right) if k == 2 else 0.0)
    for j, rate in enumerate(lam):
        assert abs(sums[j]/N - k/rate) < 0.022
        assert abs(sqs[j]/N - k*(k+1)/rate**2) < 0.13
        if k == 2:
            assert abs(marks[j]/N - 0.5) < 0.008
print('POISSON_GAP_MOMENTS_AND_ZERO_MARKS_OK')

# The ratio of the characteristic log-domain conditional density at an interior
# simplex point to its limiting value approaches one as the threshold decreases.
for k in (1, 2):
    u1, u2, z = 0.2, 0.35, 0.7
    deviations = []
    for l in (15.0, 35.0, 70.0):
        t = (l*u1, l*u2, l*(1-u1-u2)+z)
        correction = math.prod(math.exp(-math.exp(-ti)) for ti in t)
        deviations.append(abs(1-correction))
    assert deviations[2] < deviations[1] < deviations[0]
print('LOG_SIMPLEX_LOCAL_DENSITY_LIMIT_OK')
print('POISSON_CUBOID_MARKED_SMALL_VOLUME_CHECKS_OK')
