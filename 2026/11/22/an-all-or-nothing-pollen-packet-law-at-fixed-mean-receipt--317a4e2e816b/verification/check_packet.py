#!/usr/bin/env python3
"""Standalone deterministic diagnostics for the uniform-packet Poisson threshold model.

The infinite-range theorem is proved analytically in RESULT.md; finite tests are not a proof.
Standard-library dependencies only.
"""
import math
from fractions import Fraction

assertions = 0

def test(condition, note):
    global assertions
    assertions += 1
    if not condition:
        raise AssertionError(note)

def upper_tail(n, mean):
    """P(Poisson(mean) >= n), n >= 1; suitable for the moderate test grid."""
    assert n >= 1 and mean > 0
    p = math.exp(-mean)
    cumulative = p
    for j in range(1, n):
        p *= mean / j
        cumulative += p
    return max(0.0, 1.0 - cumulative)

def score(k, r, mean):
    return upper_tail((r+k-1)//k, mean/k)

def coeff(n, j):
    # In the difference ratio R_n, this is a^(j-1) times the j-th coefficient.
    assert 2 <= j <= n+1
    result = Fraction(1, 1)
    for ell in range(j-1):
        result *= Fraction(n-ell, n)
    return result

# Every shared coefficient grows, and the newly introduced coefficient is positive.
for n in range(1, 65):
    for j in range(2, n+2):
        test(coeff(n+1,j) >= coeff(n,j), ('coefficient ordering',n,j))
        if j >= 3:
            test(coeff(n+1,j) > coeff(n,j), ('strict coefficient ordering',n,j))
    test(coeff(n+1,n+2) > 0, ('new positive term',n))

# Success endpoints dominate every allowed intermediate integer packet size.
for r in range(2, 31):
    for t in range(1, 110):
        a = 0.15 + 0.019*t
        lam = r*a
        left, right = score(1,r,lam), score(r,r,lam)
        best = max(left,right)
        for k in range(2,r+9):
            if k == r:
                continue
            gap = best-score(k,r,lam)
            test(gap > -3e-13, ('endpoint dominance',r,t,k,gap))
            if gap > 5e-10:
                test(gap > 0, ('strict endpoint dominance',r,t,k))

# Numerical bracketing, not a substitute for the analytic existence/uniqueness proof.
def endpoint_diff(r, lam):
    return score(1,r,lam)-score(r,r,lam)

def bisection(r):
    lo = 0.05*r
    hi = 2.5*r + 10.0
    test(endpoint_diff(r,lo)<0, ('below switch',r))
    test(endpoint_diff(r,hi)>0, ('above switch',r))
    for _ in range(75):
        mid = (lo+hi)/2
        if endpoint_diff(r,mid)<0:
            lo=mid
        else:
            hi=mid
    return (lo+hi)/2

for r,expected in [(2,2.51286241725234),(3,3.62037611848942),
                   (4,4.71081081873076),(10,11.10269898164167)]:
    root=bisection(r)
    test(abs(root-expected)<4e-10, ('switch location',r,root))

# The standardized crossover moves toward the stated normal quantile.
normal_quantile = 0.33747496376420244
std_last = 1.0
for r in (10,20,50,100,200):
    root=bisection(r)
    standardized=(root-r)/math.sqrt(r)
    test(standardized > normal_quantile, ('positive correction',r))
    test(standardized < std_last, ('decreasing correction',r))
    std_last=standardized

print(f"PASS: {assertions} deterministic diagnostic assertions")
print("Numerical crossover checks r=2,3,4,10 and increasing-r normal scaling: PASS")
