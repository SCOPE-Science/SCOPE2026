"""Exact finite checks of cyclic-triangle / strongly connected quadruple moments.
Usage: python verify.py
No nonstandard Python packages required. Infinite-n claims rest on the proof.
"""
from fractions import Fraction as F
from itertools import combinations
from math import comb


def tournament_moments(n):
    edges = tuple(combinations(range(n), 2))
    triples = tuple(combinations(range(n), 3))
    quads = tuple(combinations(range(n), 4))
    sum_a = sum_b = sum_aa = sum_bb = sum_ab = 0
    nstates = 1 << len(edges)
    for mask in range(nstates):
        def beats(u, v):
            a, b = min(u, v), max(u, v)
            bit = (mask >> edge_pos[(a, b)]) & 1
            return bool(bit) if u < v else not bit

        def cyc(x, y, z):
            return ((beats(x, y) and beats(y, z) and beats(z, x)) or
                    (beats(x, z) and beats(z, y) and beats(y, x)))

        def strong4(quad):
            for root in quad:
                reached = {root}
                frontier = [root]
                while frontier:
                    u = frontier.pop()
                    for v in quad:
                        if v not in reached and beats(u, v):
                            reached.add(v)
                            frontier.append(v)
                if len(reached) != 4:
                    return False
            return True

        a = sum(cyc(*triple) for triple in triples)
        b = sum(strong4(quad) for quad in quads)
        sum_a += a
        sum_b += b
        sum_aa += a*a
        sum_bb += b*b
        sum_ab += a*b
    t = F(1, nstates)
    ea, eb = sum_a*t, sum_b*t
    va, vb, cab = sum_aa*t-ea*ea, sum_bb*t-eb*eb, sum_ab*t-ea*eb
    edge_name = f'n={n} ({nstates} tournaments)'
    assert ea == F(comb(n, 3), 4), (edge_name, 'mean A')
    assert eb == F(3*comb(n, 4), 8), (edge_name, 'mean B')
    assert va == F(3*comb(n, 3), 16), (edge_name, 'variance A', va)
    assert cab == F(3*comb(n, 4), 8), (edge_name, 'covariance', cab)
    assert vb == F(3*(n-3)*(4*n-11)*comb(n, 3), 256), (edge_name, 'variance B', vb)
    beta = F(n-3, 2)
    assert vb-beta*beta*va == F(3*(n-3)*comb(n, 3), 256)
    assert cab*cab / (va*vb) == F(4*n-12, 4*n-11)
    print(edge_name, 'PASSED', 'means', ea, eb, 'variances', va, vb, 'covariance', cab)


if __name__ == '__main__':
    for n in (4, 5, 6):
        edge_pos = {e: i for i, e in enumerate(combinations(range(n), 2))}
        tournament_moments(n)
    print('All rational complete-enumeration checks passed; n>=7 requires the analytic proof.')
