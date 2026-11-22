"""Reproduce the integral C6 rotation module of the six-rung prism's
perfect-matching complex. Requires Python 3, NumPy, SymPy.

All simplices, boundaries, unimodular reductions, and symmetry maps are
built from the labelled graph. No precomputed homology data is loaded.
"""
from itertools import combinations
import numpy as np
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

n = 6
# Graph vertices 2*i+s, i in Z/6, s in {0,1}.
E = sorted({tuple(sorted(e)) for i in range(n) for e in (
    (2*i, 2*i+1),
    (2*i, 2*((i+1) % n)),
    (2*i+1, 2*((i+1) % n)+1),
)})
assert len(E) == 18
perfect = []
def extend(remaining, chosen):
    if not remaining:
        perfect.append(tuple(sorted(chosen)))
        return
    v = min(remaining)
    for j, (a, b) in enumerate(E):
        if a == v and b in remaining:
            extend(remaining - {v, b}, chosen + (j,))
        elif b == v and a in remaining:
            extend(remaining - {v, a}, chosen + (j,))
extend(frozenset(range(2*n)), ())
perfect = sorted(set(perfect))
assert len(perfect) == 20
faces = [set([()])] + [set() for _ in range(n)]
for matching in perfect:
    for k in range(1, n+1):
        faces[k].update(combinations(matching, k))
faces = [sorted(row) for row in faces]
assert [len(row) for row in faces] == [1,18,117,276,270,120,20]
pos = [{s: i for i, s in enumerate(row)} for row in faces]

def boundary(k):
    out = np.zeros((len(faces[k-1]), len(faces[k])), dtype=np.int64)
    for col, simplex in enumerate(faces[k]):
        for i in range(len(simplex)):
            out[pos[k-1][simplex[:i]+simplex[i+1:]], col] += (-1)**i
    return out

A0 = boundary(3)  # degree 2 -> degree 1
B0 = boundary(4)  # degree 3 -> degree 2
assert not np.any(A0 @ B0)
A, B = A0.copy(), B0.copy()
N = len(faces[3])
V = np.eye(N, dtype=np.int64)  # new C2 basis in old coordinates
W = np.eye(N, dtype=np.int64)  # inverse coordinate transform
live_rows = list(range(A.shape[0])); live_cols = list(range(A.shape[1]))
paired_C2 = []
# Kill 100 D2 unit pivots using columns; update the C3->C2 matrix
# under every change of degree-2 basis.
while True:
    options = []
    for r in live_rows:
        nz = [c for c in live_cols if A[r, c]]
        for c in nz:
            if abs(A[r, c]) == 1:
                options.append((len(nz), r, c))
                break
    if not options:
        break
    _, row, col = min(options)
    unit = A[row, col]
    for j in live_cols:
        if j == col or A[row,j] == 0:
            continue
        alpha = int(A[row,j] // unit)
        A[:,j] -= alpha * A[:,col]
        V[:,j] -= alpha * V[:,col]
        W[col,:] += alpha * W[j,:]
        B[col,:] += alpha * B[j,:]
    live_rows.remove(row); live_cols.remove(col); paired_C2.append(col)
    assert max(np.max(np.abs(A)), np.max(np.abs(B)),
               np.max(np.abs(V)), np.max(np.abs(W))) < 100000
assert len(paired_C2) == 100
assert not np.any(A[:,live_cols])
assert not np.any(B[paired_C2,:])
# In the remaining kernel generators, kill 170 D3 unit pivots.
ker = live_cols.copy(); third = list(range(B.shape[1])); paired_B = []
while True:
    options = []
    for r in ker:
        nz = [j for j in third if B[r,j]]
        for c in nz:
            if abs(B[r,c]) == 1:
                options.append((len(nz),r,c))
                break
    if not options:
        break
    _, row, col = min(options)
    unit = B[row,col]
    # C3 basis changes clear the pivot row.
    for j in third:
        if j == col or B[row,j] == 0:
            continue
        alpha = int(B[row,j] // unit)
        B[:,j] -= alpha * B[:,col]
    # C2 basis changes clear the pivot column.
    for i in ker:
        if i == row or B[i,col] == 0:
            continue
        alpha = int(B[i,col] // unit)
        B[i,:] -= alpha * B[row,:]
        W[i,:] -= alpha * W[row,:]
        V[:,row] += alpha * V[:,i]
    ker.remove(row); third.remove(col); paired_B.append(row)
    assert max(np.max(np.abs(B)),np.max(np.abs(V)),np.max(np.abs(W))) < 100000
assert len(paired_B) == 170 and len(ker) == 6
assert not np.any(B[np.ix_(ker,third)])
# Verify the chain-level reductions (not merely reported pivot counts).
assert np.array_equal(W @ V, np.eye(N, dtype=np.int64))
assert not np.any(A0 @ V[:,ker])
assert not np.any(W[np.ix_(ker,list(range(N)))] @ B0)

def permutation_sign(values):
    return (-1)**sum(values[i] > values[j] for i in range(len(values)) for j in range(i+1,len(values)))

edge_rotation = [E.index(tuple(sorted((2*((a//2+1)%n)+a%2,
                                         2*((b//2+1)%n)+b%2)))) for a,b in E]

def rotate_two_chain(chain):
    y = np.zeros(N, dtype=np.int64)
    for i, coeff in enumerate(chain):
        if not coeff:
            continue
        image = [edge_rotation[k] for k in faces[3][i]]
        y[pos[3][tuple(sorted(image))]] += permutation_sign(image)*coeff
    return y

R = np.zeros((6,6), dtype=np.int64)
for j, col in enumerate(ker):
    rotated = rotate_two_chain(V[:,col])
    assert not np.any(A0 @ rotated)
    coordinates = W @ rotated
    R[:,j] = coordinates[ker]
expected = np.array([
    [ 0,-1,-1, 0, 0, 1],
    [ 0, 0, 0, 0, 1,-1],
    [-1,-1, 0, 0, 0, 1],
    [-1, 0, 0, 0, 0, 0],
    [ 0,-1, 0, 0, 0, 0],
    [ 0,-1,-1, 1, 1, 0],
],dtype=np.int64)
assert np.array_equal(R,expected)
assert np.array_equal(np.linalg.matrix_power(R,6),np.eye(6,dtype=np.int64))
RR = sp.Matrix(R.tolist())
assert RR.charpoly().as_expr() == RR.charpoly().gen**6-1
assert [sp.trace(RR**j) for j in range(6)] == [6,0,0,0,0,0]
assert tuple(smith_normal_form(RR-sp.eye(6),domain=ZZ).diagonal()) == (1,1,1,1,3,0)
print('PASS: 20 perfect matchings, face counts', [len(row) for row in faces])
print('PASS: integral unit pivots D2=100, D3=170, free H2 rank 6')
print('PASS: chain-level cycle and boundary checks, integral inverse basis')
print('PASS: rotation matrix:',R.tolist())
print('PASS: rotation characteristic polynomial x^6-1, regular rational character')
print('PASS: coinvariants Smith factors 1,1,1,1,3,0 => Z + Z/3')
