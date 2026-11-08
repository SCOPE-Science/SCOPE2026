"""Exact finite checks for a two-balance modal formula on random directed graphs.

Run with Python 3 (standard library only): python checker.py.
The infinite mixed-Poisson limit is proved analytically, not by this checker.
"""
from fractions import Fraction
from itertools import product
from math import comb, pi

TYPES = tuple((x, y) for x in (-1, 0, 1) for y in (-1, 0, 1))
WEIGHT = {-1: 1, 0: 2, 1: 1}


def balance_subsets(deltas, v):
    other = [d for j, d in enumerate(deltas) if j != v]
    count = 0
    for mask in range(1 << len(other)):
        x = sum(d[0] for j, d in enumerate(other) if mask >> j & 1)
        y = sum(d[1] for j, d in enumerate(other) if mask >> j & 1)
        count += (x == 0 and y == 0)
    return Fraction(count, 1 << len(other))


def exact_finite_statistics(n):
    p0, mean, second_factorial = Fraction(0), Fraction(0), Fraction(0)
    for deltas in product(TYPES, repeat=n):
        weight = Fraction(1, 16**n)
        for d in deltas:
            weight *= WEIGHT[d[0]] * WEIGHT[d[1]]
        ps = [balance_subsets(deltas, v) / 2 for v in range(1, n)]
        q0 = Fraction(1)
        for p in ps:
            q0 *= (1 - p)
        p0 += weight * q0
        mean += weight * sum(ps)
        second_factorial += weight * sum(ps[i] * ps[j]
                                             for i in range(len(ps))
                                             for j in range(len(ps)) if i != j)
    return p0, mean, second_factorial


def direct_p0_n3():
    # Every directed edge on three vertices is enumerated; loop edges are forbidden.
    n, favorable, total = 3, 0, 0
    arcs = [(i, j) for i in range(n) for j in range(n) if i != j]
    for deltas in product(TYPES, repeat=n):
        w = 1
        for d in deltas:
            w *= WEIGHT[d[0]] * WEIGHT[d[1]]
        for mask in range(1 << len(arcs)):
            adj = [[False] * n for _ in range(n)]
            for k, (u, v) in enumerate(arcs):
                adj[u][v] = bool((mask >> k) & 1)
            z = 0
            for v in range(1, n):
                good = all(sum(deltas[j][coord] for j in range(n) if adj[v][j]) == 0
                           for coord in range(2))
                z += bool(adj[0][v]) and good
            total += w
            favorable += w * (z == 0)
    assert total == 16**n * 2**len(arcs)
    return Fraction(favorable, total)


def exact_unconditional_mean(n):
    # Condition on the outdegree K: two independent balance tests have
    # success probability [binom(2K,K)/4^K]^2.
    return sum((Fraction(comb(n-1, k), 2**(n-1))
                * Fraction(comb(2*k, k), 4**k)**2
                for k in range(n)), Fraction(0)) * Fraction(n-1, 2)


def main():
    for n in (2, 3, 4):
        p0, mean, factorial2 = exact_finite_statistics(n)
        assert mean == exact_unconditional_mean(n), (n, mean)
        assert 0 < p0 < 1 and 0 <= factorial2 <= n*n
        print('n=', n, 'P(Z=0)=', p0, 'E[Z]=', mean,
              'E[(Z)_2]=', factorial2)
        if n == 3:
            assert p0 == direct_p0_n3(), 'direct arc enumeration disagrees'
    limit_mean = 1 / pi
    assert abs(float(exact_unconditional_mean(300)) - limit_mean) < 0.001
    assert abs((2/pi)/2 - limit_mean) < 1e-15
    print('DENSE_MODAL_UNIFORM_MIXED_POISSON_FINITE_CHECKS_OK')

if __name__ == '__main__':
    main()
