#!/usr/bin/env python3
"""Finite exact and numerical sanity checks for the quadratic inverse-sheet construction.

This is not a replacement for the all-m compact inverse-function proof.
"""
import math

JLO, JHI = 1 / 8, 7 / 8
JPRIME_LO, JPRIME_HI = 1 / 16, 15 / 16

def L(z):
    return 4 * z * (1 - z)

def G(a, b, u, v):
    return a * u + v, 1.5 * b * u * (1 - u)

def laps(m):
    N = 2 ** m
    x = [math.sin(j * math.pi / (2 * N)) ** 2 for j in range(N + 1)]
    return [j for j in range(N) if x[j] > JLO and x[j+1] < JHI], x

def check():
    assert abs(G(0, 8 / 3, .2, .6)[0] - .6) < 1e-14
    assert abs(G(0, 8 / 3, .2, .6)[1] - L(.2)) < 1e-14
    u, v = .23, .67
    p, q = G(0, 8 / 3, u, v)
    p, q = G(0, 8 / 3, p, q)
    assert abs(p - L(u)) < 1e-14 and abs(q - L(v)) < 1e-14
    k3, x3 = laps(3)
    assert k3 == [2, 3, 4, 5]
    assert 1 / 8 < x3[2] and x3[6] < 7 / 8
    assert abs(x3[2] - (2 - math.sqrt(2)) / 4) < 1e-14
    assert abs(x3[6] - (2 + math.sqrt(2)) / 4) < 1e-14
    assert 8 * math.sqrt(15) / 8 > 1
    theta = math.asin(1 / math.sqrt(8))
    kappa = 1 - 4 * theta / math.pi
    assert kappa > .5
    for m in range(3, 11):
        js, _ = laps(m)
        assert len(js) >= 4 and abs(len(js) - kappa * 2 ** m) <= 3
        assert 2 ** m * math.sqrt(15) / 8 > 1
        for j in js:
            # At each inverse-branch target in the enlarged target interval,
            # the trigonometric derivative bound applies.
            for target in (1 / 16, 1 / 8, 1 / 2, 7 / 8, 15 / 16):
                phase = j * math.pi / 2 + math.asin(math.sqrt(target))
                # sin^2(2^m theta)=target; select proper alternating inverse.
                if j % 2:
                    phase = (j + 1) * math.pi / 2 - math.asin(math.sqrt(target))
                th = phase / (2 ** m)
                xx = math.sin(th) ** 2
                derivative = 2 ** m * abs(math.sin(2 ** (m + 1) * th)) / math.sin(2 * th)
                assert derivative + 1e-7 >= (2 ** m) * math.sqrt(15) / 8
                assert abs(L_iter(xx, m) - target) < 1e-8
    print('LOGISTIC_HORSESHOE_VERIFY_OK')

def L_iter(z, n):
    for _ in range(n):
        z = L(z)
    return z

if __name__ == '__main__':
    check()
