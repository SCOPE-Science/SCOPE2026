#!/usr/bin/env python3
"""Standalone deterministic checks for a Brownian first-passage rank-response theorem.

Scientific evidence only. Uses Python's standard library; finite numerical tests
are not a proof of the infinite-distance-scale induction.
"""
import math

PI = math.pi
SQRT_PI = math.sqrt(PI)


def base_survival(distance, diffusivity, time):
    if time <= 0:
        return 1.0
    return math.erf(distance / (2.0 * math.sqrt(diffusivity * time)))


def kernel(u):
    if u <= 0:
        return 0.0
    p = 1.0 / math.sqrt(u)
    return ((u + 2.0) * math.erfc(p)
            - (u + 1.0) * math.erfc(p / 2.0)
            + 2.0 * math.sqrt(u / PI)
            * (math.exp(-1.0 / (4.0 * u)) - math.exp(-1.0 / u)))


def response(distance, diffusivity, time):
    return distance * distance / diffusivity * kernel(diffusivity * time / (distance * distance))


def simpson(fun, a, b, n):
    assert n > 0 and n % 2 == 0
    step = (b - a) / n
    total = fun(a) + fun(b)
    for k in range(1, n):
        total += (4 if (k % 2) else 2) * fun(a + k * step)
    return total * step / 3.0


def integral_response(distance, diffusivity, time):
    def f(v):
        return base_survival(distance, diffusivity, v) * base_survival(distance, diffusivity, time - v)
    return simpson(f, 0.0, time, 6000) - time * base_survival(distance, diffusivity, time)


def mixture_response(distances, weights, diffusivity, time):
    return sum(w * response(d, diffusivity, time) for d, w in zip(distances, weights))


def mixture_fraction(distances, weights, diffusivity, time):
    return sum(w * math.erfc(d / (2.0 * math.sqrt(diffusivity * time)))
               for d, w in zip(distances, weights))


def laplace_response_exact(distance, diffusivity, s):
    a = distance / math.sqrt(diffusivity)
    z = a * math.sqrt(s)
    return (math.exp(-2.0 * z) + (z / 2.0 - 1.0) * math.exp(-z)) / (s * s)


def run():
    count = 0
    # Direct convolution integration is numerically independent of erfc inversion.
    for d in (0.7, 1.0, 2.5):
        for D in (0.5, 1.0, 3.0):
            for factor in (0.25, 0.5, 1.0, 2.0):
                t = factor * d * d / D
                got = response(d, D, t)
                other = integral_response(d, D, t)
                assert abs(got - other) < 1.5e-8 * (1 + abs(got)), (d, D, factor, got, other)
                count += 1
    # Check the Laplace-domain differentiation identity by a second inversion route:
    # numerical quadrature of the already-derived time response.
    for d in (0.5, 1.0, 2.0):
        for D in (0.7, 2.0):
            for s in (0.9, 1.5):
                truncation = 60.0 / s
                numeric = simpson(lambda t: math.exp(-s * t) * response(d, D, t),
                                  0.0, truncation, 16000)
                exact = laplace_response_exact(d, D, s)
                assert abs(numeric - exact) < 3e-7 * (1 + abs(exact)), (d, D, s, numeric, exact)
                count += 1
    # Exact asymptotic sign mechanisms, with deliberately moderate domains.
    for u in (0.005, 0.01, 0.02):
        leading = 2 / SQRT_PI * u**1.5 * math.exp(-1 / (4 * u))
        assert kernel(u) > 0 and 0.7 < kernel(u) / leading < 1.01
        count += 1
    for u in (100.0, 1000.0, 10000.0):
        leading = 1.0 - math.sqrt(u / PI)
        assert kernel(u) < 0 and abs(kernel(u) / leading - 1) < 0.015
        count += 1
    # All alternating signs in a concrete three-scale mixture.
    distances = (1.0, 100.0, 10000.0)
    weights = (1.0 / 3.0,) * 3
    times = []
    signs = []
    fractions = []
    for d in distances:
        for u, sign in ((0.25, 1), (2.0, -1)):
            t = u * d * d
            val = mixture_response(distances, weights, 1.0, t)
            frac = mixture_fraction(distances, weights, 1.0, t)
            assert val * sign > 1e-4, (t, val, sign)
            times.append(t)
            fractions.append(frac)
            signs.append(sign)
            count += 1
    assert all(a < b for a, b in zip(times, times[1:]))
    assert all(a < b for a, b in zip(fractions, fractions[1:]))
    assert signs == [1, -1, 1, -1, 1, -1]
    count += 3
    # Additional scale-separation stress test; checks not a proof for all K.
    for K in (2, 3, 4):
        ds = tuple(100.0 ** j for j in range(K))
        ws = tuple(1.0 / K for j in range(K))
        seq = []
        for d in ds:
            for u in (0.25, 2.0):
                seq.append(mixture_response(ds, ws, 1.0, u * d * d))
        assert all(seq[j] > 0 if j % 2 == 0 else seq[j] < 0 for j in range(len(seq)))
        count += len(seq)
    print("PASS: %d deterministic checks; six witness signs +,-,+,-,+,-" % count)
    print("Example time, rank fraction, zero-rate survival response:")
    for t, f in zip(times, fractions):
        print("%.8g %.12g %.12g" % (t, f, mixture_response(distances, weights, 1.0, t)))


if __name__ == '__main__':
    run()
