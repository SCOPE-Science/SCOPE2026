"""Finite reproducibility checks for the growing-index sibling profile theorem.

No finite computation certifies the functional asymptotics; their proof is analytic.
Requires only Python 3.10+ standard library. Run: python verification_check.py
"""
from functools import lru_cache
from fractions import Fraction
from math import comb, exp, factorial, floor, lgamma, log, pi, sqrt
from random import Random

CHECKS = 0

def check(test, message):
    global CHECKS
    if not test:
        raise AssertionError(message)
    CHECKS += 1


def exact_deficit_expectation(n, j):
    """Independent exact finite-state absorbing-chain computation."""
    @lru_cache(None)
    def f(state):
        if min(state) >= 1:
            return Fraction(sum(k < j for k in state))
        active = [i for i, count in enumerate(state) if count < j]
        value = Fraction(0)
        for i in active:
            updated = list(state)
            updated[i] += 1
            value += f(tuple(updated))
        return value / len(active)
    return f((0,) * n)


def alternating_deficit_mean(n, j):
    return sum((Fraction(((-1) ** (k + 1)) * comb(n, k), k ** (j - 1))
               for k in range(1, n + 1)), Fraction(0))


def poisson_pmf(k, t):
    if k < 0:
        return 0.0
    if t == 0:
        return 1.0 if k == 0 else 0.0
    return exp(-t + k * log(t) - lgamma(k + 1))


def poisson_cdf_below(j, t):
    """P(Poi(t) < j), evaluated via stable log-sum-exp."""
    if j <= 0:
        return 0.0
    if t == 0:
        return 1.0
    terms = [-t + k * log(t) - lgamma(k + 1) for k in range(j)]
    m = max(terms)
    return exp(m) * sum(exp(v - m) for v in terms)


def gaussian_density(x):
    return exp(-x * x / 2) / sqrt(2 * pi)


def poisson_knuth(rng, rate):
    limit = exp(-rate)
    prod = 1.0
    count = 0
    while True:
        count += 1
        prod *= rng.random()
        if prod <= limit:
            return count - 1


def main():
    for n in range(2, 5):
        for j in range(2, 7):
            exact = exact_deficit_expectation(n, j)
            formula = alternating_deficit_mean(n, j)
            check(exact == formula, f"absorbing chain: n={n}, j={j}")
    # A coefficient-level identity for the derivative of the Poisson CDF.
    for j in range(1, 21):
        p = [Fraction(1, factorial(k)) for k in range(j)]
        dp_minus_p = [((k + 1) * p[k + 1] if k + 1 < j else Fraction(0)) - p[k]
                      for k in range(j)]
        target = [Fraction(0)] * (j - 1) + [-Fraction(1, factorial(j - 1))]
        check(dp_minus_p == target, f"CDF derivative polynomial: j={j}")
    # Verify local central-limit approximations to the required Poisson mass.
    for L in [400.0, 1600.0, 6400.0]:
        for x in [-1.0, -0.5, 0.0, 0.5, 1.0]:
            j = floor(L + x * sqrt(L))
            for g in [-0.5, 0.0, 0.5]:
                v = sqrt(L) * poisson_pmf(j - 1, L + g)
                tol = 0.085 if L == 400.0 else (0.045 if L == 1600.0 else 0.026)
                check(abs(v - gaussian_density(x)) < tol,
                      f"local limit: L={L}, x={x}, g={g}, error={abs(v-gaussian_density(x))}")
    # Check exact derivative/integral as an independent finite-difference diagnostic.
    for L in [25.0, 100.0]:
        for x in [-0.7, 0.0, 0.9]:
            j = floor(L + x * sqrt(L))
            h = 1e-3
            derivative = (poisson_cdf_below(j, L + h) - poisson_cdf_below(j, L - h))/(2*h)
            check(abs(derivative + poisson_pmf(j - 1, L)) < 2e-6,
                  f"Poisson-CDF drift: L={L}, x={x}")
    # Independent Poisson clocks: counts at max of first arrivals are
    # 1 + Poisson(max E_i - E_i); compare the finite rank-one approximation.
    rng = Random(739621)
    n = 2000
    L = log(n)
    x = 0.5
    j = floor(L + x * sqrt(L))
    b = poisson_cdf_below(j, L)
    pred_coef = gaussian_density(x)
    errors = []
    for _ in range(110):
        first = [-log(1.0-rng.random()) for _ in range(n)]
        cover = max(first)
        count = sum(1 + poisson_knuth(rng, cover-u) < j for u in first)
        observed = sqrt(L) * (count/n - b)
        predicted = -pred_coef * (cover-L)
        errors.append(abs(observed-predicted))
    mae = sum(errors) / len(errors)
    check(mae < 0.18, f"finite-size Poissonized diagnostic: MAE={mae}")
    print(f"PASS: {CHECKS} exact/numerical assertions; finite-size diagnostic MAE={mae:.6f}")
    print("Limitation: numerical tests do not prove the functional limit or originality.")

if __name__ == '__main__':
    main()
