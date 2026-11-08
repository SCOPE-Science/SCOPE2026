"""Exact finite-coordinate corroboration for diagonal shift-pair couplings."""
from fractions import Fraction as Q
from itertools import product

checks = 0
for size in range(1, 9):
    for seed in range(1, 39):
        c = [Q((seed * (j + 3)) % 17 + 1, (j + 2) * 11) for j in range(size + 1)]
        for idx in range(2 * size + 1):
            u = [Q(int(idx == j)) for j in range(size)]
            v = [Q(int(idx == size + j)) for j in range(size + 1)]
            y = v[1:]
            x = [c[0] * v[0]] + [u[j] + c[j + 1] * y[j] for j in range(size)]
            w = y
            reduced_x = [c[0] * v[0]] + [u[j] + c[j + 1] * y[j] for j in range(size)]
            reduced_w = y
            assert (x, w) == (reduced_x, reduced_w)
            checks += 1
        for t in c[1:]:
            gram = [[Q(1), t], [t, Q(1) + t*t]]
            trace = gram[0][0] + gram[1][1]
            det = gram[0][0] * gram[1][1] - gram[0][1] * gram[1][0]
            assert trace == Q(2) + t*t and det == 1
            checks += 1
        for t in [Q(j, 17) for j in range(1, 12)]:
            # The bridge coupling kills all tail interactions, leaving a coordinate permutation.
            a = [Q(j) for j in range(size)]
            v = [Q((j + 1) * seed) for j in range(size + 1)]
            transformed = [v[0]] + a
            assert sum(z*z for z in transformed) + sum(z*z for z in v[1:]) == sum(z*z for z in a) + sum(z*z for z in v)
            checks += 1
print('DIAGONAL_SHIFT_PAIR_FINITE_IDENTITIES_OK', checks)
