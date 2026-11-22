"""Exact-arithmetic checks of cyclic C1 quadratic interpolation variation.

Pure standard-library Python 3. These finite checks complement the all-n proof.
"""
from fractions import Fraction as F
from random import Random


def cell_variation(y, delta, m):
    """Total variation of y + m*t + (delta-m)*t*t on 0 <= t <= 1."""
    if delta != m:
        t = -m / (2 * (delta - m))
        if 0 < t < 1:
            mid = y + m * t + (delta - m) * t * t
            return abs(mid - y) + abs(y + delta - mid)
    return abs(delta)


def interpolate_odd(data):
    n = len(data)
    assert n >= 3 and n % 2 == 1
    delta = [data[(i + 1) % n] - data[i] for i in range(n)]
    m = [sum((-1) ** k * delta[(i + k) % n] for k in range(n))
         for i in range(n)]
    assert all(m[i] + m[(i + 1) % n] == 2 * delta[i]
               for i in range(n))
    var = sum(cell_variation(data[i], delta[i], m[i]) for i in range(n))
    vin = sum(abs(z) for z in delta)
    return var, vin, delta, m


def data_from_delta(d):
    n = len(d)
    assert sum(d) == 0
    y = [F(0)]
    for z in d[:-1]:
        y.append(y[-1] + z)
    assert y[0] - y[-1] == d[-1]
    return y


def main():
    rng = Random(24015)
    checked_pairs = 0
    checked_random = 0
    for n in range(3, 42, 2):
        for p in range(n):
            for q in range(n):
                if p == q:
                    continue
                d = [F(int(i == p) - int(i == q)) for i in range(n)]
                var, vin, delta, m = interpolate_odd(data_from_delta(d))
                assert vin == 2
                assert var <= n
                assert all(z in (-2, 0, 2) for z in m)
                if q == (p + 1) % n:
                    assert var == n
                checked_pairs += 1
        isolated = [F(1)] + [F(0)] * (n - 1)
        out, inn, _, _ = interpolate_odd(isolated)
        assert (out, inn) == (n, 2)
        for _ in range(90):
            data = [F(rng.randint(-9, 9), 7) for i in range(n)]
            out, inn, _, _ = interpolate_odd(data)
            assert 2 * out <= n * inn
            checked_random += 1
    print('EXACT_ODD_CYCLE_PAIR_TRANSPORT_AND_EXTREMIZERS_PASS', checked_pairs)
    print('EXACT_RATIONAL_RANDOM_DATA_BV_BOUND_PASS', checked_random)
    for n in range(4, 66, 2):
        sign = [(-1) ** i for i in range(n)]
        # With zero data: t(1-t)*alternating sign joins C1 at all knots.
        assert all(sign[(i+1) % n] == -sign[i] for i in range(n))
        # Unit data at site zero violates compatibility.
        data = [F(1)] + [F(0)] * (n - 1)
        delta = [data[(i+1) % n] - data[i] for i in range(n)]
        assert sum(sign[i] * delta[i] for i in range(n)) != 0
        # A compatible nonconstant datum supplies a solvable example.
        data = [F(0)] * n
        data[0] = data[1] = F(1)
        delta = [data[(i+1) % n] - data[i] for i in range(n)]
        assert sum(sign[i] * delta[i] for i in range(n)) == 0
        m = [F(0)] * n
        m[0] = F(0)
        for i in range(n-1):
            m[i+1] = 2 * delta[i] - m[i]
        assert m[n-1] + m[0] == 2 * delta[n-1]
    print('EVEN_CYCLE_COMPATIBILITY_AND_NULL_SPLINE_PASS')
    print('ALL_PERIODIC_QUADRATIC_VARIATION_CERTIFICATES_PASS')


if __name__ == '__main__':
    main()
