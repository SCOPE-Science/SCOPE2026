"""Finite numerical diagnostics for the quartic Hilbert-space modulus.

Run using Python 3 with no third-party dependencies. The proof is analytic;
these checks verify algebraic normalizations and a range of finite examples.
"""
import math
import random


def profile(d, a):
    assert 0 < d <= 2 and a > 0
    h = d / 2
    s = math.sqrt(max(0., 1. - h * h))
    p = 1. + a * a
    q = 2. * a * s
    c = 2. * q / (p + math.sqrt(p * p + 8. * q * q))
    return 4. * a * d * math.sqrt(1. - c * c) * (p + q * c), c


def fourth_difference(x, y, z):
    xz = sum((xx + zz) ** 2 for xx, zz in zip(x, z))
    yz = sum((yy + zz) ** 2 for yy, zz in zip(y, z))
    return abs(xz * xz - yz * yz)


rng = random.Random(20261121)
checks = 0
for d in [0.03, 0.3, 0.8, 1.25, 1.9, 2.0] + [rng.uniform(.05, 1.99) for _ in range(24)]:
    h = d / 2
    s = math.sqrt(max(0., 1. - h * h))
    x, y = (s, h), (s, -h)
    for a in [.02, .1, .4, 1., 2., 6.] + [10. ** rng.uniform(-1.6, .8) for _ in range(12)]:
        value, c = profile(d, a)
        z = (a * c, a * math.sqrt(1. - c * c))
        assert abs(fourth_difference(x, y, z) - value) < 1e-9 * max(1., value)
        checks += 1
        assert abs(a ** 4 * profile(d, 1. / a)[0] - value) < 1e-8 * max(1., value)
        checks += 1
        assert 0 <= c <= .5 + 1e-12
        checks += 1
        if d < 2.:
            higher, _ = profile(d + (2. - d) / 20., a)
            assert higher > value
            checks += 1
        # Orthogonal components never beat the planar maximizer.
        for _ in range(80):
            ang = 2. * math.pi * rng.random()
            rad = a * math.sqrt(rng.random())
            zz = (rad * math.cos(ang), rad * math.sin(ang))
            assert fourth_difference(x, y, zz) <= value + 1e-9 * max(1., value)
            checks += 1
            extra = a * rng.random() * .2
            scale = min(1., a / math.hypot(rad, extra))
            zz3 = (zz[0] * scale, zz[1] * scale, extra * scale)
            assert fourth_difference((s, h, 0.), (s, -h, 0.), zz3) <= value + 1e-9 * max(1., value)
            checks += 1
print('QUARTIC_STEINHAUS_HILBERT_FINITE_CHECK_OK', checks)
