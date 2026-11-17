"""Exact identities and finite numerical cross-checks for Hardy-annulus monomial commutators.
Run: python3 checker.py.  Finite checks supplement, not replace, the proof.
"""
from fractions import Fraction
from math import exp, log, acosh, cosh

assertions = 0

def check(condition, message):
    global assertions
    assertions += 1
    if not condition:
        raise AssertionError(message)

for r in (Fraction(1, 2), Fraction(2, 3), Fraction(3, 4)):
    for k in range(1, 10):
        q = r ** (2 * k)
        for n in range(-14, 15):
            forward = (1 + r ** (2 * (n + k))) / (1 + r ** (2 * n))
            backward = (1 + r ** (2 * n)) / (1 + r ** (2 * (n - k)))
            eig = (1 - q) ** 2 / ((1 + r ** (2 * n)) * (1 + r ** (2 * (k - n))))
            check(forward - backward == eig, ('exact eigenvalue', r, k, n))
            check(eig > 0, ('positivity', r, k, n))
            mirror = (1 - q) ** 2 / ((1 + r ** (2 * (k - n))) * (1 + r ** (2 * n)))
            check(eig == mirror, ('reflection', r, k, n))
        positions = list(range(-20, k + 21))
        values = [(1 - q) ** 2 / ((1 + r ** (2 * n)) * (1 + r ** (2 * (k - n)))) for n in positions]
        if k % 2 == 0:
            expected = (1 - r ** k) ** 2
        else:
            expected = (1 - q) ** 2 / ((1 + r ** (k - 1)) * (1 + r ** (k + 1)))
        check(max(values) == expected, ('exact norm', r, k))
        for N in (4, 12):
            left = sum((1 - q) ** 2 / ((1 + r ** (2 * n)) * (1 + r ** (2 * (k - n)))) for n in range(-N, N + 1))
            shift = lambda n: (1 + r ** (2 * (n + k))) / (1 + r ** (2 * n))
            right = sum((shift(n) for n in range(N - k + 1, N + 1)), Fraction(0)) - sum((shift(n) for n in range(-N - k, -N)), Fraction(0))
            check(left == right, ('finite telescoping', r, k, N))

for a in (0.5, 1.0, 2.0):
    for k in (2, 5, 20, 100):
        r = exp(-a / k)
        b = a / k
        peak = (1 - exp(-a)) ** 2
        q = exp(-2 * a)
        K = (1 - q) ** 2 / (2 * exp(-a))
        for z in (0.001, 0.03, 0.2, 0.5, 0.9, 0.99):
            threshold = peak * z
            halfwidth = acosh(K / threshold - cosh(a)) / (2 * b)
            indices = range(int(k / 2 - halfwidth) - 3, int(k / 2 + halfwidth) + 4)
            count = sum((1 - q)**2 / ((1 + exp(-2 * b * n)) * (1 + exp(-2 * b * (k - n)))) > threshold for n in indices)
            expected = 2 * halfwidth
            check(abs(count - expected) <= 1 + 1e-9, ('count discrepancy', a, k, z, count, expected))

# Numerical integration of the continuum density; validates the closed p=1,2 moments.
for a in (0.5, 1.0, 2.0):
    q = exp(-2 * a)
    size = 20000
    bound = 80.0
    h = 2 * bound / size
    moment = [0.0, 0.0]
    for j in range(size + 1):
        t = -bound + j * h
        density = (1 - q) ** 2 / ((1 + exp(-2 * a * t)) * (1 + exp(-2 * a * (1 - t))))
        weight = 0.5 if j in (0, size) else 1.0
        moment[0] += weight * density * h
        moment[1] += weight * density * density * h
    check(abs(moment[0] - (1 - q)) < 1e-8, ('W1 continuum', a))
    check(abs(moment[1] - (1 - q*q) + (1 - q)**2 / a) < 1e-8, ('W2 continuum', a))
print('ANNULUS_MONOMIAL_SPECTRAL_CHECKS_OK', assertions)
