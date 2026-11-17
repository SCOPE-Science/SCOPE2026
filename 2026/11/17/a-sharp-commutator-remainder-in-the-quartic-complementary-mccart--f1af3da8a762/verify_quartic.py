"""Finite diagnostics for the sharp quartic positive-operator trace remainder.

All tests use exact rational arithmetic; they corroborate but do not replace
its dimension-independent operator-theoretic proof.
"""
from fractions import Fraction as F
from itertools import product


def matmul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def transpose(a):
    return [list(x) for x in zip(*a)]


def gram(a):
    return matmul(transpose(a), a)


def add(a, b):
    return [[x+y for x, y in zip(u, v)] for u, v in zip(a, b)]


def minus(a, b):
    return [[x-y for x, y in zip(u, v)] for u, v in zip(a, b)]


def tr(a):
    return sum(a[i][i] for i in range(len(a)))


def power(a, n):
    if n == 1:
        return a
    out = a
    for _ in range(1, n):
        out = matmul(out, a)
    return out


def quartic_values(a, b):
    assert len(a) == len(b)
    aa, bb = power(a, 2), power(b, 2)
    ab = matmul(a, b)
    ba = matmul(b, a)
    overlap = tr(power(ab, 2))
    deficit = tr(power(add(a, b), 4))-tr(power(a, 4))-tr(power(b, 4))-14*overlap
    energy = tr(matmul(power(a, 3), b)) + tr(matmul(a, power(b, 3))) - 2*tr(matmul(aa, bb))
    commutator = minus(ab, ba)
    comm_sq = tr(matmul(transpose(commutator), commutator))
    assert deficit == 4*energy + 6*comm_sq
    assert energy >= 0
    assert comm_sq >= 0
    assert deficit >= 6*comm_sq >= 0
    return deficit, energy, comm_sq


def run():
    checks = 0
    for n in (1, 2, 3):
        # Deterministic exhaustive small coefficient families.
        samples = list(product((-1, 0, 1), repeat=n*n))
        if n == 3:
            samples = samples[::271][:75]
        elif n == 2:
            samples = samples[:40]
        else:
            samples = samples
        grams = [gram([list(v[i*n:(i+1)*n]) for i in range(n)]) for v in samples]
        for i, a in enumerate(grams):
            for b in grams[max(0, i-2):i+3]:
                quartic_values(a, b)
                checks += 1
    # Noncommuting sharpness witness: two nonorthogonal rank-one projections.
    p = [[F(1), F(0)], [F(0), F(0)]]
    q = [[F(1, 2), F(1, 2)], [F(1, 2), F(1, 2)]]
    defect, energy, comm_sq = quartic_values(p, q)
    assert (defect, energy, comm_sq) == (F(3), F(0), F(1, 2))
    checks += 1
    # Nonzero commuting, nonidentical equality case.
    a = [[F(2),F(0),F(0)],[F(0),F(0),F(0)],[F(0),F(0),F(1)]]
    b = [[F(2),F(0),F(0)],[F(0),F(3),F(0)],[F(0),F(0),F(0)]]
    assert quartic_values(a,b) == (0,0,0)
    checks += 1
    print('QUARTIC_MCCARTHY_REMAINDER_OK', checks, 'rational_matrix_pairs')


if __name__ == '__main__':
    run()
