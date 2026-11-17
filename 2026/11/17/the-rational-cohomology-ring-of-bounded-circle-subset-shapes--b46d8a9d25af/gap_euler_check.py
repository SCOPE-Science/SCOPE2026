#!/usr/bin/env python3
"""Independent cycle-index check for the Euler characteristics of unlabeled circle-shape strata.

For a nonempty m-point subset modulo O(2), successive positive cyclic gaps give
an open (m-1)-simplex modulo the dihedral group D_m.  The compactly supported
Euler characteristic is (1/(2m)) * sum_{g in D_m} (-1)^(cycles(g)-1).
"""
from fractions import Fraction


def cycles_of_permutation(perm):
    n = len(perm)
    seen = set()
    number = 0
    for i in range(n):
        if i not in seen:
            number += 1
            j = i
            while j not in seen:
                seen.add(j)
                j = perm[j]
    return number


def stratum_euler(m):
    total = 0
    for j in range(m):
        # m rotations and m reflections, including the nonfaithful D_1,D_2 actions.
        for sgn in (1, -1):
            p = [((sgn * i + j) % m) for i in range(m)]
            total += (-1) ** (cycles_of_permutation(p) - 1)
    return Fraction(total, 2 * m)


def predicted_ring_rank(k):
    return (k + 3) // 4


def check(limit=100):
    previous = Fraction(0)
    data = []
    for k in range(1, limit + 1):
        step = stratum_euler(k)
        predicted_step = 1 if k % 4 == 1 else 0
        assert step == predicted_step, (k, step, predicted_step)
        previous += step
        assert previous == predicted_ring_rank(k), (k, previous)
        if k <= 12 or k in (20, 40, 60, 80, 100):
            data.append((k, int(step), int(previous), predicted_ring_rank(k)))
    return data


if __name__ == '__main__':
    print('k stratum_chi_c cumulative_chi predicted_ring_dimension')
    for row in check():
        print(*row)
    print('PASS: exact cycle-index verification through k=100')
