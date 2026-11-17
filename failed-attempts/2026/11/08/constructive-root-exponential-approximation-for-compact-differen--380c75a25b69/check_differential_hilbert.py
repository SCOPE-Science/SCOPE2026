"""Exact finite checks for a dyadic low-rank approximation of a Cauchy-weighted operator.

Run with Python 3 and only the standard library. The checks test finite algebraic
identities and examples; the infinite-dimensional statements need the written proof.
"""
from fractions import Fraction as Q
import math

checks = 0

def ck(condition, message="identity"):
    global checks
    if not condition:
        raise AssertionError(message)
    checks += 1


def center(j):
    return Q(3 * (2 ** j), 2)


def reciprocal(n, k):
    return Q(1, n + k + 1)


def approx_reciprocal(n, k, j, terms):
    c = center(j)
    return sum(((c - k) ** h) / ((n + c + 1) ** (h + 1))
               for h in range(terms))


def weight(gamma, n):
    """Gamma(gamma+2) n! / Gamma(n+gamma+2), via exact recurrence."""
    v = Q(1)
    for q in range(1, n + 1):
        v *= Q(q, 1) / (q + gamma + 1)
    return v


for j in range(7):
    c = center(j)
    for k in range(2 ** j, 2 ** (j + 1)):
        for n in (0, 1, 2, 3, 7, 12, 25):
            ratio = abs(c - k) / (n + c + 1)
            ck(ratio <= Q(1, 3), 'uniform geometric ratio')
            for terms in (1, 2, 3, 4, 5, 6):
                exact = reciprocal(n, k)
                partial = approx_reciprocal(n, k, j, terms)
                ck(exact - partial == exact * ((c - k)/(n+c+1)) ** terms,
                   'geometric remainder identity')
                ck(abs(exact - partial) <= exact * Q(1, 3) ** terms,
                   'relative geometric error')

# Exact low-rank factors: one column for k=0 plus R factors for each shell.
for L in (1, 2, 3, 4, 5):
    R = L
    for n in range(12):
        for k in range(2 ** L):
            factors = []
            factors.append((Q(1, n + 1), Q(1) if k == 0 else Q(0)))
            for j in range(L):
                c = center(j)
                for h in range(R):
                    left = Q(1) / (n + c + 1) ** (h + 1)
                    right = ((c - k) ** h) if (2 ** j <= k < 2 ** (j + 1)) else Q(0)
                    factors.append((left, right))
            value = sum(a * b for a, b in factors)
            expected = (reciprocal(n, k) if k == 0 else
                        approx_reciprocal(n, k, k.bit_length() - 1, R))
            ck(value == expected, 'separable factorization')
            ck(len(factors) == 1 + L * L, 'constructive rank count')

for gamma in (Q(-3, 4), Q(-1, 2), Q(-1, 4), Q(3, 4), Q(2), Q(5, 2)):
    w = Q(1)
    for n in range(1, 45):
        w *= Q(n, 1) / (n + gamma + 1)
        ck(w == weight(gamma, n), 'Bergman moment recurrence')
        ck(w > 0, 'moment positivity')

# Squared normalized matrix coefficients and truncation estimates are rational.
for alpha, beta in ((Q(-1, 2), Q(7, 4)),
                    (Q(-1, 4), Q(3)),
                    (Q(-3, 4), Q(3, 2))):
    ck(beta > alpha + 2, 'positive gap')
    for n in range(15):
        for k in range(15):
            b2 = (Q(n+1, n+k+1)**2)*weight(beta, n)/weight(alpha, k)
            ck(b2 > 0, 'normalized matrix square positivity')
            ck(b2 == ((n+1)**2 * weight(beta, n)) /
               ((n+k+1)**2 * weight(alpha, k)), 'normalized coefficient')

# A numerical cross-check that selected column sums have the expected decay.
# The sums are finite lower approximants, so this is not a proof of the tail.
for a, b in ((-0.5, 1.75), (-0.25, 3.0), (-0.75, 1.5)):
    def wf(gamma, n):
        return math.exp(math.lgamma(gamma+2) + math.lgamma(n+1) -
                        math.lgamma(n+gamma+2))
    tau = min(b-a-2, -a)
    sampled = []
    for k in (4, 8, 16, 32, 64, 128):
        col = sum(((n+1)/(n+k+1))**2 * wf(b, n)/wf(a, k)
                  for n in range(600))
        ck(col > 0 and math.isfinite(col), 'finite column sum')
        sampled.append(col * (k+1)**(1+tau) / math.log(k+2))
    ck(all(math.isfinite(v) for v in sampled), 'column asymptotic test')

print('DIFFERENTIAL_HILBERT_DYADIC_EXACT_OK', checks)
