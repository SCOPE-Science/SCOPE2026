"""Finite diagnostics for the singular stationary-law limit.

Uses only the Python standard library. The analytical proof is in RESULT.md.
"""
import math


def coefficients(c, n):
    """Partial fractions for independent Laplace scales c**j, j=0..n-1."""
    out = []
    for j in range(n):
        scale2 = c ** (2 * j)
        prod = 1.0
        for k in range(n):
            if k != j:
                prod *= 1.0 - c ** (2 * k) / scale2
        out.append(1.0 / prod)
    return out


def density(x, c, n):
    return sum(a * math.exp(-abs(x) / c**j) / (2 * c**j)
               for j, a in enumerate(coefficients(c, n)))


def laplace(x):
    return 0.5 * math.exp(-abs(x))


def simpson(f, a, b, n=60000):
    assert n % 2 == 0
    h = (b - a) / n
    total = f(a) + f(b)
    for j in range(1, n):
        total += (4 if j & 1 else 2) * f(a + j * h)
    return total * h / 3


def run():
    tests = 0
    # Each truncated convolution is a probability density with the right variance.
    for c in (0.05, 0.1, 0.2, 0.35):
        for n in (2, 3, 4):
            co = coefficients(c, n)
            assert abs(sum(co) - 1) < 1e-8
            tests += 1
            integral = 2 * simpson(lambda x: density(x, c, n), 0, 24, 60000)
            assert abs(integral - 1) < 0.000008
            tests += 1
            # Exact characteristic function at a fixed frequency.
            omega = 0.7
            lhs = sum(a / (1 + (c**j * omega)**2) for j, a in enumerate(co))
            rhs = math.prod(1 / (1 + (c**j * omega)**2) for j in range(n))
            assert abs(lhs - rhs) < 2e-8
            tests += 1
    # Finite convolutions provide independent checks of asymptotic signs.
    for c in (0.04, 0.06, 0.10, 0.15):
        central = (density(0.0, c, 4) - laplace(0)) / c
        assert abs(central + 0.5) < 0.08
        tests += 1
        for y in (0.6, 1.0, 2.0):
            profile = (density(c * y, c, 4) - laplace(c * y)) / c
            assert abs(profile + 0.5 * math.exp(-y)) < 0.09
            tests += 1
        # Total-variation convergence uses a different, macroscopic power c**2.
        tv = simpson(lambda x: abs(density(x, c, 4) - laplace(x)), 0, 24, 90000)
        assert 0 < tv < c*c / (1-c*c) + 5e-8
        assert 0.4 < tv / c**2 < 1.01
        tests += 2
        eps = 0.5
        tail = 2 * simpson(lambda x: density(x, c, 4), eps, 24, 60000)
        assert tail > math.exp(-eps)
        tests += 1
        # The density ratio crosses one exactly once in the predicted window.
        ratio = lambda x: density(x, c, 4) / laplace(x)
        assert ratio(0) < 1 < ratio(3)
        tests += 1
        last = ratio(0)
        for j in range(1, 101):
            now = ratio(3 * j / 100)
            assert now >= last - 1e-9
            tests += 1
            last = now
        lo, hi = 0.0, 3.0
        for j in range(45):
            mid = (lo + hi) / 2
            if ratio(mid) > 1:
                hi = mid
            else:
                lo = mid
        xcross = (lo + hi) / 2
        leading = c * math.log(1 / c) / (1-c)
        assert abs(xcross / leading - 1) < 0.12
        tests += 1
    return tests

if __name__ == '__main__':
    print(f'PASS: {run()} finite diagnostic assertions')
