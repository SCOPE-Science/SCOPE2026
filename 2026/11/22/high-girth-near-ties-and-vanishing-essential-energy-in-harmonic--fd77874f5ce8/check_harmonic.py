#!/usr/bin/env python3
"""Exact rational checks for two-terminal three-path harmonic births.

Standard-library only. Finite tests corroborate the general algebraic proof.
"""
from collections import Counter
from fractions import Fraction


def check(a: int, b: int) -> None:
    assert a >= 2 and b >= a
    # Each path is oriented from the first terminal to the second.
    vertices = ["u", "v"]
    p = ["u"] + [f"p_{i}" for i in range(1, a)] + ["v"]
    q = ["u"] + [f"q_{i}" for i in range(1, b)] + ["v"]
    vertices.extend(p[1:-1] + q[1:-1])
    edges = [(p[i], p[i+1]) for i in range(a)]
    edges += [(q[i], q[i+1]) for i in range(b)]
    edges += [("u", "v")]
    assert len(set(vertices)) == a+b and len(set(edges)) == a+b+1
    c = [Fraction(-b, a+b)]*a + [Fraction(-a, a+b)]*b + [Fraction(1)]
    old = [Fraction(1)]*a + [Fraction(-1)]*b + [Fraction(0)]
    diff = Counter()
    for (src, dest), coef in zip(edges, c):
        diff[src] -= coef
        diff[dest] += coef
    assert all(coef == 0 for coef in diff.values()), 'not a cycle'
    dot = sum(x*y for x, y in zip(c, old))
    assert dot == 0, 'not orthogonal to old cycle'
    norm2 = sum(x*x for x in c)
    assert norm2 == 1 + Fraction(a*b, a+b)
    assert Fraction(1, 1) / norm2 == Fraction(a+b, a+b+a*b)
    # Independent 1-D minimum norm calculation: e - P + t(P-Q).
    t = Fraction(a, a+b)
    independent = [t-1]*a + [-t]*b + [Fraction(1)]
    assert independent == c
    deg = Counter()
    for u,v in edges:
        deg[u] += 1
        deg[v] += 1
    assert sorted(deg.values()) == [2]*(a+b-2) + [3,3]
    assert a + 1 >= 3
    assert max(abs(z) for z in c[:-1]) < abs(c[-1])
    print(f"PASS: a={a}, b={b}, path_coeff={abs(c[0])}, other_coeff={abs(c[a])}, essential_energy={1/norm2}, girth={a+1}")


if __name__ == '__main__':
    for ab in [(2,2),(2,3),(2,7),(3,20),(4,9),(7,91),(15,300),(47,4700)]:
        check(*ab)
    print('PASS: eight exact cases; general conclusions follow from the written proof, not enumeration.')
