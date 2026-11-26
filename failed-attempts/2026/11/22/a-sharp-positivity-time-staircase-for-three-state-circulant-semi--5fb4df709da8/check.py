#!/usr/bin/env python3
"""Independent finite-precision checks for a three-state circulant matrix-exponential theorem.

Run: python3 check.py
Only standard-library dependencies are used. This is a test, not an infinite proof.
"""
import math

ROOT3 = math.sqrt(3.0)
PI = math.pi
I = [[float(i == j) for j in range(3)] for i in range(3)]
P = [[1.0 / 3.0] * 3 for _ in range(3)]
J = [[0.0, -1.0 / ROOT3, 1.0 / ROOT3],
     [1.0 / ROOT3, 0.0, -1.0 / ROOT3],
     [-1.0 / ROOT3, 1.0 / ROOT3, 0.0]]


def product(a, b):
    return [[sum(a[i][h] * b[h][j] for h in range(3))
             for j in range(3)] for i in range(3)]


def add(a, b):
    return [[a[i][j] + b[i][j] for j in range(3)] for i in range(3)]


def scale(a, t):
    return [[t * a[i][j] for j in range(3)] for i in range(3)]


def exp_matrix(b):
    """Scaling and squaring with a Taylor approximation, independent of Fourier formula."""
    norm = max(sum(abs(v) for v in row) for row in b)
    k = max(0, math.ceil(math.log2(norm / 0.25))) if norm else 0
    c = scale(b, 2.0 ** -k)
    ans = [row[:] for row in I]
    term = [row[:] for row in I]
    for n in range(1, 38):
        term = scale(product(term, c), 1.0 / n)
        ans = add(ans, term)
    for _ in range(k):
        ans = product(ans, ans)
    return ans


def generator(a):
    return add(scale(add(I, scale(P, -1)), -a), J)


def explicit_exponential(a, theta):
    d = math.exp(-a * theta)
    return add(P, scale(add(scale(add(I, scale(P, -1)), math.cos(theta)),
                            scale(J, math.sin(theta))), d))


def envelope(theta):
    return max(-2 * math.cos(theta), math.cos(theta) + ROOT3 * abs(math.sin(theta)))


def h(a):
    return math.log(2.0 / math.hypot(1.0, a)) + a * math.atan(a)


def r(a):
    return 3.0 * h(a) / (PI * a)


def gap_count(a):
    if a >= ROOT3:
        return 0
    return max(0, math.ceil((r(a) - 1.0) / 2.0))


def mid_gap(a, k):
    return (2 * k + 1) * PI / 3.0 - math.atan(a)


def bisect(f, x, y, iterations=80):
    fx = f(x)
    fy = f(y)
    assert fx * fy <= 0, (x, y, fx, fy)
    for _ in range(iterations):
        m = (x + y) / 2
        fm = f(m)
        if fx * fm <= 0:
            y, fy = m, fm
        else:
            x, fx = m, fm
    return (x + y) / 2


def critical(k):
    return bisect(lambda a: r(a) - (2 * k + 1), 1.e-6, ROOT3)


def test():
    checks = 0
    for x, y in [(J, J), (J, P), (P, J), (P, P)]:
        q = product(x, y)
        target = (scale(add(I, scale(P, -1)), -1) if x is J and y is J
                  else P if x is P and y is P else [[0.0]*3 for _ in range(3)])
        assert max(abs(q[i][j] - target[i][j]) for i in range(3) for j in range(3)) < 1.e-14
        checks += 9
    for a in (0.04, 0.05, 0.1, 0.25, 0.5, 1., 1.7, ROOT3, 2.1):
        b = generator(a)
        assert all(abs(sum(row)) < 1.e-14 for row in b)
        checks += 3
        for theta in (0., .01, .2, 1.05, 1.8, 2.4, 3.14, 4.5, 8., 13., 26., 70.):
            e = exp_matrix(scale(b, theta))
            actual = explicit_exponential(a, theta)
            assert max(abs(e[i][j] - actual[i][j]) for i in range(3) for j in range(3)) < 4.e-11, (a, theta, e, actual)
            checks += 9
            f = envelope(theta)
            is_good = all(e[i][j] >= -1e-10 for i in range(3) for j in range(3))
            formula_good = math.exp(a*theta) >= f - 1.e-10
            assert is_good == formula_good, (a, theta, e, f)
            checks += 1
        n = gap_count(a)
        if a < ROOT3:
            assert n >= 1
            for k in range(n):
                th = mid_gap(a, k)
                assert envelope(th) > math.exp(a*th), (a,k,th)
                checks += 1
            for k in range(n, n+5):
                th = mid_gap(a, k)
                assert envelope(th) <= math.exp(a*th), (a,k,th)
                checks += 1
        else:
            assert n == 0
            checks += 1
    assert gap_count(.1) == 3
    assert gap_count(.05) == 7
    assert gap_count(.25) == 1
    assert gap_count(ROOT3) == 0
    checks += 4
    for k in range(1, 7):
        alpha = critical(k)
        assert 0 < alpha < ROOT3 and abs(r(alpha) - (2*k+1)) < 2e-9
        assert gap_count(alpha * .999) == k + 1, (k,alpha)
        assert gap_count(alpha * 1.001) == k, (k,alpha)
        checks += 3
    for a in (.05, .1, .25, .5, 1.5):
        n = gap_count(a)
        for k in range(n):
            left, right = 2*k*PI/3, 2*(k+1)*PI/3
            center = mid_gap(a,k)
            fn = lambda th: math.log(2*math.cos(th-(2*k+1)*PI/3))-a*th
            lower = left if k == 0 else bisect(fn, left, center)
            upper = bisect(fn, center, right)
            assert lower < center < upper
            assert fn((lower+upper)/2)>0
            if k>0: assert abs(fn(lower))<1.e-12
            assert abs(fn(upper))<1.e-12
            checks += 4
    print('PASS', checks, 'finite numerical assertions; the theorem requires the written proof.')
    print('Critical damping/frequency ratios for extra gaps:')
    for k in range(1,5):
        print(k, '%.13f' % critical(k))

if __name__ == '__main__':
    test()
