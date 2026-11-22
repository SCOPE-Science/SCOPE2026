"""Exact facet-volume checks and numerical diagnostics for lecture-hall simplex area minimization.

Requires Python 3 standard library. Finite tests corroborate, but do not replace, the proof.
"""
from fractions import Fraction as Q
from itertools import product
from math import factorial, sqrt, exp, log, isfinite


def det(a):
    n = len(a)
    if n == 0:
        return Q(1)
    b = [list(row) for row in a]
    out = Q(1)
    for k in range(n):
        r = next((r for r in range(k, n) if b[r][k]), None)
        if r is None:
            return Q(0)
        if r != k:
            b[r], b[k] = b[k], b[r]
            out = -out
        piv = b[k][k]
        out *= piv
        for i in range(k + 1, n):
            v = b[i][k] / piv
            for j in range(k + 1, n):
                b[i][j] -= v * b[k][j]
            b[i][k] = 0
    return out


def square_facet_areas(s):
    n = len(s)
    verts = [[Q(0)] * n]
    for j in range(n):
        verts.append([Q(0)] * j + list(s[j:]))
    result = []
    for excluded in range(n + 1):
        face = [v for i, v in enumerate(verts) if i != excluded]
        edges = [[v[k] - face[0][k] for k in range(n)] for v in face[1:]]
        gram = [[sum(a[k] * b[k] for k in range(n)) for b in edges] for a in edges]
        result.append(det(gram) / (factorial(n - 1) ** 2))
    return result


def formula_facet_squares(s):
    n = len(s)
    a = [1 / si for si in s]
    qs = [a[0] ** 2] + [a[i - 1] ** 2 + a[i] ** 2 for i in range(1, n)] + [a[-1] ** 2]
    volfac = Q(1)
    for si in s:
        volfac *= si
    volfac /= factorial(n - 1)
    return [volfac ** 2 * q for q in [qs[-1]] + qs[:-1]]


def objective_and_gradient(t):
    y = [exp(x) for x in t]
    n = len(y)
    q = [y[0]] + [sqrt(y[i] ** 2 + y[i + 1] ** 2) for i in range(n - 1)] + [y[-1]]
    f = sum(q)
    g = [y[i] ** 2 * (1 / q[i] + 1 / q[i + 1]) for i in range(n)]
    return f, [gi - f / n for gi in g]


def solve(n):
    t = [0.] * n
    rate = 0.3
    for _ in range(16000):
        val, g = objective_and_gradient(t)
        err = max(abs(z) for z in g)
        if err < 2e-10:
            break
        alpha = rate
        while alpha > 1e-13:
            tn = [u - alpha * gi for u, gi in zip(t, g)]
            fn, _ = objective_and_gradient(tn)
            if fn < val - 1e-4 * alpha * sum(gi * gi for gi in g):
                t = tn
                break
            alpha *= 0.5
        else:
            break
    return t, objective_and_gradient(t)


def main():
    count = 0
    choices = [Q(1, 2), Q(1), Q(3, 2), Q(2), Q(3)]
    for n in range(2, 6):
        for index, raw in enumerate(product(choices, repeat=n)):
            if n == 5 and index >= 125:
                break
            assert square_facet_areas(raw) == formula_facet_squares(raw), (n, raw)
            count += 1
    for n in range(2, 13):
        t, (value, g) = solve(n)
        assert max(abs(v) for v in g) < 1e-7, (n, g)
        assert abs(sum(t)) < 1e-8
        assert max(abs(t[i] - t[n - 1 - i]) for i in range(n)) < 1e-8
        equal = 2 + (n - 1) * sqrt(2)
        assert value <= equal + 1e-9
        if n > 2:
            assert t[0] < t[1] - 1e-4
            assert value < equal - 1e-5
        else:
            assert abs(t[0]) < 1e-8
        if n == 3:
            ratio = exp(t[1] - t[0]); target = sqrt(5) / 2
            assert abs(ratio - target) < 1e-8
            assert abs(value - 5 * (2 / sqrt(5)) ** (1 / 3)) < 1e-8
        print('n=%d  optimum=%.12f  equal=%.12f  maxKKT=%.2g' % (n, value, equal, max(abs(z) for z in g)))
    print('LECTURE_HALL_FIXED_VOLUME_SURFACE_OPTIMIZER_PASS: %d rational facet profiles and 11 numerical KKT cases' % count)

if __name__ == '__main__':
    main()
