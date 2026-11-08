"""Finite numerical cross-checks for the exact cubic Gabor ambiguity theorem.

Run: python CHECK.py
No optional dependencies. Finite checks corroborate but cannot prove the theorem.
"""
import cmath
import math


def test(p, a, epsilon):
    n = p ** a
    zeta = [cmath.exp(2j * math.pi * t / n) for t in range(n)]
    chirp = [zeta[(j ** 3) % n] for j in range(n)]
    perturb = [v + (epsilon if j == 0 else 0.0) for j, v in enumerate(chirp)]
    norm_sq = n + 2 * epsilon + epsilon ** 2
    target_min = 2 * epsilon * math.sin(math.pi / (2 * p ** (a - 1)))
    minimum = float('inf')
    zero_count = 0
    rank_expected = (p * n * n + 1) // (p + 1)
    tol = 5e-8 * n
    for k in range(n):
        # Directly form the sequences in the defining time-domain sum.
        row = [perturb[(j - k) % n] * perturb[j].conjugate()
               for j in range(n)]
        row0 = [chirp[(j - k) % n] * chirp[j].conjugate()
                for j in range(n)]
        for ell in range(n):
            coeff = sum(row[j] * zeta[(ell * j) % n] for j in range(n))
            orig = sum(row0[j] * zeta[(ell * j) % n] for j in range(n))
            value = abs(coeff)
            minimum = min(minimum, value)
            if k == 0:
                expected_zero = ell != 0
            else:
                t, kk = 0, k
                while kk % p == 0:
                    kk //= p
                    t += 1
                expected_zero = ell % (p ** t) != 0
            if expected_zero:
                assert abs(orig) < tol, (p, a, k, ell, orig)
                zero_count += 1
            else:
                expected_abs = n if k == 0 else p ** ((a + t) / 2)
                assert abs(abs(orig) - expected_abs) < tol, (p, a, k, ell, orig)
    assert n * n - zero_count == rank_expected, (p, a, zero_count)
    assert abs(minimum - target_min) < tol, (p, a, minimum, target_min)
    ell = (p ** (a - 1) + 1) // 2
    coeff_at_witness = sum(perturb[(j - p) % n] * perturb[j].conjugate()
                           * zeta[(ell * j) % n] for j in range(n))
    assert abs(abs(coeff_at_witness) - target_min) < tol
    cond = norm_sq / target_min
    assert cond > 1 and abs(minimum / norm_sq - 1 / cond) < tol
    print('PASS', p, a, epsilon, 'rank', rank_expected,
          'unnormalized-min', round(minimum, 12))


if __name__ == '__main__':
    for pp, aa in [(5, 2), (7, 2), (5, 3)]:
        for ee in (1.0, 0.4):
            test(pp, aa, ee)
    print('CUBIC_PRIME_POWER_ONE_IMPULSE_CHECKS_PASSED')
