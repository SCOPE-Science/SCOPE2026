"""Finite exact arithmetic checks for a Markov stick-breaking diversity theorem.

All computations here test algebraic ingredients and finite models; the analytic
proof of the functional limit is in RESULT.md. Uses Python's standard library.
"""
from fractions import Fraction as F
from itertools import product

p, q = F(1, 4), F(1, 3)
P = ((1 - p, p), (q, 1 - q))
pi = (q / (p + q), p / (p + q))
y = (F(1), F(2))  # corresponding breaks are 1-exp(-1), 1-exp(-2)
mu = sum(pi[i] * y[i] for i in (0, 1))
lam = 1 - p - q
var = sum(pi[i] * (y[i] - mu) ** 2 for i in (0, 1))
sigma2 = var * (1 + lam) / (1 - lam)
assert pi == (F(4, 7), F(3, 7))
assert mu == F(10, 7) and lam == F(5, 12)
assert sigma2 == F(204, 343)
assert sigma2 / mu ** 3 == F(51, 250)
checks = 4

# Exact Markov covariance: multiply P^h by the centered observable.
rowpowers = ((F(1), F(0)), (F(0), F(1)))
for h in range(0, 65):
    covariance = sum(pi[i] * (y[i]-mu) * rowpowers[i][j] * (y[j]-mu)
                     for i in (0, 1) for j in (0, 1))
    assert covariance == var * lam ** h, (h, covariance)
    checks += 1
    rowpowers = tuple(tuple(sum(rowpowers[i][k]*P[k][j] for k in (0, 1))
                              for j in (0, 1)) for i in (0, 1))

# Exhaustively enumerate all Markov paths up to length 11 to check
# partial-sum variance against the exact Green--Kubo finite sum.
for m in range(1, 12):
    mean = F(0)
    second = F(0)
    total = F(0)
    for path in product((0, 1), repeat=m):
        prob = pi[path[0]]
        for k in range(1, m):
            prob *= P[path[k-1]][path[k]]
        s = sum(y[i] for i in path)
        total += prob
        mean += prob * s
        second += prob * s * s
    expected_var = m*var + 2*sum((m-h)*var*lam**h for h in range(1, m))
    assert total == 1 and mean == m*mu
    assert second - mean**2 == expected_var
    checks += 3

# Fixed stationary marginal with tunable autocorrelation.
for k in range(1, 20):
    rho = F(k, 20)
    p0 = q0 = (1-rho)/2
    assert p0 > 0 and q0 > 0
    # Two-state spectral multiplier versus geometric-covariance formula.
    assert (1+rho)/(1-rho) == 1 + 2*sum(rho**j for j in range(1, 301)) + 2*rho**301/(1-rho)
    checks += 1
print('PASS:', checks, 'exact rational checks; example Brownian variance coefficient =', sigma2 / mu**3)
