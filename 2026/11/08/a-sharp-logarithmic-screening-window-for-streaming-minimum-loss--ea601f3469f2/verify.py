"""Exact finite-step checks for a two-target minimum-loss sampling model.

Run: python3 verify.py
Only Python's standard library is needed. The infinite-time statements in
RESULT.md are proved analytically, not by this finite checker.
"""
from fractions import Fraction
from itertools import product
from math import ceil, log

checks = 0


def exact_transition(beta, k, state):
    """Exhaustively enumerate fresh independent candidate labels (0 good; 1 bad)."""
    alpha = 1 - beta
    out_bad = Fraction(0)
    for picks in product((0, 1), repeat=k):
        bad_count = sum(picks)
        weight = alpha ** (k - bad_count) * beta ** bad_count
        if state == 0:
            chosen = 1 if bad_count == k else 0
        else:
            chosen = 0 if bad_count == 0 else 1
        out_bad += weight * chosen
    return out_bad


def step_bad_mass(beta, k, u):
    alpha = 1 - beta
    p, q = beta ** k, alpha ** k
    return (1 - u) * p + u * (1 - q)


for beta in (Fraction(1, 5), Fraction(1, 4), Fraction(1, 3), Fraction(2, 5)):
    alpha = 1 - beta
    for k in range(1, 9):
        p, q = beta ** k, alpha ** k
        assert exact_transition(beta, k, 0) == p
        checks += 1
        assert exact_transition(beta, k, 1) == 1 - q
        checks += 1
        assert p + q <= 1
        checks += 1
        pi = p / (p + q)
        assert step_bad_mass(beta, k, pi) == pi
        checks += 1
        for init in (Fraction(0), Fraction(1), Fraction(2, 7)):
            u = init
            for n in range(1, 8):
                u = step_bad_mass(beta, k, u)
                assert u == pi + (1 - p - q) ** n * (init - pi)
                checks += 1
    for ks in ((1, 2, 3, 4), (4, 1, 5, 2), (3, 3, 3, 3), (2, 5, 1, 6)):
        for init in (Fraction(0), Fraction(1)):
            # Independent forward propagation by the explicitly enumerated 2-by-2 transitions.
            v = [1-init, init]
            u = init
            for k in ks:
                row_0_bad = exact_transition(beta, k, 0)
                row_1_bad = exact_transition(beta, k, 1)
                w = [v[0]*(1-row_0_bad) + v[1]*(1-row_1_bad),
                     v[0]*row_0_bad + v[1]*row_1_bad]
                v = w
                u = step_bad_mass(beta, k, u)
                assert sum(v) == 1 and v[1] == u
                checks += 1

# The critical logarithmic slopes are strictly ordered when clean labels predominate.
for beta in (.05, .2, .35, .49):
    alpha = 1-beta
    low, high = 1 / log(1/beta), 1 / log(1/alpha)
    assert low < high
    checks += 1
    for c in (low*.75, low, (low+high)/2, high, high*1.25):
        k = [ceil(c*log(t+1)) for t in (1,2,10,100,10000)]
        assert all(z>=1 for z in k) and k == sorted(k)
        checks += 1
print('PASS:', checks, 'exact-rational and deterministic consistency checks')
