"""Reproduce the exact small-field determinants and sampled Fourier eigenvalues.

Only Python standard library is needed. This finite test supplements the proof.
"""
from itertools import product
from math import gcd, isclose, log, pi, sin
from cmath import exp


def determinant_integer(rows):
    a = [list(row) for row in rows]
    n = len(a)
    sign, previous = 1, 1
    for k in range(n - 1):
        if not a[k][k]:
            replacement = next((i for i in range(k + 1, n) if a[i][k]), None)
            if replacement is None:
                return 0
            a[k], a[replacement] = a[replacement], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                numerator = a[i][j] * pivot - a[i][k] * a[k][j]
                assert numerator % previous == 0
                a[i][j] = numerator // previous
            a[i][k] = 0
        previous = pivot
    return sign * a[-1][-1]


def prime_field_spectrum(p, coefficients=(1, 1, 1)):
    d = len(coefficients)
    v = list(product(range(p), repeat=d))
    nonsquare = next(t for t in range(2, p) if pow(t, (p - 1) // 2, p) == p - 1)
    def quadratic(x):
        return sum(c * a * a for c, a in zip(coefficients, x)) % p
    weights = [int(quadratic(x) == 1) - int(quadratic(x) == nonsquare) for x in v]
    roots = [exp(-2j * pi * t / p) for t in range(p)]
    eigenvalues = []
    for xi in v:
        total = sum(w * roots[sum(a * b for a, b in zip(xi, x)) % p]
                    for x, w in zip(v, weights) if w)
        eigenvalues.append(total)
    expected_logdet = ((d - 1) // 2) * p ** d * log(p) + p ** (d - 1) * log(2)
    actual_logdet = sum(log(abs(z)) for z in eigenvalues)
    assert isclose(actual_logdet, expected_logdet, abs_tol=1e-7)
    assert isclose(min(map(abs, eigenvalues)),
                   2 * p ** ((d - 1) // 2) * sin(pi / (2 * p)), abs_tol=1e-8)
    assert isclose(max(map(abs, eigenvalues)),
                   2 * p ** ((d - 1) // 2), abs_tol=1e-8)
    return v, weights


for p in (3, 5, 7):
    v, weights = prime_field_spectrum(p)
    if p in (3, 5):
        d = 3
        matrix = []
        nonsquare = next(t for t in range(2, p) if pow(t, (p - 1) // 2, p) == p - 1)
        for x in v:
            matrix.append([int(sum((a - b)**2 for a, b in zip(x, y)) % p == 1)
                           - int(sum((a - b)**2 for a, b in zip(x, y)) % p == nonsquare)
                           for y in v])
        det = determinant_integer(matrix)
        assert abs(det) == 2 ** (p ** 2) * p ** (p ** 3)
        print('Exact determinant verified for p=', p, 'd=3, size=', len(v))
    print('Full Fourier-spectrum magnitude and log determinant verified for p=', p)

# Anisotropic-coordinate example of the arbitrary quadratic-form hypothesis.
prime_field_spectrum(3, (1, 1, 2))
print('Nontrivial quadratic discriminant case verified for p=3')

# A field extension: F_9 = F_3[alpha] / (alpha^2 - 2).
p = 3
q = 9
field = tuple(range(q))
add = [[0] * q for _ in field]
mul = [[0] * q for _ in field]
for x in field:
    a, b = divmod(x, 3)
    for y in field:
        c, e = divmod(y, 3)
        add[x][y] = 3 * ((a + c) % 3) + (b + e) % 3
        mul[x][y] = 3 * ((a * c + 2 * b * e) % 3) + (a * e + b * c) % 3
squares = {mul[x][x] for x in field if x}
r1, r2 = 3, next(x for x in field if x and x not in squares)
vecs = list(product(field, repeat=3))
roots = [exp(-2j * pi * r / 3) for r in range(3)]
trace = [2 * (x // 3) % 3 for x in field]
for diag in ((3, 3, 3), (3, 3, 6)):
    weights = []
    for x in vecs:
        val = 0
        for c, t in zip(diag, x):
            val = add[val][mul[c][mul[t][t]]]
        weights.append(int(val == r1) - int(val == r2))
    magnitudes = []
    for xi in vecs:
        frequency = 0j
        for x, w in zip(vecs, weights):
            if not w:
                continue
            dot = 0
            for a, b in zip(xi, x):
                dot = add[dot][mul[a][b]]
            frequency += w * roots[trace[dot]]
        magnitudes.append(abs(frequency))
    target_logdet = (q ** 3) * log(q) + (q ** 3 // p) * log(2)
    assert isclose(sum(map(log, magnitudes)), target_logdet, abs_tol=1e-7)
    assert isclose(min(magnitudes), q, abs_tol=1e-8)
    assert isclose(max(magnitudes), 2 * q, abs_tol=1e-8)
    print('F9 direct spectrum and determinant verified for diagonal form', diag)

print('ALL_CHECKS_PASSED')
