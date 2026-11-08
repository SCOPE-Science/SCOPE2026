#!/usr/bin/env python3
"""Exact rational cellular certificate for a matching-complex representation."""
from itertools import combinations, permutations
from math import comb, factorial
from collections import Counter
import json
import sympy as S

LETTERS = range(5)
VERTICES = tuple(combinations(LETTERS, 2))
EDGES = tuple((a, b) for a, b in combinations(range(10), 2)
              if set(VERTICES[a]).isdisjoint(VERTICES[b]))
assert len(EDGES) == 15
FACES = {k: tuple(c for c in combinations(range(15), k)
                  if len({v for e in c for v in EDGES[e]}) == 2 * k)
         for k in range(1, 6)}
POSITION = {k: {face: i for i, face in enumerate(FACES[k])} for k in FACES}
assert [len(FACES[k]) for k in range(1, 6)] == [15, 75, 145, 90, 6]

def boundary(k):
    matrix = S.zeros(len(FACES[k - 1]), len(FACES[k]))
    for j, face in enumerate(FACES[k]):
        for t in range(k):
            shorter = face[:t] + face[t+1:]
            matrix[POSITION[k - 1][shorter], j] = (-1) ** t
    return matrix

BOUNDARIES = {k: boundary(k) for k in range(2, 6)}
assert all(BOUNDARIES[k-1] * BOUNDARIES[k] == S.zeros(
    BOUNDARIES[k-1].rows, BOUNDARIES[k].cols) for k in (3, 4, 5))

# An exact rational basis for the image of each boundary.  Only the
# independently selected coordinate rows are needed for the trace.
IMAGE = {}
for k in range(2, 6):
    matrix = BOUNDARIES[k]
    _, cols = matrix.rref()
    basis = matrix[:, list(cols)]
    _, rows = basis.T.rref()
    rows = tuple(rows)
    assert len(rows) == len(cols)
    minor = basis[list(rows), :]
    inverse = minor.inv()  # exact rationals, never finite-field inference
    assert inverse * minor == S.eye(len(rows))
    IMAGE[k] = (basis, rows, inverse)
assert [IMAGE[k][0].cols for k in range(2, 6)] == [14, 61, 79, 6]

def cycle_type(p):
    seen, lengths = set(), []
    for start in LETTERS:
        if start in seen:
            continue
        t, length = start, 0
        while t not in seen:
            seen.add(t)
            t = p[t]
            length += 1
        lengths.append(length)
    return tuple(sorted(lengths, reverse=True))

def permutation_sign(p):
    inversions = sum(p[i] > p[j] for i in LETTERS
                     for j in LETTERS if i < j)
    return -1 if inversions % 2 else 1

def induced_edge_permutation(p):
    vm = tuple(VERTICES.index(tuple(sorted(p[i] for i in v)))
               for v in VERTICES)
    return tuple(EDGES.index(tuple(sorted(vm[v] for v in e))) for e in EDGES)

def signed_face(face, em):
    image = [em[e] for e in face]
    inversions = sum(image[i] > image[j] for i in range(len(image))
                     for j in range(i+1, len(image)))
    return tuple(sorted(image)), (-1 if inversions % 2 else 1)

def chain_trace(k, em):
    return sum(sign for face in FACES[k]
               for image, sign in [signed_face(face, em)] if image == face)

def image_trace(k, em):
    basis, rows, inverse = IMAGE[k]
    row_number = {row: i for i, row in enumerate(rows)}
    moved = S.zeros(len(rows), basis.cols)
    for i, face in enumerate(FACES[k - 1]):
        destination, sign = signed_face(face, em)
        ii = row_number.get(POSITION[k-1][destination])
        if ii is None:
            continue
        for j in range(basis.cols):
            if basis[i, j]:
                moved[ii, j] += sign * basis[i, j]
    return S.trace(inverse * moved)

def verify_equivariance(em):
    # Check d g = g d on every oriented simplex, using exact signed faces.
    for k in range(2, 6):
        for face in FACES[k]:
            target, a = signed_face(face, em)
            left = {}
            for i, e in enumerate(target):
                ff = target[:i] + target[i+1:]
                left[ff] = left.get(ff, 0) + a * ((-1) ** i)
            right = {}
            for i in range(k):
                shorter = face[:i] + face[i+1:]
                ff, b = signed_face(shorter, em)
                right[ff] = right.get(ff, 0) + b * ((-1) ** i)
            assert left == right

results, count = {}, Counter()
for perm in permutations(LETTERS):
    class_key = cycle_type(perm)
    count[class_key] += 1
    em = induced_edge_permutation(perm)
    verify_equivariance(em)
    if class_key in results:
        continue
    c = {k: chain_trace(k, em) for k in range(1, 6)}
    b = {k: image_trace(k, em) for k in range(2, 6)}
    # exact reduced homology trace = chain trace - incoming and outgoing
    h = {k-1: c[k] - b.get(k, 0) - b.get(k+1, 0)
         for k in range(1, 6)}
    f = sum(perm[i] == i for i in LETTERS)
    n2 = class_key.count(2)
    sign = permutation_sign(perm)
    assert h == {0: S.Integer(1), 1: S.Integer(0),
                 2: S.Integer(sign*f),
                 3: S.Integer(comb(f, 2) + n2 - f),
                 4: S.Integer(0)}
    assert sum((-1)**k*h[k] for k in range(5)) == sum(
        (-1)**(k-1)*c[k] for k in range(1, 6))
    results[class_key] = [int(h[2]), int(h[3])]

assert sum(count.values()) == factorial(5) == 120
assert sorted(count.values()) == [1, 10, 15, 20, 20, 24, 30]
# H_2 is a signed permutation module. H_3 is the two-row Specht module
# S^(3,2), because the 2-subset permutation module is 1 + standard + S^(3,2).
for j in (0, 1):
    assert sum(count[key] * results[key][j] for key in results) == 0
    assert sum(count[key] * results[key][j]**2 for key in results) == 120 if j == 1 else True
# The H_2 representation has two distinct constituents, with inner product 2.
assert sum(count[key] * results[key][0]**2 for key in results) == 240

print('PETERSEN_MATCHING_S5_CHARACTERS_EXACT_PASS')
print('faces_by_cardinality=[15,75,145,90,6]')
print('ranks_of_boundary_2_through_5=[14,61,79,6]')
print('reduced_betti=(0,0,5,5,0)')
for key in sorted(results, reverse=True):
    print('cycle_type=%s class_size=%d traces_H2_H3=%s' %
          (''.join(str(v) for v in key), count[key], results[key]))
print('all_120_group_elements_checked_for_signed_boundary_equivariance')
print('characters=sign_times_point_permutation_and_Specht_3_2')
