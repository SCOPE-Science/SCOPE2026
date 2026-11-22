#!/usr/bin/env python3
"""Finite checks of inverse-branch counts for a cosine-memristor map.

Dependencies: Python 3 standard library. This checks examples only; it does not
replace the infinite-range analytic proof in RESULT.md.
"""
import math

TAU = 2.0 * math.pi


def phase(x, b, v):
    return b * x * math.cos(v - x)


def phase_derivative(x, b, v):
    return b * (math.cos(v - x) + x * math.sin(v - x))


def bisect_zero(f, left, right, steps=64):
    a, z = left, right
    ya = f(a)
    yz = f(z)
    assert ya * yz < 0
    for _ in range(steps):
        mid = (a + z) / 2
        ym = f(mid)
        if ya * ym <= 0:
            z, yz = mid, ym
        else:
            a, ya = mid, ym
    return (a + z) / 2


def count_levels(lo, hi, offset):
    a, b = sorted((lo, hi))
    return max(0, math.floor((b - offset) / TAU)
               - math.ceil((a - offset) / TAU) + 1)


def count_preimages(radius, b, v, s):
    """Count phase-level crossings by monotonic intervals for generic samples.

    No endpoint in the examples is a crossing; no critical point is a crossing.
    """
    assert radius > 1 and b > 0 and abs(s) <= 1
    step = 0.04
    n = math.ceil(2 * radius / step)
    grid = [-radius + 2 * radius * j / n for j in range(n + 1)]
    critical = [-radius]
    for x0, x1 in zip(grid, grid[1:]):
        d0, d1 = phase_derivative(x0, b, v), phase_derivative(x1, b, v)
        if d0 * d1 < 0:
            critical.append(bisect_zero(lambda x: phase_derivative(x, b, v), x0, x1))
    critical.append(radius)
    shifts = [math.asin(s)] if abs(s) == 1 else [math.asin(s), math.pi - math.asin(s)]
    count = 0
    for left, right in zip(critical, critical[1:]):
        for offset in shifts:
            count += count_levels(phase(left, b, v), phase(right, b, v), offset)
    return count, len(critical) - 2


def main():
    cases = [(1.3, 0.7, 0.2), (1.3, 0.7, 1.0), (0.8, -1.1, 0.0)]
    for b, v, s in cases:
        factor = (2 if abs(s) < 1 else 1) * b / math.pi**2
        values = []
        for radius in (20, 40, 80, 160):
            count, ncrit = count_preimages(radius, b, v, s)
            assert 0 <= ncrit < 2 * radius / math.pi + 8
            assert abs(count - factor * radius**2) < 5 * radius
            values.append((radius, count))
        assert abs(values[-1][1] / 160**2 - factor) < 0.002
        print(f'case b={b}, V={v}, phase-target={s}: {values}; coefficient={factor:.8f}')
    print('COSINE_MEMRISTOR_INVERSE_VERIFY_OK')


if __name__ == '__main__':
    main()
