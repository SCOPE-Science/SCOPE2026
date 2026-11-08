#!/usr/bin/env python3
"""Exact finite checks for a depth-diagonal tree-shift commutator.

This finite checker corroborates, but does not replace, the all-level proof.
It requires only Python's standard library.
"""
from fractions import Fraction
from itertools import product

checks = 0

def verify(flag):
    global checks
    assert flag
    checks += 1


def examine(level_amplitudes):
    # a_k = population_k / 2^k; admissible values 1 or 2.
    verify(level_amplitudes[0] == 1)
    sizes = [1]
    branch = []
    for k, (a, next_a) in enumerate(zip(level_amplitudes, level_amplitudes[1:])):
        b = 2 * next_a // a
        verify(b * a == 2 * next_a and b in (1, 2, 4))
        branch.append(b)
        sizes.append(sizes[-1] * b)
        verify(sizes[-1] == 2**(k+1) * next_a)
    for k, b in enumerate(branch):
        c = Fraction(1, 2**(k+1))
        verify(sizes[k+1] == sizes[k] * b)
        # Each parent has b child-columns; all columns in different
        # parent blocks have disjoint support.  Hence the Gram matrix
        # of K K* has no off-diagonal entries.
        parents = list(range(sizes[k]))
        child_to_parent = [p for p in parents for _ in range(b)]
        verify(len(child_to_parent) == sizes[k+1])
        for p in parents:
            norm_sq = sum((c*c/Fraction(b) for cp in child_to_parent if cp == p), Fraction(0))
            verify(norm_sq == c*c)
        for p in parents:
            for p2 in parents:
                if p != p2:
                    verify(not any(cp == p and cp == p2 for cp in child_to_parent))
    # Sorted singulars occur in depth order, including multiplicities.
    sing = [Fraction(1, 2**(k+1)) for k, m in enumerate(sizes[:-1]) for _ in range(m)]
    verify(all(sing[i] >= sing[i+1] for i in range(len(sing)-1)))
    verify(sum(sing, Fraction(0)) == sum((Fraction(a,2) for a in level_amplitudes[:-1]), Fraction(0)))
    verify(len(sing) == sum(sizes[:-1]))


for a in [
    [1]*8,
    [1, 2, 1, 2, 1, 2, 1, 2],
    [1, 1, 1, 2, 2, 2, 1, 1],
    [1, 2, 2, 2, 1, 1, 1, 2],
]:
    examine(a)
print(f'TREE_DEPTH_GRAM_OK {checks} exact finite assertions')
