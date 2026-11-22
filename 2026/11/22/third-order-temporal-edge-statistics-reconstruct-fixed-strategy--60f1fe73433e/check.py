"""Exact rational checks for fixed-strategy vertex-clock edge-environment dynamics.

Run: python check.py
Only Python standard library is needed.
"""
from fractions import Fraction as F
from itertools import combinations


def stationary_model(edges, n, p, q, omega):
    ecount = len(edges)
    assert 0 < p < 1 and 0 < q < 1 and 0 < omega < 1
    assert all(0 <= a < n and 0 <= b < n and a != b for a, b in edges)
    incident = [tuple(i for i, (a, b) in enumerate(edges) if v in (a, b))
                for v in range(n)]
    size = 1 << ecount
    prob = [[F(0) for _ in range(size)] for _ in range(size)]
    for state in range(size):
        prob[state][state] += 1 - omega
        for v in range(n):
            outs = [(state, F(1))]
            for e in incident[v]:
                nxt = []
                orig = (state >> e) & 1
                flip = q if orig else p
                for target, mass in outs:
                    nxt.append((target, mass * (1 - flip)))
                    nxt.append((target ^ (1 << e), mass * flip))
                outs = nxt
            for target, mass in outs:
                prob[state][target] += omega * mass / n
    assert all(sum(row) == 1 for row in prob)
    pi = p / (p + q)
    invariant = [pi ** s.bit_count() * (1 - pi) ** (ecount - s.bit_count())
                 for s in range(size)]
    assert sum(invariant) == 1
    for target in range(size):
        assert sum(invariant[s] * prob[s][target] for s in range(size)) == invariant[target]
    r = 1 - p - q
    result = {}
    for mask in range(1, size):
        signature = []
        for state in range(size):
            x = F(1)
            for e in range(ecount):
                if mask & (1 << e):
                    x *= ((state >> e) & 1) - pi
            signature.append(x)
        value = (1 - omega) + omega * sum(
            r ** sum(bool(mask & (1 << e)) for e in incident[v])
            for v in range(n)) / n
        for s in range(size):
            assert sum(prob[s][t] * signature[t] for t in range(size)) == value * signature[s], (s, mask)
        norm = (pi * (1 - pi)) ** mask.bit_count()
        assert sum(invariant[s] * signature[s] ** 2 for s in range(size)) == norm
        result[mask] = value
    return result


def run():
    p, q, omega = F(1, 2), F(1, 4), F(2, 3)
    a = [(0,1),(0,2),(0,3),(4,5),(5,6),(6,4)]  # claw then triangle
    b = [(0,1),(1,2),(2,0),(3,4),(3,5),(3,6)]  # triangle then claw
    la = stationary_model(a, 7, p, q, omega)
    lb = stationary_model(b, 7, p, q, omega)
    for order in (1,2):
        for inds in combinations(range(6), order):
            mask = sum(1 << i for i in inds)
            assert la[mask] == lb[mask]
    triple = (1 << 0) | (1 << 1) | (1 << 2)
    r = 1-p-q
    expected = omega * (1-r)**3 / 7
    assert la[triple] == F(155,224)
    assert lb[triple] == F(41,56)
    assert lb[triple] - la[triple] == expected == F(9,224)
    assert la[1] == F(6,7)
    assert la[3] == F(43,56)  # adjacent pair
    assert la[(1<<0) | (1<<3)] == F(5,7)  # disjoint pair
    assert la[3] - la[(1<<0) | (1<<3)] == omega*(1-r)**2 / 7
    assert all(x == y for mask,x in la.items() for y in [lb[mask]] if mask.bit_count()<=2)
    print('PASS: exact 64-state matrices, invariant laws, all 63 eigenrelations on each graph')
    print('PASS: all order-one and order-two stationary-lag signatures match')
    print('PASS: third-order claw/triangle separation is', expected)
    print('Parameters p=1/2 q=1/4 omega=2/3 N=7; no isolated vertices.')


if __name__ == '__main__':
    run()
