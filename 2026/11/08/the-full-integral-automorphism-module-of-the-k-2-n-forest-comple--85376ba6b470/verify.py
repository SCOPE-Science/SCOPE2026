"""Finite exact checks for the complete-bipartite graphic-matroid forest complex.

Run: python3 verify.py
Only finite instances are checked; the uniform theorem uses a separate proof.
"""
from itertools import permutations
from math import factorial


def permutation_sign(p):
    return -1 if sum(p[i] > p[j] for i in range(len(p)) for j in range(i + 1, len(p))) % 2 else 1


def faces(n):
    # Edge 2*i+s corresponds to the edge from row s to column i.
    return [mask for mask in range(1 << (2*n)) if sum(((mask >> (2*i)) & 3) == 3 for i in range(n)) <= 1]


def signed_reduced_lefschetz(n, simplices, perm, row_swap):
    edgemap = [2*perm[i//2] + ((i % 2) ^ row_swap) for i in range(2*n)]
    result = -1  # empty augmented simplex contributes -1 to ordinary Lefschetz sum
    for face in simplices:
        if not face:
            continue
        image_order = [edgemap[e] for e in range(2*n) if (face >> e) & 1]
        image_mask = sum(1 << e for e in image_order)
        if image_mask != face:
            continue
        inversions = sum(image_order[i] > image_order[j] for i in range(len(image_order)) for j in range(i+1, len(image_order)))
        result += (-1) ** (len(image_order)-1+inversions)
    # The only reduced homology is in degree n.
    return (-1)**n * result


for n in range(3, 7):
    simplices = faces(n)
    # K_0 has 3^n faces, B_i adds 3^(n-1) faces, sharing K_0.
    assert len(simplices) == (n+3)*3**(n-1)
    f = [sum(mask.bit_count() == d for mask in simplices) for d in range(n+2)]
    assert f[0] == 1 and f[n+1] == n*(2**(n-1))
    reduced_euler = -1 + sum((-1)**(d-1)*f[d] for d in range(1, len(f)))
    assert reduced_euler == (-1)**n*(n-1)
    checked = 0
    for perm in permutations(range(n)):
        sig = permutation_sign(perm)
        fixed = sum(perm[i] == i for i in range(n))
        for swap in (0, 1):
            got = signed_reduced_lefschetz(n, simplices, perm, swap)
            expected = (-1)**(n*swap)*sig*(fixed-1)
            assert got == expected, (n, perm, swap, got, expected)
            checked += 1
    assert checked == 2*factorial(n)
    print(f'n={n} faces_including_empty={len(simplices)} f_vector={f[1:]} '
          f'character_checks={checked} PASS')
print('K2N_FOREST_FULL_AUTOMORPHISM_CHARACTER_PASS')
