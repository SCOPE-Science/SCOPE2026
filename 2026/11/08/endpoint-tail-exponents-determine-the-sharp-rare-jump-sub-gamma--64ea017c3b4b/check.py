"""Finite diagnostics for the endpoint-dependent rare-jump sub-gamma theorem.

Requires only the Python standard library. This is a diagnostic program,
not a proof of an asymptotic theorem.
"""
from fractions import Fraction
import math

assertions = 0


def check(condition, context):
    global assertions
    assertions += 1
    if not condition:
        raise AssertionError(context)


def factorial_coeff(beta, n):
    # For J of density beta*(1-J)^(beta-1) on [0,1], beta=1 or 2.
    return Fraction(math.factorial(beta + 2), math.factorial(n + beta + 2))


def two_point_moment(beta, k):
    # E[J^k] for Beta(1,beta), beta=1,2.
    if beta == 1:
        return Fraction(1, k + 1)
    return Fraction(2, (k + 1) * (k + 2))


def transformed_coeff(beta, n):
    return Fraction(2, math.factorial(n + 2)) * two_point_moment(beta, n + 2) / two_point_moment(beta, 2)


for beta in (1, 2):
    for n in range(100):
        check(factorial_coeff(beta, n) == transformed_coeff(beta, n),
              (beta, n, "coefficient identity"))
    check(factorial_coeff(beta, 0) == 1, (beta, "constant"))


def transform(s, beta):
    # Closed MGFs for the size-square/Beta(1,2) remainder of Beta(1,beta) jumps.
    # Only evaluated at s >= 10 to avoid cancellation.
    k = beta + 2
    residual = math.exp(s) - sum(s ** j / math.factorial(j) for j in range(k))
    fres = math.exp(s) - sum(s ** j / math.factorial(j) for j in range(k - 1))
    f = math.factorial(k) * residual / s ** k
    fp = math.factorial(k) * (fres / s ** k - k * residual / s ** (k + 1))
    return f, fp


def stationary(s, beta, d):
    f, fp = transform(s, beta)
    h = d * (f - 1)
    return s * fp / (f - 1) - 1 - h


def root_for_L(beta, L):
    d = math.exp(-L)
    a = max(10.0, L - 2.0)
    z = L + 15.0 * math.log(L) + 10.0
    check(stationary(a, beta, d) > 0, (beta, L, "lower bracket"))
    check(stationary(z, beta, d) < 0, (beta, L, "upper bracket"))
    for _ in range(90):
        m = (a + z) / 2
        if stationary(m, beta, d) > 0:
            a = m
        else:
            z = m
    return (a + z) / 2


for beta, kconst in ((1, 6), (2, 24)):
    diffs = []
    for L in (25.0, 50.0, 100.0, 200.0):
        root = root_for_L(beta, L)
        f, fp = transform(root, beta)
        delta = math.exp(-L)
        h = delta * (f - 1)
        c = (h / (1 + h)) / root
        s0 = L + (beta + 3) * math.log(L) - math.log(kconst)
        check(root > L, (beta, L, "location"))
        check(h > 0 and c > 0, (beta, L, "positivity"))
        check(abs(stationary(root, beta, delta)) < 2e-9,
              (beta, L, "stationarity"))
        check(abs(h / root - 1) < 0.3, (beta, L, "balance"))
        check(abs(c * L - 1) < 0.4, (beta, L, "leading scale"))
        diffs.append(abs(root - s0))
    check(diffs[-1] < diffs[0], (beta, "shrinking location remainder"))
    check(diffs[-1] < 0.8, (beta, "long-log quantitative remainder"))

print(f"PASS: {assertions} exact-rational and numeric diagnostic assertions")
print("The theorem over arbitrary endpoint-regular jump laws is proved analytically, not by this finite checker.")
