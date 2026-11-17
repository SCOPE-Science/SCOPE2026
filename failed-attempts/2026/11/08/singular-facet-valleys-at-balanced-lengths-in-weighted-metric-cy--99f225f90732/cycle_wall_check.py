"""Exact-rational direct active-set checks for one-edge weighted metric cycles.

Run: python cycle_wall_check.py
The checker enumerates independent edge-constraint subsets and their signs,
reconstructs actual Lipschitz potentials, and compares unique vertices with
closed binomial counts and neighboring nondegenerate regimes.
"""
from fractions import Fraction
from itertools import product
from math import comb


def vertices(n, t):
    t = Fraction(t)
    m = n - 1
    lengths = (Fraction(1),) * m + (t,)
    values = set()
    for omitted in range(n):
        retained = [j for j in range(n) if j != omitted]
        for signs in product((-1, 1), repeat=m):
            difference = [Fraction(0)] * n
            for j, eps in zip(retained, signs):
                difference[j] = eps * lengths[j]
            difference[omitted] = -sum(difference)
            if abs(difference[omitted]) > lengths[omitted]:
                continue
            potential = [Fraction(0)]
            for j in range(m):
                potential.append(potential[-1] + difference[j])
            assert potential[-1] - potential[0] == -difference[-1]
            assert all(abs(difference[j]) <= lengths[j] for j in range(n))
            active = sum(abs(difference[j]) == lengths[j] for j in range(n))
            assert active >= m
            values.add(tuple(potential))
    return values


def closed_at_wall(n, p):
    m = n - 1
    return sum(comb(m, k) for k in range(m + 1)
               if abs(m - 2 * k) <= p)


def active_count(n, t, potential):
    lengths = (Fraction(1),) * (n-1) + (Fraction(t),)
    edges = [potential[i+1]-potential[i] for i in range(n-1)]
    edges.append(potential[0]-potential[-1])
    return sum(abs(e) == ell for e, ell in zip(edges, lengths))


def run():
    cases = 0
    for n in range(4, 12):
        m = n-1
        for p in range(1, m):
            if (m-p) % 2:
                continue
            lo = vertices(n, Fraction(2*p-1, 2))
            wall = vertices(n, p)
            hi = vertices(n, Fraction(2*p+1, 2))
            k = (m-p)//2
            C = comb(m, k)
            assert len(wall) == closed_at_wall(n, p), (n,p,'wall')
            assert len(lo)-len(wall) == (m+p-2)*C, (n,p,'left')
            assert len(hi)-len(wall) == (m-p)*C, (n,p,'right')
            assert sum(active_count(n,p,v) == n for v in wall) == 2*C
            assert sum(active_count(n,p,v) == n-1 for v in wall) == len(wall)-2*C
            print('n=%d p=%d left=%d wall=%d right=%d nonsimplicial=%d'%(
                n,p,len(lo),len(wall),len(hi),2*C))
            cases += 1
    assert cases == 20, cases
    print('ALL_WEIGHTED_CYCLE_WALL_TESTS_PASSED',cases,'critical_cases')


if __name__ == '__main__':
    run()
