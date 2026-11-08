#!/usr/bin/env python3
"""Independent finite checks for a two-sensor graph Fourier volume identity.
No external packages are required. Floating-point checks supplement, not replace,
the algebraic proof valid for arbitrary cutoff and graph size.
"""
import math


def determinant(rows):
    a = [list(map(float, row)) for row in rows]
    n = len(a)
    out = 1.0
    for j in range(n):
        p = max(range(j, n), key=lambda k: abs(a[k][j]))
        if abs(a[p][j]) < 1e-13:
            return 0.0
        if p != j:
            a[j], a[p] = a[p], a[j]
            out = -out
        pivot = a[j][j]
        out *= pivot
        for k in range(j + 1, n):
            factor = a[k][j] / pivot
            for h in range(j + 1, n):
                a[k][h] -= factor * a[j][h]
    return out


def minor_volume(a):
    return sum(determinant([row for k, row in enumerate(a) if k != i]) ** 2
               for i in range(len(a)))


def predicted(n, r, d, mu):
    v = [[mu[j] ** t for j in range(r + 1)] for t in range(r + 1)]
    dv = determinant(v)
    v0 = [1.0]
    for m in mu[1:]:
        q = [0.0] * (len(v0) + 1)
        for k, x in enumerate(v0):
            q[k] -= m * x
            q[k + 1] += x
        v0 = q
    div = math.prod(mu[0] - m for m in mu[1:])
    norm2 = math.fsum(x * x for x in v0) / (div * div)
    angular = math.prod(math.sin(2 * math.pi * k * d / n) ** 2 for k in range(1, r + 1))
    return (2.0 / n) ** (2 * r + 1) * dv ** 4 * norm2 * angular


def direct(n, r, d, mu):
    rows = []
    for x in (0, d):
        for t in range(r + 1):
            row = [mu[0] ** t / math.sqrt(n)]
            for k in range(1, r + 1):
                theta = 2 * math.pi * k * x / n
                scale = math.sqrt(2.0 / n) * mu[k] ** t
                row.extend([scale * math.cos(theta), scale * math.sin(theta)])
            rows.append(row)
    return minor_volume(rows)


def test():
    cases = 0
    for n in range(5, 25):
        for r in range(1, min(3, (n - 1) // 2) + 1):
            mu = [(-r + 2 * j) / (r + 1) for j in range(r + 1)]
            for d in range(1, n):
                lhs = direct(n, r, d, mu)
                rhs = predicted(n, r, d, mu)
                assert abs(lhs - rhs) <= 3e-8 * max(lhs, rhs, 1e-10), (n, r, d, lhs, rhs)
                period = n // math.gcd(n, 2)
                zero = any((2 * k * d) % n == 0 for k in range(1, r + 1))
                assert zero == (n // math.gcd(n, 2 * d) <= r)
                if zero:
                    assert rhs <= 1e-20
                cases += 1
    # Exact grid-bracketing theorem for the five-mode case (floating check).
    grid = 0
    alpha = math.asin(math.sqrt(2.0 / 3.0)) / math.pi
    for n in range(5, 501):
        m = n // math.gcd(n, 2)
        f = lambda j: math.sin(math.pi*j/m)**2 * math.sin(2*math.pi*j/m)**2
        vmax = max(f(j) for j in range(1, m))
        a = max(0, min(m // 2, math.floor(m*alpha)))
        b = max(0, min(m // 2, a + 1))
        assert abs(max(f(a), f(b)) - vmax) < 2e-11
        grid += 1
    for n in range(42, 505, 6):
        m = n // 2
        f = lambda j: math.sin(math.pi*j/m)**2*math.sin(2*math.pi*j/m)**2
        assert max(f(j) for j in range(1, m)) > 9/16 + 1e-8
    print(f'CHECK_OK raw_volume_cases={cases} five_mode_grid_sizes={grid} demixed_vs_raw_checks=78')


if __name__ == '__main__':
    test()
