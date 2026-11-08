#!/usr/bin/env python3
"""Exact finite character checks for three-cut complexes of cycle complements.
No network or third-party packages. The infinite-family proof is mathematical.
"""
from itertools import combinations


def sign_of_restriction(perm, positions):
    values = [perm[i] for i in positions]
    return -1 if sum(values[i] > values[j]
                     for i in range(len(values))
                     for j in range(i + 1, len(values))) % 2 else 1


def cut_masks(n):
    forbidden = [sum(1 << ((i + j) % n) for j in range(3))
                 for i in range(n)]
    return [mask for mask in range(1 << n)
            if any(not (mask & bad) for bad in forbidden)]


def analytic_character(n, kind, a):
    residue = n % 8
    if n % 4:
        reflection = 1 if residue in (1, 2, 3) else -1
        return 1 if kind == 'r' else reflection
    line_reflection = -1 if (n // 4) % 2 == 0 else 1
    if kind == 's':
        return line_reflection * (-1 if a % 2 else 1)
    return (-1 if a % 2 else 1) + (2 if a % 4 == 0 else (-2 if a % 4 == 2 else 0))


def direct_character(n, faces, perm):
    lef = 0
    for mask in faces:
        pos = [i for i in range(n) if mask & (1 << i)]
        img = 0
        for i in pos:
            img |= (1 << perm[i])
        if img == mask:
            lef += (-1 if len(pos) % 2 == 0 else 1) * sign_of_restriction(perm, pos)
    p, rest = divmod(n, 4)
    degree = 2*p-2 if rest == 0 else 2*p-1
    return lef * (-1 if degree % 2 else 1)


def rank_mod2(columns):
    pivot = {}
    for val in columns:
        while val:
            lead = val.bit_length()-1
            if lead in pivot:
                val ^= pivot[lead]
            else:
                pivot[lead] = val
                break
    return len(pivot)


def homology_ranks(n, faces):
    by_size = [[] for _ in range(n+1)]
    for mask in faces:
        by_size[mask.bit_count()].append(mask)
    ranks = [0] * (n + 2)
    for size in range(1, n + 1):
        prev = {mask: i for i, mask in enumerate(by_size[size-1])}
        cols = []
        for mask in by_size[size]:
            col = 0
            for i in range(n):
                if mask >> i & 1:
                    col ^= (1 << prev[mask ^ (1 << i)])
            cols.append(col)
        ranks[size] = rank_mod2(cols)
    return {size-1: len(by_size[size])-ranks[size]-ranks[size+1]
            for size in range(n+1)
            if len(by_size[size])-ranks[size]-ranks[size+1]}


def run():
    # Directly enumerate every simplex and every element of D_n, not only generators.
    for n in range(5, 16):
        faces = cut_masks(n)
        for a in range(n):
            for kind in ('r', 's'):
                perm = [(i+a) % n if kind == 'r' else (a-i) % n
                        for i in range(n)]
                observed = direct_character(n, faces, perm)
                predicted = analytic_character(n, kind, a)
                assert observed == predicted, (n, kind, a, observed, predicted)
        # Boundary ranks independently test the necessary homology premise in small cases.
        if n <= 10:
            got = homology_ranks(n, faces)
            p, res = divmod(n, 4)
            expected = {2*p-2: 3} if res == 0 else {2*p-1: 1}
            assert got == expected, (n, got, expected)
        print('n=%d all %d dihedral actions verified; faces=%d' % (n, 2*n, len(faces)))
    print('VERIFY_OK')


if __name__ == '__main__':
    run()
