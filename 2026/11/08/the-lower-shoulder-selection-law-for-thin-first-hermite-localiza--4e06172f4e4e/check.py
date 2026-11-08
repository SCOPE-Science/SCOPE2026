#!/usr/bin/env python3
"""Numerical sanity checks for first-Hermite annulus asymptotics.

Independent of the asymptotic proof. Python standard library only.
"""
import math


def radial(n, u):
    # Smooth at u=n, including n=0; no direct powers of enormous u.
    if u <= 0:
        raise ValueError('positive radii required')
    return math.exp(-u + n * math.log(u) - math.lgamma(n + 1)) * (u - n) ** 2 / u


def annulus(n, s, width, panels=128):
    if panels % 2:
        raise ValueError('even Simpson panel count required')
    h = width / panels
    val = radial(n, s) + radial(n, s + width)
    for j in range(1, panels):
        val += (4 if j % 2 else 2) * radial(n, s + j * h)
    return val * h / 3


def one_case(s, width):
    R = s + width / 2
    lo = max(0, int(R - 5 * math.sqrt(R)))
    hi = int(R + 5 * math.sqrt(R)) + 2
    vals = {n: annulus(n, s, width) for n in range(lo, hi)}
    lower = max((vals[n], n) for n in vals if n < R)
    upper = max((vals[n], n) for n in vals if n > R)
    pred_gap = 2 * width / (3 * math.e * math.sqrt(math.pi) * R)
    ratio = (lower[0] - upper[0]) / pred_gap
    assert lower[0] > upper[0] > 0
    assert abs((lower[1] - R) / math.sqrt(R) + math.sqrt(2)) < .4
    assert abs((upper[1] - R) / math.sqrt(R) - math.sqrt(2)) < .4
    assert 0.90 < ratio < 1.14, (s, width, ratio)
    return lower[1], upper[1], round(ratio, 6)


def main():
    for u in (1.4, 10.2, 50.5, 100.0):
        # This is the diagonal resolution-of-the-identity check.
        tot = sum(radial(n, u) for n in range(int(u + 20 * math.sqrt(u)) + 51))
        assert abs(tot - 1) < 3e-10, (u, tot)
    out = [one_case(s, L) for s, L in ((200, 1), (1000, 1), (2000, 2), (10000, 3))]
    print('THIN_HERMITE_ANNULUS_PASS normalization=4 shoulder_cases=4')
    for (s, L), (low, high, ratio) in zip(((200, 1), (1000, 1), (2000, 2), (10000, 3)), out):
        print('area_center', s + L / 2, 'left_index', low,
              'right_index', high, 'gap_coefficient_ratio', ratio)


if __name__ == '__main__':
    main()
