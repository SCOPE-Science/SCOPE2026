"""Independent finite checks for the phase-only cyclic Gabor spectral identities.

Python 3 standard library only. Finite checks supplement the analytic argument.
"""
import cmath
import math
import random

PI = math.pi
TOL = 2e-10
rng = random.Random(20261106)
checks = 0


def almost(a, b, tol=TOL):
    global checks
    assert abs(a - b) < tol, (a, b, abs(a - b))
    checks += 1


def determinant_integer(a):
    """Exact Bareiss determinant, integer input."""
    a = [row[:] for row in a]
    n = len(a)
    if n == 1:
        return a[0][0]
    sgn = 1
    prev = 1
    for k in range(n - 1):
        if a[k][k] == 0:
            j = next(j for j in range(k + 1, n) if a[j][k])
            a[j], a[k] = a[k], a[j]
            sgn = -sgn
        pivot = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                numerator = a[i][j] * pivot - a[i][k] * a[k][j]
                assert numerator % prev == 0
                a[i][j] = numerator // prev
        for i in range(k + 1, n):
            a[i][k] = 0
        prev = pivot
    return sgn * a[n - 1][n - 1]


for p in range(2, 23):
    m = [[0 for _ in range(p)] for _ in range(p)]
    m[0][0] += 1
    m[0][p - 1] += 1
    for r in range(1, p):
        m[r][r] = 1
        m[r][r - 1] = -1
    assert abs(determinant_integer(m)) == 2
    checks += 1

for p in range(2, 11):
    n = 2 * p
    for trial in range(17):
        phases = [2 * PI * rng.random() for _ in range(n)]
        g = [cmath.exp(1j * v) / math.sqrt(n) for v in phases]
        rows = []
        for shift in (0, 1):
            for k in range(p):
                rows.append([cmath.exp(2j * PI * k * j / p) * g[(j - shift) % n]
                             for j in range(n)])
        # Frame operator built directly from all N synthesis columns.
        s = [[sum(v[i] * v[j].conjugate() for v in rows)
              for j in range(n)] for i in range(n)]
        for i in range(n):
            almost(s[i][i].real, 1)
            almost(s[i][i].imag, 0)
            for j in range(n):
                if i % p != j % p:
                    almost(s[i][j], 0)
        diffs = [phases[r] - phases[p + r] for r in range(p)]
        angle = [diffs[0] + diffs[p - 1]] + [diffs[r] - diffs[r - 1]
                                               for r in range(1, p)]
        for r in range(p):
            i, j = r, r + p
            a, d, b = s[i][i].real, s[j][j].real, s[i][j]
            root = math.sqrt((a - d)**2 + 4 * abs(b)**2)
            eig_low = (a + d - root) / 2
            eig_high = (a + d + root) / 2
            q = abs(math.cos(angle[r] / 2))
            almost(eig_low, 1-q)
            almost(eig_high, 1+q)

# One-block CDF is the angular fraction of 1-|cos(U/2)| <= x.
mesh = 32768
for x in (0.025, 0.1, 0.36, 0.8):
    actual = sum((1 - abs(math.cos(PI * (j + 0.5) / mesh))) <= x
                 for j in range(mesh)) / mesh
    predicted = 2 / PI * math.acos(1 - x)
    almost(actual, predicted, 8 / mesh)

# Hard-edge law of the minimum: exact finite p formula versus limit.
for p in (1000, 10000):
    for t in (0.25, 1.0, 4.0):
        x = t / p**2
        exact = (2 / PI * math.asin(1 - x)) ** p
        limit = math.exp(-2 * math.sqrt(2*t) / PI)
        almost(exact, limit, 0.002)

assert checks >= 2500
print(f'PHASE_GABOR_IID_SPECTRUM_CHECKS_PASSED {checks}')
