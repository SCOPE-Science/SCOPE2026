"""Reproducible finite sanity checks for a support-function reflection theorem.

The continuous uniqueness theorem rests on the proof in RESULT.md, not on
these sampled evaluations. Only Python's standard library is required.
"""
import math

PI = math.pi


def dot(a, b):
    return a[0] * b[0] + a[1] * b[1]


def normal(theta):
    return (math.cos(theta), math.sin(theta))


def tangent(theta):
    return (-math.sin(theta), math.cos(theta))


def h_orig(theta, r, e):
    return r + e * math.cos(3 * theta)


def support_diff_half(theta, z, e):
    return e * math.cos(3 * theta) - dot(z, normal(theta))


def support_diff_half_deriv(theta, z, e):
    return -3 * e * math.sin(3 * theta) - dot(z, tangent(theta))


def max_support_center(theta, z, r, e):
    h = h_orig(theta, r, e)
    reflected = 2 * dot(z, normal(theta)) + h_orig(theta + PI, r, e)
    return max(h, reflected) - dot(z, normal(theta))


def g(theta):
    return abs(math.cos(theta)) ** 3


def gd(theta):
    c, s = math.cos(theta), math.sin(theta)
    return -3 * c * abs(c) * s


def integrate_periodic(fun, count=60000):
    step = 2 * PI / count
    return step * sum(fun(step * i) for i in range(count))


def find_transversal_root(z, e):
    n = 1200
    previous = support_diff_half(0.0, z, e)
    for i in range(1, n + 1):
        theta = i * 2 * PI / n
        current = support_diff_half(theta, z, e)
        if previous * current < 0:
            lo, hi = (i - 1) * 2 * PI / n, theta
            value = previous
            for _ in range(75):
                mid = (lo + hi) / 2
                vm = support_diff_half(mid, z, e)
                if value * vm > 0:
                    lo, value = mid, vm
                else:
                    hi = mid
            return (lo + hi) / 2
        previous = current
    raise AssertionError('No transversal root found')


def check():
    for r, e in [(1.0, 0.05), (1.3, 0.11), (2.5, 0.005)]:
        assert r > 8 * e
        centers = [(-3 * e * math.cos(2 * PI * k / 3),
                    -3 * e * math.sin(2 * PI * k / 3)) for k in range(3)]
        assert all(abs(math.hypot(*z) - 3 * e) < 2e-14 for z in centers)
        for k, z in enumerate(centers):
            alpha = 2 * PI * k / 3
            for j in range(1440):
                t = (j + 0.125) * 2 * PI / 1440
                f = support_diff_half(t, z, e)
                expected = 4 * e * math.cos(t - alpha) ** 3
                assert abs(f - expected) < 1e-12
                hs = max_support_center(t, z, r, e)
                assert abs(hs - r - 4 * e * abs(math.cos(t - alpha)) ** 3) < 1e-12
                rho = r - 8 * e * math.copysign(1.0, math.cos(t - alpha)) * math.cos(3 * (t - alpha))
                assert rho > r - 8 * e - 1e-12
            for t in (alpha + PI / 2, alpha + 3 * PI / 2):
                assert abs(support_diff_half(t, z, e)) < 2e-13
                assert abs(support_diff_half_deriv(t, z, e)) < 2e-13
        per = integrate_periodic(lambda t: r + 4 * e * g(t))
        area = 0.5 * integrate_periodic(lambda t: (r + 4 * e * g(t))**2 - (4 * e * gd(t))**2)
        predicted_per = 2 * PI * r + 32 * e / 3
        predicted_area = PI * r * r + 32 * r * e / 3 - 4 * PI * e * e
        assert abs(per - predicted_per) < 1e-9, (per, predicted_per)
        assert abs(area - predicted_area) < 1e-9, (area, predicted_area)
        orig_area = 0.5 * integrate_periodic(lambda t: h_orig(t,r,e)**2 - (3*e*math.sin(3*t))**2)
        assert abs(orig_area - (PI * r*r - 4*PI*e*e)) < 1e-9
        for z in [(0, 0), (e, 0), (0, 2 * e), (0.4 * e, -0.7 * e)]:
            t = find_transversal_root(z, e)
            assert abs(support_diff_half(t,z,e)) < 1e-12
            assert abs(support_diff_half_deriv(t,z,e)) > 1e-3 * e
    print('ANALYTIC_THREE_REFLECTION_CENTERS_CHECKS_OK')


if __name__ == '__main__':
    check()
