"""Exact, finite independent checks for birthday/coverage dependence.

Standard library only. No finite check is used to certify an all-size theorem.
"""
from collections import Counter
from fractions import Fraction as Q
from itertools import product
from math import factorial, sqrt, pi

checks = 0

def check(condition, context):
    global checks
    assert condition, context
    checks += 1

def H(n):
    return sum((Q(1, k) for k in range(1, n + 1)), Q(0))

def probability_first_repeat(n, t):
    return Q(factorial(n), factorial(n - t + 1)) * Q(t - 1, n ** t)

def finite_formula(n):
    surv = Q(1)
    inner = Q(0)
    out = Q(0)
    for j in range(2, n + 1):
        if j == 2:
            surv = Q(n - 1, n)
        else:
            surv *= Q(n - j + 1, n)
        inner += Q(j - 1, n - j + 1)
        out -= surv * inner
    return out

def conditional_formula(n):
    h = n * H(n)
    result = Q(0)
    probs = [probability_first_repeat(n, t) for t in range(2, n + 2)]
    check(sum(probs) == 1, ('mass', n))
    for t, p in enumerate(probs, 2):
        conditional_c = t + n * H(n - t + 1) if t <= n else n
        result += p * t * (conditional_c - h)
    check(sum(p * (t + n * H(n - t + 1) if t <= n else n)
              for t, p in enumerate(probs, 2)) == h, ('cover mean', n))
    return result

def prefix_enumeration_formula(n):
    """Independent enumeration of all n^(n+1) draw prefixes.

The first repeat is known by this prefix. If coverage has not happened,
complete it using a Markov expected-remaining-time recurrence.  This is
not the geometric covariance derivation.
    """
    L = n + 1
    states = Counter()
    for seq in product(range(n), repeat=L):
        seen = set()
        first_repeat = None
        first_cover = None
        for time, label in enumerate(seq, 1):
            if label in seen and first_repeat is None:
                first_repeat = time
            seen.add(label)
            if len(seen) == n and first_cover is None:
                first_cover = time
        assert first_repeat is not None
        states[first_repeat, first_cover, len(seen)] += 1
    E_T = Q(0); E_C = Q(0); E_TC = Q(0)
    for (t, cover, k), multiplicity in states.items():
        # For a Markov chain with k seen types, the expected extra
        # draws is n * (1/(n-k)+ ... + 1), derived independently
        # by first-step recursion for the distinct-count chain.
        future_mean = Q(0)
        if cover is None:
            for m in range(k, n):
                future_mean = Q(n, n - m) + future_mean
        c = cover if cover is not None else L + future_mean
        E_T += multiplicity * t
        E_C += multiplicity * c
        E_TC += multiplicity * t * c
    normalizer = n ** L
    return E_TC / normalizer - E_T * E_C / normalizer ** 2

for n in range(2, 120):
    v = finite_formula(n)
    check(v < 0, ('sign', n))
    check(v == conditional_formula(n), ('conditional identity', n))
for n in range(2, 7):
    check(prefix_enumeration_formula(n) == finite_formula(n), ('prefix exhaustive', n))

# All-time conditional first-order stochastic ordering: for 2 <= t < n
# the two coupled cover times differ by Geom((n-t+1)/n)-1 >= 0;
# at the last boundary they differ by Geom(1/n) >= 1. We additionally
# check the exact conditional means for finite n.
for n in range(2, 101):
    gm = [t + n * H(n - t + 1) for t in range(2, n + 1)] + [n]
    for i in range(len(gm) - 1):
        check(gm[i] > gm[i + 1], ('regression sign', n, i))

# Finite asymptotic diagnostics, not substitutes for the analytic limit.
limit = -sqrt(pi / 8)
for n in [100, 1000, 10000]:
    S = 1.0
    inner = 0.0
    cov = 0.0
    for j in range(2, n + 1):
        if j == 2:
            S = (n - 1) / n
        else:
            S *= (n - j + 1) / n
        inner += (j - 1) / (n - j + 1)
        cov -= S * inner
    check(abs(cov / sqrt(n) - limit) < 0.01, ('asymptotic diagnostic', n))
print('PASS:', checks, 'exact/finite assertions; all-size statements require the manuscript proof')
