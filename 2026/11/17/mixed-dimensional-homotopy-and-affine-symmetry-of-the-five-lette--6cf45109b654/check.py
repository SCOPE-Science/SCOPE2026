#!/usr/bin/env python3
"""Exact integral word-chain and symmetry calculation for the five-letter affine permutation complex."""
from collections import Counter
from itertools import combinations
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form

P = 5
WORDS = sorted({tuple((a*x+b) % P for x in range(P))
                for a in range(1, P) for b in range(P)})
FACES = []
for length in range(1, P+1):
    FACES.append(sorted({tuple(w[i] for i in inds)
                         for w in WORDS
                         for inds in combinations(range(P), length)}))
assert len(WORDS) == 20
assert list(map(len, FACES)) == [5, 20, 60, 80, 20]
assert len(FACES[2]) == P*(P-1)*(P-2)

def boundary(k):
    index = {f: i for i, f in enumerate(FACES[k-1])}
    result = sp.zeros(len(FACES[k-1]), len(FACES[k]))
    for j, word in enumerate(FACES[k]):
        for pos in range(k+1):
            face = word[:pos]+word[pos+1:]
            result[index[face], j] = (-1)**pos
    return result

B = {k: boundary(k) for k in range(1, P)}
for k in range(2, P):
    assert B[k-1]*B[k] == sp.zeros(B[k-1].rows, B[k].cols)

smith = {}
for k in range(1, P):
    D = smith_normal_form(B[k], domain=sp.ZZ)
    factors = [abs(int(D[i,i])) for i in range(min(D.shape)) if D[i,i]]
    smith[k] = dict(rank=len(factors), nonunit=[x for x in factors if x != 1])
assert [smith[k]['rank'] for k in range(1, P)] == [4,16,43,20]
assert all(not smith[k]['nonunit'] for k in range(1, P))

# Each 4-cell has a unique free 3-face obtained by deleting its second letter.
four_face_occurrences = Counter(
    w[:pos] + w[pos+1:] for w in WORDS for pos in range(P))
assert len(four_face_occurrences) == 80
assert Counter(four_face_occurrences.values()) == {1:60, 2:20}
for w in WORDS:
    assert four_face_occurrences[w[:1]+w[2:]] == 1

# Explicit integral two-cocycle.  Its class generates rational H^2.
COCHAIN = {
 (0,2,1):-1, (0,3,2):1, (0,4,2):1, (1,0,3):1,
 (1,2,0):-1, (1,4,2):1, (1,4,3):1, (2,1,3):-1,
 (2,3,0):1, (2,4,0):1, (2,4,1):1, (3,0,1):1,
 (3,1,2):-1, (3,4,1):1,
}
idx = {w:i for i,w in enumerate(FACES[2])}
c = sp.zeros(len(FACES[2]),1)
for w,v in COCHAIN.items(): c[idx[w]] = v
assert B[3].T*c == sp.zeros(len(FACES[3]),1)
coboundaries = B[2].T
base_rank = coboundaries.rank()
assert base_rank == 16
assert coboundaries.row_join(c).rank() == 17

def image_of_cochain(a,b):
    v = sp.zeros(len(FACES[2]),1)
    for w,val in COCHAIN.items():
        v[idx[tuple((a*x+b)%P for x in w)]] = val
    return v
assert coboundaries.row_join(image_of_cochain(1,1)-c).rank() == 16
assert coboundaries.row_join(image_of_cochain(2,0)+c).rank() == 16
assert coboundaries.row_join(image_of_cochain(2,0)-c).rank() == 17

# A direct Lefschetz trace calculation: action on ordered cells fixes only
# pointwise-fixed words, since positions are not permuted.
def fixed_reduced_lefschetz(a,b):
    fixed = 0
    for k, faces in enumerate(FACES):
        fixed += (-1)**k*sum(all((a*x+b)%P == x for x in w) for w in faces)
    return fixed-1
for a in range(1, P):
    for b in range(P):
        if a==1 and b==0: expected = -16
        elif a==1: expected = -1
        else: expected = 0
        assert fixed_reduced_lefschetz(a,b) == expected

print('AFFINE_PERMUTATION_5_CHECK_PASS')
print('cell_counts', list(map(len,FACES)))
print('smith_ranks_and_nonunits', smith)
print('reduced_homology', {2:'Z',3:'Z^17'}, 'all_other_degrees_zero')
print('top_cell_collapses', len(WORDS))
print('H2_character', 'Legendre_multiplier_character')
print('H3_rational_character', 'Legendre + inflated_regular_C4 + 3*augmentation_F5')
