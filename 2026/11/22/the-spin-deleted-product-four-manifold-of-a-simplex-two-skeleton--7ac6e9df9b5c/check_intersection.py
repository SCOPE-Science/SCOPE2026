#!/usr/bin/env python3
"""Exact mod-2 intersection-form and orientation check for a finite deleted product.
No external packages or input files are needed. Python 3.10+.
"""
from itertools import combinations

N = 7
vertices = tuple(range(N))
faces = [list(combinations(vertices, k)) for k in (1, 2, 3)]
cells = {d: [] for d in range(5)}
for A_faces in faces:
    for B_faces in faces:
        for a in A_faces:
            for b in B_faces:
                if set(a).isdisjoint(b):
                    cells[len(a) + len(b) - 2].append((a, b))
index = {d: {cell: j for j, cell in enumerate(cells[d])} for d in cells}
assert [len(cells[d]) for d in range(5)] == [42, 210, 490, 420, 140]


def coboundary_transposed_rows(d):
    """Rows of the degree-d cellular boundary matrix, written as bit vectors."""
    result = []
    for a, b in cells[d]:
        bits = 0
        if len(a) > 1:
            for i in range(len(a)):
                bits ^= 1 << index[d - 1][(a[:i] + a[i+1:], b)]
        if len(b) > 1:
            for j in range(len(b)):
                bits ^= 1 << index[d - 1][(a, b[:j] + b[j+1:])]
        result.append(bits)
    return result


boundary = {d: coboundary_transposed_rows(d) for d in range(1, 5)}

# Check every adjacent cellular boundary composition (over F2).
for d in (2, 3, 4):
    for row in boundary[d]:
        acc = 0
        while row:
            bit = row & -row
            row ^= bit
            acc ^= boundary[d - 1][bit.bit_length() - 1]
        assert acc == 0


def echelon(vectors):
    """Reduced-by-leading-bit row echelon basis over F2."""
    pivots = {}
    for row in vectors:
        x = row
        while x:
            head = x.bit_length() - 1
            if head not in pivots:
                pivots[head] = x
                break
            x ^= pivots[head]
    return pivots


def reduce_leading(x, pivots):
    while x and (x.bit_length() - 1) in pivots:
        x ^= pivots[x.bit_length() - 1]
    return x


ranks = [len(echelon(boundary[d])) for d in range(1, 5)]
assert ranks == [41, 169, 281, 139]
piv_3 = echelon(boundary[3])
# A pivot h in the row-echelon system is determined by variables < h.
free_columns = [j for j in range(490) if j not in piv_3]
ker_d2 = []
for j in free_columns:
    x = 1 << j
    for head in sorted(piv_3):
        if (piv_3[head] & x).bit_count() % 2:
            x ^= 1 << head
    assert all((row & x).bit_count() % 2 == 0 for row in boundary[3])
    ker_d2.append(x)
assert len(ker_d2) == 209

# Coboundary of each 1-cochain, by transposing the degree-2 boundary.
coboundaries = [0] * 210
for j, row in enumerate(boundary[2]):
    while row:
        bit = row & -row
        row ^= bit
        coboundaries[bit.bit_length() - 1] ^= 1 << j

piv_cob = echelon(coboundaries)
assert len(piv_cob) == 169
assert all(all((row & x).bit_count() % 2 == 0 for row in boundary[3])
           for x in coboundaries)
combined = dict(piv_cob)
basis = []
for cocycle in ker_d2:
    residue = reduce_leading(cocycle, combined)
    if residue:
        combined[residue.bit_length()-1] = residue
        basis.append(cocycle)
assert len(basis) == 40 and len(combined) == 209

# Product Alexander-Whitney cup evaluation on each 4-dimensional product cell.
# Its three mod-2 contributions correspond to p=0,1,2.
terms = []
for A, B in cells[4]:
    assert len(A) == len(B) == 3
    terms.append(tuple((index[2][(A[:p+1], B[:3-p])],
                        index[2][(A[p:], B[2-p:])])
                       for p in (0, 1, 2)))


def cup(u, v):
    result = 0
    for term in terms:
        for i, j in term:
            result ^= ((u >> i) & 1) & ((v >> j) & 1)
    return result

pairing = [[cup(u, v) for v in basis] for u in basis]
assert all(pairing[i][j] == pairing[j][i]
           for i in range(40) for j in range(40))
assert all(pairing[i][i] == 0 for i in range(40))
assert len(echelon([sum(v << i for i, v in enumerate(row))
                    for row in pairing])) == 40
# Cup pairings with coboundaries must vanish on the closed fundamental cycle.
assert all(cup(u, v) == 0 for u in coboundaries for v in basis)


def inversion_sign(word):
    return (-1) ** sum(x > y for i, x in enumerate(word)
                        for y in word[i+1:])

orientation = []
for A, B in cells[4]:
    leftover = next(k for k in vertices if k not in A and k not in B)
    orientation.append(inversion_sign(A + B + (leftover,)))

# Signed integer boundary of the proposed fundamental 4-cycle.
fundamental_boundary = [0] * len(cells[3])
for j, (A, B) in enumerate(cells[4]):
    for i in range(3):
        fundamental_boundary[index[3][(A[:i]+A[i+1:], B)]] += orientation[j] * (-1)**i
    for i in range(3):
        fundamental_boundary[index[3][(A, B[:i]+B[i+1:])]] += orientation[j] * (-1)**(3+i)
assert fundamental_boundary == [0] * len(cells[3])
# Factor transposition preserves orientation on each 2x2 cell but reverses [M].
assert all(orientation[index[4][(B, A)]] == -orientation[j]
           for j, (A, B) in enumerate(cells[4]))

print('cells: 42 210 490 420 140')
print('cellular boundary ranks over F2: 41 169 281 139')
print('all adjacent boundary compositions zero: yes')
print('degree-2 cocycles/coboundaries/cohomology: 209 169 40')
print('product-AW cup-pairing mod 2: symmetric yes, rank 40, diagonal all zero')
print('coboundary-cocycle cup pairings vanish: yes')
print('signed integral fundamental cycle: boundary zero')
print('coordinate swap reverses fundamental orientation: yes')
print('ALL CHECKS PASSED')
