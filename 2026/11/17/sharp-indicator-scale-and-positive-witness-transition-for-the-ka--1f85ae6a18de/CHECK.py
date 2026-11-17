"""Supplementary finite-cell checks for a logarithmic centralizer gauge.

Run: python CHECK.py
These tests are illustrative; the theorem is proved analytically.
"""
import math
import random

PHI = (1.0 + math.sqrt(5.0)) / 2.0
TSTAR = math.exp(-PHI)

def witness_cost(cells, indicator):
    # Each cell: (mass, real witness value), and a 0/1 target indicator.
    s = sum(m * abs(x) for m, x in cells)
    if s == 0:
        return sum(m * a for (m, _), a in zip(cells, indicator))
    cost = s
    for (m, x), a in zip(cells, indicator):
        omega = x * math.log(abs(x) / s) if x else 0.0
        cost += m * abs(a - omega)
    return cost

def lower_bound(t):
    L = math.log(1.0/t)
    return t/L*(1.0 - t/math.e)

def upper_bound(t):
    return t/math.log(1.0/t)

def positive_infimum(t):
    delta = min(t, TSTAR)
    return t - delta + delta / math.log(1.0/delta)

def positive_construct(t):
    delta = min(t, TSTAR)
    L = math.log(1.0/delta)
    # E subset A: three intervals with masses delta, t-delta, 1-t
    return witness_cost([(delta, 1.0/L), (t-delta, 0.0), (1-t, 0.0)], [1,1,0])

# Normalization identities and positive extremizers.
for i in range(1, 300):
    t = 0.0001 + i / 301.0 * .9998
    c = positive_construct(t)
    q = positive_infimum(t)
    assert math.isclose(c, q, rel_tol=2.e-11, abs_tol=2.e-13), (t, c, q)
    if t <= TSTAR:
        assert lower_bound(t) <= q <= upper_bound(t)*(1.0+1.e-12)

# Random signed/positive test configurations in a finite equal-cell partition.
random.seed(6079)
for N in (5, 8, 15, 22):
    for m in range(1, N):
        t = m / N
        for _ in range(160):
            xs = [random.choice((-1.0,1.0)) * math.exp(random.uniform(-14, 4)) for i in range(N)]
            masses = [(1.0/N, x) for x in xs]
            c = witness_cost(masses, [1]*m + [0]*(N-m))
            if t <= TSTAR:
                assert c >= lower_bound(t) - 5.e-12, (N,m,c,lower_bound(t))
            # Positive restriction always lies above the global infimum
            if all(x >= 0 for x in xs):
                assert c >= positive_infimum(t) - 5.e-12


# Complex phases cannot violate the same analytic envelope.
for N in (7, 11):
    for m in range(1, N):
        t=m/N
        if t > TSTAR:
            continue
        for _ in range(220):
            zz=[math.exp(random.uniform(-9,2))*complex(math.cos(v),math.sin(v)) for v in [random.uniform(-math.pi,math.pi) for i in range(N)]]
            c=witness_cost([(1.0/N,z) for z in zz],[1]*m+[0]*(N-m))
            assert c>=lower_bound(t)-5.e-12, (N,m,c,lower_bound(t))

# Check the exact dual elementary envelope on a large scalar grid.
for s in [10**(-k/3) for k in range(-6, 27)]:
    # W is determined by the monotone equation W exp(W) = 1/s.
    lo, hi=0.0, max(3.0,math.log(1/s)+5) if s<1 else 3.0
    while hi*math.exp(hi) < 1.0/s:hi *= 2
    for _ in range(90):
        mid=(lo+hi)/2
        if mid*math.exp(mid) < 1/s:lo=mid
        else:hi=mid
    W=(lo+hi)/2
    for k in range(-100,101):
        u=s*math.exp(k/13.)
        h=min(1.,max(0.,u*math.log(u/s)))
        assert h <= u*W+1e-11
        if u<s:
            assert abs(u*math.log(u/s)) <= s/math.e+1e-11*s

print('OK: 299 positive-witness formula comparisons, 7,360 random real-witness configurations, 660 complex-witness configurations, 6,633 scalar envelope checks.')
