"""Reproduce exact ridge metric identities for canonical star symmetric-edge polytopes.

Run with: python star_ridge_verify.py
Requires Python standard library only. The limiting statements are proved
analytically in RESULT.md; finite tests here are corroboration, not proof.
"""
from fractions import Fraction
from itertools import product
from math import atan2, comb, pi, sqrt


def exact_determinant(matrix):
    """Fraction-preserving Gaussian elimination; empty determinant is one."""
    a = [[Fraction(v) for v in row] for row in matrix]
    n = len(a)
    determinant = Fraction(1)
    for k in range(n):
        pivot = next((i for i in range(k, n) if a[i][k] != 0), None)
        if pivot is None:
            return Fraction(0)
        if pivot != k:
            a[pivot], a[k] = a[k], a[pivot]
            determinant *= -1
        w = a[k][k]
        determinant *= w
        for i in range(k + 1, n):
            c = a[i][k] / w
            for j in range(k + 1, n):
                a[i][j] -= c * a[k][j]
            a[i][k] = 0
    return determinant


def signed_root(d, i, sign):
    v = [0] * (d + 1)
    v[0], v[i + 1] = -sign, sign
    return v


def facet_normal(d, signs):
    S = sum(signs)
    return [Fraction(-S, d + 1)] + [Fraction(x * (d + 1) - S, d + 1) for x in signs]


def dot(x, y):
    return sum(a * b for a, b in zip(x, y))


def expected_ridge_data(d, t):
    B = d * (d - 1) - t * t
    # Squared ridge measure times ((d-2)!)**2.
    # Squared tangent of the exterior dihedral angle (d >= 3).
    return B, Fraction(4 * (d + 1) * B, (B - 1) ** 2) if d >= 3 else None


checked_ridges = 0
checked_spectra = 0
for d in range(2, 8):
    counts = {}
    for missing in range(d):
        for vals in product((-1, 1), repeat=d - 1):
            t = sum(vals)
            plus = list(vals)
            minus = list(vals)
            plus.insert(missing, 1)
            minus.insert(missing, -1)
            fp, fm = facet_normal(d, plus), facet_normal(d, minus)
            for signs, f in ((plus, fp), (minus, fm)):
                for j in range(d):
                    b = signed_root(d, j, 1)
                    assert dot(f, b) == signs[j]
                assert dot(f, f) == d - Fraction(sum(signs) ** 2, d + 1)
            cp = dot(fp, fm)
            aa, bb = dot(fp, fp), dot(fm, fm)
            expected_area_sq, expected_tan_sq = expected_ridge_data(d, t)
            if d >= 3:
                assert cp > 0
                assert (aa * bb - cp * cp) / (cp * cp) == expected_tan_sq
            else:
                assert cp == 0  # all four angles are right angles
            vertices = [signed_root(d, j, sign) for j, sign in enumerate(plus) if j != missing]
            base = vertices[0]
            differences = [[u - v for u, v in zip(w, base)] for w in vertices[1:]]
            gram = [[dot(a, b) for b in differences] for a in differences]
            assert exact_determinant(gram) == expected_area_sq
            counts[abs(t)] = counts.get(abs(t), 0) + 1
            checked_ridges += 1
    for j, count in counts.items():
        expect = d * (1 if j == 0 else 2) * comb(d - 1, (d - 1 + j) // 2)
        assert count == expect, (d, j, count, expect)
        checked_spectra += 1
    assert sum(counts.values()) == d * 2 ** (d - 1)

for d in (30, 100, 300):
    avg_weighted_angle = 0.0
    for k in range(d):
        t = d - 1 - 2 * k
        a = sqrt(d * (d - 1) - t * t)
        numerator = 2 * sqrt((d + 1) * (d * (d - 1) - t * t))
        denominator = d * (d - 1) - 1 - t * t
        phi = atan2(numerator, denominator)
        avg_weighted_angle += (comb(d - 1, k) / 2 ** (d - 1)) * a * phi
    assert abs(d * (avg_weighted_angle / (2 * sqrt(d)) - 1) + 5 / 6) < 0.03

print('STAR_RIDGE_PASS', 'exact_ridges=', checked_ridges,
      'exact_spectral_classes=', checked_spectra, 'curvature_checks=3')
