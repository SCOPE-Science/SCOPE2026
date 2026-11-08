"""Exact independent checks for iid species-accumulation variance peaks.

Run: python3 checker.py
Only Python standard library is used.
"""
from fractions import Fraction
from itertools import combinations
from math import exp, log, log1p, expm1


def variance_identity(probs, n):
    q = [1 - x for x in probs]
    ans = sum((x ** n - x ** (2 * n) for x in q), Fraction(0))
    ans += 2 * sum(
        ((1 - probs[i] - probs[j]) ** n - (q[i] * q[j]) ** n
         for i, j in combinations(range(len(probs)), 2)),
        Fraction(0),
    )
    return ans


def variance_subset_dp(probs, n):
    # Independent calculation: probabilities for subsets of seen species.
    distribution = {0: Fraction(1)}
    for _ in range(n):
        nxt = {}
        for mask, prob in distribution.items():
            for i, q in enumerate(probs):
                new_mask = mask | (1 << i)
                nxt[new_mask] = nxt.get(new_mask, Fraction(0)) + prob * q
        distribution = nxt
    assert sum(distribution.values()) == 1
    mean = sum((prob * mask.bit_count() for mask, prob in distribution.items()), Fraction(0))
    second = sum((prob * mask.bit_count() ** 2 for mask, prob in distribution.items()), Fraction(0))
    return second - mean * mean


def stable_float_variance(probs, n):
    logs = [log1p(-x) for x in probs]
    unobserved = [exp(n * x) for x in logs]
    v = sum(x * (1 - x) for x in unobserved)
    for i, j in combinations(range(len(probs)), 2):
        ab = log1p(-probs[i] - probs[j])
        v += 2 * exp(n * (logs[i] + logs[j])) * expm1(n * (ab - logs[i] - logs[j]))
    return v


def main():
    p = [Fraction(7, 15), Fraction(7, 15), Fraction(1, 15)]
    for n in range(1, 12):
        assert variance_identity(p, n) == variance_subset_dp(p, n)
    assert variance_identity(p, 3) - variance_identity(p, 2) == Fraction(38864, 1265625)
    assert variance_identity(p, 3) - variance_identity(p, 4) == Fraction(4074196, 284765625)
    assert variance_identity(p, 9) - variance_identity(p, 8) == Fraction(7455903885441788, 6568408355712890625)
    assert variance_identity(p, 9) - variance_identity(p, 10) == Fraction(10874721037204676764, 36947297000885009765625)
    for n in (3, 9):
        assert variance_identity(p, n) > variance_identity(p, n - 1)
        assert variance_identity(p, n) > variance_identity(p, n + 1)

    # Exact moment checks on additional independently selected rational vectors.
    extra = [
        [Fraction(1, 2), Fraction(1, 3), Fraction(1, 6)],
        [Fraction(4, 5), Fraction(1, 10), Fraction(1, 10)],
        [Fraction(1, 4)] * 4,
        [Fraction(5, 8), Fraction(1, 8), Fraction(1, 8), Fraction(1, 8)],
    ]
    for q in extra:
        for n in range(1, 12):
            assert variance_identity(q, n) == variance_subset_dp(q, n)

    # A finite illustration of the asymptotic analytic construction, not its proof.
    e = 1 / 1000
    q = [1 - e - e ** 2 - e ** 3, e, e ** 2, e ** 3]
    highs = [round(log(2) / e ** j) for j in (1, 2, 3)]
    lows = [round(e ** (-j - 0.5)) for j in (1, 2, 3)]
    assert all(hi < lo for hi, lo in zip(highs, lows))
    assert all(stable_float_variance(q, n) > 0.24 for n in highs)
    assert all(stable_float_variance(q, n) < 0.04 for n in lows)
    print("PASS: 55 independent exact dynamic-program comparisons; four exact three-species peak inequalities; multiscale numerical illustration")


if __name__ == "__main__":
    main()
