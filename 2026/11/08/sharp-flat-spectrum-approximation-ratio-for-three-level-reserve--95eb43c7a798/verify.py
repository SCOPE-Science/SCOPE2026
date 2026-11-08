"""Exact arithmetic checks for a three-level singular-value bit allocator.

The checks corroborate, but do not replace, the general proof.
Run: python verify.py
No external dependencies.
"""

from fractions import Fraction as F
from itertools import combinations_with_replacement

checks = 0


def check(condition, context):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(context)


def coefficient(bits):
    q = 2 ** (bits - 1) - 1
    return F(1, q) + F(1, 4 * q * q)


def source_greedy(rank, widths, average_budget):
    """Direct transcription of the reserve test for unit singular values."""
    c = [coefficient(w) for w in widths]
    budget = rank * average_budget
    if rank * c[-1] > budget:
        return None
    remainder = budget
    remaining = rank
    counts = [0] * len(widths)
    for level in range(len(widths) - 1):
        used = F(0)
        while remaining and used + c[level] + c[-1] * (remaining - 1) <= remainder:
            used += c[level]
            remaining -= 1
            counts[level] += 1
        remainder -= used
    counts[-1] = remaining
    stored = sum(w * n for w, n in zip(widths, counts))
    error = sum(ci * n for ci, n in zip(c, counts))
    check(error <= budget, (rank, widths, average_budget, counts))
    return tuple(counts), stored


def closed_greedy(rank, widths, average_budget):
    lo, mi, hi = widths
    a, b, h = map(coefficient, widths)
    if not (h <= average_budget <= a):
        raise ValueError("average budget outside feasible nontrivial domain")
    nlo = min(rank, (rank * (average_budget - h)) // (a - h))
    slack = rank * (average_budget - h) - nlo * (a - h)
    nmi = min(rank - nlo, slack // (b - h))
    nhi = rank - nlo - nmi
    return (nlo, nmi, nhi), lo * nlo + mi * nmi + hi * nhi


def continuous_optimum(widths, e):
    lo, mi, hi = widths
    a, b, h = map(coefficient, widths)
    if h <= e <= b:
        return hi - F(hi - mi) * (e - h) / (b - h)
    if b <= e <= a:
        return mi - F(mi - lo) * (e - b) / (a - b)
    raise ValueError(e)


def continuous_greedy(widths, e):
    lo, _, hi = widths
    a, _, h = map(coefficient, widths)
    return hi - F(hi - lo) * (e - h) / (a - h)


def critical_ratio(widths):
    _, mi, _ = widths
    b = coefficient(mi)
    return continuous_greedy(widths, b) / mi


def brute_optimum(rank, widths, budget):
    result = None
    for nl in range(rank + 1):
        for nm in range(rank - nl + 1):
            nh = rank - nl - nm
            err = sum(n * coefficient(w) for n, w in zip((nl, nm, nh), widths))
            if err <= budget:
                stored = sum(n * w for n, w in zip((nl, nm, nh), widths))
                if result is None or stored < result:
                    result = stored
    return result


def run():
    palettes = [(2, 4, 8), (4, 8, 16), (6, 10, 32), (8, 12, 32)]
    for widths in palettes:
        lo, mi, hi = widths
        a, b, h = map(coefficient, widths)
        check(a > b > h > 0, widths)
        check(F(mi - lo, a - b) < F(hi - mi, b - h), (widths, 'convexity slope'))
        check(critical_ratio(widths) > 1, widths)
        for rank in range(1, 13):
            critical = source_greedy(rank, widths, b)
            closed = closed_greedy(rank, widths, b)
            check(critical == closed, ('critical', rank, widths, critical, closed))
            check(brute_optimum(rank, widths, rank * b) == rank * mi, ('critical optimum', rank, widths))
            for nl in range(rank + 1):
                for nm in range(rank - nl + 1):
                    nh = rank - nl - nm
                    e = (nl * a + nm * b + nh * h) / rank
                    direct = source_greedy(rank, widths, e)
                    closed = closed_greedy(rank, widths, e)
                    check(direct == closed, ('formula', rank, widths, e, direct, closed))
                    opt = brute_optimum(rank, widths, rank * e)
                    check(direct[1] >= opt, ('optimality', rank, widths, e))
                    check(rank * continuous_optimum(widths, e) <= opt, ('LP lower', rank, widths, e))
                    check(opt <= rank * continuous_optimum(widths, e) + (hi - lo), ('LP rounding', rank, widths, e))
                    check(direct[1] <= rank * continuous_greedy(widths, e) + (hi - lo), ('greedy error', rank, widths, e))
                    check(direct[1] >= rank * continuous_greedy(widths, e) - (hi - lo) * (1 + (a - h) / (b - h)), ('greedy bound', rank, widths, e))
            for i in range(101):
                e = h + F(i, 100) * (a - h)
                ratio = continuous_greedy(widths, e) / continuous_optimum(widths, e)
                check(1 <= ratio <= critical_ratio(widths), ('envelope', widths, i))
    # A concrete flat-spectrum family with a small blockwise relative certificate.
    widths = (8, 12, 32)
    rank = 64
    e = coefficient(12)
    counts, payload = source_greedy(rank, widths, e)
    check(counts == (3, 15, 46), (widths, counts))
    check(payload == 1676, payload)
    check(brute_optimum(rank, widths, rank * e) == 768, ('exact optimum rank 64'))
    check(F(payload, 768) == F(419, 192), ('exact ratio rank 64'))
    check(F(rank) * e < F(1, 20), ('relative budget < 5%'))
    # Exact rational H=8 anchor.
    check(critical_ratio((2, 4, 8)) == F(33283, 18179), 'anchor ratio')
    print('PASS', checks, 'exact-rational checks')
    print('palette=(8,12,32) rank=64: counts=', counts, 'payload=', payload,
          'optimal=768', 'ratio=', F(payload, 768))
    print('limiting flat-spectrum worst-budget ratio=', float(critical_ratio(widths)))
    print('relative budget for orthogonal flat block=', float(rank * e))


if __name__ == '__main__':
    run()
