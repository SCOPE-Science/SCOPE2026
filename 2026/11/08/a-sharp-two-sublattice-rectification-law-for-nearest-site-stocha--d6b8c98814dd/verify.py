"""Standalone finite checks of an exact two-sublattice resetting-current formula.

Python 3 standard library only. Numerical checks do not replace the proof.
"""
import math
import random

checks = 0


def check(test, message):
    global checks
    if not test:
        raise AssertionError(message)
    checks += 1


def laplace_cdf(x, k):
    if x < 0:
        return math.exp(k * x) / 2
    return 1 - math.exp(-k * x) / 2


def analytic_p_d(a, b, k):
    s = math.sinh(k * (a + b) / 2)
    p = (math.sinh(k * a / 2) + math.sinh(k * b / 2)) / (2 * s)
    d = (a * math.sinh(k * b / 2) - b * math.sinh(k * a / 2)) / (2 * s)
    return p, d


def direct_p_d(a, b, k):
    # Integrate the exponential-time Brownian displacement density over each
    # Voronoi interval, retaining farther-than-nearest-site transitions.
    length = a + b
    count = max(40, math.ceil(32 / (k * length)))
    p, d, total = 0.0, 0.0, 0.0
    for n in range(-count, count + 1):
        even_site = n * length
        odd_site = even_site + a
        pe = laplace_cdf(even_site + a / 2, k) - laplace_cdf(even_site - b / 2, k)
        po = laplace_cdf(odd_site + b / 2, k) - laplace_cdf(odd_site - a / 2, k)
        total += pe + po
        p += po
        d += even_site * pe + odd_site * po
    return p, d, total


def velocity(a, b, D, r_even, r_odd):
    k0, k1 = math.sqrt(r_even / D), math.sqrt(r_odd / D)
    p0, d0 = analytic_p_d(a, b, k0)
    p1, d1 = analytic_p_d(a, b, k1)
    return (p1 * d0 - p0 * d1) / (p1 / r_even + p0 / r_odd)


def simulate(a, b, D, r_even, r_odd, steps=300000, seed=929):
    # Simulation in physical time, not independent Laplace/time draws.
    rng = random.Random(seed)
    length, x, time = a + b, 0.0, 0.0
    for _ in range(steps):
        n = round(x / length)
        rate = r_even if abs(x - n * length) < 1e-7 else r_odd
        hold = rng.expovariate(rate)
        y = x + rng.gauss(0, math.sqrt(2 * D * hold))
        j = math.floor(y / length)
        residue = y - j * length
        if residue < a / 2:
            x = j * length
        elif residue < a + b / 2:
            x = j * length + a
        else:
            x = (j + 1) * length
        time += hold
    return x / time


for a, b in ((1, 2), (2, 1), (0.5, 1.5), (1, 5), (1, 1)):
    for k in (0.15, 0.45, 1.0, 2.0, 4.0):
        p, d = analytic_p_d(a, b, k)
        pd, dd, total = direct_p_d(a, b, k)
        check(abs(total - 1) < 2e-10, 'cell mass')
        check(abs(p - pd) < 2e-10, 'parity probability')
        check(abs(d - dd) < 2e-9, 'mean increment')
        check(0 < p < 1, 'irreducibility')

for a, b in ((1, 2), (2, 1), (0.7, 1.2), (1, 1)):
    for r0, r1 in ((4, 1), (1, 4), (0.2, 2), (1, 1), (8, 0.4)):
        v = velocity(a, b, 1, r0, r1)
        target_sign = (b - a) * (r0 - r1)
        check((v > 1e-12) if target_sign > 0 else ((v < -1e-12) if target_sign < 0 else abs(v) < 1e-12), 'sharp sign classification')

check(abs(velocity(1, 2, 1, 4, 1) - 0.052736115947430405) < 1e-14, 'numeric example')
check(abs(simulate(1, 2, 1, 4, 1) - velocity(1, 2, 1, 4, 1)) < 0.007, 'physical-time simulation')
check(abs(simulate(1, 2, 1, 1, 4) - velocity(1, 2, 1, 1, 4)) < 0.007, 'reversed clocks simulation')

for t in (0.0001, 0.0005, 0.001):
    exact = velocity(1, 2, 1, 4 * t, t)
    asymp = 0.1 * t * t
    check(abs(exact / asymp - 1) < 0.002, 'weak-rate coefficient')

check(abs(velocity(1, 2, 1, 400, 100)) < 0.001, 'fast-rate decay')
check(abs(velocity(1, 2, 1, 4000, 1000)) < 1e-7, 'faster-rate decay')
print('PASS:', checks, 'deterministic assertions')
