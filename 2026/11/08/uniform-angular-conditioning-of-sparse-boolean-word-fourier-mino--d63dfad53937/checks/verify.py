"""Finite checks for low-weight binary-word Fourier minors.

Dependencies: Python 3.10+ and numpy. These finite tests supplement a general proof.
"""
import cmath
import itertools
import math
import numpy as np


def support_ball(n, radius):
    return [frozenset(combo) for level in range(radius + 1)
            for combo in itertools.combinations(range(n), level)]


def matrices(n, radius, modulus):
    sets = support_ball(n, radius)
    phase = cmath.exp(2j * math.pi / modulus)
    d = phase - 1
    forward = np.array([[phase ** len(a & b) for b in sets]
                        for a in sets], dtype=complex)
    inverse = np.empty_like(forward)
    for i, a in enumerate(sets):
        for j, b in enumerate(sets):
            union = len(a | b)
            inverse[i, j] = (0 if union > radius else
                (-1) ** (len(a) + len(b)) * sum(
                    math.comb(n - union, level - union) / d ** level
                    for level in range(union, radius + 1)))
    return forward, inverse


def main():
    count = 0
    worst_residual = 0.0
    worst_det_rel = 0.0
    for radius in (0, 1, 2):
        for n in range(max(2, radius), 8):
            for modulus in (2, 3, 4, 5, 11):
                f, finv = matrices(n, radius, modulus)
                ident = np.eye(len(f))
                err = max(np.max(np.abs(f @ finv - ident)),
                          np.max(np.abs(finv @ f - ident)))
                worst_residual = max(worst_residual, float(err))
                assert err < 2e-9, (n, radius, modulus, err)
                exponent = n * sum(math.comb(n - 1, j)
                                   for j in range(radius))
                d = cmath.exp(2j * math.pi / modulus) - 1
                predicted_det = d ** exponent
                actual_det = np.linalg.det(f)
                rel = abs(actual_det / predicted_det - 1)
                worst_det_rel = max(worst_det_rel, float(rel))
                assert rel < 3e-7, (n, radius, modulus, rel)
                count += 1
    ratios = []
    for radius, n in ((1, 32), (2, 12), (2, 16)):
        for modulus in (3, 5, 17, 257):
            f, finv = matrices(n, radius, modulus)
            delta = 2 * math.sin(math.pi / modulus)
            predicted = n ** (2 * radius) / (
                math.factorial(radius)**2 * delta**radius)
            cond = np.linalg.norm(f, 2) * np.linalg.norm(finv, 2)
            ratios.append((radius, n, modulus, round(float(cond/predicted), 6)))
    print(f'FINITE_PHASE_BALL_CHECKS_PASS cases={count} '
          f'worst_inverse_residual={worst_residual:.3g} '
          f'worst_relative_det_error={worst_det_rel:.3g}')
    print('Selected finite ratio diagnostics', ratios)
    print('The ratios are not used to infer the asymptotic theorem.')

if __name__ == '__main__':
    main()
