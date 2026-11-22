#!/usr/bin/env python3
"""Reproducible finite checks for the displaced-target elephant-walk theorem.

Exact finite calculations are checks of algebra, not proofs of an infinite limit.
The continuous expected-range calculations below are Monte Carlo diagnostics only.
"""
from fractions import Fraction
from math import sqrt, pi
from random import Random

A = Fraction(3, 4)
checks = 0


def verify(condition):
    global checks
    if not condition:
        raise AssertionError(f"Check {checks + 1} failed")
    checks += 1


def transition(m, x):
    plus = (1 + A * Fraction(x, m)) / 2
    minus = 1 - plus
    return plus, minus


def hitting_dp(n, x, target, steps):
    """Probability of hitting target at one of the times n through n+steps."""
    if x == target:
        return Fraction(1)
    alive = {x: Fraction(1)}
    success = Fraction(0)
    for m in range(n, n + steps):
        nxt = {}
        for state, probability in alive.items():
            pp, pm = transition(m, state)
            for s, edge_probability in ((state + 1, pp), (state - 1, pm)):
                mass = probability * edge_probability
                if s == target:
                    success += mass
                else:
                    nxt[s] = nxt.get(s, Fraction(0)) + mass
        alive = nxt
    return success


def hitting_enumerate(n, x, target, steps):
    """Independent complete enumeration of a finite path tree."""
    def rec(m, state, left):
        if state == target:
            return Fraction(1)
        if left == 0:
            return Fraction(0)
        pp, pm = transition(m, state)
        return pp * rec(m + 1, state + 1, left - 1) + pm * rec(m + 1, state - 1, left - 1)
    return rec(n, x, steps)


for n in range(2, 12):
    for x in range(-n, n + 1, 2):
        pp, pm = transition(n, x)
        verify(Fraction(0) < pp < Fraction(1) and Fraction(0) < pm < Fraction(1))
        verify(pp + pm == 1)
        verify(pp * (x + 1) + pm * (x - 1) == (1 + A / n) * x)
        verify(pp * (x + 1) ** 2 + pm * (x - 1) ** 2 == (1 + 2 * A / n) * x*x + 1)
        # R_(n,n+1) = n/(n+a), so the discounted next-step mean is x.
        verify(Fraction(n, 1) * (pp * (x + 1) + pm * (x - 1)) / (n + A) == x)

for n in range(2, 9):
    for x in range(-n, n + 1, 2):
        for target in range(-4, 5):
            for steps in range(0, 7):
                verify(hitting_dp(n, x, target, steps) == hitting_enumerate(n, x, target, steps))


def osc(seq):
    return max(seq) - min(seq)

# Exact deterministic range inequalities, tested over rational sequences.
for path in (
    [Fraction(0), Fraction(1), Fraction(-1), Fraction(2)],
    [Fraction(0), Fraction(-2), Fraction(3), Fraction(-1)],
    [Fraction(0), Fraction(1, 3), Fraction(2, 3), Fraction(1)],
):
    boundary = [Fraction(1), Fraction(2, 3), Fraction(1, 3), Fraction(0)]
    for c in range(-8, 9):
        shifted = [x - c * b for x, b in zip(path, boundary)]
        verify(abs(osc(shifted) - abs(c)) <= osc(path))
        verify(abs(osc(shifted) - osc(path)) <= abs(c))
        flipped = [x + c * b for x, b in zip(path, boundary)]
        verify(osc(shifted) + osc(flipped) >= 2 * osc(path))

# Seeded numerical sanity checks; NOT infinite-dimensional certificates.
rng = Random(271828)
a = 0.75
delta = 2 * a - 1
v = 1 / delta
steps = 512
samples = 2400
bound = [(1 - j / steps) ** (a / delta) for j in range(steps + 1)]
cs = (0.0, 1.0, 3.0)
sums = [0.0] * len(cs)
for _ in range(samples):
    b = [0.0]
    for j in range(steps):
        b.append(b[-1] + rng.gauss(0.0, sqrt(v / steps)))
    for i, c in enumerate(cs):
        shifted = [x - c*g for x, g in zip(b, bound)]
        sums[i] += osc(shifted)
means = [s / samples for s in sums]
verify(abs(means[0] - sqrt(8 * v / pi)) < 0.17)
verify(means[2] > means[0])
verify(means[2] >= 3.0 - 0.17)  # diagnostic tolerance, not a formal bound
print(f"Exact checks: {checks - 3}; seeded finite-grid diagnostics: 3; all passed")
print("Brownian-grid range means at c=0,1,3:", *(f"{m:.6f}" for m in means))
print("Analytic value at c=0:", f"{sqrt(8*v/pi):.6f}")
print("No Monte Carlo estimate was used to prove the theorem.")
