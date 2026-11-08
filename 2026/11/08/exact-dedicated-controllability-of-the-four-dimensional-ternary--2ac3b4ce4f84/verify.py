#!/usr/bin/env python3
"""Exact, standard-library verification of the ternary 4-cube incidence-network certificate."""
from itertools import product
from math import comb

Q, D, PRIME = 3, 4, 101
POINTS = list(product(range(Q), repeat=D))
LINES = [(axis, other) for axis in range(D)
         for other in product(range(Q), repeat=D-1)]
NP, NL = len(POINTS), len(LINES)
assert (NP, NL) == (81, 108)

def rank(A, p=PRIME, return_pivots=False):
    """Exact Gaussian elimination in F_p; a nonzero minor mod p is nonzero over Q."""
    if not A:
        return [] if return_pivots else 0
    B = [[int(x) % p for x in row] for row in A]
    nr, nc = len(B), len(B[0]); r = 0; cols = []
    for c in range(nc):
        pivot = next((i for i in range(r,nr) if B[i][c]), None)
        if pivot is None:
            continue
        B[r], B[pivot] = B[pivot], B[r]
        inv = pow(B[r][c], -1, p)
        B[r][c:] = [(v*inv) % p for v in B[r][c:]]
        for i in range(r+1, nr):
            mult = B[i][c]
            if mult:
                B[i][c:] = [(a-mult*b) % p for a,b in zip(B[i][c:], B[r][c:])]
        cols.append(c); r += 1
        if r == nr:
            break
    return cols if return_pivots else r

# The 81-by-108 binary point--axis-line incidence matrix.
N = [[int(tuple(point[k] for k in range(D) if k != axis) == remaining)
      for axis, remaining in LINES] for point in POINTS]
assert all(sum(row) == 4 for row in N)
assert all(sum(N[i][j] for i in range(NP)) == 3 for j in range(NL))

# Lexicographic column pivots; only the complementary lines are actuated.
pivot_lines = rank(N, return_pivots=True)
actuated_lines = [j for j in range(NL) if j not in set(pivot_lines)]
actuated_points = [i for i,point in enumerate(POINTS) if all(x in (0,1) for x in point)]
assert len(pivot_lines) == 65
assert len(actuated_lines) == 43
assert len(actuated_points) == 16
assert rank([[N[i][j] for j in pivot_lines] for i in range(NP)]) == 65

# Exact 81-by-81 Gram matrix M=NN^T via geometry:
# M_ii=4, M_ij=1 if the points differ in exactly one coordinate.
M = [[4 if a==b else (1 if sum(x!=y for x,y in zip(a,b))==1 else 0)
      for b in POINTS] for a in POINTS]
assert all(M[i][j] == sum(N[i][k]*N[j][k] for k in range(NL))
           for i in range(NP) for j in range(NP))

# Multiplication by the shifted sparse Gram matrix in F_101.
neighbors = [[(j, val) for j,val in enumerate(row) if val] for row in M]
def times_shift(A, eigenvalue):
    out = [[0]*NP for _ in range(len(A))]
    for row_index, row in enumerate(A):
        target = out[row_index]
        for k, value in enumerate(row):
            if not value: continue
            for j,mval in neighbors[k]:
                target[j] += value*mval
            target[k] -= value*eigenvalue
        out[row_index] = [x % PRIME for x in target]
    return out

I = [[int(i==j) for j in range(NP)] for i in range(NP)]
expected = {0:16, 3:32, 6:24, 9:8, 12:1}
results = {}
for eig in expected:
    P = I
    for other in expected:
        if other != eig:
            P = times_shift(P, other)
    # Point actuator observations: selection of rows of P.
    obs = [P[i][:] for i in actuated_points]
    if eig != 0:
        # Line actuator observations are rows of N^T P.
        for line_index in actuated_lines:
            obs.append([sum(N[k][line_index] * P[k][j] for k in range(NP)) % PRIME
                        for j in range(NP)])
    computed = rank(obs)
    assert computed == expected[eig], (eig,computed,expected[eig])
    results[eig] = computed

# The two exceptional Laplacian eigenspaces reside on different sides.
# Full column rank of the unactuated line incidence submatrix
# proves injective observation of ker N by the other 43 lines.
# The rank-16 point observation above proves injectivity of ker N^T.
assert (NP - 65, NL - 65) == (16,43)
assert sum(expected.values()) == NP
assert 16+43+2*(32+24+8+1) == NP+NL

# The placement is not a zero-forcing set: the process cannot even start.
black = set(actuated_points) | {NP+j for j in actuated_lines}
for node in black:
    nbrs = ({NP+j for j in range(NL) if N[node][j]}
            if node < NP else {i for i in range(NP) if N[i][node-NP]})
    assert len(nbrs - black) != 1

print('VERIFY_OK')
print('vertices=189 degrees=(4,3) rank_incidence=65')
print('Laplacian modes: 3 has mult 43; 4 has mult 16; other mult 32,24,8,1 paired')
print('min coordinate actuators=59: 16 points, 43 lines')
print('modular prime=101 spectral observation ranks=',results)
print('point_indices=',actuated_points)
print('line_indices=',actuated_lines)
print('zero_forcing_stalls=True')
