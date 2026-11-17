#!/usr/bin/env python3
"""Finite diagnostics for the coordinate-entropy summation identity.

No finite calculation is used as a proof for arbitrary sequence lengths.
"""
import math
import random


def ent(p):
    return -sum(z * math.log(z) for z in p if z > 0)


def phi(v):
    a = [abs(z) for z in v]
    s = sum(a)
    return s * (1 + ent([z / s for z in a])) if s > 0 else 0.0


def test():
    rng = random.Random(20261111)
    count = 0
    for m in range(2, 9):
        for n in range(2, 8):
            for _ in range(200):
                x = [
                    [(rng.random() if rng.random() < 0.5 else -rng.random())
                     if rng.random() < 0.65 else 0.0 for _ in range(m)]
                    for _ in range(n)
                ]
                if not any(abs(z)>0 for row in x for z in row):
                    x[0][0] = 1.0
                S = sum(sum(abs(z) for z in row) for row in x)
                if not S:
                    continue
                alpha = [sum(abs(z) for z in row) / S for row in x]
                b = [sum(abs(x[i][j]) for i in range(n)) for j in range(m)]
                beta = [z / S for z in b]
                hc = sum(alpha[i] * ent([abs(z) / (S * alpha[i]) for z in x[i]])
                         for i in range(n) if alpha[i] > 0)
                hij = ent(alpha) + hc - ent(beta)
                y = [sum(x[i][j] for i in range(n)) for j in range(m)]
                cancel = phi(b) - phi(y)
                lhs = (1 + math.log(n)) * sum(phi(row) for row in x) - phi(y)
                rhs = S * (math.log(n) - ent(alpha) + math.log(n) * hc + hij) + cancel
                assert abs(lhs - rhs) < 1e-8 * max(1, S)
                assert lhs > -1e-9 and cancel > -1e-9
                count += 1
    for n in range(2, 31):
        x = [[float(i == j) for j in range(n)] for i in range(n)]
        y = [sum(row[j] for row in x) for j in range(n)]
        assert abs(phi(y) - (1 + math.log(n)) * sum(phi(row) for row in x)) < 1e-9
    assert count == 8400, count
    print('ENTROPY_GAUGE_DEFICIT_OK', count)


if __name__ == '__main__':
    test()
