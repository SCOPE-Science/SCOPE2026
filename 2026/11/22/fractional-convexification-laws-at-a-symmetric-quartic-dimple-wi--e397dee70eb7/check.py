"""Supplemental numerical checks for a Pascal limaçon and its convex hull.

Run with Python 3.9+. Standard-library-only checks are not proofs.
"""
import math


def simpson(f, a, b, n=8000):
    assert n % 2 == 0 and a < b
    h = (b - a) / n
    value = f(a) + f(b)
    for k in range(1, n):
        value += (4 if k % 2 else 2) * f(a + h * k)
    return h * value / 3


def contact(q):
    assert .5 < q < 1
    t = math.acos(1 / (2 * q))
    return t, math.sin(t)


def area_defect(q):
    t, s = contact(q)
    return (7 * q / 4 + 1 / (8 * q)) * s - (1 + q * q / 2) * t


def area_defect_by_cap(q):
    t, _ = contact(q)
    def f(z):
        c = math.cos(z)
        x = -c + q * c * c
        yp = c - q * math.cos(2 * z)
        return (x + 1 / (4 * q)) * yp
    return 2 * simpson(f, 0, t)


def perimeter_defect(q):
    t, s = contact(q)
    return 2 * simpson(lambda z: math.sqrt(1 + q * q - 2 * q * math.cos(z)), 0, t) - s


def monotone_hull(points):
    points = sorted(points)
    def cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
    lower = []
    for p in points:
        while len(lower) > 1 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    upper = []
    for p in reversed(points):
        while len(upper) > 1 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    return lower[:-1] + upper[:-1]


def polygon_measure(vertices):
    area = 0.0
    perim = 0.0
    for i, (x, y) in enumerate(vertices):
        x2, y2 = vertices[(i + 1) % len(vertices)]
        area += x * y2 - x2 * y
        perim += math.hypot(x2 - x, y2 - y)
    return abs(area) / 2, perim


def test():
    n = 12000
    count = 0
    for q in (.501, .51, .55, .65, .75, .9):
        t, s = contact(q)
        assert abs(math.cos(t) - 1 / (2 * q)) < 1e-14
        assert area_defect(q) > 0 and perimeter_defect(q) > 0
        assert abs(area_defect(q) - area_defect_by_cap(q)) < 4e-12
        count += 4

    for q in (.51, .65, .9):
        points = []
        for k in range(n):
            theta = 2 * math.pi * k / n
            radial = 1 + q * math.cos(theta)
            points.append((radial * math.cos(theta), radial * math.sin(theta)))
        hull = monotone_hull(points)
        area, perim = polygon_measure(hull)
        analytic_area = math.pi * (1 + q * q / 2) + area_defect(q)
        full_perim = 2 * simpson(lambda t: math.sqrt(1 + q * q - 2 * q * math.cos(t)), 0, math.pi)
        analytic_perim = full_perim - perimeter_defect(q)
        assert abs(area - analytic_area) < 5e-6, (q, area, analytic_area)
        assert abs(perim - analytic_perim) < 5e-6, (q, perim, analytic_perim)
        count += 2

    for delta in (.02, .005, .001):
        q = .5 + delta
        a_ratio = area_defect_by_cap(q) / delta ** 2.5
        p_ratio = perimeter_defect(q) / delta ** 3.5
        assert abs(a_ratio - 32 / 15) < 10 * delta
        assert abs(p_ratio - 512 / 105) < 15 * delta
        count += 2
    print('Checks passed:', count)
    print('All checks are finite numerical diagnostics; the proof is analytic.')


if __name__ == '__main__':
    test()
