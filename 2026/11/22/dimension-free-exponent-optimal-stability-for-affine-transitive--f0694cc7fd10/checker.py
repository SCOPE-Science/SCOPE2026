"""Reproducible finite-cycle sanity checks for Fourier synthesis stability.

Run: python checker.py
Only the Python standard library is required. Numerical checks supplement,
but do not replace, the dimension-free proof in RESULT.md.
"""
import cmath
import math
import random

RNG = random.Random(20261121)


def ft(f):
    n = len(f)
    return [sum(f[x] * cmath.exp(-2j * math.pi * k * x / n)
                for x in range(n)) / math.sqrt(n) for k in range(n)]


def lp(v, r):
    return sum(abs(x) ** r for x in v) ** (1 / r)


def verify(f, support, r):
    n = len(f)
    F = ft(f)
    R = lp(F, r)
    mask = [1 if j in support else 0 for j in range(n)]
    C = len(support) / (math.sqrt(n) * lp(ft(mask), r))
    k = max(range(n), key=lambda j: abs(F[j]))
    deficit = 1 - abs(F[k]) / (C * R)
    if deficit < -1e-10:
        raise AssertionError(("sharp constant", n, r, deficit))
    deficit = max(0.0, deficit)
    g = [f[j] * cmath.exp(-2j * math.pi * k * j / n)
         for j in range(n)]
    avg = sum(g[j] for j in support) / len(support)
    h = [avg if j in support else 0 for j in range(n)]
    distance = lp(ft([a - b for a, b in zip(g, h)]), r) / R
    if r < 2:
        rhs = 2 * math.sqrt((1 - (1 - deficit) ** 2) / (r - 1))
    elif r == 2:
        rhs = math.sqrt(1 - (1 - deficit) ** 2)
        if abs(distance - rhs) > 3e-9:
            raise AssertionError(("Hilbert identity", n, distance, rhs))
    else:
        rhs = 2 * (1 - (1 - deficit) ** r) ** (1 / r)
    if distance > rhs + 1e-9:
        raise AssertionError(("stability", n, r, distance, rhs))


count = 0
for n in range(3, 11):
    # A full cycle is translation-transitive; a pair is reflection-transitive;
    # even residues in an even cycle are transitive under translations by 2.
    sets = [set(range(n)), {0, 1}]
    if n % 2 == 0:
        sets.append(set(range(0, n, 2)))
    for S in sets:
        for _ in range(35):
            f = [complex(RNG.uniform(-1, 1), RNG.uniform(-1, 1))
                 if j in S else 0j for j in range(n)]
            for r in (1.2, 1.5, 1.9, 2.0, 2.3, 3.0, 4.0, 8.0):
                verify(f, S, r)
                count += 1

# Analytically computed deficits of the two sharpness families.
for r in (1.2, 1.5, 1.9, 2.0, 2.5, 4.0, 8.0):
    for t in (0.05, 0.1, 0.2):
        if r > 2:
            deficit = 1 - (1 + t ** r) ** (-1 / r)
            distance = t / (1 + t ** r) ** (1 / r)
            if not (0.4 < distance / deficit ** (1 / r) < 3.5):
                raise AssertionError("superquadratic exponent witness")
        else:
            deficit = 1 - ((2 ** r + 2) /
                           (2 ** r + 2 * (1 + 3 * t * t) ** (r / 2))) ** (1 / r)
            f = [1 + t, 1 - t, 0]
            distance = lp(ft([t, -t, 0]), r) / lp(ft(f), r)
            if not (0.4 < distance / math.sqrt(deficit) < 3.5):
                raise AssertionError("subquadratic exponent witness")

print("PASS", count, "random inequality tests and 21 sharpness checks")
