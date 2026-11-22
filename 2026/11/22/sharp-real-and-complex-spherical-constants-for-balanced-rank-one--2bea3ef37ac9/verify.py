"""Finite diagnostics for balanced rank-one multiplier norm constants.

Run with `python verify.py`. Finite computations are not an infinite proof.
"""
import cmath
import math


def real_constant(d):
    return math.sqrt(math.pi) * math.gamma((d + 1) / 2) / math.gamma(d / 2)


def complex_constant(d):
    return math.gamma(d + 0.5) / (math.gamma(1.5) * math.gamma(d))


def exact_planar_unconditional_by_signs(n):
    roots = [cmath.exp(1j * math.pi * j / n) for j in range(n)]
    maximum = 0.0
    for mask in range(1 << n):
        value = sum(z if (mask >> j) & 1 else -z for j, z in enumerate(roots))
        maximum = max(maximum, abs(value))
    return maximum


def main():
    checks = 0
    for d in range(1, 17):
        cr, cc = real_constant(d), complex_constant(d)
        assert cr >= 1 - 1e-12 and cc >= 1 - 1e-12
        checks += 2
    for d, r, c in [(1, 1, 1), (2, math.pi / 2, 1.5), (3, 2, 15 / 8),
                    (4, 3 * math.pi / 4, 35 / 16)]:
        assert math.isclose(real_constant(d), r, rel_tol=1e-12)
        assert math.isclose(complex_constant(d), c, rel_tol=1e-12)
        checks += 2
    for n in range(2, 14):
        got = exact_planar_unconditional_by_signs(n)
        want = 1 / math.sin(math.pi / (2 * n))
        assert math.isclose(got, want, rel_tol=2e-12, abs_tol=2e-12), (n, got, want)
        checks += 1
        assert n / got < math.pi / 2
        checks += 1
    for n in (100, 1000):
        ratio = n * math.sin(math.pi / (2 * n))
        assert 0 < math.pi / 2 - ratio < math.pi**3 / (48 * n**2)
        checks += 1
    for n in (10000, 100000):
        ratio = n * math.sin(math.pi / (2 * n))
        assert abs(math.pi / 2 - ratio) < 1e-8
        checks += 1
    for d in (5, 10, 20, 50, 100):
        # Stirling's leading constants, checked with deliberately loose finite-d error.
        ar = real_constant(d) / math.sqrt(math.pi * d / 2)
        ac = complex_constant(d) / (2 * math.sqrt(d / math.pi))
        assert 0.8 < ar < 1.01 and 0.9 < ac < 1.15
        checks += 2
    print(f"VERIFICATION_OK {checks}")


if __name__ == "__main__":
    main()
