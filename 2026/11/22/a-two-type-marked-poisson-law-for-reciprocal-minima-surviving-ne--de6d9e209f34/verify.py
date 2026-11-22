"""Deterministic checks for the common reciprocal-minima overlap law.

Uses standard Python only. Exhaustive finite tests verify selected coefficients;
the asymptotic Poisson process follows from the integral proof in RESULT.md.
"""
import itertools
import math
from fractions import Fraction

checks = 0

def require(condition, context):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(context)


def beta_int(a, b, eps):
    """Exact integral of (1-u)^a (1-eps*u)^b over 0..1."""
    eps = Fraction(eps)
    return sum((math.comb(b, j) * ((-eps) ** j)
                * Fraction(math.factorial(j) * math.factorial(a),
                           math.factorial(a + j + 1))
                for j in range(b + 1)), Fraction(0))


def expected_counts(n, eps):
    """Exact retained and replaced common-minima expectations."""
    eps = Fraction(eps)
    m = 2*n-2
    retained = n*n * (1-eps) * beta_int(m, m, eps)
    replaced = n*n * eps * Fraction(2, m+1) * beta_int(m+1, m, eps)
    return retained, replaced


def count_minima(flat, n):
    rows = [min(range(n), key=lambda j: flat[i*n+j]) for i in range(n)]
    cols = [min(range(n), key=lambda i: flat[i*n+j]) for j in range(n)]
    return sum(cols[j] == i for i, j in enumerate(rows))


def minima_sites(flat, n):
    rows = [min(range(n), key=lambda j: flat[i*n+j]) for i in range(n)]
    cols = [min(range(n), key=lambda i: flat[i*n+j]) for j in range(n)]
    return {(i, j) for i, j in enumerate(rows) if cols[j] == i}

# Exhaust all rank orders for one matrix; their distribution is universal.
for n in (2, 3):
    histogram = {}
    for ordering in itertools.permutations(range(n*n)):
        v = count_minima(ordering, n)
        histogram[v] = histogram.get(v, 0) + 1
    total = math.factorial(n*n)
    mean = sum(Fraction(k*v, total) for k, v in histogram.items())
    variance = sum((Fraction(k)-mean)**2 * Fraction(v, total)
                   for k, v in histogram.items())
    require(mean == Fraction(n*n, 2*n-1), (n, 'mean'))
    require(variance == Fraction(n*n*(n-1), 2*(2*n-1)**2),
            (n, 'variance'))
    require(expected_counts(n, 0) == (mean, Fraction(0)),
            (n, 'identical-copy endpoint'))
    require(expected_counts(n, 1) ==
            (Fraction(0), Fraction(n*n, (2*n-1)**2)),
            (n, 'independent-copy endpoint'))

# Two entire independent matrices at n=2: 24^2 exhaustive pairs.
matrices = list(itertools.permutations(range(4)))
pairs = [minima_sites(a, 2) for a in matrices]
counts = {}
for A in pairs:
    for B in pairs:
        q = len(A & B)
        counts[q] = counts.get(q, 0) + 1
require(sum(Fraction(k*v, 24*24) for k, v in counts.items())
        == Fraction(4, 9), 'n=2 independent common mean')
require(sum(Fraction(k*(k-1)*v, 24*24)
            for k, v in counts.items()) == Fraction(1, 9),
        'n=2 independent common second factorial moment')

# Exact nontrivial refresh-case finite formula; retained versus replaced.
r, f = expected_counts(2, Fraction(1, 2))
require(r == Fraction(31, 60), 'n=2 half-refresh retained')
require(f == Fraction(49, 180), 'n=2 half-refresh replaced')
require(r+f == Fraction(71, 90), 'n=2 half-refresh total')

# Independent direct integration check by midpoint Riemann sums, using
# the unsimplified two-dimensional competitor probability h(u,v).
def h(u, v, eps):
    return (1-eps)*(1-max(u, v)) + eps*(1-u)*(1-v)

for n, eps in [(2, .5), (3, .5), (4, .8)]:
    N = 500
    s_diag = sum(h((i+.5)/N, (i+.5)/N, eps)**(2*n-2)
                 for i in range(N))/N
    s_off = sum(h((i+.5)/N, (j+.5)/N, eps)**(2*n-2)
                for i in range(N) for j in range(N))/(N*N)
    rd, fd = expected_counts(n, Fraction(str(eps)))
    require(abs(n*n*(1-eps)*s_diag - float(rd)) < 0.002,
            (n, eps, 'direct diagonal integral'))
    require(abs(n*n*eps*s_off - float(fd)) < 0.002,
            (n, eps, 'direct two-dimensional integral'))

# Large-n exact positive-integrand quadrature checks for Poisson rates.
def midpoint_integral(n, eps, additional=0):
    m = 2*n-2
    N = max(30000, 200*n)
    # All values are nonnegative; midpoint integration is stable.
    return sum(((1-(j+.5)/N)**(m+additional) *
                (1-eps*(j+.5)/N)**m)
               for j in range(N))/N

for c in (0, 1, 3):
    for n in (200, 500):
        eps = 1-c/n
        er = n*n*(1-eps)*midpoint_integral(n, eps)
        ef = n*n*eps*2/(2*n-1)*midpoint_integral(n, eps, 1)
        require(abs(er-c/4) < 0.025, (n, c, 'retained limit', er))
        require(abs(ef-.25) < 0.025, (n, c, 'replaced limit', ef))

print('PASS', checks, 'deterministic checks')
