"""Independent reproducibility checks for the parabolic-arc acute-triangle law.

Run: python3 check_parabolic_acuteness.py
Uses only Python's standard library. Numerical checks do not replace the proof.
"""
import math
import random


def predicted(a):
    if a <= 1.0:
        return 0.0
    s = math.sqrt(a * a - 1.0)
    result = (s ** 3 + 3 * s - 3 * a * math.acosh(a)) / a ** 3
    if a > math.sqrt(2):
        r = math.sqrt(a * a - 2.0)
        result -= (r ** 3 + 6 * r - 6 * a * math.acosh(a / math.sqrt(2))) / a ** 3
    return result


def f(x):
    return x - 1 - math.log(x) if x > 1 else 0


def simpson(fun, left, right, n=12000):
    h = (right - left) / n
    total = fun(left) + fun(right)
    for k in range(1, n):
        total += (4 if k % 2 else 2) * fun(left + k * h)
    return h * total / 3


def independent_integral(a):
    if a <= 1:
        return 0
    s = math.sqrt(a * a - 1)
    im = simpson(lambda v: f(a * a - v * v), -s, s)
    ie = 0
    if a > math.sqrt(2):
        r = math.sqrt(a * a - 2)
        ie = simpson(lambda p: f(2 * p * (a - p)), (a-r)/2, (a+r)/2)
    return 3 * (im - 4 * ie) / (4 * a ** 3)


def triple_is_acute(u, v, w):
    # Evaluate the actual two-dimensional Euclidean dot products.
    p = [(t, t*t) for t in (u, v, w)]
    for i in range(3):
        x, y = p[i]
        j, k = [m for m in range(3) if m != i]
        vx, vy = p[j][0] - x, p[j][1] - y
        wx, wy = p[k][0] - x, p[k][1] - y
        if vx*wx + vy*wy <= 0:
            return False
    return True


def conditions(u, v, w):
    return (1 + (u+v)*(u+w) > 0 and
            1 + (u+v)*(v+w) < 0 and
            1 + (u+w)*(v+w) > 0)


def main():
    for a in (0.7, 1, 1.01, 1.2, 1.4, math.sqrt(2), 1.42, 1.5, 2, 3, 5, 10, 30):
        lhs = independent_integral(a)
        rhs = predicted(a)
        assert abs(lhs-rhs) < 3e-10, (a, lhs, rhs)
        assert -1e-9 <= rhs <= 1+1e-9
    rng = random.Random(241916)
    for a in (0.9, 1.05, 1.2, 1.5, 2, 3, 5, 10):
        n = 240000
        count = 0
        for _ in range(n):
            u, v, w = sorted(rng.uniform(-a,a) for j in range(3))
            c = triple_is_acute(u, v, w)
            assert c == conditions(u,v,w)
            count += int(c)
        p = predicted(a)
        observed = count/n
        sigma = math.sqrt(p*(1-p)/n)
        assert abs(observed-p) < max(0.0002, 5*sigma), (a, observed, p, sigma)
    for delta in (1e-3, 3e-4):
        ratio = predicted(1+delta)/delta**2.5
        assert abs(ratio-8*math.sqrt(2)/5) < 0.02
    for delta in (1e-3, 3e-4):
        a = math.sqrt(2)+delta
        r = math.sqrt(a*a-2)
        correction = (r**3+6*r-6*a*math.acosh(a/math.sqrt(2))) / a**3
        assert abs(correction/delta**2.5-4*2**0.25/5) < 0.01
    for a in (100, 1000):
        leading = (3*math.log(a)-1.5)/a**2
        assert abs(predicted(a)-leading) < 1.2/a**4
    # Volume of the onset limiting body: integral_{-1}^1 (1-z²)^2/2 dz.
    assert abs(simpson(lambda z: (1-z*z)**2/2, -1, 1) - 8/15) < 1e-12
    print("PARABOLIC_ARC_ACUTENESS_CHECKS_OK")

if __name__ == '__main__':
    main()
