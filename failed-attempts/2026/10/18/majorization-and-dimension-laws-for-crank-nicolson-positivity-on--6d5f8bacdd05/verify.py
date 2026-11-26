"""Exact and floating-point spot checks for anisotropic Boolean-cube CN positivity.

No third-party dependencies. Analytical all-dimensional statements are proved in RESULT.md.
"""
from fractions import Fraction as F
from itertools import product
from math import comb, sqrt

assertions = 0

def check(test, message):
    global assertions
    assertions += 1
    if not test:
        raise AssertionError(message)

def resolvent_kernel(weights, h):
    """Walsh transform of the resolvent kernel, with exact rational entries."""
    d = len(weights)
    N = 1 << d
    masses = [sum((weights[i] for i in range(d) if (mask >> i) & 1), F(0))
              for mask in range(N)]
    return [sum(((F(-1) if ((mask & z).bit_count() & 1) else F(1)) /
                 (1 + h * masses[mask]) for mask in range(N)), F(0)) / N
            for z in range(N)]

def numerical_threshold(weights):
    d = len(weights)
    masses = [sum(weights[i] for i in range(d) if (mask >> i) & 1)
              for mask in range(1 << d)]
    masses.sort()
    def val(h):
        return sum(1 / (1 + h * x) for x in masses) / (1 << d) - 0.5
    high = 1.0
    while val(high) > 0:
        high *= 2
        if high > 1e15:
            raise RuntimeError('Exceeded finite-root search range')
    low = 0.0
    for _ in range(100):
        mid = (low + high) / 2
        if val(mid) >= 0:
            low = mid
        else:
            high = mid
    return (low + high) / 2

# Exact Walsh transform, nonnegative off-diagonal entries, stochasticity.
for weights in [(F(1), F(1)), (F(1), F(3)),
                (F(1), F(2), F(3)),
                (F(2), F(2), F(2), F(2)),
                (F(1), F(2), F(3), F(4))]:
    d = len(weights)
    for h in [F(1, 20), F(1, 2), F(1), F(3), F(10)]:
        R = resolvent_kernel(weights, h)
        check(sum(R) == F(1), f'resolvent mass {weights} {h}')
        check(all(v > 0 for v in R), f'resolvent positivity {weights} {h}')
        CN = [2*x - (1 if z == 0 else 0) for z,x in enumerate(R)]
        check(sum(CN) == F(1), f'CN mass {weights} {h}')
        check(all(x > 0 for x in CN[1:]), f'CN offdiagonal {weights} {h}')
        check((all(x >= 0 for x in CN)) == (R[0] >= F(1,2)),
              f'CN exact diagonal reduction {weights} {h}')

# Exact matrix inversion comparison (2, 3, and 4 dimensions).
def inverse(M):
    n = len(M)
    A = [M[i][:] + [F(int(i == j)) for j in range(n)] for i in range(n)]
    for col in range(n):
        pivot = next(i for i in range(col, n) if A[i][col] != 0)
        A[col], A[pivot] = A[pivot], A[col]
        den = A[col][col]
        A[col] = [z / den for z in A[col]]
        for i in range(n):
            if i != col and A[i][col] != 0:
                mult = A[i][col]
                A[i] = [A[i][j] - mult*A[col][j] for j in range(2*n)]
    return [row[n:] for row in A]

for weights in [(F(1), F(3)), (F(1), F(2), F(4)), (F(2), F(1), F(2), F(1))]:
    d = len(weights)
    n = 1 << d
    h = F(2, 5)
    Lap = [[F(0) for j in range(n)] for i in range(n)]
    for i in range(n):
        for bit, w in enumerate(weights):
            Lap[i][i] += w
            Lap[i][i ^ (1 << bit)] -= w
    inv = inverse([[F(int(i == j)) + h * Lap[i][j] / 2
                    for j in range(n)] for i in range(n)])
    kernel = resolvent_kernel(weights, h)
    for i in range(n):
        for j in range(n):
            check(inv[i][j] == kernel[i ^ j], f'full inverse vs Walsh {weights} {i} {j}')

# Strict pair balancing under a fixed sum: exact rational arithmetic.
for d in range(2, 8):
    weights = [F(i + 1, 2) for i in range(d)]
    for i in range(d):
        for j in range(i+1, d):
            m = (weights[i] + weights[j]) / 2
            balanced = weights[:]
            balanced[i] = balanced[j] = m
            for h in [F(1, 9), F(2, 3), F(7)]:
                raw = resolvent_kernel(weights, h)[0]
                new = resolvent_kernel(balanced, h)[0]
                check(new < raw, f'strict balancing {d} {i} {j} {h}')

# Uniform dimensions are grouped by their binomial Walsh multiplicities.
def numerical_threshold_uniform(d):
    def val(t):
        return sum(comb(d,j) / (1 + t*j/d) for j in range(d+1)) / (1 << d) - 0.5
    low, high = 2.0, 4.0
    for _ in range(80):
        mid = (low+high)/2
        if val(mid)>0:
            low = mid
        else:
            high = mid
    return (low+high)/2

# Dimensionless uniform critical thresholds and their sharp asymptotic.
old = float('inf')
for d in range(2, 31):
    t = numerical_threshold_uniform(d)
    check(t > 2, f'lower Jensen threshold {d}')
    check(t < old, f'strict dimension monotonicity {d}')
    check(t <= 1+sqrt(5)+1e-11, f'upper 2D threshold {d}')
    old = t
check(abs(numerical_threshold_uniform(2) - (1+sqrt(5))) < 1e-11,
      'exact two-dimensional golden-ratio threshold')
for d in [50, 100, 200, 400]:
    t = numerical_threshold_uniform(d)
    approx = 2 + 1/d + 5/(4*d*d)
    check(abs(t - approx)*d**3 < 5, f'second correction asymptotic {d}')

# Exact centered second/fourth binomial moment identities used in the asymptotic proof.
for d in range(2, 45):
    values = [F(comb(d,j), 1 << d) for j in range(d+1)]
    deviations = [F(j,d) - F(1,2) for j in range(d+1)]
    m2 = sum((p*x*x for p,x in zip(values,deviations)), F(0))
    m4 = sum((p*x**4 for p,x in zip(values,deviations)), F(0))
    check(m2 == F(1,4*d), 'binomial second central moment')
    check(m4 == F(3,16*d*d)-F(1,8*d**3),
          'binomial fourth central moment')

# Verify the diagonal sign on both sides of numerically located critical steps.
for weights in [[1,1],[1,3],[1,2,3],[2,3,5,7]]:
    cutoff = numerical_threshold(weights)
    for h,expected in [(cutoff*.99, True),(cutoff*1.01,False)]:
        d=len(weights)
        masses=[sum(weights[i] for i in range(d) if mask & (1<<i))
                for mask in range(1<<d)]
        value=sum(1/(1+h*m) for m in masses)/(1<<d)
        check((value>=.5)==expected,'critical-step numerical sign')

# Two-rate exact cubic sign certificate after clearing strictly positive denominators.
for a,b in [(F(1), F(1)), (F(1), F(7)), (F(1, 12), F(11,12))]:
    W = a+b
    for h in [F(1, 4), F(1), F(2), F(5), F(20)]:
        r = resolvent_kernel((a,b),h)[0] - F(1, 2)
        polynomial = 2 + 2*W*h - a*b*W*h**3
        check((r > 0) == (polynomial > 0), 'two-coordinate cubic sign')
        check((r == 0) == (polynomial == 0), 'two-coordinate cubic equality')

for e in [1e-3, 1e-4, 1e-5]:
    h = numerical_threshold([e, 1-e])
    estimate = sqrt(2/(e*(1-e))) + .5
    check(abs(h-estimate) < .05, f'degenerate two-coordinate scale {e}')

print(f'PASS: {assertions} independent finite assertions. Analytic claims require the accompanying proof.')
