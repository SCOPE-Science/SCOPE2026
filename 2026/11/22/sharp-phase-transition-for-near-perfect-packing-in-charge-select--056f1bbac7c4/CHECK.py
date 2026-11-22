"""Reproduce finite checks for the near-integer beta parking exponent theorem.

Python 3 standard library only. These checks do not replace the proof.
"""
import math


def beta(a, b):
    return math.exp(math.lgamma(a) + math.lgamma(b) - math.lgamma(a + b))


def exact_exponent(n, q):
    if n < 2:
        return 0.0
    if q <= 0.5:
        return (n - 1) * q
    return (n - 1) // 2 + ((n - 1) % 2) * q


def recurrence(n, q):
    E = [0.0] * (n + 1)
    C = [1.0 if j < 2 else 0.0 for j in range(n + 1)]
    base = beta(q, q)
    for j in range(2, n + 1):
        exponents = [q + E[j - 1]]
        exponents += [1 + E[k] + E[j - 1 - k] for k in range(1, j - 1)]
        E[j] = min(exponents)
        if abs(E[j] - exponents[0]) < 1e-9:
            C[j] += 2 * (j - 1) ** (-q) * C[j - 1] * beta(q, E[j - 1] + 1) / base
        for k in range(1, j - 1):
            if abs(E[j] - 1 - E[k] - E[j - 1 - k]) < 1e-9:
                density = (k * (j - 1 - k)) ** (q - 1) / ((j - 1) ** (2 * q - 1) * base)
                C[j] += density * C[k] * C[j - 1 - k] * beta(E[k] + 1, E[j - 1 - k] + 1)
        if not (math.isfinite(C[j]) and C[j] > 0):
            raise AssertionError((q, j, C[j]))
    return E, C


def simpson(fun, count=256):
    assert count % 2 == 0
    total = fun(0.0) + fun(1.0)
    for i in range(1, count):
        total += (4 if i % 2 else 2) * fun(i / count)
    return total / (3 * count)


def p2(q, eps):
    x = eps / (1 + eps)
    return 2 * x ** q / (q * beta(q, q)) * simpson(lambda v: (1 - x * v ** (1 / q)) ** (q - 1), 128)


def p3_parts(q, eps):
    length = 2 + eps
    B = beta(q, q)
    def density(u):
        return (u * (length - u)) ** (q - 1) / (length ** (2 * q - 1) * B)
    center = eps * simpson(lambda v: density(1 + eps * v))
    # Substitution u=eps*v**(1/q) removes integrable endpoint singularity.
    edge = 2 * eps ** q / (q * length ** (2 * q - 1) * B) * simpson(
        lambda v: (length - eps * v ** (1 / q)) ** (q - 1)
        * p2(q, eps * (1 - v ** (1 / q))), 192)
    return center, edge


def run():
    tests = 0
    for q in (0.12, 0.25, 0.5, 0.75, 1.0):
        E, C = recurrence(35, q)
        for n in range(2, 36):
            assert abs(E[n] - exact_exponent(n, q)) < 1e-8
            tests += 1
        B = beta(q, q)
        assert abs(C[2] - 2 / (q * B)) < 1e-9
        central = 2 ** (1 - 2 * q) / B
        edge = 2 ** (1 - q) / (q * B)
        best = (central if q >= 0.5 else 0) + (edge if q <= 0.5 else 0)
        assert abs(C[3] - best) < 1e-9
        if q in (0.25, 0.5, 0.75):
            eps = 0.001
            measured_center, measured_edge = p3_parts(q, eps)
            assert abs(measured_center / (central * eps) - 1) < 0.003
            assert abs(measured_edge / (edge * eps ** (2 * q)) - 1) < 0.004
            tests += 2
    print('PASS:', tests, 'recurrence/coefficient/quadrature checks')


if __name__ == '__main__':
    run()
