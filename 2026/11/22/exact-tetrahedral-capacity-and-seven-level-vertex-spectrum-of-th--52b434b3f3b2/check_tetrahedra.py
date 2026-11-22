#!/usr/bin/env python3
"""Exact integer certificate for volumes of tetrahedra in an Archimedean truncated tetrahedron."""
from itertools import combinations, permutations
from collections import Counter
from fractions import Fraction

original = ((1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1))
vertex_pairs = tuple((i,j) for i in range(4) for j in range(4) if i != j)
vertices = tuple(tuple(2*original[i][k] + original[j][k] for k in range(3)) for i,j in vertex_pairs)

def signed_det(indices):
    a,b,c,d = (vertices[i] for i in indices)
    matrix = tuple(tuple(v[k]-a[k] for k in range(3)) for v in (b,c,d))
    # Leibniz's signed-permutation determinant, independent of cross-product implementations.
    total = 0
    for p in permutations(range(3)):
        inversions = sum(p[i] > p[j] for i in range(3) for j in range(i+1,3))
        total += (-1)**inversions * matrix[0][p[0]] * matrix[1][p[1]] * matrix[2][p[2]]
    return total

choices = tuple(combinations(range(12),4))
spectrum = Counter(abs(signed_det(q)) for q in choices)
expected = {0:78, 16:48, 32:192, 48:27, 64:120, 80:6, 96:24}
assert spectrum == expected, (spectrum,expected)
assert sum(spectrum.values()) == 495
maximal = {q for q in choices if abs(signed_det(q)) == 96}
triangular_faces = tuple((3*i,3*i+1,3*i+2) for i in range(4))
facial_pairs=[]
for base in combinations(range(12),3):
    candidates = {j for j in range(12) if j not in base and abs(signed_det(base+(j,))) == 96}
    for face in triangular_faces:
        if set(face).issubset(candidates):
            oriented = {signed_det(base+(j,)) for j in face}
            assert len(oriented)==1 and {abs(v) for v in oriented}=={96}
            facial_pairs.append((base,face))
assert len(facial_pairs) == 8, facial_pairs
assert {tuple(sorted(base+(j,))) for base,face in facial_pairs for j in face} == maximal
# Four vertex permutations act on directed original tetrahedron edges.
seed=next(iter(maximal))
orbit = {tuple(sorted(vertex_pairs.index((p[vertex_pairs[i][0]],p[vertex_pairs[i][1]])) for i in seed))
         for p in permutations(range(4))}
assert orbit == maximal
# The original tetrahedron has oriented determinant 432, volume 72.
# Cutting four similar corner tetrahedra of linear ratio 1/3 leaves 23/27 of the volume.
assert Fraction(72)*Fraction(23,27) == Fraction(184,3)
assert Fraction(96,6) / Fraction(184,3) == Fraction(6,23)
assert Fraction(96-80,6) == Fraction(8,3)
print('PASS: 495 determinant values, seven levels, 24 maximizers, eight continuous facial families, one symmetry orbit.')
print('SIGNED_DETERMINANT_COUNTS', sorted(spectrum.items()))
for base,face in facial_pairs:
    print('FAMILY',base,face)
