"""Numerical reproducibility checks for a two-sex Poisson founding-quorum theorem.

This diagnostic uses only Python's standard library. Universal results are proved
analytically in RESULT.md; a finite check is not a proof.
"""

from math import exp, expm1, factorial, fsum, isclose, log, log1p, lgamma


def beta_mgf(r, y):
    """E[exp(y V)], where V~Beta(1,r-1); r=1 means V=1."""
    assert r >= 1 and y >= 0
    if r == 1:
        return exp(y)
    term = 1.0
    terms = [1.0]
    for j in range(1, 10000):
        term *= y / (r - 1 + j)
        terms.append(term)
        if term <= 2e-16 * fsum(terms) and j > max(5, y):
            return fsum(terms)
    raise ArithmeticError("series did not converge")


def poisson_quorum_tail(r, y):
    """Pr[Poisson(y) >= r], without cancellation for small y."""
    assert r >= 1 and y >= 0
    if y == 0:
        return 0.0
    if y < 1.0:
        term = y ** r / factorial(r)
        terms = [term]
        for j in range(r + 1, 10000):
            term *= y / j
            terms.append(term)
            if term < 2e-16 * fsum(terms):
                break
        return exp(-y) * fsum(terms)
    term = 1.0
    terms = [term]
    for j in range(1, r):
        term *= y / j
        terms.append(term)
    return -expm1(-y) - exp(-y) * (fsum(terms) - 1.0)


def log_beta_mgf(r, y):
    """Stable log of the beta MGF also at large intensity."""
    assert r >= 1 and y >= 0
    if r == 1:
        return y
    if y <= 200:
        return log(beta_mgf(r, y))
    s = 1.0
    term = 1.0
    for j in range(1, r - 1):
        term *= y / j
        s += term
    return y + lgamma(r) - (r - 1) * log(y) + log1p(-exp(-y) * s)


def founding_success(n, r, male):
    female = n - male
    assert n > 0 and r >= 1 and 0 <= male <= n
    return -expm1(-male) * poisson_quorum_tail(r, female)


def optimum(n, r):
    """Bisection of the independent positive-series stationarity equation."""
    lo, hi = 0.0, n
    for _ in range(110):
        y = (lo + hi) / 2
        if y + log_beta_mgf(r, y) < n:
            lo = y
        else:
            hi = y
    y = (lo + hi) / 2
    return n - y


def run():
    checks = 0
    def check(flag, note):
        nonlocal checks
        checks += 1
        if not flag:
            raise AssertionError(note)

    for r in range(1, 13):
        for n in (0.01, 0.1, 0.5, 1, 2, 4, 7, 10, 20, 50, 100):
            x = optimum(n, r)
            y = n - x
            check(0 < x < n, ("interior", n, r))
            check(isclose(exp(x), beta_mgf(r, y), rel_tol=2e-12), ("root", n, r))
            optimum_probability = founding_success(n, r, x)
            for i in range(1, 100):
                u = n * i / 100
                check(founding_success(n, r, u) <= optimum_probability + 1e-13 * max(1e-10, optimum_probability), ("grid", n, r, i))
            if r == 1:
                check(isclose(x / n, 0.5, abs_tol=1e-11), ("r1", n))
            else:
                check(1 / (r + 1) < x / n < 0.5, ("bias", n, r))

    for r in range(2, 15):
        fractions = [optimum(n, r) / n for n in (0.01, 0.03, 0.1, 0.3, 1, 3, 10, 30, 100, 250)]
        check(all(a < b for a, b in zip(fractions, fractions[1:])), ("increasing", r))
        for n in (0.02, 0.2, 2, 20, 200):
            check(optimum(n, r + 1) < optimum(n, r), ("quorum ordering", n, r))

    for r in range(2, 11):
        n = 0.005
        exact_fraction = optimum(n, r) / n
        linear_fraction = 1 / (r + 1) + r * (r - 1) * n / (2 * (r + 1) ** 4)
        check(abs(exact_fraction - linear_fraction) < 1e-6, ("small-n expansion", r))
        n = 1000000.0
        actual_x = optimum(n, r)
        approx_x = n / 2 - (r - 1) * log(n / 2) / 2 + log(factorial(r - 1)) / 2
        check(abs(actual_x - approx_x) < 0.01, ("large-n expansion", r))
        y = n - actual_x
        term = 1.0
        tsum = 1.0
        for j in range(1, r):
            term *= y / j
            tsum += term
        first, second = -actual_x, -y + log(tsum)
        peak = max(first, second)
        log_failure = peak + log(exp(first-peak) + exp(second-peak))
        log_predicted = log(2) - n/2 + (r-1)*log(n/2)/2 - lgamma(r)/2
        check(abs(log_failure-log_predicted) < 0.01, ("failure asymptotic", r))

    print("PASS:", checks, "diagnostic assertions")
    for r, n in ((2, 4.0), (3, 10.0), (7, 4.0)):
        x = optimum(n, r)
        print("r=%d n=%.1f male=%.12f male_fraction=%.12f quorum_probability=%.12f" %
              (r, n, x, x / n, founding_success(n, r, x)))

if __name__ == "__main__":
    run()
