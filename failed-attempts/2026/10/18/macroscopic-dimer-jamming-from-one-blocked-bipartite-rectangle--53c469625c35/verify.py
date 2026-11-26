"""Reproducible finite checks for blocked-biclique random dimer adsorption.

Python 3 standard library; run with `python verify.py`.
"""
from functools import lru_cache
from fractions import Fraction
from itertools import permutations
from math import exp, log
from random import Random


def asymptotic_vacancy_fraction(alpha, beta):
    assert 0 < alpha < 1 and 0 < beta < 1
    s = 1.0 / alpha if abs(alpha - beta) < 1e-14 else log(beta / alpha) / (beta - alpha)
    return alpha * exp(-(1.0 - beta) * s)


@lru_cache(maxsize=None)
def exact_terminal_distribution(a, b, c, d):
    """Probability map for the number of unmatched left-side vertices."""
    assert a >= 0 and b >= 0 and c >= 0 and d >= 0 and a + b == c + d
    weights = (a * d, b * c, b * d)
    denominator = sum(weights)
    if not denominator:
        return {a + b: Fraction(1)}
    targets = ((a - 1, b, c, d - 1),
               (a, b - 1, c - 1, d),
               (a, b - 1, c, d - 1))
    out = {}
    for w, state in zip(weights, targets):
        if w:
            for k, p in exact_terminal_distribution(*state).items():
                out[k] = out.get(k, Fraction(0)) + Fraction(w, denominator) * p
    assert sum(out.values()) == 1
    return out


def direct_order_distribution(vertices_on_each_side, forbidden_edges):
    """Enumerate every priority order on a small labelled bipartite graph."""
    n = vertices_on_each_side
    edges = [(i, j + n) for i in range(n) for j in range(n)
             if (i, j) not in forbidden_edges]
    outcomes = {}
    count = 0
    for ordered_edges in permutations(edges):
        matched = set()
        for x, y in ordered_edges:
            if x not in matched and y not in matched:
                matched.add(x)
                matched.add(y)
        remaining = n - sum(x in matched for x in range(n))
        outcomes[remaining] = outcomes.get(remaining, 0) + 1
        count += 1
    return {k: Fraction(v, count) for k, v in outcomes.items()}


def simulate(a, b, c, d, rng):
    """Independently sample a uniform surviving edge after each accepted match."""
    while (total := a * d + b * c + b * d) > 0:
        r = rng.randrange(total)
        if r < a * d:
            a -= 1
            d -= 1
        elif r < a * d + b * c:
            b -= 1
            c -= 1
        else:
            b -= 1
            d -= 1
    return a + b


def run_checks():
    direct = direct_order_distribution(2, {(0, 0)})
    expected = {0: Fraction(2, 3), 1: Fraction(1, 3)}
    assert direct == expected
    assert exact_terminal_distribution(1, 1, 1, 1) == expected
    assert exact_terminal_distribution(2, 2, 2, 2) == {
        0: Fraction(22, 63), 1: Fraction(184, 315), 2: Fraction(1, 15)
    }
    assert exact_terminal_distribution(1, 2, 1, 2) == {
        0: Fraction(5, 6), 1: Fraction(1, 6)
    }
    for n in range(2, 8):
        for a in range(1, n):
            for c in range(1, n):
                dist = exact_terminal_distribution(a, n - a, c, n - c)
                assert sum(dist.values()) == 1
                assert dist == exact_terminal_distribution(c, n - c, a, n - a)
                assert all(0 <= k <= min(a, c) for k in dist)
    for alpha, beta in [(0.4, 0.4), (0.3, 0.4), (0.2, 0.6)]:
        observed = asymptotic_vacancy_fraction(alpha, beta)
        reverse = asymptotic_vacancy_fraction(beta, alpha)
        assert abs(observed - reverse) < 2e-15
        n = 2000
        a, c = round(alpha * n), round(beta * n)
        rng = Random(451001 + a + 37 * c)
        trials = 2000
        empirical = sum(simulate(a, n-a, c, n-c, rng) for _ in range(trials)) / (n * trials)
        assert abs(empirical - observed) < 0.008, (alpha, beta, empirical, observed)
        print(f"(alpha,beta)=({alpha},{beta}) predicted={observed:.10f} simulated={empirical:.10f}")
    print('Exact rational recurrences, literal edge-order comparison, and simulations: PASS')


if __name__ == '__main__':
    run_checks()
