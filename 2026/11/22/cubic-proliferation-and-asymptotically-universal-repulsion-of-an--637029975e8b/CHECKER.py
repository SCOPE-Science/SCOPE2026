#!/usr/bin/env python3
"""Finite numerical corroboration of the sine-phase crossing theorem; not an infinite proof.
Run: python3 CHECKER.py. Uses only Python's standard library.
"""
import math


def bisect_root(fun, lo, hi):
    fl = fun(lo)
    fh = fun(hi)
    if fl == 0.0:
        return lo
    if fh == 0.0:
        return hi
    assert fl * fh < 0, (lo, hi, fl, fh)
    for _ in range(75):
        mid = (lo + hi) / 2
        fm = fun(mid)
        if fl * fm <= 0:
            hi, fh = mid, fm
        else:
            lo, fl = mid, fm
    return (lo + hi) / 2


def cubic_phase(x, b):
    return math.pi * ((1 + b) * x - b * x**3 / 4)


def phase(x, a, b, sign):
    return cubic_phase(x, b) + sign * math.asin(min(1, x / a))


def phase_derivative(x, a, b, sign):
    return math.pi * (1 + b - 3 * b * x * x / 4) + sign / math.sqrt((a - x) * (a + x))


def crossings_on_interval(a, b, left, right, sign):
    # The selected interval is strictly decreasing for both phase branches.
    low = phase(right, a, b, sign)
    high = phase(left, a, b, sign)
    off = 0 if sign == 1 else math.pi
    k0 = math.ceil((low - off) / (2 * math.pi) + 1e-11)
    k1 = math.floor((high - off) / (2 * math.pi) - 1e-11)
    values = []
    for k in range(k0, k1 + 1):
        target = off + 2 * math.pi * k
        root = bisect_root(lambda x: phase(x, a, b, sign) - target, left, right)
        values.append(root)
    return values


def one_step_eigenvalues(x, a, b):
    v = a * math.pi * math.cos(cubic_phase(x, b))
    tr = 1 + v * (1 + b - b * x * x / 4)
    det = v * (1 + b - 5 * b * x * x / 4)
    disc = tr * tr - 4 * det
    if disc < 0:
        return (math.sqrt(det), math.sqrt(det))
    sq = math.sqrt(disc)
    return ((abs(tr + sq) / 2), (abs(tr - sq) / 2))


def test_case(a, b, L, frac):
    end = frac * a
    assert L < end
    for sign in (1, -1):
        assert phase_derivative(L, a, b, sign) < 0
        assert phase_derivative(end, a, b, sign) < 0
    xs = sorted(crossings_on_interval(a, b, L, end, 1) + crossings_on_interval(a, b, L, end, -1))
    assert len(xs) > 1
    min_ev = math.inf
    for x in xs:
        q = -x / 2
        z = a * math.sin(math.pi * x * (1 + b - b * q * q))
        assert abs(z + x) < 1e-8
        assert abs(q + x - x / 2) < 1e-12
        eigs = one_step_eigenvalues(x, a, b)
        min_ev = min(min_ev, min(eigs))
        assert min(eigs) > 1, (x, eigs)
    print(f'a={a}, b={b}, range=[{L},{end}], roots={len(xs)}, min |eigenvalue|={min_ev:.5f}')




def count_all_phase_crossings(a, b):
    """Use phase monotonicity, not a uniform residual mesh, to count sample roots."""
    small = 1e-10
    # At the sample parameter values the minus phase has one maximum;
    # the plus phase has a maximum and a very near-endpoint minimum.
    minus_max = bisect_root(lambda x: phase_derivative(x, a, b, -1), 0, a * .5)
    plus_max = bisect_root(lambda x: phase_derivative(x, a, b, +1), 0, a * .5)
    plus_min = bisect_root(lambda x: phase_derivative(x, a, b, +1), a * .5, a - small)
    def level_count(phase_fun, knots, offset):
        total = 0
        for left, right in zip(knots[:-1], knots[1:]):
            v0 = (phase_fun(left) - offset) / (2 * math.pi)
            v1 = (phase_fun(right) - offset) / (2 * math.pi)
            total += max(0, math.floor(max(v0, v1) + 1e-10) - math.ceil(min(v0, v1) - 1e-10) + 1)
        return total
    cp = level_count(lambda x: phase(x, a, b, 1), [0, plus_max, plus_min, a], 0)
    cm = level_count(lambda x: phase(x, a, b, -1), [0, minus_max, a], math.pi)
    return cp + cm - 1  # remove the equilibrium at the origin

def test_phase_symmetry():
    for b in (.5, 1, 2):
        for x in (.125, .5, 2.25):
            q = -x / 2
            p = x * (1 + b - b * q * q)
            assert abs(p - ((1 + b) * x - b * x**3 / 4)) < 1e-12
            # Characteristic determinant = derivative in x minus derivative in q.
            one = 1 + b - b * q * q
            two = -2 * b * q * x
            assert abs((one - two) - (1 + b - 5 * b * x * x / 4)) < 1e-12


if __name__ == '__main__':
    test_phase_symmetry()
    for a, expected in ((5, 26), (10, 234), (20, 1964)):
        count = count_all_phase_crossings(a, 1)
        assert count == expected, (a, count)
        print(f'a={a}, b=1: all antipodal cycles={count}, cubic-minus-linear={a**3/4-2*a}')
    test_case(10, 1, 5, .8)
    test_case(20, 1, 5, .8)
    test_case(20, .5, 5, .8)
    print('All finite checks passed; unbounded-parameter statements follow from the written proof.')
