#!/usr/bin/env python3
"""Exact finite diagnostics for a switched-coordinate value certificate.

This checker supplements, but does not replace, the all-dimension proof.
It uses only Python's standard library and rational arithmetic.
"""
from fractions import Fraction as F
from itertools import product


def groups(n, m):
    return [tuple(range(j, n, m)) for j in range(m)]


def check(n, m, rho):
    assert 2 <= n and 1 <= m <= n and F(0) < rho < F(1)
    blocks = groups(n, m)
    radius = max(map(len, blocks))
    beta = rho * rho / (1 - rho * rho)
    bound = F(radius) / (radius - (radius - 1) * rho * rho)
    assert bound == (1 + beta) / (1 + beta / radius)
    # Exact diagonal Bellman LMIs for the co-complete graph.
    for i in range(n):
        owner = i % m
        for target in range(m):
            for k in range(n):
                lhs = 1 + (beta if k in blocks[owner] else 0)
                rhs = 1 + (rho * rho * (1 + (beta if i in blocks[target] else 0)) if k == i else 0)
                assert lhs >= rhs, (n, m, rho, i, target, k)
    # Exhaustive rational-vector probes for small ambient dimensions.
    for sample in product((-2, -1, 0, 1, 2), repeat=min(n, 5)):
        x = tuple(sample) + (0,) * max(0, n - 5)
        if not any(x):
            continue
        energy = sum(z * z for z in x)
        target = energy + beta * max(z * z for z in x)
        cert = energy + beta * max(sum(x[i] ** 2 for i in b) for b in blocks)
        assert target <= cert <= bound * target, (n, m, rho, x)
    # The largest block with equal-amplitude support attains the bound.
    support = max(blocks, key=len)
    x = tuple(1 if i in support else 0 for i in range(n))
    energy = sum(t * t for t in x)
    target = energy + beta
    cert = energy + beta * energy
    assert cert / target == bound
    return 1


def check_sign_average():
    # An example with nonzero off-diagonal terms verifies the exact cancellation.
    p = ((F(7, 3), F(-5, 7), F(2, 3)),
         (F(-5, 7), F(11, 4), F(4, 9)),
         (F(2, 3), F(4, 9), F(13, 5)))
    vals = []
    for signs in product((-1, 1), repeat=3):
        vals.append(sum(F(signs[i] * signs[j], 3) * p[i][j]
                        for i in range(3) for j in range(3)))
    assert sum(vals, F(0)) / len(vals) == sum(p[i][i] for i in range(3)) / 3
    return 1


def check_pigeonhole():
    cases = 0
    for n in range(2, 7):
        for m in range(1, n + 1):
            for assignment in product(range(m), repeat=n):
                occupancy = [assignment.count(j) for j in range(m)]
                assert max(occupancy) >= (n + m - 1) // m
                cases += 1
    return cases


def main():
    cases = 0
    for n in range(2, 10):
        for m in range(1, n + 1):
            for rho in (F(1, 4), F(2, 3), F(9, 10)):
                cases += check(n, m, rho)
    assert check_sign_average() == 1
    pigeon = check_pigeonhole()
    print(f"PASS: {cases} rational graph-and-witness cases; "
          f"{pigeon} exhaustive finite assignments; one exact sign-average check")


if __name__ == "__main__":
    main()
