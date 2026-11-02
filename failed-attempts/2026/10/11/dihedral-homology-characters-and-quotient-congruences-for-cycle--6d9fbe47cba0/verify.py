#!/usr/bin/env python3
"""Exact independent-chain and fixed-face checks for cycle matching complexes."""
from math import gcd


def path_eval(m):
    return (1, 0, -1, -1, 0, 1)[m % 6]


def cycle_eval(d):
    return (2, 1, -1, -2, -1, 1)[d % 6]


def homology_degree(n):
    return (n // 3 - 1) if n % 3 != 2 else n // 3


def predicted_lefschetz(n, a, reflection):
    if not reflection:
        return -cycle_eval(gcd(n, a))
    if n % 2:
        return -path_eval((n - 1) // 2)
    if a % 2 == 0:
        return -path_eval(n // 2 + 1)
    return -path_eval(n // 2 - 2)


def is_face(n, mask):
    return all(not ((mask >> i) & 1 and (mask >> ((i + 1) % n)) & 1)
               for i in range(n))


def signed_fixed_face_sum(n, a, reflection):
    permutation = [(a - j if reflection else a + j) % n for j in range(n)]
    total = -1  # The reduced empty face contributes -1.
    inspected = 0
    for mask in range(1, 1 << n):
        if not is_face(n, mask):
            continue
        vertices = [j for j in range(n) if mask >> j & 1]
        images = [permutation[j] for j in vertices]
        if sorted(images) != vertices:
            continue
        inversions = sum(x > y for j, x in enumerate(images) for y in images[j + 1:])
        total += (-1) ** (len(vertices) - 1 + inversions)
        inspected += 1
    return total, inspected


def binary_rank(columns):
    pivots = {}
    for value in columns:
        while value:
            pivot = value.bit_length() - 1
            if pivot in pivots:
                value ^= pivots[pivot]
            else:
                pivots[pivot] = value
                break
    return len(pivots)


def independent_reduced_betti(n):
    faces = {}
    for mask in range(1, 1 << n):
        if is_face(n, mask):
            faces.setdefault(mask.bit_count() - 1, []).append(mask)
    maximum = max(faces)
    boundary_rank = {}
    for k in range(maximum + 1):
        if k == 0:
            boundary_rank[k] = 1
            continue
        rows = {mask: i for i, mask in enumerate(faces[k - 1])}
        columns = []
        for mask in faces.get(k, []):
            bitset = 0
            for j in range(n):
                if mask >> j & 1:
                    bitset ^= 1 << rows[mask ^ (1 << j)]
            columns.append(bitset)
        boundary_rank[k] = binary_rank(columns)
    return {k: len(faces[k]) - boundary_rank[k] - boundary_rank.get(k + 1, 0)
            for k in range(maximum + 1)}


def run():
    characters = fixed_faces = homology_cases = 0
    for n in range(3, 17):
        q = homology_degree(n)
        for reflection in (False, True):
            for a in range(n):
                result, count = signed_fixed_face_sum(n, a, reflection)
                expected = predicted_lefschetz(n, a, reflection)
                assert result == expected, (n, a, reflection, result, expected)
                characters += 1
                fixed_faces += count
        cyclic_sum = sum(predicted_lefschetz(n, a, False) for a in range(n))
        full_sum = cyclic_sum + sum(predicted_lefschetz(n, a, True) for a in range(n))
        cyclic_rank = (-1) ** q * cyclic_sum // n
        dihedral_rank = (-1) ** q * full_sum // (2 * n)
        assert cyclic_rank == (1 if gcd(n, 6) == 1 else 0), (n, cyclic_rank)
        assert dihedral_rank == (1 if n % 12 in (1, 11) else 0), (n, dihedral_rank)
        assert -cycle_eval(n) == (-1) ** q * (2 if n % 3 == 0 else 1)
        if n <= 12:
            betti = independent_reduced_betti(n)
            assert betti.get(q) == (2 if n % 3 == 0 else 1), (n, betti)
            assert all(value == 0 for degree, value in betti.items() if degree != q), (n, betti)
            homology_cases += 1
    print('VERIFY_OK', characters, 'signed character comparisons,', fixed_faces,
          'fixed oriented faces,', homology_cases,
          'exact reduced mod-2 chain-rank calculations; n=3..16 character and quotient checks')


if __name__ == '__main__':
    run()
