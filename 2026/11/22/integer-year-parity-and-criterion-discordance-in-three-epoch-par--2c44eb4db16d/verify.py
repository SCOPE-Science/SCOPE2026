#!/usr/bin/env python3
"""Standalone numerical and exact-arithmetic consistency checks for a 3-epoch annual-parallax design.

The mathematical proof of global optimality is in RESULT.md; finite tests are not a proof.
"""
import math
from fractions import Fraction

count = 0

def check(assertion, message):
    global count
    assert assertion, message
    count += 1


def variance_factor(K, t):
    # Var(pi_hat) / sigma^2; infinite when the parallax column is aliased.
    q = 1 - math.cos(2 * math.pi * t)
    if abs(q) < 1e-13:
        return math.inf
    return (1 + (1-t/K)**2 + (t/K)**2) / (q*q)


def score(K, t):
    # reciprocal of the variance factor
    q = 1 - math.cos(2 * math.pi * t)
    return q*q / (1 + (1-t/K)**2 + (t/K)**2)


def even_root(K):
    assert K >= 2 and K % 2 == 0
    def eq(v):
        return math.pi / math.tan(math.pi * v) - v / (1.5*K*K + 2*v*v)
    low, high = 0.2, 0.5
    for _ in range(100):
        m = (low+high)/2
        if eq(m) > 0:
            low = m
        else:
            high = m
    return (low+high)/2

# Linear nuisance cancellation; coefficients sum to zero, cancel an affine trend.
for K in range(1, 41):
    for i in range(1, 111):
        t = K * i / 111
        a, b, pi = 2.3, -0.41, 0.77
        y = lambda s: a + b*s + pi*math.cos(2*math.pi*s)
        z = y(t) - (1-t/K)*y(0) - t/K*y(K)
        expected = pi * (math.cos(2*math.pi*t)-1)
        check(abs(z-expected) < 2e-12, ('contrast', K, t))

# Odd endpoints: exact central phase attains universal information bound.
for K in range(1, 60, 2):
    t = K/2
    check(abs(variance_factor(K,t)-3/8) < 2e-13, ('odd exact',K))
    for i in range(1, 1601):
        u = K*i/1601
        check(score(K,u) <= 8/3 + 3e-12, ('odd global',K,u))

# Even endpoints: two exactly symmetric strict global optima, not half-integers.
previous_even_var = math.inf
for K in range(2, 61, 2):
    v = even_root(K)
    u0,u1 = K/2-v,K/2+v
    check(0<v<0.5,('root interval',K))
    check(abs(score(K,u0)-score(K,u1)) < 2e-13,('symmetry',K))
    check(variance_factor(K,u0) > 3/8, ('parity loss',K))
    check(variance_factor(K,u0) < previous_even_var, ('monotone even',K))
    previous_even_var=variance_factor(K,u0)
    check(score(K,u0) > score(K,K/2-0.5), ('c versus D',K))
    for i in range(1, 2401):
        u = K*i/2401
        check(score(K,u) <= score(K,u0)+4e-12,('even global',K,u))

# The elementary exact finite-epoch cases do not depend on floating-point cosine.
for K in range(1,21):
    for j in range(1, 2*K):
        t = Fraction(j,2)
        if j%2==0:
            continue  # identical annual phase and hence not identifiable
        D = 1+(1-t/K)**2+(t/K)**2
        V = D/4
        check(V>=Fraction(3,8),('exact lower bound',K,j))
        if 2*t==K:
            check(V==Fraction(3,8),('odd midpoint',K))

# Asymptotic correction and concrete two-year benchmark.
for K in [20,40,80,160]:
    shift = 0.5-even_root(K)
    check(abs(shift*K*K-1/(3*math.pi*math.pi))<0.001,('large K',K))
check(abs(even_root(2)-0.49230937782822337)<5e-13,'K=2 root')
check(abs(variance_factor(2,1-even_root(2))-0.40576956644067164)<1e-12,'K=2 var')
print(f'PASS {count} deterministic assertions; no infinite-proof claim.')
