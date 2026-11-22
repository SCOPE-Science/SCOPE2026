"""Reproducible finite diagnostics for endpoint-detrended path distance covariance.

Finite checks supplement the exact integration and the asymptotic arguments.
Uses only Python's standard library. Run: python CHECKER.py
"""
import itertools
import math
import random
from fractions import Fraction

checks = 0

def verify(condition, message):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(message)


def centered_distances(x):
    n = len(x)
    a = [[abs(u - v) for v in x] for u in x]
    row = [sum(v) / n for v in a]
    mean = sum(row) / n
    return [[a[i][j] - row[i] - row[j] + mean for j in range(n)] for i in range(n)], mean


def squared_dcov(x, y):
    a, ax = centered_distances(x)
    b, by = centered_distances(y)
    n = len(x)
    return sum(a[i][j]*b[i][j] for i in range(n) for j in range(n))/(n*n)


def corr(x, y):
    v = squared_dcov(x,y)
    xx = squared_dcov(x,x)
    yy = squared_dcov(y,y)
    if xx*yy == 0:
        return 0.0
    return math.sqrt(max(0.0, v/math.sqrt(xx*yy)))

# Brownian bridge's covariance and increment second moments (exact arithmetic).
for denominator in range(2,32):
    for i in range(denominator+1):
        for j in range(i,denominator+1):
            s = Fraction(i,denominator)
            t = Fraction(j,denominator)
            cov = s*(1-t)
            var = s*(1-s)+t*(1-t)-2*cov
            gap = t-s
            verify(var == gap*(1-gap), 'bridge increment variance')

# All defining polynomial integrals are exactly evaluated by rational arithmetic.
# 2 integral_0^1 [a - 2a^2 + a^3] da = 1/6.
verify(2*(Fraction(1,2)-2*Fraction(1,3)+Fraction(1,4)) == Fraction(1,6),
       'squared expected-distance integral')
# Euler beta integral for mean distance is B(3/2,3/2) = pi/8.
verify(abs(math.gamma(1.5)**2 / math.gamma(3) - math.pi/8) < 2e-15,
       'beta integral')
expected = 1/(3*math.pi) - math.pi/32
verify(0 < expected < 0.01, 'positive exact mean')

# Numerical quadrature independently confirms the bridge expected distance's
# constancy in time (even away from the symmetric midpoint).
steps = 10000
for s in (0, .05, .17, .37, .5, .89, 1):
    approximation = sum(math.sqrt((a := abs(s-(i+.5)/steps))*(1-a)) for i in range(steps))/steps
    verify(abs(approximation-math.pi/8) < .00002, 'expected distance is time-independent')

# Check the exact finite-grid Gaussian bridge expectation by two independent
# deterministic calculations: centering the full expected-distance matrix
# versus the closed cyclic row-mean formula.
for n in range(2,53):
    distances = [[math.sqrt((a:=abs(i-j)/n)*(1-a)) for j in range(n)] for i in range(n)]
    row_means = [sum(row)/n for row in distances]
    mean = sum(row_means)/n
    m = sum(math.sqrt(h*(n-h)) for h in range(1,n))/(n*n)
    centered = [[distances[i][j] - row_means[i]-row_means[j]+mean
                 for j in range(n)] for i in range(n)]
    matrix_expression = (2/math.pi)*sum(z*z for row in centered for z in row)/(n*n)
    closed_expression = (2/math.pi)*((n*n-1)/(6*n*n) - m*m)
    verify(all(abs(v-m) < 3e-15 for v in row_means), 'cyclic expected distance row means')
    verify(abs(matrix_expression-closed_expression) < 3e-14, 'finite Gaussian identity')
    verify(closed_expression > 0, 'finite positivity')

# Independently verify the exact uniform-permutation expectation identity.
for x,y in [([0,2,3,8],[2,1,4,0]),
            ([0,2,5,1,4],[3,9,1,0,8]),
            ([0,2,5,1,4,9],[2,1,7,3,5,0])]:
    n=len(x)
    _, ax = centered_distances(x)
    _, by = centered_distances(y)
    permuted = sum(squared_dcov(x,[y[i] for i in p]) for p in itertools.permutations(range(n)))/math.factorial(n)
    verify(abs(permuted-ax*by/(n-1)) < 2e-12, 'exact conditional permutation expectation')

# Distance correlation is continuous and takes value one on identical nonconstant paths.
for n in (11,21,41,81):
    h = [1-abs(2*(i/(n-1)) - 1) for i in range(n)]
    verify(abs(corr(h,h)-1) < 2e-11, 'deterministic support at one')
    verify(abs(corr(h,[2*v+3 for v in h])-1) < 2e-11, 'affine invariance')

# Repeated independent Brownian-bridge grids give an empirical positive
# squared distance-covariance mean of the predicted order of magnitude.
rng = random.Random(20261116)
n=65
replicates=400
values=[]
for rep in range(replicates):
    paths=[]
    for k in range(2):
        w=[0.0]
        for i in range(1,n):
            w.append(w[-1]+rng.gauss(0,1)/math.sqrt(n-1))
        paths.append([w[i]-i*w[-1]/(n-1) for i in range(n)])
    values.append(squared_dcov(*paths))
empirical = sum(values)/len(values)
m = sum(math.sqrt(h*(n-h)) for h in range(1,n))/(n*n)
finite_exact = (2/math.pi)*((n*n-1)/(6*n*n) - m*m)
verify(abs(empirical-finite_exact) < .003, 'Monte Carlo bridge mean numerical sanity check')

print(f'PASS {checks} assertions, finite Monte Carlo mean {empirical:.9f}; finite expectation {finite_exact:.9f}; analytic limit {expected:.9f}')
