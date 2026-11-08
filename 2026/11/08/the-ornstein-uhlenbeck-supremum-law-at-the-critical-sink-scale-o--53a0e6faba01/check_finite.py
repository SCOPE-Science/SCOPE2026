"""Finite-state algebraic diagnostics for the binomial-update boundary model.

Run with Python 3.10+: python check_finite.py
The proof of the limiting law is analytic and is not replaced by these tests.
"""
from fractions import Fraction as Q
from math import comb

checks = 0

def eq(a, b):
    global checks
    assert a == b, (a, b)
    checks += 1


def transition(n, p, q, y):
    u = (1-q) * (n-y)*p/n
    d = (1-q) * y*(1-p)/n
    return d, 1-u-d, u

for n in range(2, 35):
    for p in [Q(1, 5), Q(1, 3), Q(1, 2), Q(2, 3), Q(4, 5)]:
        for q in [Q(1, 9), Q(2, 7), Q(1, 2), Q(5, 6)]:
            pi = [Q(comb(n, y))*(p**y)*((1-p)**(n-y)) for y in range(n+1)]
            eq(sum(pi), Q(1))
            for y in range(n+1):
                d, stay, u = transition(n, p, q, y)
                eq(d+stay+u, Q(1))
                eq(u-d, -(1-q)*(Q(y)-n*p)/n)
                eq(d+u, (1-q)*(p+(1-2*p)*Q(y)/n))
                assert min(d,stay,u) >= 0
                checks += 1
                if y < n:
                    next_d, _, _ = transition(n, p, q, y+1)
                    eq(pi[y]*u, pi[y+1]*next_d)
            eq(sum(pi[y]*Q(y) for y in range(n+1)), n*p)
            eq(sum(pi[y]*(Q(y)-n*p)**2 for y in range(n+1)), n*p*(1-p))

# Direct microscopic verification that refreshing one chosen Bernoulli coordinate
# leaves the Bernoulli product law invariant, even for a fixed update index.
from itertools import product
for n in range(2, 7):
    for p in [Q(1,4), Q(2,5), Q(3,4)]:
        states = list(product((0,1), repeat=n))
        initial = {s: p**sum(s)*(1-p)**(n-sum(s)) for s in states}
        for index in range(n):
            updated = {s: Q(0) for s in states}
            for state, w in initial.items():
                for value in (0,1):
                    out = list(state)
                    out[index] = value
                    updated[tuple(out)] += w*(p if value else 1-p)
            for state in states:
                eq(updated[state], initial[state])

# Consistency of the first-hit boundary: each transition changes the gap
# (n-Z-Y) by at most one, never jumping from positive to negative.
for n in range(2, 18):
    for y in range(n+1):
        for z in range(n+1-y):
            if n-z-y == 0:
                continue
            for dy, dz in ((-1,0),(0,0),(1,0),(0,1)):
                if dy == 1 and y == n:
                    continue
                gap_new = n-(z+dz)-(y+dy)
                assert gap_new >= 0
                checks += 1

print(f'PASS: {checks} exact finite assertions')
