"""Independent exact-matrix check of the multipartite weighted-blockade zero-mode theorem.

Requires Python 3 and sympy. Run: python verify_kernel.py
"""
from itertools import product
from fractions import Fraction
from math import prod
import sympy as S


def physical_hamiltonian(parts):
    # Construct directly from allowed occupation bit strings of a complete
    # multipartite blockade graph, not by gluing prebuilt hypercube matrices.
    offsets = [sum(len(p) for p in parts[:i]) for i in range(len(parts))]
    all_masks = [0]
    for i, p in enumerate(parts):
        for bits in range(1, 1 << len(p)):
            all_masks.append(bits << offsets[i])
    position = {b: i for i, b in enumerate(all_masks)}
    H = S.zeros(len(all_masks))
    for j, bits in enumerate(all_masks):
        for i, p in enumerate(parts):
            for k, strength in enumerate(p):
                target = bits ^ (1 << (offsets[i] + k))
                if target not in position:
                    continue
                H[j, position[target]] = S.Rational(strength)
    assert H == H.T
    return H


def predicted(parts):
    d = [sum(sum(z * w for z, w in zip(signs, part)) == 0
             for signs in product((-1, 1), repeat=len(part)))
         for part in parts]
    active = [x for x in d if x > 0]
    inactive = len(d) - len(active)
    if inactive:
        count = sum(x-1 for x in active) + inactive - 1
        return count, S.Integer(0), d
    a = [S.Rational(x, 2**len(p)) for x, p in zip(d, parts)]
    count = sum(d) - len(d) + 1
    weight = 1/(sum(1/x for x in a)-(len(a)-1))
    return count, S.factor(weight), d


def actual(H):
    kernel = H.nullspace()
    if not kernel:
        return 0, S.Integer(0)
    B = S.Matrix.hstack(*kernel)
    gram = B.T * B
    row = B[0, :]
    weight = (row * gram.inv() * row.T)[0]
    return len(kernel), S.factor(weight)

CASES = [
 ((1,), (1,), (1,)),
 ((1, 1), (1, 1), (1, 1)),
 ((1, 1, 2), (1, 1), (1, 1, 1, 1)),
 ((1, 1, 3), (1, 1), (1, 1, 1, 1)),
 ((1, 2, 3), (1, 1), (1, 1, 2)),
 ((1, 2, 3), (1, 2, 3), (1,)),
 ((1, 1), (1, 2), (1, 1)),
 ((1, 1), (1, 1), (1,)),
 ((1, 1, 2), (1, 1, 2), (1,)),
 ((1, 1, 2), (1, 1, 2), (1, 1)),
 ((1,), (1,), (1,), (1,)),
 ((1, 1), (1, 1), (1,), (1,)),
 ((1, 2), (1, 2), (1,)),
 ((1, 2), (1, 1, 2), (1, 1)),
 ((1, 1), (1, 1), (2, 2)),
 ((1, 1, 1), (1, 1), (1, 2)),
 ((1, 1, 1, 1), (1,), (1,)),
]

if __name__ == '__main__':
    for parts in CASES:
        expected_n, expected_w, d = predicted(parts)
        observed_n, observed_w = actual(physical_hamiltonian(parts))
        assert (observed_n, observed_w) == (expected_n, expected_w), (
            parts, (observed_n, observed_w), (expected_n, expected_w))
        print('PASS', [list(p) for p in parts], 'zero_counts', d,
              'nullity', observed_n, 'vacuum_zero_weight', observed_w)
    print('ALL PASS', len(CASES), 'exact full-matrix cases')
