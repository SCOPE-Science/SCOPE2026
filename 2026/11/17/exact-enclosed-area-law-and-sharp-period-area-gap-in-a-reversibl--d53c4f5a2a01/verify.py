"""Numerical cross-checks for the explicit two-zone crossing-area theorem.
Only finite checks; the proof is analytical and is supplied separately.
"""
import math


def area_data(a, d, tr, theta):
    w = math.sqrt(d - tr * tr / 4.0)
    c = tr / (2.0 * w)
    p = a / d
    ss, cc = math.sin(theta), math.cos(theta)
    v = p * w * ((cc - math.exp(-c * theta)) / ss - c)
    bottom = p * w * ((math.exp(c * theta) - cc) / ss - c)
    area = (bottom * bottom - v * v) / tr
    explicit = (4.0 * p * p * w * w / tr
                * (math.cosh(c * theta) - cc) / ss
                * (math.sinh(c * theta) / ss - c))
    return w, c, p, v, bottom, area, explicit


def simpson(fn, lo, hi, n=2000):
    h = (hi - lo) / n
    out = fn(lo) + fn(hi)
    for i in range(1, n):
        out += (4 if i % 2 else 2) * fn(lo + h * i)
    return out * h / 3


def theta_at_speed(a, d, tr, speed):
    lo, hi = math.pi + 1e-10, 2 * math.pi - 1e-8
    for _ in range(80):
        mid = (lo + hi) / 2
        got = area_data(a, d, tr, mid)[3]
        if got > speed:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def check(a, d, tr, speed):
    theta = theta_at_speed(a, d, tr, speed)
    w, c, p, v, bottom, area, explicit = area_data(a, d, tr, theta)
    assert v > 0 and bottom < 0 and math.pi < theta < 2 * math.pi
    assert abs(v - speed) < 1e-7 * max(1, speed)
    def xp(s):
        b = (v + tr * p / 2) / w
        return math.exp(tr*s/2) * (
            tr / 2 * (p * math.cos(w * s) - b * math.sin(w * s))
            - p * w * math.sin(w * s) - b * w * math.cos(w * s))
    area_int = 2 * simpson(lambda s: xp(s)**2, 0.0, theta/w)
    for other in (area_int, explicit):
        assert abs(other-area) <= 2e-7 * max(1., area), (a, d, tr, v, area, other)
    return area, 2 * theta / w


if __name__ == '__main__':
    for aa, dd, tt in [(2.,2.,1.), (1.,3.,.2), (3.,5.,3.)]:
        for v in (0.1, 1., 10., 100.):
            check(aa, dd, tt, v)
        w = math.sqrt(dd-tt**2/4.)
        c = tt / (2*w)
        p = aa / dd
        a_big, t_big = check(aa, dd, tt, 100000.)
        constant = 2 * p * (1 + math.exp(-math.pi*c)) * math.sqrt((math.exp(2*math.pi*c)-1)/tt)
        assert abs((t_big-2*math.pi/w)*math.sqrt(a_big)/constant-1)<3e-4
    print('CROSSING_AREA_AND_PERIOD_EDGE_CHECK_OK')
