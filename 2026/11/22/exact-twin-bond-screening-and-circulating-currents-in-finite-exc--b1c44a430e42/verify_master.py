#!/usr/bin/env python3
"""Exact finite-state master-equation and localized current checks."""
from fractions import Fraction as Q
from itertools import combinations
from math import comb


def check(n, particles, conductances, forward, backward):
    e = {tuple(sorted((u, v))): Q(w) for u, v, w in conductances}
    assert (0, 1) not in e
    assert all(e.get((0, z), Q(0)) == e.get((1, z), Q(0))
               for z in range(2, n))
    s = sum((e.get((0, z), Q(0)) for z in range(2, n)), Q(0))
    a, b = Q(forward), Q(backward)
    d = (b - a) / (s + a + b)
    states = [sum(1 << j for j in seq)
              for seq in combinations(range(n), particles)]
    z = comb(n, particles)
    weights = {x: (1 + d * (((x >> 0) & 1) - ((x >> 1) & 1))) / z
               for x in states}
    assert sum(weights.values()) == 1
    incoming = {x: Q(0) for x in states}
    rates = list(e.items()) + [((0, 1), None)]
    for x in states:
        for (u, v), c in rates:
            hu, hv = (x >> u) & 1, (x >> v) & 1
            if hu == hv:
                continue
            rate = (a if hu else b) if c is None else c
            y = x ^ (1 << u) ^ (1 << v)
            incoming[x] -= weights[x] * rate
            incoming[y] += weights[x] * rate
    assert all(x == 0 for x in incoming.values())
    p = Q(particles * (n - particles), n * (n - 1))
    def current(u, v, wuv, wvu):
        return sum(weights[x] * (
            wuv * ((x >> u) & 1) * (1 - ((x >> v) & 1))
            - wvu * ((x >> v) & 1) * (1 - ((x >> u) & 1)))
                   for x in states)
    assert current(0, 1, a, b) == (a-b)*p*s/(s+a+b)
    for (u, v), c in e.items():
        if u == 0:
            want = c*d*p
        elif u == 1:
            want = -c*d*p
        else:
            want = Q(0)
        assert current(u, v, c, c) == want, (u, v, want)
    for pattern in range(1 << (n - 2)):
        lhs = sum(weights[x] for x in states if x >> 2 == pattern)
        rhs = Q(sum(x >> 2 == pattern for x in states), z)
        assert lhs == rhs
    return len(states)

cases = [
    (5, 2, [(0,2,1),(1,2,1),(2,3,3),(3,4,2)], 2, 3),
    (7, 3, [(0,2,Q(2,3)),(1,2,Q(2,3)),(0,3,Q(7,5)),
            (1,3,Q(7,5)),(2,4,4),(4,5,2),(5,6,3),
            (3,6,Q(3,4)),(2,3,1)], Q(5,3), Q(1,4)),
    (4, 1, [(0,2,2),(1,2,2),(2,3,3)], Q(3,4), Q(9,5)),
    (6, 5, [(0,2,1),(1,2,1),(0,3,2),(1,3,2),
            (2,4,1),(4,5,1),(5,3,1)], 5, 1),
    (4, 2, [(0,2,1),(1,2,1),(0,3,1),(1,3,1),(2,3,1)], 1, 1)
]
if __name__ == '__main__':
    total = sum(check(*t) for t in cases)
    print('PASS: exact row balance, all edge currents, untouched-site joint marginals;')
    print('5 connected weighted geometries/fillings,', total, 'distinct state rows')
