"""Numerical diagnostics for an exact Ricker habitat-allocation theorem.
The mathematical proof is analytic; this script only checks examples and formulas.
Uses only the Python 3 standard library.
"""
import math


def f(x):
    return x * math.exp(-x)


def d1(x):
    return (1.0 - x) * math.exp(-x)


def A(m, t):
    return sum(math.exp(-k * t) for k in range(m))


def threshold_expression(m, t):
    z = A(m, t)
    return m * (m - 1) * t * z / (m - z)


def p_of_t(m, t):
    return 1.0 / A(m, t)


def g(m, s, p):
    q = (1 - p) / (m - 1)
    return p * math.exp(-s * (p - 1 / m)) + (1 - p) * math.exp(s * (1 / m - q))


def golden_min(fn, lo, hi, steps=250):
    k = (math.sqrt(5) - 1) / 2
    a, b = lo, hi
    c, d = b - k * (b - a), a + k * (b - a)
    fc, fd = fn(c), fn(d)
    for _ in range(steps):
        if fc < fd:
            b, d, fd = d, c, fc
            c = b - k * (b - a)
            fc = fn(c)
        else:
            a, c, fc = c, d, fd
            d = a + k * (b - a)
            fd = fn(d)
    mid = (a + b) / 2
    return mid, fn(mid)


def root_z(s):
    assert s > 4
    x = s / 2
    a, b = 0.0, x
    for _ in range(120):
        z = (a + b) / 2
        h = z / math.tanh(z) if z else 1.0
        if h < x - 1:
            a = z
        else:
            b = z
    return (a + b) / 2


def objective(m, s, p):
    q = (1 - p) / (m - 1)
    return f(s * p) + (m - 1) * f(s * q)


def numerical_max(m, s):
    N = 1000
    p0 = 1 / m
    step = (1 - p0) / N
    vals = [(objective(m, s, p0 + i * step), p0 + i * step) for i in range(N + 1)]
    val, p = max(vals)
    pleft = max(p0, p - step)
    pright = min(1.0, p + step)
    pm, fmneg = golden_min(lambda z: -objective(m, s, z), pleft, pright)
    return max((val, p), (-fmneg, pm))


def main():
    checks = 0
    for t in [0.001, .01, .1, 1, 2, 5]:
        assert threshold_expression(2, t) > 4
        checks += 1
    for s in [4.0001, 4.1, 5, 8, 20, 60]:
        z = root_z(s)
        low, high = s / 2 - z, s / 2 + z
        assert 1 - 1e-12 <= low < 2 < high
        assert abs(d1(low) - d1(high)) < 1e-12
        assert f(low) + f(high) > s * math.exp(-s / 2)
        checks += 3
    table = []
    for m in range(3, 13):
        tstar, scrit = golden_min(lambda t: threshold_expression(m, t), .0001, 7)
        p = p_of_t(m, tstar)
        low = scrit * (1 - p) / (m - 1)
        high = scrit * p
        assert 2 < scrit < 2 * m
        assert 1 < low < 2 < high
        assert abs(g(m, scrit, p) - 1) < 2e-12
        assert abs(d1(low) - d1(high)) < 1e-7
        assert g(m, scrit - 0.01, p) < 1 < g(m, scrit + 0.01, p)
        checks += 5
        table.append((m, tstar, scrit, low, high))
        for ds in [-.2, -.05, 0.05, .2, 2]:
            s = scrit + ds
            fmax, pmax = numerical_max(m, s)
            equal = s * math.exp(-s / m)
            if ds < 0:
                assert abs(fmax - equal) < 1e-10
            else:
                assert fmax > equal
            assert pmax >= 1 / m
            checks += 2
    for m in [2, 3, 4, 8, 12]:
        for s in [100.0, 150.0, 250.0]:
            value, _ = numerical_max(m, s)
            limit = (m - 1) / math.e
            assert abs(value - limit) < 1e-9
            checks += 1
    for m in [3, 4, 5]:
        tstar, scrit = golden_min(lambda t: threshold_expression(m, t), .0001, 7)
        for j in range(1, 1000):
            p = 1 / m + (1 - 1 / m) * j / 1000
            assert g(m, scrit - .01, p) <= 1.00000001
            checks += 1
    print("Numerical diagnostics passed:", checks)
    print("m, t*, s_crit, smaller site, larger site [all numerical]")
    for row in table[:5]:
        print("%d %.10f %.10f %.10f %.10f" % row)
    print("Finite tests are not proof of global or continuous assertions.")


if __name__ == "__main__":
    main()
