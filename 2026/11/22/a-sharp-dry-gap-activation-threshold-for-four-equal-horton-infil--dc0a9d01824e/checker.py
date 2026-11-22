#!/usr/bin/env python3
"""Reproduce supplementary algebraic and numerical checks of the four-burst gap theorem.
The analytic proof, not sampling, establishes the theorem for all admissible inputs.
Requires Python 3 standard library only.
"""
import math
import random
from fractions import Fraction as F


def infiltration(wet, dry, k, r, fmin, fmax):
    """Direct independent wet/dry state update, with saturated wet pulses."""
    y = 1.0
    total = 0.0
    for i, width in enumerate(wet):
        a = math.exp(-k * width)
        total += fmin * width + (fmax - fmin) * y * (1 - a) / k
        y *= a
        if i < len(dry):
            y = 1 - (1 - y) * math.exp(-r * dry[i])
    return total


def expanded(wet, dry, k, r, fmin, fmax):
    """Independent pairwise deficit expansion of cumulative infiltration."""
    aa = [math.exp(-k * width) for width in wet]
    uu = [1 - x for x in aa]
    loss = 0.0
    for i in range(len(wet)):
        for j in range(i + 1, len(wet)):
            coefficient = uu[i] * uu[j]
            for middle in range(i + 1, j):
                coefficient *= aa[middle]
            loss += coefficient * math.exp(-r * sum(dry[i:j]))
    return fmin * sum(wet) + (fmax - fmin) / k * (sum(uu) - loss)


def optimum(w, D, k, r):
    a = math.exp(-k * w)
    Dc = math.log1p(a) / r
    if D <= Dc:
        return 0.0, D, 0.0
    lo, hi = 0.0, D / 2
    # At the interior optimum t^2(t+a)=exp(rD), t=exp(rx).
    for _ in range(105):
        x = (lo + hi) / 2
        lhs = 3 * x + math.log1p(a * math.exp(-r * x)) / r
        if lhs < D:
            lo = x
        else:
            hi = x
    x = (lo + hi) / 2
    return x, D - 2 * x, x


def main():
    checks = 0
    rng = random.Random(492817)
    # Fully exact rational identities after replacing exponentials by multipliers.
    for _ in range(2400):
        a = F(rng.randint(1, 9), 10)
        q = [F(rng.randint(1, 9), 10) for _ in range(3)]
        u = 1 - a
        starts = [F(1)]
        for z in q:
            starts.append(1 - (1 - a * starts[-1]) * z)
        direct = u * sum(starts)
        gap_loss = (q[0] + q[1] + q[2] + a * q[0] * q[1]
                    + a * q[1] * q[2] + a * a * q[0] * q[1] * q[2])
        algebraic = 4 * u - u * u * gap_loss
        assert direct == algebraic
        checks += 1
    for count in (2, 3, 4, 5, 7):
        for _ in range(120):
            wet = [rng.uniform(0.03, 2.5) for _ in range(count)]
            dry = [rng.uniform(0, 2) for _ in range(count - 1)]
            k = rng.uniform(.2, 2.5)
            r = rng.uniform(.2, 2.5)
            fmin = rng.uniform(0, 3)
            fmax = fmin + rng.uniform(.1, 4)
            lhs = infiltration(wet, dry, k, r, fmin, fmax)
            rhs = expanded(wet, dry, k, r, fmin, fmax)
            assert abs(lhs - rhs) < 1e-9 * max(1, abs(lhs))
            checks += 1
    for _ in range(300):
        w = rng.uniform(.05, 3)
        k = rng.uniform(.25, 4)
        r = rng.uniform(.25, 4)
        a = math.exp(-k * w)
        Dc = math.log1p(a) / r
        D = Dc * rng.uniform(.05, 5)
        best = optimum(w, D, k, r)
        value = infiltration([w] * 4, best, k, r, .2, 5)
        for _ in range(160):
            d1 = rng.random() * D
            d2 = rng.random() * (D - d1)
            d3 = D - d1 - d2
            trial = infiltration([w] * 4, (d1, d2, d3), k, r, .2, 5)
            assert value + 5e-10 >= trial
            checks += 1
        if D > Dc:
            x = best[0]
            assert x > 0 and best[1] > x
            assert abs((3*x + math.log1p(a * math.exp(-r*x))/r) - D) < 2e-12 * max(1,D)
            checks += 2
        else:
            assert best[0] == 0
        checks += 1
    for D in (.2, .5, 1.0, 3.0):
        print(f"w=k=r=1, D={D:.4f}, gaps={optimum(1,D,1,1)}")
    print(f"supplementary checks passed: {checks}")

if __name__ == '__main__':
    main()
