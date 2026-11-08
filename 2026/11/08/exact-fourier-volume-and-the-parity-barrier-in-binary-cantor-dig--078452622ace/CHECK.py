"""Direct finite-matrix checks for a Fourier-volume identity.
Run: python CHECK.py
No external packages required.
"""
import cmath
import itertools
import math


def fourier_matrix(base, gap, steps):
    n = len(steps)
    bits = list(itertools.product((0, 1), repeat=n))
    locations = [gap * sum(s[j] / base ** (j + 1) for j in range(n)) for s in bits]
    frequencies = [sum(steps[j] * s[j] * base ** j for j in range(n)) for s in bits]
    scale = 2 ** (-n / 2)
    return [[scale * cmath.exp(2j * math.pi * freq * x) for x in locations]
            for freq in frequencies]


def abs_determinant(matrix):
    z = [row[:] for row in matrix]
    n = len(z)
    val = 1.0
    for k in range(n):
        pivot = max(range(k, n), key=lambda j: abs(z[j][k]))
        if abs(z[pivot][k]) < 1e-12:
            return 0.0
        if pivot != k:
            z[k], z[pivot] = z[pivot], z[k]
        p = z[k][k]
        val *= abs(p)
        for j in range(k + 1, n):
            factor = z[j][k] / p
            for h in range(k + 1, n):
                z[j][h] -= factor * z[k][h]
            z[j][k] = 0j
    return val


def predicted(base, gap, steps):
    n = len(steps)
    product = math.prod(abs(math.sin(math.pi * gap * t / base)) for t in steps)
    return product ** (2 ** (n - 1))


def optimized(base, gap, n):
    q = base // math.gcd(base, gap)
    return (1.0 if q % 2 == 0 else math.cos(math.pi / (2 * q))) ** (n * (2 ** (n - 1)))


def main():
    count = 0
    for b, d in [(3, 2), (4, 2), (5, 4), (6, 2), (6, 3), (7, 6), (8, 2), (9, 3)]:
        for n in (1, 2, 3):
            options = [[1] * n, [(b - 1)] * n, [1 + j % (b - 1) for j in range(n)]]
            for steps in options:
                actual = abs_determinant(fourier_matrix(b, d, steps))
                expected = predicted(b, d, steps)
                assert abs(actual - expected) < 2e-8, (b, d, n, steps, actual, expected)
                count += 1
            if n <= 2:
                best = max(predicted(b, d, steps)
                           for steps in itertools.product(range(1, b), repeat=n))
                assert abs(best - optimized(b, d, n)) < 3e-10, (b, d, n, best)
                count += 1
    print(f'FINITE_CANTOR_FOURIER_VOLUME_CHECKS_PASSED {count}')

if __name__ == '__main__':
    main()
