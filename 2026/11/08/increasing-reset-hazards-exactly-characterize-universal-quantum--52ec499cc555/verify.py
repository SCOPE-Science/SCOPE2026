#!/usr/bin/env python3
"""Exact finite-horizon checks for the renewal-reset channel divisibility identity.

This program checks finite rational instances; the general theorem is proved separately.
No external libraries, data, or network access are required.
"""
from fractions import Fraction as F
from itertools import product


def age_laws(h):
    ages = [[F(1)]]
    for rate in h:
        prev = ages[-1]
        out = [sum((v * h[a] for a, v in enumerate(prev)), F(0))]
        out.extend(v * (1 - h[a]) for a, v in enumerate(prev))
        ages.append(out)
    return ages


def coefficients(h, ages, t):
    k = 1-h[t]
    before = ages[t]
    after = ages[t+1]
    return [after[a] - (k*before[a-1] if a else 0)
            for a in range(t+1)]


def conjugate_shift(m):
    d = len(m)
    return [[m[(i-1)%d][(j-1)%d] for j in range(d)] for i in range(d)]


def matrix_unit(d, i, j):
    return [[F(1) if (k == i and l == j) else F(0)
             for l in range(d)] for k in range(d)]


def channel(m, age, t, d):
    # Age t corresponds to no reset, so the original input survives with S(t).
    s = age[t]
    trace = sum(m[i][i] for i in range(d))
    y = m
    for _ in range(t):
        y = conjugate_shift(y)
    out = [[s*y[i][j] for j in range(d)] for i in range(d)]
    for a in range(t):
        out[a%d][a%d] += trace*age[a]
    return out


def link(m, k, c, d):
    y = conjugate_shift(m)
    trace = sum(m[i][i] for i in range(d))
    out = [[k*y[i][j] for j in range(d)] for i in range(d)]
    for a, ca in enumerate(c):
        out[a%d][a%d] += trace*ca
    return out


def check(h):
    ages = age_laws(h)
    assertions = 0
    for j, age in enumerate(ages):
        assert sum(age) == 1
        assertions += 1
        if j:
            assert age[-1] == __import__('functools').reduce(
                lambda p, q: p*(1-q), h[:j], F(1))
            assertions += 1
    for t in range(len(h)):
        d = t+2
        c = coefficients(h, ages, t)
        assert sum(c) == h[t]
        assertions += 1
        if all(h[t] >= h[a] for a in range(t)):
            assert all(x >= 0 for x in c)
            assertions += 1
        if t and h[t] < h[t-1]:
            assert c[t] == h[0]*ages[t-1][-1]*(h[t]-h[t-1]) < 0
            # The shift returns |t> to a different basis vector.
            assert (t+1)%d != t
            assertions += 2
        for i, j in product(range(d), repeat=2):
            x = matrix_unit(d, i, j)
            first = channel(x, ages[t], t, d)
            lhs = link(first, 1-h[t], c, d)
            rhs = channel(x, ages[t+1], t+1, d)
            assert lhs == rhs, (h, t, i, j)
            assertions += 1
    return assertions


def main():
    q = [F(i, 8) for i in range(1, 8)]
    cases = [tuple([F(1, 4)]*6),
             (F(3,4),F(1,4),F(1,2),F(3,8)),
             (F(1,4),F(3,4),F(7,8),F(7,8)),
             (F(1,8),F(2,8),F(3,8),F(4,8),F(5,8),F(6,8))]
    # A deterministic varied sample of rational hazard profiles; not an exhaustive proof.
    for n in range(1, 7):
        cases.extend(tuple(q[(13*k+17*n+11*i*i+7*i) % 7]
                           for i in range(n)) for k in range(40))
    total = sum(check(h) for h in cases)
    assert coefficients((F(3,4),F(1,4)),
                        age_laws((F(3,4),F(1,4))),1) == [F(5,8),-F(3,8)]
    print(f'PASS: {len(cases)} finite rational profiles, {total} exact identities/checks')
    print('PASS: explicit qubit descent witness has negative output -3/8')
    print('LIMIT: finite checks do not establish the all-dimensional iff theorem')

if __name__ == '__main__':
    main()
