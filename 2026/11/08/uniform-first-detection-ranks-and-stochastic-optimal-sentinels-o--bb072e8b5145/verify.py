#!/usr/bin/env python3
"""Exact finite checks of the ring SI sentinel first-detection theorem.

Uses only the Python standard library. No random simulations, PDFs, network,
or external files are required. Finite checks support, but do not replace,
the universal proof given in RESULT.md.
"""
from fractions import Fraction
from functools import lru_cache
from itertools import combinations, product
from math import comb, factorial

checks = 0

def check(condition, reason):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(reason)

def gaps(n, sensors):
    ss = tuple(sorted(sensors))
    return tuple((ss[(i+1) % len(ss)] - ss[i]) % n or n
                 for i in range(len(ss)))

def tail_coefficient_from_gaps(n, g, m):
    return Fraction(sum(max(x - m - 1, 0) for x in g), n)

def markov_event_tails(n, sensors):
    """Independent direct SI frontier enumeration at each infection event.

    Infection chooses one of the currently active SI oriented boundary edges
    uniformly, and first infection of a sensor is absorbing. Every active
    pre-detection state has exactly two oriented SI edges on the cycle.
    """
    sensor_mask = sum(1 << j for j in sensors)
    mass = {1 << j: Fraction(1, n) for j in range(n)
            if not (sensor_mask & (1 << j))}
    out = []
    for m in range(n + 1):
        out.append(sum(mass.values(), Fraction(0)))
        nxt = {}
        for mask, probability in mass.items():
            edges = []
            for v in range(n):
                if mask & (1 << v):
                    for nb in ((v-1) % n, (v+1) % n):
                        if not (mask & (1 << nb)):
                            edges.append(nb)
            check(len(edges) == 2, ('two-frontier', n, sensors, mask, edges))
            for nb in edges:
                if not (sensor_mask & (1 << nb)):
                    new = mask | (1 << nb)
                    nxt[new] = nxt.get(new, Fraction(0)) + probability / 2
        mass = nxt
    return out

def direct_expected_time(n, sensors):
    sensor_mask = sum(1 << j for j in sensors)
    @lru_cache(None)
    def moment(mask):
        if mask & sensor_mask:
            return Fraction(0)
        counts = {}
        for v in range(n):
            if mask & (1 << v):
                for nb in ((v-1) % n, (v+1) % n):
                    if not (mask & (1 << nb)):
                        counts[nb] = counts.get(nb, 0) + 1
        total = sum(counts.values())
        check(total == 2, ('CTMC-degree', n, sensors, mask, counts))
        # lambda=1: E=tau + expected residual after next infection.
        return (Fraction(1) + sum((count * moment(mask | (1 << nb))
                                   for nb, count in counts.items()), Fraction(0))) / total
    return sum((moment(1 << j) for j in range(n)), Fraction(0)) / n

# 1. Conditional uniform event ranks, even after every possible finite
#    string of L/R transmission directions. This is stronger than a sample.
for L in range(2, 13):
    for seq in product((0, 1), repeat=L - 1):
        ranks = []
        for j in range(1, L):
            left = right = 0
            for step, d in enumerate(seq, 1):
                if d == 0:
                    left += 1
                else:
                    right += 1
                if left == j or right == L - j:
                    ranks.append(step)
                    break
            else:
                raise AssertionError(('no absorption', L, seq, j))
        check(sorted(ranks) == list(range(1, L)), ('uniform rank', L, seq, ranks))

# 2. Independent, rational, state-by-state SI Markov chain event enumeration,
#    with sensor absorption and duplicate edge multiplicities exactly retained.
for n in range(3, 10):
    for k in range(1, n + 1):
        for sensors in combinations(range(n), k):
            g = gaps(n, sensors)
            markov = markov_event_tails(n, sensors)
            for m, a in enumerate(markov):
                check(a == tail_coefficient_from_gaps(n, g, m),
                      ('event tail', n, sensors, g, m, a))
            expect = sum(markov, Fraction(0)) / 2
            theorem = Fraction(sum(L * (L - 1) for L in g), 4 * n)
            check(expect == theorem, ('mean via event tails', n, sensors, expect, theorem))
            if n <= 8:
                direct = direct_expected_time(n, sensors)
                check(direct == theorem, ('generator mean', n, sensors, direct, theorem))

# 3. Exact finite global order in infection event counts, all placements
#    at all attainable m, balanced best and adjacent worst.
for n in range(3, 11):
    for k in range(1, n + 1):
        q, r = divmod(n, k)
        best = (q,) * (k - r) + (q + 1,) * r
        worst = (n - k + 1,) + (1,) * (k - 1)
        for sensors in combinations(range(n), k):
            g = gaps(n, sensors)
            for m in range(n + 1):
                b = tail_coefficient_from_gaps(n, best, m)
                s = tail_coefficient_from_gaps(n, g, m)
                w = tail_coefficient_from_gaps(n, worst, m)
                check(b <= s <= w,
                      ('optimal rank-tail bracket', n, k, sensors, m, b, s, w))
            if sorted(g) != sorted(best):
                check(any(tail_coefficient_from_gaps(n, best, m) <
                          tail_coefficient_from_gaps(n, g, m)
                          for m in range(n + 1)),
                      ('strict lower', n, k, sensors))
            if sorted(g) != sorted(worst):
                check(any(tail_coefficient_from_gaps(n, g, m) <
                          tail_coefficient_from_gaps(n, worst, m)
                          for m in range(n + 1)),
                      ('strict upper', n, k, sensors))

# 4. Formal power-series discrete curvature identity; no floating point.
# Coefficients of h_L(s)*exp(2s) in powers of s.
def coeff(L, m):
    return Fraction((L - m - 1) * (2 ** m), factorial(m)) if 0 <= m <= L - 2 else Fraction(0)
for L in range(2, 26):
    for m in range(0, L + 3):
        left = coeff(L + 1, m) - 2 * coeff(L, m) + coeff(L - 1, m)
        right = Fraction(2 ** (L - 1), factorial(L - 1)) if m == L - 1 else Fraction(0)
        check(left == right, ('Poisson discrete curvature', L, m, left, right))

# 5. Concrete example: n=12,k=3, lambda=1.
check(Fraction(sum(x*(x-1) for x in (4,4,4)), 48) == Fraction(3,4), 'balanced example')
check(Fraction(sum(x*(x-1) for x in (10,1,1)), 48) == Fraction(15,8), 'clustered example')
print('PASS:', checks, 'exact checks, including independent frontier enumeration and CTMC means')
