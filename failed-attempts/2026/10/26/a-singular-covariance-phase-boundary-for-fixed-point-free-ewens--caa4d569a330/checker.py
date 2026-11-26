#!/usr/bin/env python3
"""Exact arithmetic checks for conditioned-Ewens cycle-count covariance.
Uses only the Python 3 standard library; no random sampling is required.
"""
from fractions import Fraction
from itertools import permutations
from math import factorial

checks = 0

def verify(condition, explanation):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(explanation)

def h_coefficients(theta, limit):
    theta = Fraction(theta)
    h = [Fraction(1), Fraction(0)]
    for k in range(1, limit):
        h.append((k*h[k] + theta*h[k-1])/(k+1))
    return h

def cov_formula(theta, h, n, a, b):
    t = Fraction(theta)
    return (t*t/Fraction(a*b)) * ((h[n-a-b]*h[n]-h[n-a]*h[n-b])/(h[n]*h[n]))

def q(k):
    return sum((Fraction(-1 if j % 2 else 1, factorial(j)) for j in range(k+1)), Fraction(0))

# Coefficients obtained two independent ways: recurrence and finite expansion.
for theta in [Fraction(1,3), Fraction(1,2), Fraction(2,3), Fraction(1), Fraction(3,2), Fraction(2), Fraction(3)]:
    h = h_coefficients(theta, 43)
    for n in range(2, 41):
        # [z^n]exp(-theta*z)(1-z)^(-theta)
        rising = [Fraction(1)]
        for k in range(1, n+1):
            rising.append(rising[-1] * (theta+k-1)/k)
        exp_coeff = [Fraction((-theta)**j, factorial(j)) for j in range(n+1)]
        independent = sum((exp_coeff[j] * rising[n-j] for j in range(n+1)), Fraction(0))
        verify(h[n] == independent, f'coefficient theta={theta}, n={n}')
        verify(h[n] > 0, 'positive normalizer')

# The uniform case: alternating covariance sign for all unequal cycle lengths.
Q = [q(n) for n in range(65)]
for a in range(2, 12):
    for b in range(a+1, 13):
        for n in range(a+b, 55):
            delta = Q[n-a-b]*Q[n]-Q[n-a]*Q[n-b]
            verify(delta != 0 and (delta > 0) == ((n-a-b)%2 == 0),
                   f'critical sign for a={a}, b={b}, n={n}')

# Direct exact enumeration over all permutations of up to eight labels.
for n in range(5, 9):
    cyc_sums = {(a,b): [0,0,0] for a in range(2,n) for b in range(a+1,n+1) if a+b<=n}
    dcount = 0
    for p in permutations(range(n)):
        if any(p[i] == i for i in range(n)):
            continue
        dcount += 1
        seen = set()
        counts = [0]*(n+1)
        for i in range(n):
            if i in seen: continue
            j=i; length=0
            while j not in seen:
                seen.add(j);length+=1;j=p[j]
            counts[length]+=1
        for (a,b), totals in cyc_sums.items():
            totals[0] += counts[a]
            totals[1] += counts[b]
            totals[2] += counts[a]*counts[b]
    verify(Fraction(dcount, factorial(n))==Q[n], f'derangement count n={n}')
    for (a,b),(sa,sb,sab) in cyc_sums.items():
        observed = Fraction(sab, dcount)-Fraction(sa*sb, dcount*dcount)
        predicted = cov_formula(1, Q, n, a, b)
        verify(observed == predicted, f'permutation census n={n}, a={a}, b={b}')

# For integer theta=2,3 the normalizers are exactly exp(-theta)
# times a polynomial plus the superfactorially small tail.
# We verify a broad rational-parameter interval of finite covariances, not
# claiming those finite signs characterize the eventual asymptotic sign.
for theta in [Fraction(1,4), Fraction(1,2), Fraction(3,4), Fraction(1), Fraction(5,4), Fraction(2), Fraction(3)]:
    h=h_coefficients(theta, 105)
    for a,b in [(2,3), (2,4), (3,5), (4,6)]:
        for n in range(a+b, 81):
            v=cov_formula(theta, h, n, a, b)
            verify(v == (theta*theta/Fraction(a*b))*(h[n-a-b]/h[n]-(h[n-a]/h[n])*(h[n-b]/h[n])),
                   'equivalent exact formulas')

print(f'PASS: {checks} exact checks (including complete derangement census for n=5..8).')
