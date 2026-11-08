"""Finite exact checks for a recursive-tree leaf-depth martingale identity.

This script verifies local identities over every recursive tree of orders
2,...,8 and every legal next-parent choice. It does not replace the
asymptotic martingale central-limit proof.
"""
from fractions import Fraction as F
from itertools import product


def observables(parents):
    n = len(parents)
    depth = [0] * n
    child_count = [0] * n
    for i in range(1, n):
        p = parents[i]
        depth[i] = 1 + depth[p]
        child_count[p] += 1
    leaf = [int(c == 0) for c in child_count]
    p = sum(depth)
    l = sum(leaf)
    e = sum(z * d for z, d in zip(leaf, depth))
    b = F(p, n)
    c = F(e) - F(l) * b
    q = sum((F(d) - b) ** 2 for d in depth) / n
    w = F(l) - F(n, 2)
    f = c - F(n, 4)
    return depth, leaf, p, l, e, b, c, q, w, f


def check():
    assertions = 0
    for n in range(2, 9):
        for rest in product(*(range(j) for j in range(1, n))):
            parents = (0,) + rest
            d, leaf, p, l, e, b, c, q, w, f = observables(parents)
            assert sum(leaf) >= 1
            assertions += 1
            lp = F(l, n)
            xis = []
            etas = []
            for parent in range(n):
                nxt = parents + (parent,)
                dd, ii, pp, ll, ee, bb, cc, qq, ww, ff = observables(nxt)
                r = F(d[parent]) - b
                ind = leaf[parent]
                assert pp == p + d[parent] + 1
                assert ll == l + 1 - ind
                assert ee == e + d[parent] + 1 - ind * d[parent]
                assert bb == b + F(r + 1, n + 1)
                assert qq == F(n, n + 1) * q + F(n, (n + 1) ** 2) * (r + 1) ** 2
                assert cc - c == F(n, n + 1) * (1 - lp - ind) * r + F(n - l + ind, n + 1)
                xi = F(n, n + 1) * ((1 - lp - ind) * r + c / n) + F(ind - lp, n + 1)
                assert ff == F(n, n + 1) * f - F(n - 1, n * (n + 1)) * w + F(1, 4 * (n + 1)) + xi
                et = qq - q - F(n - q, (n + 1) ** 2)
                xis.append(xi)
                etas.append(et)
                assertions += 8
            assert sum(xis) == 0
            assert sum(etas) == 0
            assertions += 2
            sq_leaf = sum(F(leaf[j]) * (F(d[j]) - b) ** 2 for j in range(n)) / n
            expr = (1 - lp) ** 2 * q + (2 * lp - 1) * sq_leaf - (c / n) ** 2
            a_list = [(1 - lp - leaf[j]) * (F(d[j]) - b) + c / n for j in range(n)]
            assert sum(a_list) == 0
            assert sum(a * a for a in a_list) / n == expr
            assertions += 2
    print('PASS: {} exact rational assertions, all recursive trees of sizes 2..8'.format(assertions))


if __name__ == '__main__':
    check()
