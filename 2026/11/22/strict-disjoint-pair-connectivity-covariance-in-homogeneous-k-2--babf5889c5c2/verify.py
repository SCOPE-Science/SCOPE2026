"""Exact finite-state checks for pair-connectivity covariance on a two-hub graph.

This program supplements, but does not replace, the all-order algebraic proof.
Only the Python standard library is needed.
"""
from fractions import Fraction


def brute(n, q, v):
    edges = [(0, j) for j in range(2, n + 2)] + [(1, j) for j in range(2, n + 2)]
    z = hx = hy = hxy = Fraction(0)
    for mask in range(1 << (2 * n)):
        parent = list(range(n + 2))

        def root(x):
            while parent[x] != x:
                x = parent[x]
            return x

        for i, (a, b) in enumerate(edges):
            if (mask >> i) & 1:
                parent[root(a)] = root(b)
        labels = [root(i) for i in range(n + 2)]
        weight = q ** len(set(labels)) * v ** mask.bit_count()
        xevent = labels[2] == labels[3]
        yevent = labels[4] == labels[5]
        z += weight
        hx += weight * xevent
        hy += weight * yevent
        hxy += weight * (xevent and yevent)
    return z, hx, hy, hxy


def closed(n, q, v):
    a, b = q + 2 * v, q + 2 * v + v * v
    s = v * v * (2 + v) ** 2
    z = q * (b ** n + (q - 1) * a ** n)
    hx = q * (s * b ** (n - 2) + 2 * (q - 2) * v * v * a ** (n - 2))
    hxy = q * (s * s * b ** (n - 4) + 4 * (q - 4) * v ** 4 * a ** (n - 4))
    return z, hx, hx, hxy


def factored_covariance(n, q, v):
    a, b = q + 2 * v, q + 2 * v + v * v
    r = a / b
    u = q * v / b
    y = (2 + u) ** 2 / 2
    f = q * (1 - r ** n) + (y - 2) * (2 + (q - 1) * y)
    return (4 * v ** 4 * r ** (n - 4) * f /
            (b ** 4 * (1 + (q - 1) * r ** n) ** 2))


def run():
    checks = 0
    for n in range(4, 8):
        for q in (Fraction(1, 10), Fraction(1, 2), Fraction(1), Fraction(2), Fraction(5)):
            for v in (Fraction(1, 10), Fraction(1), Fraction(7, 3)):
                exact = brute(n, q, v)
                formulas = closed(n, q, v)
                assert exact == formulas, (n, q, v, "moment disagreement")
                z, hx, hy, hxy = exact
                cov = (z * hxy - hx * hy) / z ** 2
                assert cov == factored_covariance(n, q, v), (n, q, v, "factor disagreement")
                assert cov > 0, (n, q, v, "nonpositive covariance")
                checks += 1
    print("TWO_HUB_CONNECTIVITY_EXACT_CHECKS_PASSED", checks)


if __name__ == "__main__":
    run()
