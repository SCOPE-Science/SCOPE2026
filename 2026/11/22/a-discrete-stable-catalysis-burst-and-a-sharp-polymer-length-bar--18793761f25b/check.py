"""Finite checks for the short-incidence law in an abstract word network."""
from math import erfc, expm1, gamma, isclose, log, log1p, pi, sqrt


def words(k, m):
    return k * (k**m - 1) // (k - 1)


def ordered_splits(k, m):
    return sum((j - 1) * k**j for j in range(2, m + 1))


def check_counts():
    for k in (2, 3, 4):
        for m in range(2, 10):
            direct = sum(k**i * k**j for i in range(1, m)
                         for j in range(1, m - i + 1))
            assert ordered_splits(k, m) == direct
            assert words(k, m) == sum(k**j for j in range(1, m + 1))


def check_half_pareto():
    k, n, ell, alpha, beta = 2, 60, 28, 0.5, 0.5
    theta = alpha * (1 + beta) / (1 + alpha)
    b = theta * n - alpha / (1 + alpha) * log(n, k)
    prefactor = gamma(1 - alpha) * theta**alpha * (k / (k - 1))**(1 - alpha*beta)
    u = ordered_splits(k, ell) / words(k, n)**(1 + beta)
    # For Pareto(1/2), integrate the single-catalyst Laplace deficit by parts.
    q = -expm1(-u) + sqrt(pi*u) * erfc(sqrt(u))
    probability = -expm1(words(k, ell) * log1p(-q))
    assert isclose(prefactor, 2.1078147305108117, rel_tol=1e-12)
    assert isclose(probability, 0.8504251760823844, rel_tol=1e-12)
    parameter = prefactor * k**((1 + alpha) * (ell - b))
    assert abs(words(k, ell) * q / parameter - 1) < 0.08
    return probability


def check_mark_series():
    for alpha in (0.25, 0.5, 0.75):
        z = 0.4
        coeff, s = alpha, 0.0
        for j in range(1, 40):
            assert coeff > 0
            s += coeff * z**j
            coeff *= (j-alpha)/(j+1)
        assert isclose(s, 1-(1-z)**alpha, rel_tol=1e-12)


if __name__ == '__main__':
    check_counts()
    p = check_half_pareto()
    check_mark_series()
    print(f'Finite consistency checks passed; example incidence probability = {p:.10f}')
