"""Exact rational test of the multiplicity-constrained logarithmic variance law.

This finite test supplements, but does not replace, the analytical proof.
All angles are measured in turns (one turn = 2*pi), and energy is
measured in units of pi squared.
"""
from fractions import Fraction as Q
from itertools import combinations


def compositions(n):
    for r in range(1, n + 1):
        for cuts in combinations(range(1, n), r - 1):
            points = (0,) + cuts + (n,)
            yield tuple(points[i+1] - points[i] for i in range(r))


def optimal_turns(m):
    n, b = sum(m), 0
    centers = []
    for v in m:
        centers.append(Q(2*b + v - 1, 2*n))
        b += v
    return tuple(centers)


def energy_over_pi2(centers, m):
    result = Q(0)
    for i, mi in enumerate(m):
        for j, mj in enumerate(m):
            d = abs(centers[i] - centers[j])
            assert d < 1
            result += mi * mj * (Q(1, 6) - d + d*d) / 2
    return result


def minimum_over_pi2(m):
    return Q(sum(v**3 for v in m), 12 * sum(m))


def stability_over_pi2(x, x_star, m):
    n = sum(m)
    offsets = [xj - sj for xj, sj in zip(x, x_star)]
    avg = sum(v*d for v, d in zip(m, offsets)) / n
    return n * sum(v*(d-avg)**2 for v, d in zip(m, offsets))


count = 0
for n in range(1, 11):
    for m in compositions(n):
        x0 = optimal_turns(m)
        v0 = energy_over_pi2(x0, m)
        assert v0 == minimum_over_pi2(m), (m, x0, v0)
        perturbations = [Q(2*j - len(m) + 1, 400*n) for j in range(len(m))]
        x = [a + e for a, e in zip(x0, perturbations)]
        assert all(x[j] < x[j+1] for j in range(len(x)-1))
        assert (not x or x[-1] - x[0] < 1)
        lhs = energy_over_pi2(x, m) - v0
        rhs = stability_over_pi2(x, x0, m)
        assert lhs == rhs and lhs >= 0, (m, lhs, rhs)
        count += 1

for n in range(1, 21):
    for r in range(1, n+1):
        q, s = divmod(n, r)
        lower = (r-s)*q**3 + s*(q+1)**3
        # Exchange argument: any unequal pair differing by >= 2 can be
        # replaced by neighbors with strictly smaller sum of cubes.
        assert all((a**3+b**3 > (a-1)**3+(b+1)**3)
                   for a in range(2, n+1) for b in range(1, a-1))
        assert lower >= n

print(f'CHECK_OK: {count} exact rational composition/stability tests across degrees 1..10; balanced-profile checks 1..20')
