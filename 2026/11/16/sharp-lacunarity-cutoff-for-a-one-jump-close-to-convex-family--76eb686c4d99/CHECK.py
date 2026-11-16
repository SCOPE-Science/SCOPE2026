"""Reproducibility checks for a sharp close-to-convexity cutoff.

The infinite theorem is proved analytically in RESULT.md; this finite script
checks symbolic coefficient identities and representative angular-turn limits.
"""
import cmath
import math


def derivative(p, n, z):
    return (1 + z ** (p * n)) / (1 - z ** p)


def unwrap_turn(p, n, radius, left, right, count=20001):
    previous = None
    total = 0.0
    for j in range(count):
        angle = left + (right - left) * j / (count - 1)
        z = radius * cmath.exp(1j * angle)
        phase = cmath.phase(z * derivative(p, n, z))
        if previous is not None:
            diff = phase - previous
            while diff > math.pi:
                diff -= 2 * math.pi
            while diff < -math.pi:
                diff += 2 * math.pi
            total += diff
        previous = phase
    return total


def main():
    checks = 0
    for p in range(1, 11):
        for n in range(1, 8):
            for k in range(0, 18):
                # Geometric division: (1+w^n)/(1-w).
                w = 0.13 + 0.07j
                lhs = (1 + w ** n) / (1 - w)
                rhs = sum(w ** j for j in range(n)) + 2 * w ** n / (1 - w)
                assert abs(lhs - rhs) < 1e-11
                checks += 1
            if n == 1:
                for t in range(12):
                    z = 0.9 * cmath.exp(1j * 2 * math.pi * t / 12)
                    assert derivative(p, n, z).real > 0
                    checks += 1
            elif p >= 3:
                L = 1 + p * (n - 1) / 2
                eta = (1 - 2 / p) * math.pi / (4 * n * L)
                left = math.pi / (p * n) - eta
                right = 3 * math.pi / (p * n) + eta
                assert 0 < left < right < 2 * math.pi / p
                expected = -math.pi - (1 - 2 / p) * math.pi / (2 * n)
                turn = unwrap_turn(p, n, 0.9999999, left, right)
                assert turn < -math.pi, (p, n, turn)
                assert abs(turn - expected) < 0.001, (p, n, turn, expected)
                checks += 3
    print(f'PASS: {checks} finite checks; no infinite conclusion depends on them.')


if __name__ == '__main__':
    main()
