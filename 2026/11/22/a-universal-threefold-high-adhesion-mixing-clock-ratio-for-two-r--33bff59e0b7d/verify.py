"""Exact finite-deck checks for a two-interleaver rare-bond limit.

Uses only the Python standard library. Finite checks are diagnostics,
not a proof of arbitrary-deck or infinite-time statements.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import permutations
from math import comb, factorial, exp


def rotations(n):
    return {tuple(range(k + 1, n + 1)) + tuple(range(1, k + 1)) for k in range(n)}


def first_order(n):
    subgroup = rotations(n)
    b, i = defaultdict(Fraction), defaultdict(Fraction)
    events = 0
    for k in range(1, n):
        cut_weight = Fraction(comb(n, k), 2 ** n)
        for left in (True, False):
            base = tuple(range(1, k + 1)) if left else tuple(range(k + 1, n + 1))
            other = tuple(range(k + 1, n + 1)) if left else tuple(range(1, k + 1))
            for j in range(1, len(base)):
                first, last = base[:j], base[j:]
                # Exact block midpoint keys from packet positions 1..len(base).
                early_key = Fraction(j, 2 * len(base))
                late_key = Fraction(len(base) + j, 2 * len(base))
                assert early_key < Fraction(1, 2) < late_key
                outside = first + other + last
                inside_1 = first + last + other
                inside_2 = other + first + last
                assert outside not in subgroup
                assert inside_1 in subgroup and inside_2 in subgroup
                b[outside] += cut_weight / 3
                b[inside_1] += cut_weight / 3
                b[inside_2] += cut_weight / 3
                i[outside] += cut_weight
                events += 1
    assert events == (n - 1) * (n - 2)
    for g in set(b) | set(i):
        if g not in subgroup:
            assert i[g] == 3 * b[g]
    off_b = {g: weight for g, weight in b.items() if g not in subgroup}
    off_i = {g: weight for g, weight in i.items() if g not in subgroup}
    lam_b = sum(off_b.values(), Fraction(0))
    lam_i = sum(off_i.values(), Fraction(0))
    assert lam_b == Fraction((n - 2) * (2 ** n - 2), 3 * 2 ** n)
    assert lam_i == 3 * lam_b
    return off_b, off_i, lam_b


def multiply(x, y):
    return tuple(x[t - 1] for t in y)


def coset_rep(g, h_group):
    return min(multiply(g, h) for h in h_group)


def exact_quotient(n):
    h_group = sorted(rotations(n))
    b, i, total = first_order(n)
    reps = sorted({coset_rep(g, h_group) for g in permutations(range(1, n + 1))})
    ix = {g: j for j, g in enumerate(reps)}
    identity = tuple(range(1, n + 1))
    assert len(reps) == factorial(n - 1)
    rows = []
    for g0 in reps:
        row = defaultdict(Fraction)
        for h in h_group:
            for g1, rate in b.items():
                row[ix[coset_rep(multiply(multiply(g0, h), g1), h_group)]] += rate / n
        assert ix[g0] not in row
        assert sum(row.values(), Fraction(0)) == total
        rows.append(dict(row))
    for j in range(len(reps)):
        assert sum((row.get(j, Fraction(0)) for row in rows), Fraction(0)) == total
    reachable = {ix[coset_rep(identity, h_group)]}
    while True:
        nxt = reachable | {j for k in reachable for j in rows[k]}
        if nxt == reachable:
            break
        reachable = nxt
    assert len(reachable) == len(reps)
    return rows, total, ix[coset_rep(identity, h_group)]


def tv_profile(rows, rate, start, time):
    # Poisson uniformization of a continuous-time Markov generator.
    size = len(rows)
    transition = [[(j, float(w / rate)) for j, w in row.items()] for row in rows]
    v = [0.0] * size
    v[start] = 1.0
    poisson = exp(-float(rate) * time)
    acc = [poisson * x for x in v]
    for steps in range(1, 160):
        new = [0.0] * size
        for j, m in enumerate(v):
            if m:
                for k, prob in transition[j]:
                    new[k] += m * prob
        v = new
        poisson *= float(rate) * time / steps
        acc = [x + poisson * y for x, y in zip(acc, v)]
        if steps >= 40 and poisson < 1.e-17:
            break
    assert abs(sum(acc) - 1.0) < 1.e-11
    return 0.5 * sum(abs(x - 1.0 / size) for x in acc)


def main():
    total_assertions = 0
    for n in range(4, 9):
        b, i, rate = first_order(n)
        assert len(b) > 0 and len(b) == len(i)
        print('single-bond', n, 'off-rotation rate B=', rate, 'I=', 3 * rate,
              'support=', len(b))
        total_assertions += (n - 1) * (n - 2) + len(b) + 3
    for n in (5, 6):
        rows, rate, start = exact_quotient(n)
        for t in (0.2, 0.8, 2.0):
            d0 = tv_profile(rows, rate, start, t)
            d1 = tv_profile(rows, rate, start, 3.0 * t)
            assert 0.0 < d1 < d0 < 1.0
            print('quotient', n, 't=', t, 'TV_B=', round(d0, 12),
                  'TV_I_limit=', round(d1, 12))
        total_assertions += 2 * len(rows) + 7
    print('PASS; indicative asserted structural cases:', total_assertions)


if __name__ == '__main__':
    main()
