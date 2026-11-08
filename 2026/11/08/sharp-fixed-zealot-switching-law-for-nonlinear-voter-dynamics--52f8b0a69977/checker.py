"""Self-contained finite-size checks of the stated symmetric two-zealot q-voter theorem.

The exact infinite-population asymptotic is proved in RESULT.md, not by these tests.
Run: python3 checker.py
"""
from fractions import Fraction
from math import comb, lgamma, log, exp, pi, sqrt


def rates(s, q):
    c = (s + 2) * (s + 1) ** q
    up = [Fraction((s - k) * (k + 1) ** q, c) for k in range(s + 1)]
    down = [Fraction(k * (s - k + 1) ** q, c) for k in range(s + 1)]
    return up, down


def hitting_formula(s, q):
    c = (s + 2) * (s + 1) ** q
    h = Fraction(0)
    total = Fraction(0)
    for k in range(s):
        h += Fraction(1, comb(s, k) ** (q - 1))
        total += h * Fraction(comb(s, k) ** (q - 1), (s - k) * (k + 1) ** q)
    return c * total


def linear_system_hitting(s, q):
    """Solve the raw absorbing-chain generator equations, independently of the sum formula."""
    up, down = rates(s, q)
    a = [[Fraction(0) for _ in range(s + 1)] for __ in range(s)]
    for k in range(s):
        a[k][k] = up[k] + down[k]
        if k: a[k][k - 1] = -down[k]
        if k + 1 < s: a[k][k + 1] = -up[k]
        a[k][s] = Fraction(1)
    for i in range(s):
        pivot = next(j for j in range(i, s) if a[j][i])
        a[pivot], a[i] = a[i], a[pivot]
        p = a[i][i]
        for k in range(i, s + 1): a[i][k] /= p
        for j in range(s):
            if j == i: continue
            mult = a[j][i]
            if not mult: continue
            for k in range(i, s + 1): a[j][k] -= mult * a[i][k]
    return a[0][s]


def log_scaled_asymptotic_ratio(s, q):
    """Stable float evaluation of exact finite sum divided by claimed asymptote."""
    r = q - 1
    log2 = log(2)
    c = (s + 2) * (s + 1) ** q
    summation = 0.0
    h = 1.0
    for k in range(s):
        if k: h += comb(s, k) ** (-r)
        logbin = lgamma(s + 1) - lgamma(k + 1) - lgamma(s - k + 1)
        summation += exp(r * (logbin - s * log2) - log(s - k) - q * log(k + 1)) * h
    observed = c * summation * s ** ((q - 2) / 2)
    predicted = 2 ** (q + 1) * (2 / pi) ** ((q - 2) / 2) / sqrt(q - 1)
    return observed / predicted


def main():
    checks = 0
    for q in range(2, 6):
        for s in range(2, 11):
            up, down = rates(s, q)
            for k in range(s):
                ratio = Fraction(comb(s, k), comb(s, k + 1)) ** (q - 1)
                assert up[k] / down[k + 1] == ratio
                checks += 1
            assert hitting_formula(s, q) == linear_system_hitting(s, q)
            checks += 1
    for q in (2, 3, 4, 5):
        vals = [log_scaled_asymptotic_ratio(s, q) for s in (30, 60, 120, 240)]
        assert 0.7 < vals[-1] < 1.06
        assert abs(vals[-1] - 1) < abs(vals[0] - 1)
        checks += 2
        print(f"q={q}: normalized finite-size ratios at S=30,60,120,240: "
              + ', '.join(f'{v:.8f}' for v in vals))
    print(f"PASS: {checks} checks (exact finite-state algebra and numerical asymptotic diagnostics)")

if __name__ == '__main__':
    main()
